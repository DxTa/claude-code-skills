---
name: personal-operating-layer
description: Mandatory routing and preference layer for non-trivial root tasks. Conditionally invokes skill-suggests for domain/tool tasks, applies personal collaboration defaults, and proactively activates persona skills.
---

# Personal Operating Layer

## Purpose

This skill is the first policy layer for non-trivial root tasks.

It exists to make the workflow feel personal instead of merely procedural.

Use it to:

- enforce `skill-suggests` before deeper planning or execution
- apply personal collaboration defaults and communication preferences
- choose when to bias toward brevity, rigor, synthesis, or exploration
- aggressively activate persona skills when they can improve the result
- decide whether the task should escalate into proper routing chain

## Route map

| Intent               | Route to                                                                                                          |
| -------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Engineering Tier 3+  | `engineering-core-workflow` skill (adaptive) + Ponytail minimality pass if available, otherwise ladder inline   |
| Engineering Tier 1-2 | `engineering-core-workflow` skill (lightweight) + Ponytail minimality pass if available, otherwise ladder inline |
| Exploration          | `Agent({ subagent_type: "explore", prompt: "...", inherit_context: true })`                                   |
| Verification         | `Agent({ subagent_type: "verifier", prompt: "...", inherit_context: true })`                                  |
| Review               | `Agent({ subagent_type: "code-reviewer", prompt: "...", inherit_context: true })` + Ponytail delete-list pass |
| Other                | Load suggested skills, proceed                                                                                    |

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

1. Assess whether `skill-suggests` would add value (see **When to invoke skill-suggests** below).
2. If invoked, review the suggested skills through this personal policy layer.
3. Load the recommended skills that materially help.
4. Based on the task intent and the "Route map", choose the right route prompt chain to continue.

### When to invoke skill-suggests

Invoke `skill-suggests` (at most once per root task) when:

- The task enters a **known tool or domain surface** (herdr, deploy/VSS, perf-*, ai-platform, mlflow, byob, deepstream, video-analytics, video-search, rt-vlm, evaluation, deployment) and you have not already identified the right skill.
- You are **genuinely uncertain** which skill applies — the task mentions an unfamiliar domain or tool.
- The user explicitly asks for skill discovery ("is there a skill for X?").

**Skip skill-suggests** when:

- The task is **pure methodology** (planning, debugging, refactoring, TDD, code review, brainstorming) — you already embody these; loading their SKILL.md adds cost without value.
- You already know which skill to load from context (e.g. cwd is inside a known domain repo).
- The task is a **continuation** of an active plan (`[CONTINUATION FAST-PATH]`).
- The task is a **simple/existing task** where the action is clear and no domain skill is involved.
- The user has already explicitly named a route, skill, or subagent.

When passing task context to `skill-suggests`, always include the current working directory (cwd) so path-gated skills can be filtered correctly.

If `skill-suggests` is skipped, proceed directly with personal-operating-layer routing. No explanation needed.

Invoke `skill-suggests` at most once per root task. Never retry in the same turn.

If `skill-suggests` fails, times out, or reaches max turns, fail open transparently and continue with parent routing:

`skill-suggests unavailable after one attempt; proceeding with personal-operating-layer direct routing. No skill recommendation produced.`

## Personal Routing Policy

### 1. Default Collaboration Style

- be direct, pragmatic, and specific
- bias toward action after minimal necessary context gathering
- avoid abstract planning when execution is appropriate
- preserve the user's existing work and avoid accidental cleanup of unrelated changes
- prefer the smallest correct solution, then verify it

### 2. Skill Weighting

Treat `skill-suggests` output as advisory input, not automatic authority.

When reviewing suggested skills:

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

## Output Bias

State your routing decision out loud, e.g.: `Routing gate: [intent] → [chain]`.
Default to concise, evidence-based responses.

E.g:

- Routing gate: {intent} -> {prompt chain choice}
- Routing gate: audit/review → security-auditor (specialist) + self-review

## Success Condition

This skill is working when:

- `skill-suggests` fires only when domain/tool uncertainty exists, not on every session
- suggested skills are predominantly domain/tool skills with non-inferable knowledge
- follow-through rate is above 30% (suggestions that get loaded)
- generic methodology skills are NOT being suggested or loaded unnecessarily
- persona activation feels active but not chaotic
- engineering rigor turns on only when the task actually needs it
- outputs feel more aligned with personal preferences without sacrificing correctness
