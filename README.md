---
name: skills
description: Curated Agent Skills collection with installable plugins for Claude Code and directory-based use in Pi, OpenCode, and Codex
---

# Agent Skills Collection

Curated Agent Skills with installable Claude Code plugins and directory-based skills for Pi, OpenCode, Codex, and other tools that load `SKILL.md` directories.

## Installation

### As Claude Code Marketplace Plugins

1. In Claude Code, go to Settings > Marketplace
2. Add marketplace from GitHub: `dxta/claude-code-skills`
3. Browse and install individual plugins

### As a Git Submodule for Directory-Based Tools

Recommended neutral path:

```bash
git submodule add https://github.com/dxta/claude-code-skills.git ai/skills/mine
```

Then expose the repo to each tool with symlinks or an installer:

```bash
# OpenCode
ln -s ../ai/skills/mine ~/.config/opencode/skills

# Pi coding agent
ln -s /path/to/repo/ai/skills/mine ~/.pi/agent/skills/mine

# Codex
ln -s /path/to/repo/ai/skills/mine/core/systematic-debugging ~/.codex/skills/systematic-debugging
```

For multi-source setups, keep this repo as the public `mine/` source and compose private or third-party skills outside this repository.

## Plugin Catalog

| Plugin | Skills | Agents | Commands | Description |
|--------|--------|--------|----------|-------------|
| core-thinking | 9 | - | - | Mental models: collision-zone thinking, defense-in-depth, inversion, meta-pattern recognition, root-cause tracing, scale game, simplification cascades, when-stuck, reasoning tools |
| core-workflow | 5 | 2 | 3 | Code review, planning, push-all, skill creator, spec analyzer |
| context-engineering | 4 | - | - | Master checklist, anti-patterns, agent selection, token management (CC-adapted) |
| frontend | 5 | 1 | - | Design, development, UI styling, web artifacts, web frameworks |
| backend | 2 | 1 | - | Backend development, databases |
| quality | 6 | 2 | 2 | Chaos engineering, code review, performance, PR review, test coverage, webapp testing |
| devops | 4 | 1 | 1 | Ansible, CI/CD, cloud costs, IaC |
| docs | 5 | 1 | 1 | API docs, DOCX, PDF, PPTX, XLSX |
| design | 5 | - | - | Algorithmic art, artifacts, branding, canvas, themes |
| security | 2 | 1 | - | Security pro pack, security scanner |
| comms | 6 | - | - | GCal, GDrive, GitHub, GitLab, Gmail, internal comms |
| media-and-data | 4 | - | - | Media processing, Slack GIFs, Memvid, PKM |
| tools-and-integrations | 1 | - | - | MCP builder |

## Repository Structure

This repository serves two use cases:

- **Root-level skill sources** -- Categories such as `core/`, `frontend/`, `backend/`, etc. contain skills in `<category>/<skill-name>/SKILL.md` layout. This is the source of truth and is compatible with tools that recursively load `SKILL.md` directories.
- **`plugins/` marketplace overlay** -- Claude Code plugin packages. Each plugin has a `.claude-plugin/plugin.json` manifest and a `skills/` directory of symlinks pointing back to root-level sources. Some plugins also include `agents/` and `commands/` directories.

```text
claude-code-skills/
  core/                        # Root-level skill sources
    collision-zone-thinking/
      SKILL.md
    ...
  frontend/
  backend/
  ...
  index.json                   # Full skill registry
  plugins/
    core-thinking/
      .claude-plugin/
        plugin.json            # Marketplace manifest
      skills/
        collision-zone-thinking -> ../../../core/collision-zone-thinking
        ...
    core-workflow/
      .claude-plugin/
        plugin.json
      skills/
      agents/
      commands/
    ...
```

## Skills Not in Marketplace

Some root-level skills are intentionally available only when using the repository directly as a directory/submodule source.

Examples:

- **aws/** -- AWS CDK, cost operations, and serverless EDA. Kept separate due to cloud-provider specificity; intended for explicit opt-in.
- **packs/** -- Composite skill packs (feature-dev, fullstack-starter-pack) that reference skills across categories.
- Some local workflow skills may remain directory-only before they are packaged into marketplace plugins.

## Development

### Updating Skills

Edit skill files at root level, e.g.:

```text
core/when-stuck/SKILL.md
```

Then regenerate plugin symlinks if plugin packaging changed:

```bash
scripts/sync-plugins.sh
```

### Adding a New Skill

1. Create `<category>/<skill-name>/SKILL.md`
2. Add an entry to `index.json`
3. Update the relevant plugin's symlinks and `plugin.json` if it should ship as a Claude Code plugin
4. Run `scripts/sync-plugins.sh`

## License

MIT
