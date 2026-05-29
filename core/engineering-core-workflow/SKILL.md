---
name: engineering-core-workflow
description: Engineering-only execution layer. Activates planning, retrieval, debugging, TDD, verification, review, and continuity requirements for engineering work.
---

# Engineering Core Workflow

## Purpose

This skill is the engineering-only rigor layer.

It should activate only when the task intent is clearly software-engineering work.

Its job is to turn a broad engineering request into a disciplined execution flow using:

- planning and continuity
- retrieval-first exploration
- systematic debugging
- TDD where behavior changes are being made
- verification before completion
- code review discipline

## Activation Criteria

Load this skill when the task is primarily about:

- implementing or fixing code
- refactoring or behavior changes
- debugging or root-cause analysis
- test, build, CI, deployment, migration, or repo workflow changes
- code review with technical findings
- agent workflow or automation changes that govern engineering execution

Do not load this skill for tasks that are merely:

- simple safe shell commands
- pure research or comparison without engineering execution
- lightweight docs or communication tasks

## Required Companion Skills

Once active, strongly prefer the following companion skills as needed:

- `planning-with-files` — use as continuity/sync discipline for the existing active plan file; do not create a separate plan when pi-plan-auto or another planning tool already supplied one
- `context-management`
- `systematic-debugging`
- `test-driven-development`
- `verification-before-completion`
- `code-review`
- `sia-code` and `sia-code/health-check`

## Execution Model

### 1. Continuity First

For non-trivial engineering work, maintain durable task continuity.

- use `planning-with-files` against the existing active plan file when one exists
- keep the active plan file current instead of creating duplicate plan artifacts
- treat todos as live execution state and plans as durable context

### 2. Retrieval-First Exploration

Prefer structured retrieval and repo-aware search before repetitive shell exploration.

- use `sia-code` when the index is healthy and the query is code-oriented
- for code-oriented engineering tasks, start with `sia-code_engineering_bootstrap`; if health is stale or degraded, fall back to `glob`/`grep` or ask before indexing
- use `glob`/`grep` for markdown, plans, notes, and config-heavy discovery
- for Chrome DevTools MCP, prefer an existing Chrome remote debugging endpoint and distinguish MCP server processes from browser processes before assuming Chrome was relaunched
- if retrieval is unhealthy or inappropriate for the artifact type, fall back explicitly instead of silently pretending no context exists

### 3. Debug Before Fixing

When facing failures or unexpected behavior:

- load `systematic-debugging`
- identify root cause before proposing fixes
- avoid speculative changes

### 4. TDD For Behavior Changes

For feature work and bug fixes, follow TDD unless a concrete exception applies.

- write the failing test first
- verify the failure
- write the minimum code to pass
- refactor only after green

### 5. Verification Gate

Before claiming success:

- run the proving command fresh
- inspect output and exit status
- state the result only with evidence

### 6. Review Discipline

For review requests, lead with findings, not summaries.

Prioritize:

- bugs
- regressions
- missing tests
- risky assumptions

## Delegation Model

Use `Agent({ subagent_type, prompt, inherit_context })` from `@tintinweb/pi-subagents` when delegation materially improves throughput or quality.

### When to delegate

| Step           | Inline or Delegate | When                                                                    |
| -------------- | ------------------ | ----------------------------------------------------------------------- |
| Status check   | Inline             | Always trivial                                                          |
| Continuity     | Inline             | Read plan file                                                          |
| Planning       | Inline             | Most cases                                                              |
| Retrieval      | Inline or Delegate | Inline for targeted, `Explore` for broad recon                          |
| Implementation | Inline             | Main agent + TDD skill                                                  |
| Verification   | Inline or Delegate | Inline for simple, `Agent({ subagent_type: "verifier" })` for high-risk |
| Review         | Delegate           | `Agent({ subagent_type: "code-reviewer" })` for fresh eyes              |
| Parallel recon | Delegate           | `Agent({ subagent_type: "Explore", run_in_background: true })` × N      |

### Delegation patterns

```
# Foreground — parent waits (natural boomerang replacement)
Agent({ subagent_type: "verifier", prompt: "Verify all claims...", inherit_context: true })

# Background — parallel work
Agent({ subagent_type: "Explore", prompt: "Map the auth module", run_in_background: true })
```

- parallelize analysis when scopes do not overlap
- serialize edits when file ownership overlaps
- keep final synthesis and integration in the parent
- document delegation in the task plan when used
- subagents cannot spawn further subagents — parent always orchestrates

## Anti-Patterns

Avoid:

- loading full engineering rigor for non-engineering work
- calling retrieval-first while actually thrashing in shell
- claiming verification without fresh command output
- replacing task plans with todo-only tracking
- persona-driven style overriding technical rigor

## Success Condition

This skill is working when engineering tasks show:

- stronger planning continuity
- less shell churn
- better debugging discipline
- more explicit verification evidence
- cleaner separation between lightweight tasks and engineering-heavy tasks
