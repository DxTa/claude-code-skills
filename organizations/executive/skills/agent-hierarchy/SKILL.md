---
name: agent-hierarchy
description: Design and audit a multi-agent delivery structure using exclusive write surfaces, builder and read-only reviewer roles, ownership of facts, and enforceable scope checks. Use when dividing repository work among agents, creating charters, preventing file collisions or self-review, or deciding whether an agent belongs in a roster; invoke explicitly because this affects governance.
disable-model-invocation: true
---

# Agent hierarchy

Produce an architecture and governance recommendation; the repository owner decides whether to adopt it.

## Inputs and context

Gather the real repository tree, current agents and charters, desired work, shared files, generation and review workflows, commit authority, CI capabilities, and known collisions. Inspect paths rather than inferring ownership from topic labels.

## Workflow

1. Inventory files and identify the smallest work surfaces that can be made exclusive.
2. Propose only the agents needed, each with identifier, class, remit, authority level, and exact path globs.
3. Assign builders to one editable surface and reviewers to read-only audit surfaces; keep the orchestrator outside both classes.
4. Assign one owner for each class of artifact or fact and document cross-surface handoffs.
5. Define checks for overlapping claims, unowned paths, unauthorized diffs, and producer-reviewer separation; wire them to CI when approved.
6. Test the roster against representative changes and revise until scope failures are observable.

## Output / decision record

Return repository inventory, proposed roster, exclusive surface map, artifact ownership table, authority levels, reviewer pairing, enforcement checks, sample diff results, adoption risks, and an explicit recommendation for the owner.

## Uncertainty and failure handling

When a surface cannot be stated precisely, merge the proposed responsibility into an existing owner or escalate the ambiguity. Treat generated files and shared configuration as explicit ownership decisions. Do not infer that a passing scope check proves a good division of work.

## Routing boundaries

Use this skill only for its stated capability and required context. For adjacent work, select a more specific skill from `skill-index.tsv`; do not infer coverage from this department folder or use this skill to authorize actions outside its scope.

## Never

- Recommend topic-based ownership when agents can edit the same files.
- Let a producer be the sole reviewer of its own output.
- Commit, merge, or change repository policy on the owner's behalf.
