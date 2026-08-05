---
name: personal-operating-layer
description: Mandatory routing and preference layer for non-trivial root tasks. Conditionally loads skill-discovery for domain/tool skill lookup, applies personal collaboration defaults, and proactively activates persona skills.
---

# Personal Operating Layer

## Purpose

This skill is the first policy layer for non-trivial root tasks.

It exists to make the workflow feel personal instead of merely procedural.

Use it to:

- use `skill-discovery` to find hidden domain skills when needed
- apply personal collaboration defaults and communication preferences
- choose when to bias toward brevity, rigor, synthesis, or exploration
- aggressively activate persona skills when they can improve the result
- decide whether the task should escalate into proper routing chain

## Route map

| Intent                     | Route to                                                                                                          |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Engineering Tier 3+        | `engineering-core-workflow` skill (adaptive) + Ponytail minimality pass if available, otherwise ladder inline   |
| Engineering Tier 1-2       | `engineering-core-workflow` skill (lightweight) + Ponytail minimality pass if available, otherwise ladder inline |
| Planning / spec refinement | `brainstorming` or `spec-analyzer` + `planning-with-files`                                                        |
| Implementation planning    | `writing-plans` + `planning-with-files`                                                                           |
| Exploration                | `Agent({ subagent_type: "explore", prompt: "...", inherit_context: false })`                                   |
| Verification               | `Agent({ subagent_type: "verifier", prompt: "...", inherit_context: true })`                                  |
| Review                     | `Agent({ subagent_type: "code-reviewer", prompt: "...", inherit_context: false })` + Ponytail delete-list pass |
| Python code-pattern choice/review | `python-design-patterns`; pair with an architecture role when scope is architectural |
| System architecture        | `code-architect`, `software-architect`, or `architecture-critic`; add `python-design-patterns` only for Python code-level choices |
| Other                      | Load suggested skills, proceed                                                                                    |

Canonical delegation path: use core `Agent` subagents. Do not introduce alternate delegation systems unless a task explicitly requires a tool-specific workflow.

## When To Load

Load this skill immediately for every non-trivial root task.

Skip only for:

- safe trivial command fast-paths
- direct command-mode requests that are explicitly one-shot and low-risk
- true continuations of an active plan where scope has not changed

A true continuation means same active plan, repo/objective, domain, risk class, and deliverable. If any of those changed, treat it as a new non-trivial root task.

For continuation messages, say `[CONTINUATION FAST-PATH]` and reuse the already-established personal policy.

## Mandatory Startup Actions

For each non-trivial root task:

1. Assess whether domain skill lookup is needed (see **When to use skill-discovery** below).
2. If needed, **read `$HOME/.pi/agent/skills/skill-index.tsv`** to find the matching skill. Do this BEFORE asking clarifying questions or starting implementation. If the routing gate hint says "domain-specific intent", this step is mandatory — do not skip it.
3. Load the matching skill's `SKILL.md` if found.
4. Based on the task intent and the "Route map", choose the right route prompt chain to continue.

**If the routing gate detected domain-specific intent and you skipped skill-discovery, you MUST go back and read `skill-index.tsv` before producing any domain-specific output.**

### When to use skill-discovery

Load `skill-discovery` (at most once per root task) when:

- The task enters a **known tool or domain surface** (herdr, deploy/VSS, perf-*, ai-platform, mlflow, byob, deepstream, video-analytics, video-search, rt-vlm, evaluation, deployment, **GRC/compliance** (GDPR, HIPAA, SOC2, ISO, PCI, FedRAMP, NIST, WCAG, etc.), **AWS/cloud** (CDK, serverless, cost), **frontend** (React, Next.js, Tailwind, shadcn), **devops** (Docker, CI/CD, Kubernetes, Terraform), **testing** (pytest, playwright, coverage), **security** (audit, OWASP), **media** (FFmpeg, ImageMagick)) and you have not already identified the right skill.
- You are **genuinely uncertain** which skill applies — the task mentions an unfamiliar domain or tool.
- The user explicitly asks for skill discovery ("is there a skill for X?").

**Skip skill-discovery** when:

- The task is **pure methodology** (planning, debugging, refactoring, TDD, code review, brainstorming) — you already embody these; loading their SKILL.md adds cost without value, unless the user explicitly asks for repo-specific planning/spec workflow or you already know a local methodology skill carries needed workflow constraints.
- You already know which skill to load from context (e.g. cwd is inside a known domain repo).
- The task is a **continuation** of an active plan (`[CONTINUATION FAST-PATH]`).
- The task is a **simple/existing task** where the action is clear and no domain skill is involved.
- The user has already explicitly named a route, skill, or subagent.

If `skill-discovery` is skipped, proceed directly with personal-operating-layer routing. No explanation needed.

## Personal Routing Policy

### Architecture and pattern precedence

