---
name: marketing-analytics
description: Plan, audit, and interpret marketing measurement through event schemas, consent-aware tracking, attribution, experiments, and decision-focused reporting. Use when instrumenting a site or funnel, reconciling analytics tools, evaluating channel performance, or deciding whether a campaign caused incremental demand.
---

# Marketing analytics

Instrumentation is a contract about decisions, not a collection of events.

## Inputs and context

Gather business questions, funnel stages, event sources, consent model, event names and properties, identity rules, campaign taxonomy, source-of-truth systems, attribution options, baseline data, and report audience.

## Workflow

1. Write the decision each measure supports, then define event timing, schema, ownership, and naming consistently.
2. Test events through the actual user path, including single-page navigation, duplicate-fire behavior, blocked consent, bot filtering, and internal traffic.
3. Reconcile key definitions across tools and document differences in timestamps, identity, attribution windows, and exclusions.
4. Choose an attribution view deliberately, state its bias, and use holdouts or incrementality tests when the causal question matters.
5. Build a report for one audience with comparison, decision threshold, source, freshness, and known data limitations.
6. Review tracking health and attribution assumptions after site, consent, campaign, or platform changes.

## Output / decision record

Return tracking plan, event schema, validation evidence, definition reconciliation, attribution model and bias, report specification, decision, confidence, and follow-up checks.

## Uncertainty and failure handling

Do not fill gaps from an unverified dashboard. Mark consent loss, ad blockers, missing identity, bot traffic, and unknown campaign source as measurement limitations. If attribution cannot answer causality, propose an experiment or state that the effect is unestablished.

## Routing boundaries

Use this skill only for its stated capability and required context. For adjacent work, select a more specific skill from `skill-index.tsv`; do not infer coverage from this department folder or use this skill to authorize actions outside its scope.

## Never

- Add an event with no decision or owner.
- Switch attribution models to make a channel look better.
- Report a precise result when instrumentation is known to be incomplete.
