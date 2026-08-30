---
name: interface-redesign
description: Improve an existing interface by auditing real tasks, separating structural from visual problems, and sequencing high-impact changes. Use this when a product feels dated or generic, a redesign is proposed, or you need to choose restyling over rebuilding.
---

# Interface redesign

Judge changes against user tasks and measurable product outcomes, not taste alone.

## Inputs and context

Collect the real interface, target users and tasks, device widths, analytics or usability evidence, design tokens and components, constraints, baseline friction, and the outcome to improve. Mark visual hypotheses separately from observed problems.

## Workflow

1. Walk the primary task as a new and returning user on representative devices; capture exact states and transitions.
2. Classify findings as structural, systemic, craft, or cosmetic, with severity and evidence.
3. Link each significant finding to a user consequence and measurable outcome such as completion, error, or conversion.
4. Test whether token, hierarchy, state, or component changes solve the problem before recommending a rebuild.
5. Sequence changes by user impact, confidence, effort, and reversibility; define a validation checkpoint.

## Output and decision record

Return findings with location, evidence, consequence, severity, proposed change, effort, expected measure, assumptions, and a first-step plan. State what is deliberately not changing.

## Uncertainty and failure handling

Do not infer usability from a screenshot or stakeholder preference. If analytics and observation disagree, run a focused usability test or instrumentation review before committing to a direction.

## Routing boundaries

Use this skill only for its stated capability and required context. For adjacent work, select a more specific skill from `skill-index.tsv`; do not infer coverage from this department folder or use this skill to authorize actions outside its scope.

## Never

- Rebuild when a measured restyle addresses the structural issue.
- Call aesthetic preference a usability finding without user evidence.
- Hide empty, loading, error, narrow, or accessibility states from the audit.
