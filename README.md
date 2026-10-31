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

## Claude plugin marketplace

`.claude-plugin/marketplace.json` exposes the skills as plugins (one per category, `org-<department>` per organization, plus `gpu-perf`, `nemo-dev`, `llm-eval`, `video-ai`, `agent-meta`, `gitops` for top-level skills). It is generated, so do not edit it by hand:

```bash
python3 scripts/build-marketplace.py          # regenerate after adding/moving a skill
python3 scripts/build-marketplace.py --check  # CI: fail if stale
claude plugin validate . --strict
```

A new top-level skill must be added to `STANDALONE_GROUPS` in the script, or the build fails.

Install:

```bash
/plugin marketplace add DxTa/claude-code-skills
/plugin install core@dxta-skills
```

In Claude Desktop, add `DxTa/claude-code-skills` as a marketplace. Keep plugin files out of Git LFS: marketplace clones do not fetch LFS content.

## License

MIT
