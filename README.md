---
name: skills
description: Curated Agent Skills collection for Claude Code, Pi, OpenCode, Codex, and directory-based tools
---

# Agent Skills Collection

Canonical skill sources live in this repository. Tools load `SKILL.md` files recursively through their configured links or installers.

## Layout

- Existing skills retain their category paths: `core/`, `frontend/`, `backend/`, `quality/`, `security/`, and others.
- Re-authored organizational imports live at `organizations/<department>/skills/<skill>/SKILL.md`.
- `packs/` remains opt-in and is excluded from Codex flattening.
- `index.json` is generated from filesystem paths and frontmatter by `scripts/build-index.py`.

## Organization imports

`organizations/import-matrix.tsv` records all 143 Headcount source skills, local equivalents, dispositions, destinations, and activation review. It is an audit record, not a runtime source.

The current import records Headcount snapshot commit `1f3f550` from <https://cbrock84.github.io/headcount/org-chart.html>. It contains 19 locally covered capabilities and 124 re-authored imports. External plugin manifests, prose, code, examples, and assets are not copied.

Sensitive or role-oriented organizational skills may use `disable-model-invocation: true`; they provide decision support and do not replace qualified legal, financial, HR, security, or executive review.

## Discovery

Use generated index aliases for canonical skill names and relative skill directories:

```bash
python3 scripts/build-index.py --check
read "$HOME/.pi/agent/skills/skill-index.tsv"
```

For tool setup, link this repository as the configured skills directory. Do not create duplicate compatibility trees; update the canonical source and regenerate indexes.

## License

MIT
