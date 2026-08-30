#!/usr/bin/env python3
"""Build the nested skill registry from SKILL.md files."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
from pathlib import Path

FRONTMATTER = re.compile(r"^---\n(.*?)\n---(?:\n|$)", re.DOTALL)
FIELD = re.compile(r"^([A-Za-z0-9_-]+):(?:[ \t]+(.*))?$")


def read_field(frontmatter: str, key: str) -> str:
    lines = frontmatter.splitlines()
    for index, line in enumerate(lines):
        match = FIELD.match(line)
        if not match or match.group(1) != key:
            continue
        value = (match.group(2) or "").strip()
        if value in {">", "|", ">-", "|-", ">+", "|+"}:
            parts = []
            for continuation in lines[index + 1 :]:
                if FIELD.match(continuation):
                    break
                if continuation.startswith((" ", "\t")):
                    parts.append(continuation.strip())
            value = " ".join(parts)
        return value.strip("'\"").strip()
    return ""


def skill_records(root: Path) -> list[tuple[str, str]]:
    records = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(name for name in dirnames if name != ".git")
        if "SKILL.md" not in filenames:
            continue
        skill_file = Path(dirpath) / "SKILL.md"
        match = FRONTMATTER.match(skill_file.read_text(encoding="utf-8"))
        frontmatter = match.group(1) if match else ""
        name = read_field(frontmatter, "name") or skill_file.parent.name
        if not re.fullmatch(r"[a-z0-9-]+", name):
            raise ValueError(f"Invalid skill name {name!r}: {skill_file}")
        relative = skill_file.parent.relative_to(root).as_posix()
        records.append((name, relative))
    return sorted(records, key=lambda record: (record[0], record[1]))


def read_existing_aliases(index_path: Path, valid_paths: set[str]) -> dict[str, str]:
    if not index_path.exists():
        return {}
    try:
        data = json.loads(index_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ValueError(f"Invalid existing index {index_path}: {error}") from error
    aliases = data.get("skills", {})
    if not isinstance(aliases, dict):
        raise ValueError(f"Expected object at skills in {index_path}")
    return {
        str(alias): str(relative)
        for alias, relative in aliases.items()
        if str(relative) in valid_paths
    }


def build_index(root: Path) -> dict[str, object]:
    records = skill_records(root)
    paths = {relative for _, relative in records}
    aliases = read_existing_aliases(root / "index.json", paths)
    registry: dict[str, str] = dict(aliases)

    for name, relative in records:
        for alias in (name, relative):
            previous = registry.get(alias)
            if previous is not None and previous != relative:
                raise ValueError(f"Alias {alias!r} points to both {previous!r} and {relative!r}")
            registry[alias] = relative

    return {"skills": dict(sorted(registry.items())), "version": 1}


def render(index: dict[str, object]) -> str:
    return json.dumps(index, indent=2, ensure_ascii=False) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if index.json is stale")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    index_path = root / "index.json"
    try:
        expected = render(build_index(root))
    except (OSError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1

    if args.check:
        current = index_path.read_text(encoding="utf-8") if index_path.exists() else ""
        if current != expected:
            print(f"STALE: {index_path}; run {Path(__file__).name}", file=sys.stderr)
            return 1
        print(f"OK: {len(json.loads(expected)['skills'])} registry entries")
        return 0

    index_path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix="index.", suffix=".json", dir=index_path.parent)
    with os.fdopen(fd, "w", encoding="utf-8") as stream:
        stream.write(expected)
    os.replace(temporary, index_path)
    print(f"indexed {len(json.loads(expected)['skills'])} registry entries -> {index_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
