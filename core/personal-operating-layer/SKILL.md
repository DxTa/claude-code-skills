---
name: personal-operating-layer
description: Mandatory routing and preference layer for non-trivial root tasks. Enforces skill-suggests, applies personal collaboration defaults, and proactively activates persona skills.
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

| Intent               | Route to                                                                          |
| -------------------- | --------------------------------------------------------------------------------- |
| Engineering Tier 3+  | `engineering-core-workflow` skill (adaptive)                                      |
| Engineering Tier 1-2 | `engineering-core-workflow` skill (lightweight)                                   |
| Exploration          | `Agent({ subagent_type: "Explore", prompt: "...", inherit_context: true })`       |
| Verification         | `Agent({ subagent_type: "verifier", prompt: "...", inherit_context: true })`      |
| Review               | `Agent({ subagent_type: "code-reviewer", prompt: "...", inherit_context: true })` |
| Other                | Load suggested skills, proceed                                                    |

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

1. Invoke `skill-suggests` with the user request.
2. Review the suggested skills through this personal policy layer.
3. Load the recommended skills that materially help.
4. Based on the task intent and the "Route map", choose the right route prompt chain to continue

Do not skip `skill-suggests` for non-trivial root tasks.

If the user explicitly names a route, skill, or subagent, treat that as strong routing input, not permission to skip `skill-suggests`. The suggested result may still be `No specific skill needed - explicit route is sufficient.`

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

Treat `skill-suggests` as mandatory input, not automatic authority.

When reviewing suggested skills:

- prefer process skills before implementation skills
- prefer one strong relevant workflow skill over many weakly relevant skills
- load domain skills only when the task genuinely enters that domain
- reject decorative or redundant skills when they do not improve the task

### 3. Persona Activation Policy

Persona activation is proactive.

If a persona skill could materially improve the task, load it without waiting for an explicit request.

Examples:

- token pressure or explicit brevity -> `caveman`
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

- non-trivial tasks always run through `skill-suggests`
- persona activation feels active but not chaotic
- engineering rigor turns on only when the task actually needs it
- outputs feel more aligned with personal preferences without sacrificing correctness
