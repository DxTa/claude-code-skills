---
name: skill-discovery
description: Find and load locally installed skills that match a task but are absent from available_skills. Use skill-index.tsv to search by keyword/domain, then read the exact SKILL.md path before applying it.
---

# Skill Discovery

## When to Use

- You need specialized knowledge for a task but no visible skill matches.
- User asks about a domain (AWS, frontend, testing, perf, GRC, AI platform, etc.) and you suspect a skill exists.
- You see a skill name referenced in AGENTS.md routing or session context but it is not in your available_skills list.
- You need an organizational workflow such as finance, legal-risk, people, operations, revenue, marketing, customer experience, or corporate strategy.

## How to Find Hidden Skills

### Step 1: Read the skill index

The index is at the **skills root**, NOT inside `mine/` or any subdirectory:

```bash
read $HOME/.pi/agent/skills/skill-index.tsv
```

**Do NOT** use `skills/mine/skill-index.tsv` or `skills/mine/skill-discovery/skill-index.tsv` — the file is directly at `skills/skill-index.tsv`.

The TSV has 4 columns: `name`, `source`, `path`, `description`.

If the file is not found, fall back:
```bash
find $HOME/.pi/agent/skills -maxdepth 1 -name 'skill-index.tsv'
```

After reading index, use semantic search for advisory candidates:

```bash
node "$HOME/.dotfiles/pi/scripts/agent-semantic-search.mjs" search --catalog skills --query "<one-sentence task>" --top-k 5
```

Search returns ordered `results` array with up to five candidates, not one selected skill. Use candidates to choose one primary and, when separate concerns need them, up to two secondary skills. If command fails because model, cache, or index is unavailable, continue with keyword/directory matching; never use stale output.

### Step 2: Match by keyword

Scan the `description` column for keywords related to the task. Examples:

| User asks about | Skill name to look for |
|---|---|
| React, Next.js, Tailwind | `frontend-development`, `frontend-design`, `ui-styling`, `web-frameworks` |
| AWS, CDK, serverless, Lambda | `aws-cdk-development`, `aws-serverless-eda`, `aws-cost-operations` |
| Performance, profiling, CUDA graphs | `perf-analysis`, `perf-cuda-graphs`, `perf-memory-tuning`, `perf-optimization` |
| GDPR, HIPAA, SOC2, compliance | `gdpr-compliance`, `hipaa-compliance`, `soc2`, `iso27001` |
| Docker, CI/CD, GitHub Actions | `ci-cd-pipeline-builder`, `github-act`, `cicd` |
| Testing, coverage, webapp | `test-coverage-analyzer`, `webapp-testing`, `performance-test-suite` |
| PR review, security audit | `pr-review-toolkit`, `security-test-scanner`, `code-review-plugin` |
| Video, analytics, streams | `video-analytics`, `video-search`, `rt-vlm` |
| Deployment, vLLM, serving | `deployment`, `deploy` |
| AI Platform, CVAT, MLDB | `ai-platform-coding-practices`, `ai-platform-review-contract`, `ai-platform-annotation-cvat`, `ai-platform-dataset-dvc` |
| Documentation, markdown | `docs` for NeMo-RL; otherwise search repository guidance |
| Communication, Gmail, Calendar | `gmail`, `gcal`, `gdrive`, `internal-comms` |
| Organizational workflows | Search `mine/organizations/` for department and skill name |

### Step 3: Read matching SKILL.md files

For every primary or secondary skill you choose, construct its full path from the indexed name and path. Prefer exact description matches over name-only matches:

```bash
read $HOME/.pi/agent/skills/<path-from-index>
```

The `path` column is relative to `$HOME/.pi/agent/skills/`. For example, if the index shows path `mine/perf-optimization/SKILL.md`, the full read path is `$HOME/.pi/agent/skills/mine/perf-optimization/SKILL.md`. Organizational imports use paths such as `$HOME/.pi/agent/skills/mine/organizations/finance/skills/financial-modeling/SKILL.md`.

### Step 4: Apply selected skills

Read each selected `SKILL.md` completely, including `Never`, routing boundaries, and referenced files. Use one primary skill; add at most two secondary skills only when each covers a separate concern. Stop when task is covered. Do not treat a skill name, agent name, or keyword hit as proof that the skill applies.

For sensitive, consequential, or role-title skills, require explicit user or agent selection and preserve the skill's decision-support boundaries. Do not add them to broad automatic routing rules.

## Notes

- `disable-model-invocation: true` excludes a skill from normal system discovery; it remains loadable through an explicit agent `skills:` selection or explicit skill request. Workflow agents expose explicitly selected hidden skills without making them globally automatic.
- Agent frontmatter `skills:` values must resolve by skill name or exact indexed path. Index aliases are for discovery; use the `path` column when reading files.
- The index is auto-generated. If a skill is missing from the index, search by directory: `find $HOME/.pi/agent/skills -name SKILL.md -path '*keyword*'`.
- GRC/compliance skills live under `third-party/grc-skills/extracted/`.
- Perf skills live under `mine/perf-*`.
- AI platform skills live under `work/ai-platform/`.