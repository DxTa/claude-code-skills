---
name: unit-economics
description: Evaluate contribution margin, acquisition cost, payback, lifetime value, and cohort behavior to decide whether growth, pricing, or a channel is economically sustainable.
disable-model-invocation: true
---

# Unit economics

This produces financial decision support. Preserve the unit definition, cohort window, source dates,
accounting basis, currency, and jurisdiction assumptions. Qualified finance professionals must
interpret material accounting or tax effects; expose uncertainty in observed and estimated inputs.

## Inputs and context

Collect the unit being measured, revenue and discounts, variable delivery costs, sales and marketing
spend, acquisition counts, retention and expansion data, segment definitions, and observation window.

## Workflow

1. Define one unit and period, then reconcile its revenue to source records.
2. Calculate contribution using all costs that change with the unit; label allocated costs separately.
3. Compute acquisition cost from the full relevant spend and matching acquired population.
4. Estimate payback from contribution, and derive lifetime value only from observed retention evidence.
5. Segment by cohort, channel, plan, and customer type; compare trends rather than one blended ratio.
6. Stress-test retention, price, variable cost, and acquisition assumptions before recommending scale.

## Output / decision record

Return a metric definition sheet, cohort tables, contribution and payback view, sensitivity range,
quality limitations, recommendation, trade-offs, and the evidence required for the next review.

## Uncertainty and failure handling

Do not extrapolate beyond the observation window without a labeled scenario. Investigate mix shifts,
missing variable costs, cohort censoring, and denominator changes; escalate material interpretation to
qualified finance review.

## Routing boundaries

Use this skill only for its stated capability and required context. For adjacent work, select a more specific skill from `skill-index.tsv`; do not infer coverage from this department folder or use this skill to authorize actions outside its scope.

## Never

- Compare acquisition cost with revenue while ignoring contribution.
- Present lifetime value without its retention window.
- Treat a blended ratio as proof every segment is healthy.
