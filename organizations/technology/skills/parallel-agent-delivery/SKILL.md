---
name: parallel-agent-delivery
description: Determines when work can be safely split across agents or sessions and defines disjoint surfaces, handoffs, and verification. Use for broad audits, independent implementation tasks, or parallel planning; do not use to parallelize coupled edits or bypass a repository owner's review and approval.
---

# Parallel agent delivery

Parallel work is safe only when its boundaries can be demonstrated, not merely hoped for.

## Inputs and context

Collect the parent objective, task graph, repository and file ownership, dependencies, shared state, required tools, acceptance criteria, coordination channel, deadlines, and approval policy. Identify sensitive data and actions that cannot be delegated.

## Workflow

1. Break the objective into outputs and dependencies. Mark each task's inputs, exclusive write surface, read-only sources, and verifier.
2. Dispatch in parallel only when tasks have disjoint writes, no prerequisite output, and independent acceptance checks. Keep coupled planning and integration sequential.
3. Give each worker a complete brief: goal, allowed paths, exclusions, assumptions, expected artifact, and structured return format. Avoid sharing credentials or unnecessary sensitive context.
4. Require each result to report files changed, evidence, unresolved issues, and any deviation. Review every result before integration; resolve disagreements against authoritative repository evidence.
5. Integrate through the repository's normal owner-approved review path. Run combined checks after integration and preserve a rollback point.
6. Stop or re-sequence work when a hidden dependency, overlapping file, failed check, or changed requirement appears.

## Output and decision record

Return the task graph, parallelization proof, worker briefs, write-surface map, dependencies, result review, integration order, checks and outcomes, approval status, and rollback plan.

## Uncertainty and failure handling

Treat an unclear ownership boundary or shared mutable state as a sequential dependency. A worker that returns incomplete or conflicting evidence is not automatically retried; quarantine its output and request the missing information through the owner-approved process.

## Routing boundaries

Use this skill only for its stated capability and required context. For adjacent work, select a more specific skill from `skill-index.tsv`; do not infer coverage from this department folder or use this skill to authorize actions outside its scope.

## Never

- Never assign two workers the same write surface or merge unreviewed output.
- Never expose credentials or sensitive context merely to increase parallelism.
- Never commit, merge, or alter an owned repository without human approval.
