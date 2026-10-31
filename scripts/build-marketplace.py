#!/usr/bin/env python3
"""Build .claude-plugin/marketplace.json from the SKILL.md tree.

Every SKILL.md must land in exactly one plugin:
  * <category>/<skill>/SKILL.md                    -> plugin "<category>"
  * organizations/<dept>/skills/<skill>/SKILL.md   -> plugin "org-<dept>"
  * <skill>/SKILL.md (top level)                   -> plugin from STANDALONE_GROUPS

Category plugins use their directory as `source`, so installing one copies only
that subtree. Standalone groups live at the repo root and use `source: "./"`.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
from collections import defaultdict
from pathlib import Path

MARKETPLACE_NAME = "dxta-skills"
OWNER = {"name": "DxTa", "url": "https://github.com/DxTa"}
MARKETPLACE_DESCRIPTION = "Curated Agent Skills collection (engineering, GPU perf, video AI, org roles)"

# Top-level skill directory -> plugin name.
STANDALONE_GROUPS: dict[str, str] = {
    **{
        name: "gpu-perf"
        for name in (
            "converting-cutile-to-triton",
            "perf-activation-recompute",
            "perf-analysis",
            "perf-cpu-offloading",
            "perf-cuda-graphs",
            "perf-expert-parallel-overlap",
            "perf-hierarchical-context-parallel",
            "perf-host-analysis",
            "perf-host-optimization",
            "perf-memory-tuning",
            "perf-optimization",
            "perf-parallelism-strategies",
            "perf-torch-cuda-graphs",
            "perf-torch-sync-free",
            "perf-tp-dp-comm-overlap",
            "perf-workload-profiling",
        )
    },
    **{
        name: "nemo-dev"
        for name in (
            "bump-base-image",
            "bump-dependency",
            "cicd",
            "copyright",
            "create-issue",
            "debug",
            "docs",
            "error-handling",
        )
    },
    **{
        name: "llm-eval"
        for name in (
            "accessing-mlflow",
            "byob",
            "deployment",
            "evaluation",
        )
    },
    **{
        name: "video-ai"
        for name in (
            "deepstream-dev",
            "deepstream-import-vision-model",
            "deploy",
            "rt-vlm",
            "video-analytics",
            "video-search",
        )
    },
    **{
        name: "agent-meta"
        for name in (
            "context-management",
            "find-skills",
            "skill-discovery",
            "skill-evolution",
        )
    },
    "argo-gitops": "gitops",
}

DESCRIPTIONS: dict[str, str] = {
    "agent-meta": "Skill discovery, skill evolution, and context-window management",
    "aws": "AWS CDK, serverless event-driven architecture, and cost operations",
    "backend": "Backend development and database design",
    "comms": "GitHub/GitLab operations, Gmail, Google Calendar/Drive, internal comms",
    "core": "Engineering fundamentals: debugging, TDD, code review, design patterns, problem solving",
    "data": "Personal knowledge management and memvid video memory",
    "design": "Algorithmic art, canvas design, brand guidelines, themes, artifacts",
    "devops": "Ansible, CI/CD pipelines, IaC, cloud cost, local GitHub Actions",
    "frontend": "Frontend design/development, UI styling, web frameworks, web artifacts",
    "gitops": "Argo CD and Argo Workflows GitOps operations for Kubernetes",
    "gpu-perf": "Megatron Bridge / TensorRT-LLM / PyTorch GPU performance tuning and profiling",
    "herdr": "Markdown preview split pane",
    "integration": "MCP server builder",
    "llm-eval": "LLM evaluation (NEL, BYOB, MLflow) and model serving (vLLM, SGLang, TRT-LLM)",
    "media": "Media processing and Slack GIF creation",
    "nemo-dev": "NeMo / Megatron repo workflow: CI, dependency bumps, issues, conventions",
    "packs": "Opt-in bundles: feature-dev and fullstack starter",
    "quality": "Testing, coverage, PR review, performance and chaos testing",
    "security": "Security review and test scanning",
    "video-ai": "NVIDIA DeepStream, VSS deployment, real-time VLM, video search and analytics",
}

FRONTMATTER = re.compile(r"^---\n(.*?)\n---(?:\n|$)", re.DOTALL)
NAME_FIELD = re.compile(r"^name:[ \t]*(.+?)[ \t]*$", re.MULTILINE)
PLUGIN_NAME = re.compile(r"[a-z0-9][a-z0-9-]*")


def skill_dirs(root: Path) -> list[Path]:
    found = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if not d.startswith("."))
        if "SKILL.md" in filenames:
            found.append(Path(dirpath).relative_to(root))
    return sorted(found)


def skill_name(root: Path, rel: Path) -> str:
    match = FRONTMATTER.match((root / rel / "SKILL.md").read_text(encoding="utf-8"))
    name = NAME_FIELD.search(match.group(1)) if match else None
    return name.group(1).strip("'\"") if name else rel.name


def assign(rel: Path) -> tuple[str, Path]:
    """Return (plugin name, plugin source dir relative to repo root)."""
    parts = rel.parts
    if len(parts) == 1:
        plugin = STANDALONE_GROUPS.get(parts[0])
        if plugin is None:
            raise ValueError(f"Top-level skill {parts[0]!r} has no plugin; add it to STANDALONE_GROUPS")
        return plugin, Path(".")
    if parts[0] == "organizations":
        if len(parts) != 4 or parts[2] != "skills":
            raise ValueError(f"Unexpected organizations layout: {rel}")
        return f"org-{parts[1]}", Path("organizations", parts[1])
    if len(parts) != 2:
        raise ValueError(f"Unexpected skill depth: {rel}")
    return parts[0], Path(parts[0])


def build(root: Path) -> dict[str, object]:
    groups: dict[str, dict[str, object]] = {}
    names: dict[str, dict[str, Path]] = defaultdict(dict)

    for rel in skill_dirs(root):
        plugin, source = assign(rel)
        group = groups.setdefault(plugin, {"source": source, "skills": []})
        if group["source"] != source:
            raise ValueError(f"Plugin {plugin!r} mixes sources {group['source']} and {source}")
        name = skill_name(root, rel)
        if name in names[plugin]:
            raise ValueError(f"Duplicate skill {name!r} in plugin {plugin!r}: {names[plugin][name]} and {rel}")
        names[plugin][name] = rel
        group["skills"].append("./" + rel.relative_to(source).as_posix())

    unused = set(STANDALONE_GROUPS) - {p.name for p in skill_dirs(root) if len(p.parts) == 1}
    if unused:
        raise ValueError(f"STANDALONE_GROUPS references missing skills: {sorted(unused)}")

    plugins = []
    for plugin in sorted(groups):
        if not PLUGIN_NAME.fullmatch(plugin):
            raise ValueError(f"Invalid plugin name {plugin!r}")
        group = groups[plugin]
        source = group["source"].as_posix()
        if plugin.startswith("org-"):
            description = f"Organizational role skills: {plugin[4:].replace('-', ' ')}"
        else:
            description = DESCRIPTIONS.get(plugin)
            if description is None:
                raise ValueError(f"Missing description for plugin {plugin!r}")
        plugins.append(
            {
                "name": plugin,
                "source": "./" if source == "." else f"./{source}",
                "description": description,
                "category": "organization" if plugin.startswith("org-") else "development",
                "strict": False,
                "skills": sorted(group["skills"]),
            }
        )

    return {
        "$schema": "https://anthropic.com/claude-code/marketplace.schema.json",
        "name": MARKETPLACE_NAME,
        "description": MARKETPLACE_DESCRIPTION,
        "owner": OWNER,
        "plugins": plugins,
    }


def render(data: dict[str, object]) -> str:
    return json.dumps(data, indent=2, ensure_ascii=False) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if marketplace.json is stale")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    target = root / ".claude-plugin" / "marketplace.json"
    try:
        data = build(root)
    except (OSError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    expected = render(data)
    summary = f"{len(data['plugins'])} plugins, {sum(len(p['skills']) for p in data['plugins'])} skills"

    if args.check:
        current = target.read_text(encoding="utf-8") if target.exists() else ""
        if current != expected:
            print(f"STALE: {target}; run {Path(__file__).name}", file=sys.stderr)
            return 1
        print(f"OK: {summary}")
        return 0

    target.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix="marketplace.", suffix=".json", dir=target.parent)
    with os.fdopen(fd, "w", encoding="utf-8") as stream:
        stream.write(expected)
    os.replace(tmp, target)
    print(f"wrote {summary} -> {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
