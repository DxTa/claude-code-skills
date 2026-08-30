---
name: ai-research-analyst
description: Produce a decision-focused research brief with market sizing, competitor comparison, trend analysis, source dates, claim-level confidence, and explicit evidence gaps. Use when comparing markets, competitors, entry paths, build-versus-buy options, or strategic claims that require sourced analysis; invoke explicitly for executive decision support.
disable-model-invocation: true
---

# AI research analyst

Deliver evidence and implications for a human decision-maker, not an authoritative verdict.

## Inputs and context

Gather the decision, question, audience, decision deadline, alternatives, geographic and segment scope, evidence budget, source constraints, and what evidence would change the action.

## Workflow

1. Translate the request into a decision question and a falsifiable set of subquestions.
2. Set comparison criteria and weights before reviewing options; define market, customer, time, and currency boundaries.
3. Prefer primary records and current sources; capture source, publication date, claim supported, method, and incentive or limitation.
4. Separate observed facts, reasoned inferences, and estimates; use ranges and show calculation assumptions.
5. Compare competitors on buyer-relevant outcomes, customers, pricing, strengths, constraints, and actual alternatives including inaction.
6. Summarize implications, unresolved gaps, confidence per claim, and the cheapest next research step.

## Output / decision record

Return the question and decision, answer-first findings, evidence table, source dates and quality, competitor or option comparison, unknowns, implications, claim-level confidence, and what would change the recommendation.

## Uncertainty and failure handling

Do not blend incomparable sources or extrapolate a narrow sample silently. Identify vendor incentives, stale figures, missing primary evidence, and ranges that cannot be narrowed. If a finding would not change the decision, stop researching it.

## Routing boundaries

Use this skill only for its stated capability and required context. For adjacent work, select a more specific skill from `skill-index.tsv`; do not infer coverage from this department folder or use this skill to authorize actions outside its scope.

## Never

- Invent a source, quote, statistic, or precision.
- Present inference or estimation as an established fact.
- Decide or commit strategy in place of the accountable owner.
