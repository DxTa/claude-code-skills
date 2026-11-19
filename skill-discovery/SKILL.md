---
name: skill-discovery
description: Proactively find and load the skills a task needs. Run at the start of each new task, at each phase change (plan, implement, debug, review, done), and when a domain term appears that no visible skill covers. Searches the skill index cheaply; never loads the whole index.
---

# Skill Discovery

## When to Run

- Start of each new task.
- Each phase change: plan, implement, debug, review, verify, done.
- A domain term appears (AWS, perf, GRC, compliance, data, marketing) and no visible skill covers it.
- Not on every turn. Within one phase, keep the current selection, except for a newly uncovered concern: search for it at once.
- Subagents: this text is preloaded. Start at Search Cheaply.

## Search Cheaply

The full index is about 110 KB. Do not open it. Search it.

1. Semantic search, one sentence describing the task:

```bash
node "$HOME/.dotfiles/pi/scripts/agent-semantic-search.mjs" search --catalog skills --query "<one-sentence task>" --top-k 5
```

`results` are candidates, not decisions. If `fallback` is `lexical` (stale embeddings), treat the ranking as weaker. If the command fails, use step 2.

2. Keyword search, output capped:

```bash
grep -i "<keyword>" "$HOME/.pi/agent/skills/skill-index.tsv" | cut -f1,3 | head -20
```

Columns: `name`, `source`, `path`, `description`. For close calls, replace `cut -f1,3` with `cut -f1,4 | cut -c1-200` to see descriptions.

3. Directory fallback when the index misses a skill:

```bash
command find -H "$HOME/.pi/agent/skills" -name SKILL.md -path "*<keyword>*" | head -20
```

## Select

- One primary skill that drives the phase.
- Add a secondary skill for each separate concern the phase has. No fixed cap. Each added skill must change a concrete action. Example: TDD plus clean-code for a refactor.
- A keyword hit is not a reason to load. Load a skill because it changes what you will do.
- Sensitive, consequential, or role-title skills (for example chief-*, legal, HR, finance, compliance sign-off) load only when the user or an agent's `skills:` list names them. Do not add them to automatic routing.

## Load and Apply

1. Read each chosen SKILL.md fully with `read`. Path: `$HOME/.pi/agent/skills/<path column>`.
2. Follow its `Never` rules, routing boundaries, and referenced files.
3. Stop loading when the phase is covered.

## Report

One line:

- `Skills: <primary>; +<secondary>, <secondary>`
- `Skills: none fit (<query>)`, then continue with normal tools.

## Self-Reflect at Each Phase Change

Answer both in one line each before the next phase:

1. Did a loaded skill change any action? No: drop it.
2. Is a concern uncovered now? Yes: search for that concern only.

## Keyword Map

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

## Notes

- `disable-model-invocation: true` excludes a skill from normal system discovery; it remains loadable through an explicit agent `skills:` selection or explicit skill request. Workflow agents expose explicitly selected hidden skills without making them globally automatic.
- Agent frontmatter `skills:` values must resolve by skill name or exact indexed path. Index aliases are for discovery; use the `path` column when reading files.
- The index is auto-generated. If a skill is missing from the index, search by directory: `command find -H $HOME/.pi/agent/skills -name SKILL.md -path '*keyword*'`.
- GRC/compliance skills live under `third-party/grc-skills/extracted/`.
- Perf skills live under `mine/perf-*`.
- AI platform skills live under `work/ai-platform/`.
