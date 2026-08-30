---
name: data-governance
description: Establish dataset ownership, metric definitions, quality checks, access purpose, lineage, and safe deprecation. Use when teams report different numbers, no source of truth is known, a dataset needs wider access, quality is unreliable, or data should be retired without breaking unseen consumers.
---

# Data governance

Make approved data easier to use than an unmanaged copy.

## Inputs and context

Gather dataset purpose and contents, metric definitions, producing and consuming systems, owner candidates, quality history, access groups, personal or regulated fields, lineage, retention needs, and current consumers.

## Workflow

1. Write plain-language definitions with computation, grain, timezone, exclusions, owner, and caveats.
2. Assign one accountable owner for each dataset and metric; keep platform operators distinct from business stewards where useful.
3. Establish continuous tests for freshness, volume, uniqueness, nullability, referential integrity, and distribution.
4. Set access by purpose: broadly available for non-personal internal data, least privilege and periodic review for sensitive data.
5. Record upstream and downstream lineage and an incident path for quality failures.
6. Deprecate with an announcement and consumer check before removal; document replacement and deadline.

## Output / decision record

Return definitions, owner and steward, source of truth, quality rules and recent status, access purpose and groups, lineage, retention or deprecation plan, known gaps, and next review date.

## Uncertainty and failure handling

Do not merge conflicting definitions into an ambiguous label. Mark unknown consumers and use a deprecation window before removal. Escalate privacy, lawful-basis, security, and regulated-data questions to qualified reviewers.

## Routing boundaries

Use this skill only for its stated capability and required context. For adjacent work, select a more specific skill from `skill-index.tsv`; do not infer coverage from this department folder or use this skill to authorize actions outside its scope.

## Never

- Let two systems silently claim the same fact as authoritative.
- Repair recurring data errors only in a dashboard.
- Remove a dataset solely because visible usage is low.
