#!/usr/bin/env python3
"""Lint the repo so the Claude plugin marketplace cannot silently break.

`claude plugin validate` checks the manifest schema, but it does not check
that plugin sources and skill paths exist. This script does, and also checks:
  * every SKILL.md belongs to exactly one plugin
  * SKILL.md frontmatter is valid YAML with a valid name and description
  * paths stay inside the repo and inside their plugin source
  * no plugin source has a top-level bin/ (rejected by claude.ai)
  * no symlinks inside plugin sources (they don't survive install copies)
  * nothing is stored in Git LFS (marketplace clones don't fetch LFS content)
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / ".claude-plugin" / "marketplace.json"
FRONTMATTER = re.compile(r"^---\n(.*?)\n---(?:\n|$)", re.DOTALL)
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
LFS_POINTER = b"version https://git-lfs.github.com/spec/"

errors: list[str] = []


def error(message: str) -> None:
    errors.append(message)


def inside(path: Path, parent: Path) -> bool:
    try:
        path.resolve().relative_to(parent.resolve())
        return True
    except ValueError:
        return False


def tracked_files() -> list[str]:
    out = subprocess.run(
        ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    ).stdout
    return [p for p in out.decode().split("\0") if p]


def lint_skill(skill_dir: Path) -> None:
    rel = skill_dir.relative_to(ROOT)
    text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    match = FRONTMATTER.match(text)
    if not match:
        error(f"{rel}/SKILL.md: missing '---' frontmatter at top of file")
        return
    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        error(f"{rel}/SKILL.md: frontmatter is not valid YAML: {str(exc).splitlines()[0]}")
        return
    if not isinstance(data, dict):
        error(f"{rel}/SKILL.md: frontmatter must be a mapping")
        return
    name = data.get("name")
    if not isinstance(name, str) or not NAME.fullmatch(name) or len(name) > 64:
        error(f"{rel}/SKILL.md: name {name!r} must be lowercase-hyphenated, <= 64 chars")
    elif name != skill_dir.name:
        error(f"{rel}/SKILL.md: name {name!r} must match directory {skill_dir.name!r}")
    description = data.get("description")
    if not isinstance(description, str) or not description.strip():
        error(f"{rel}/SKILL.md: description must be a non-empty string")
    elif len(description) > 1024:
        error(f"{rel}/SKILL.md: description is {len(description)} chars (max 1024)")


def main() -> int:
    try:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot read {MANIFEST}: {exc}", file=sys.stderr)
        return 1

    claimed: dict[Path, str] = {}
    plugin_names: set[str] = set()
    for plugin in manifest.get("plugins", []):
        pname = plugin.get("name", "<unnamed>")
        if pname in plugin_names:
            error(f"plugin {pname}: duplicate plugin name")
        plugin_names.add(pname)

        source = plugin.get("source")
        if not isinstance(source, str) or not source.startswith("./") or ".." in Path(source).parts:
            error(f"plugin {pname}: source {source!r} must be a './' path inside the repo")
            continue
        source_dir = ROOT / source
        if not source_dir.is_dir() or not inside(source_dir, ROOT):
            error(f"plugin {pname}: source {source} does not exist")
            continue
        if (source_dir / "bin").exists():
            error(f"plugin {pname}: top-level bin/ in {source} is rejected by claude.ai")
        if (source_dir / ".claude-plugin" / "plugin.json").exists() and plugin.get("strict") is False:
            error(f"plugin {pname}: plugin.json + strict:false + skills conflict; plugin will not load")

        skills = plugin.get("skills") or []
        if not skills:
            error(f"plugin {pname}: no skills listed")
        for entry in skills:
            if not isinstance(entry, str) or not entry.startswith("./") or ".." in Path(entry).parts:
                error(f"plugin {pname}: skill path {entry!r} must be a './' path without '..'")
                continue
            skill_dir = source_dir / entry
            if not inside(skill_dir, source_dir):
                error(f"plugin {pname}: skill {entry} escapes source {source}")
            elif not (skill_dir / "SKILL.md").is_file():
                error(f"plugin {pname}: skill {source.rstrip('/')}/{entry[2:]} has no SKILL.md")
            else:
                key = skill_dir.resolve()
                if key in claimed:
                    error(f"plugin {pname}: skill {entry} already in plugin {claimed[key]}")
                claimed[key] = pname

    files = tracked_files()
    for rel in files:
        path = ROOT / rel
        if path.name == "SKILL.md" and path.is_file():
            lint_skill(path.parent)
            if path.parent.resolve() not in claimed:
                error(f"{rel}: not in any plugin; run scripts/build-marketplace.py")
        if path.is_symlink():
            error(f"{rel}: symlinks are not supported in plugin content")
        elif path.is_file():
            with path.open("rb") as stream:
                if stream.read(len(LFS_POINTER)) == LFS_POINTER:
                    error(f"{rel}: Git LFS pointer; commit the real file instead")

    attributes = ROOT / ".gitattributes"
    if attributes.exists() and re.search(r"filter=lfs", attributes.read_text(encoding="utf-8")):
        error(".gitattributes: Git LFS filters are not allowed (marketplace clones skip LFS)")

    if errors:
        for message in errors:
            print(f"ERROR: {message}", file=sys.stderr)
        print(f"{len(errors)} error(s)", file=sys.stderr)
        return 1
    print(f"OK: {len(plugin_names)} plugins, {len(claimed)} skills, {len(files)} files checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
