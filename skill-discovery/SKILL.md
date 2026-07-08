---
name: skill-discovery
description: Find and load locally installed skills that are hidden from the default prompt. Use when you need a skill not visible in available_skills — read skill-index.tsv to find it by keyword/domain, then read the SKILL.md path.
---

# Skill Discovery

## When to Use

- You need specialized knowledge for a task but no visible skill matches.
- User asks about a domain (AWS, frontend, testing, perf, GRC, AI platform, etc.) and you suspect a skill exists.
- You see a skill name referenced in AGENTS.md routing or session context but it is not in your available_skills list.

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
| PR review, security audit | `pr-review-toolkit`, `security-auditor`, `code-review-plugin` |
| Video, analytics, streams | `video-analytics`, `video-search`, `rt-vlm` |
| Deployment, vLLM, serving | `deployment`, `deploy`, `evaluation` |
| AI Platform, CVAT, MLDB | `ai-platform-coding-practices`, `ai-platform-review-contract` |
| Documentation, markdown | `docs`, `mcp-builder` |
| Communication, Gmail, Calendar | `gmail`, `gcal`, `gdrive`, `internal-comms` |

### Step 3: Read the matching SKILL.md

Once you find a matching skill name and path from the index, construct the full path:

```bash
read $HOME/.pi/agent/skills/<path-from-index>
```

The `path` column is relative to `$HOME/.pi/agent/skills/`. For example, if the index shows path `mine/perf-optimization/SKILL.md`, the full read path is `$HOME/.pi/agent/skills/mine/perf-optimization/SKILL.md`.

### Step 4: Apply the skill

Follow the loaded skill's instructions. If multiple skills match, load the most specific one first.

## Notes

- Hidden skills have `disable-model-invocation: true` — they are excluded from the system prompt to save tokens, not removed.
- The index is auto-generated. If a skill is missing from the index, search by directory: `find $HOME/.pi/agent/skills -name SKILL.md -path '*keyword*'`.
- GRC/compliance skills live under `third-party/grc-skills/extracted/`.
- Perf skills live under `mine/perf-*`.
- AI platform skills live under `work/ai-platform/`.