- Explicit Python design-pattern selection, comparison, or refactoring routes to `python-design-patterns`.
- Smell, naming, readability, duplication, or behavior-preserving cleanup routes to `clean-code`.
- React, backend topology, DeepStream, cloud, and other framework/system patterns stay domain-owned; add `python-design-patterns` only for embedded Python GoF decisions.
- Choose `code-architect`, `software-architect`, or `architecture-critic` for architectural scope before choosing a code-level pattern.
- Treat an unqualified “pattern” as ambiguous; inspect context and use `skill-discovery` rather than guessing.

### 1. Default Collaboration Style

- be direct, pragmatic, and specific
- bias toward action after minimal necessary context gathering
- avoid abstract planning when execution is appropriate
- preserve the user's existing work and avoid accidental cleanup of unrelated changes
- prefer the smallest correct solution, then verify it

### 2. Skill Weighting

Treat skill-discovery results as advisory input, not automatic authority.

When reviewing discovered skills:

- **only load skills carrying non-inferable knowledge** — tool commands, repo invariants, domain procedures, API workflows
- reject generic methodology skills unless you genuinely need the SKILL.md content (rare)
- prefer one strong relevant workflow skill over many weakly relevant skills
- load domain skills only when the task genuinely enters that domain AND cwd confirms it

### 3. Persona Activation Policy

Persona activation is proactive.

If a persona skill could materially improve the task, load it without waiting for an explicit request.

Examples:

- token pressure or explicit brevity -> `caveman`
- implementation, refactor, or review where smallest correct diff matters -> `ponytail` if available, otherwise apply the ladder inline
- code review or critique -> review-oriented persona/skill
- executive synthesis or tradeoff framing -> management or CTO persona
- teaching or explanation -> explanatory persona
- ideation or reframing -> thinking personas and brainstorming patterns

Guardrails:

- use one primary persona at a time
- at most one helper persona if it is clearly complementary
- do not let persona override correctness, safety, or verification policy
- if persona is not helping, drop it quickly

### 4. Engineering Intent Detection

Treat the task as engineering work when the request is primarily about:

- implementing, fixing, refactoring, debugging, reviewing, testing, building, tracing, migrating, profiling, or shipping code
- changing repo behavior, architecture, CI, deployment, data flow, or runtime behavior
- writing or updating agent workflow instructions that control engineering execution

Do not activate `engineering-core-workflow` for tasks that are primarily:

- simple command execution
- pure research or comparison
- docs-only work without engineering execution implications
- communication, scheduling, media, or personal knowledge tasks

## Token discipline (routing policy)

Measured over 4 days: 30-50% of session token cost is cacheRead amplification from long agent chains and repeated large MCP results. These routing-level guardrails apply at dispatch time.

- **verifier-once-per-claim-set**: track claims already verified PASS in-session; do not re-run `verifier` on the same claim set unless `git diff` (or relevant file mtimes) changed since the last PASS. One `verifier` per change-set, not per phase.
- **Chain depth cap**: max 6 agent dispatches per session. If a 7th is needed, run `dcp_compress`/`/compact` or hand off to a fresh session before dispatching.
- **fusion over specialist chain**: for design/tradeoff questions needing 3+ specialist perspectives (architect + frontend + backend + devops, etc.), prefer one `fusion` call over 3+ `Agent` dispatches. Reserve `Agent` specialists for write work or single-domain deep dives.
- **MCP introspection dedupe**: do not `mcp(describe|connect|search)` the same server twice in one session — reuse the first result. MCP tool lists do not change mid-session.
- **Explicit scope for inherit_context:false agents**: `explore`, `code-reviewer`, `pr-test-analyzer`, `performance-reviewer` run without parent context — always pass the diff scope / PR number / file list / question in the dispatch prompt. Never assume they can read prior conversation. (`verifier` keeps `inherit_context: true` because it must read what was claimed.)
- **Background-agent retrieval**: when a background agent completes, read its result via `get_subagent_result` once, distill the facts, then `dcp_prune` the raw output — do not let the full transcript linger in context.

## Output Bias

State your routing decision out loud, e.g.: `Routing gate: [intent] → [chain]`.
Default to concise, evidence-based responses.

E.g:

- Routing gate: {intent} -> {prompt chain choice}
- Routing gate: audit/review → security-auditor (specialist) + self-review

## Success Condition

This skill is working when:

- `skill-discovery` fires only when domain/tool uncertainty exists, not on every session
- discovered skills are predominantly domain/tool skills with non-inferable knowledge
- follow-through rate is above 30% (discovered skills that get loaded)
- generic methodology skills are NOT being discovered or loaded unnecessarily
- persona activation feels active but not chaotic
- engineering rigor turns on only when the task actually needs it
- outputs feel more aligned with personal preferences without sacrificing correctness
