---
name: branch-and-worktree-workflow
description: Plans isolated Git branch or worktree use for independent changes and clean integration. Use when parallel efforts, long-running work, rebasing, merging, or review preparation could disturb a repository; do not use to rewrite another person's history or bypass repository ownership and review policy.
---

# Branch and worktree workflow

Use isolation to protect unrelated work and make integration reviewable. The repository's owner and contribution policy remain authoritative.

## Inputs and context

Identify the repository root, current branch and status, upstream default branch, repository owner, requested change, collaborators, worktree locations, branch naming policy, review checks, and integration target. Capture the starting commit and any uncommitted work before creating anything.

## Workflow

1. Confirm the working tree is understood and branch from the published upstream base rather than an accidental local tip. Do not disturb uncommitted changes.
2. Create a dedicated branch or worktree for work that spans sessions or can proceed independently. Keep each write surface and concern disjoint.
3. Work in small coherent commits. Keep the branch updated with its base according to repository policy and resolve conflicts early.
4. Before integration, inspect the full diff, remove temporary files, run the repository's required checks, and verify the branch merges or rebases cleanly without losing unrelated work.
5. Ask the authorized maintainer to approve merge, rebase, or cherry-pick. After integration, remove obsolete worktrees only with confirmation and preserve any needed branch references.

## Output and decision record

Return the base and starting commit, branch/worktree path, scope boundary, commit summary, checks run and results, merge status, conflicts or residual risks, and the human approval required for integration or cleanup.

## Uncertainty and failure handling

Stop when repository ownership, base branch, worktree state, or cleanup authority is unclear. If checks fail or a conflict changes semantics, report the exact state and leave the branch intact for review. Never infer that a clean merge means the change is correct.

## Routing boundaries

Use this skill only for its stated capability and required context. For adjacent work, select a more specific skill from `skill-index.tsv`; do not infer coverage from this department folder or use this skill to authorize actions outside its scope.

## Never

- Never reset, discard, force-push, or rewrite history belonging to another contributor without explicit authority.
- Never share a write surface between parallel efforts without a deliberate integration step.
- Never merge or remove a worktree without the repository owner's approval.
