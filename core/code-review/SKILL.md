---
name: code-review
description: Routes code-review situations to the right practice, and executes a two-axis review (Standards + Spec) of a diff via parallel sub-agents. Use when reviewing a branch/PR/work-in-progress, receiving review feedback, or before any completion claim. Dispatches receiving-code-review, requesting-code-review, or verification-before-completion for their specialized concerns.
compatibility: opencode
---

# Code Review

Router + two-axis review executor. Three concerns live in sibling skills; this skill routes to them and runs the actual diff review.

## Core Principle

**Technical correctness over social comfort.** Verify before implementing. Ask before assuming. Evidence before claims.

## Route first

```
SITUATION?
│
├─ Received feedback on my code
│  └─ → `receiving-code-review` (technical evaluation, not performative agreement)
│
├─ Want a review of completed work
│  ├─ Major feature / before merge → run the Two-Axis Review below, then Ponytail delete-list pass
│  └─ After each task in subagent-driven dev → run Two-Axis Review
│
└─ About to claim work is complete
   └─ → `verification-before-completion` (evidence gate, not review)
```

## Two-Axis Review (the actual review)

Reviews the diff between `HEAD` and a fixed point the user supplies (commit SHA, branch, tag, `main`, `HEAD~5`). Two axes run as **parallel sub-agents** so they don't pollute each other's context; this skill aggregates.

### 1. Pin the fixed point
Capture the diff command once: `git diff ...HEAD` (three-dot, compares against merge-base). Note commits via `git log ..HEAD --oneline`. Confirm the ref resolves and the diff is non-empty before spawning sub-agents.

### 2. Identify the spec source (for the Spec axis)
Look in order: issue refs in commit messages (`#123`, `Closes #45`) → a path the user passed → a PRD/spec under `docs/`, `specs/`, or `.scratch/` matching the branch. If none found, ask the user; if they say there is no spec, the Spec sub-agent skips and reports "no spec available".

### 3. Identify the standards sources
Anything documenting how code should be written: `CODING_STANDARDS.md`, `CONTRIBUTING.md`, lint/style configs. Plus the **smell baseline** below always applies.

### 4. Smell baseline (Fowler)
Always carries this fixed set of Fowler code smells (_Refactoring_, ch.3) — applies even when a repo documents nothing. Two rules bind it:
- **The repo overrides.** A documented repo standard wins; where it endorses something the baseline would flag, suppress the smell.
- **Always a judgement call.** Each smell is a labelled heuristic, never a hard violation. Skip anything tooling already enforces.

Match each against the diff:
- **Mysterious Name** — function/variable/type whose name doesn't reveal what it does. → rename.
- **Duplicated Code** — same logic shape in >1 hunk/file. → extract shared shape.
- **Feature Envy** — method reaching into another object's data more than its own. → move method onto the data it envies.
- **Data Clumps** — same few fields/params travelling together. → bundle into one type.
- **Primitive Obsession** — primitive standing in for a domain concept. → give it a small type.
- **Repeated Switches** — same `switch`/`if`-cascade recurs across the change. → polymorphism or shared map.
- **Shotgun Surgery** — one logical change forces scattered edits across many files. → gather into one module.
- **Divergent Change** — one file edited for several unrelated reasons. → split.
- **Speculative Generality** — abstraction/params/hooks added for needs the spec doesn't have. → delete; inline back.
- **Message Chains** — long `a.b().c().d()` the caller shouldn't depend on. → hide behind one method.
- **Middle Man** — class/function that mostly just delegates. → cut it.
- **Refused Bequest** — subclass/implementer ignoring most of what it inherits. → drop inheritance, use composition.

### 5. Spawn both sub-agents in parallel
One message, two `Agent` calls, `general-purpose` for both.

**Standards sub-agent** — include: the diff command + commit list, the standards-source files found, **the smell baseline above pasted in full** (the sub-agent has no other access). Brief: "Report per file/hunk — (a) every place the diff violates a documented standard: cite the standard (file + rule); and (b) any baseline smell: name it and quote the hunk. Distinguish hard violations (documented-standard breaches) from judgement calls (baseline smells). A documented repo standard overrides the baseline. Skip anything tooling enforces. Under 400 words."

**Spec sub-agent** — include: the diff command + commit list, the path or fetched contents of the spec. Brief: "Report: (a) requirements the spec asked for that are missing or partial; (b) behaviour in the diff that wasn't asked for (scope creep); (c) requirements that look implemented but where the implementation looks wrong. Quote the spec line for each finding. Under 400 words."

If the spec is missing, skip the Spec sub-agent and note it in the final report.

### 6. Aggregate
Present the two reports under `## Standards` and `## Spec` headings, verbatim or lightly cleaned. Do **not** merge or rerank — the two axes are deliberately separate. End with a one-line summary: total findings per axis, and the worst issue within each axis. Don't pick a single winner across axes.

### 7. Ponytail delete-list pass
After the review, if the diff added abstractions, dependencies, wrappers, or extra files, run a Ponytail delete-list pass. Use `/ponytail-review` when available; otherwise apply the checklist inline: reuse existing helper, stdlib/native first, delete speculative flexibility, shrink wrappers.

## Why two axes
A change can pass one axis and fail the other. Code that follows every standard but implements the wrong thing → Standards pass, Spec fail. Code that does exactly what the issue asked but breaks conventions → Spec pass, Standards fail. Reporting them separately stops one axis from masking the other.

## Integration
- **Subagent-driven dev:** Two-Axis Review after each task, then Ponytail pass, then `verification-before-completion` before next.
- **Pull requests:** Verify tests pass, run Two-Axis Review before merge.
- **Receiving feedback:** route to `receiving-code-review`; do not implement before verifying.

Verify. Question. Then implement. Evidence. Then claim.