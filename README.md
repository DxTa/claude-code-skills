# Claude Code Skills Collection

63 curated skills packaged as 13 installable plugins for Claude Code. Thinking frameworks, workflow automation, development best practices, and more.

## Installation

### As Claude Code Marketplace Plugins

1. In Claude Code, go to Settings > Marketplace
2. Add marketplace from GitHub: `dxta/claude-code-skills`
3. Browse and install individual plugins

### As a Git Submodule (for OpenCode users)

```bash
git submodule add https://github.com/dxta/claude-code-skills.git opencode/skills
```

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
| tools-and-integrations | 2 | - | - | Chrome DevTools, MCP builder |

## Repository Structure

This repository serves a dual purpose:

- **Root level** -- the source of truth. Skills are organized by category (`core/`, `frontend/`, `backend/`, etc.) with each skill in its own directory containing a `SKILL.md`. This layout is directly compatible with OpenCode's skill-loading system.
- **`plugins/` directory** -- the Claude Code marketplace overlay. Each plugin has a `.claude-plugin/plugin.json` manifest and a `skills/` directory of symlinks pointing back to the root-level skill sources. Some plugins also include `agents/` and `commands/` directories.

```
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

Three root-level categories are not packaged as marketplace plugins:

- **sia-code/** (3 skills) -- Tightly coupled to the sia-code CLI tool for codebase indexing and memory. Requires local sia-code installation and is specific to the OpenCode workflow.
- **aws/** (3 skills) -- AWS CDK, cost operations, and serverless EDA. Kept separate due to cloud-provider specificity; intended for users who opt in explicitly.
- **packs/** (2 skills) -- Composite skill packs (feature-dev, fullstack-starter-pack) that bundle other skills together. These reference skills across categories and are designed for OpenCode's pack-loading mechanism.

These remain available when using the repository as a git submodule.

## Development

### Updating Skills

Edit skill files at root level (e.g., `core/when-stuck/SKILL.md`). Run `scripts/sync-plugins.sh` to regenerate plugin symlinks.

### Adding a New Skill

1. Create `<category>/<skill-name>/SKILL.md`
2. Add an entry to `index.json`
3. Update the relevant plugin's symlinks and `plugin.json`
4. Run `scripts/sync-plugins.sh`

## License

MIT
