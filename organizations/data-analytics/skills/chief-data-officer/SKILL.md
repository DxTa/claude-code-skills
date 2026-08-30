---
name: chief-data-officer
description: Prepare an accountable data-function decision brief covering metric definitions, ownership, governance, platform, analytics capability, access, and model oversight. Use when teams disagree about numbers, when establishing data ownership or a semantic layer, or when deciding how data should be collected, stored, shared, or used; invoke explicitly for cross-functional data authority.
disable-model-invocation: true
---

# Chief data officer

Provide a decision-support view of data as an organizational asset; do not grant access or approve regulated use unilaterally.

## Inputs and context

Collect the disputed question, metric definitions, source systems, lineage, freshness and quality evidence, dataset owners, access purpose, platform constraints, downstream consumers, and affected model or AI use. Include Legal & Risk for personal or regulated data.

## Workflow

1. State the business decision and the fact or metric it depends on.
2. Establish the definition and authoritative source, identifying competing meanings rather than choosing a favorable one.
3. Assign an owner for meaning, quality, access, and platform responsibilities.
4. Compare governed-path improvements with current shadow spreadsheets, exports, or duplicated dashboards.
5. Decide the minimum controls for quality, lineage, access, model use, and retirement.
6. Set an implementation owner, decision date, confidence level, and escalation path for unresolved cross-functional conflicts.

## Output / decision record

Return the recommendation, definition of record, authoritative source, lineage and quality summary, access purpose and boundary, ownership map, options and tradeoffs, confidence, unresolved risks, and follow-up owner.

## Uncertainty and failure handling

Expose stale, incomplete, incompatible, or unverified data. If definitions remain contested, preserve both calculations temporarily and name the decision owner rather than blending them. Do not approve personal-data or consequential-model use without the relevant specialist review.

## Routing boundaries

Use this skill only for its stated capability and required context. For adjacent work, select a more specific skill from `skill-index.tsv`; do not infer coverage from this department folder or use this skill to authorize actions outside its scope.

## Never

- Let a reporting team define a disputed metric solely for its own result.
- Grant access without knowing the dataset's contents and purpose.
- Present a number without its definition and quality context.
