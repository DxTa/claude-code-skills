---
name: solution-architecture
description: Makes system-architecture choices explicit through quality attributes, boundaries, options, trade-offs, and durable decision records. Use for a new system or major component, a boundary review, a build-versus-buy choice, or an architecture decision record; do not use to approve another team's design or modify an owned repository without its human owner.
---

# Solution architecture

Reserve architecture ceremony for decisions that are costly to reverse, and make the accepted trade-offs visible.

## Inputs and context

Collect the business outcome, decision owner, current system, repositories and teams involved, users and data, trust boundaries, constraints, quality attributes, workload shape, latency, availability, residency, retention, change rate, operating capacity, budget, timeline, and approval policy. Mark assumptions and exclusions.

## Workflow

1. Quantify the constraints that actually bind. Replace broad claims such as “scalable” or “secure” with observable thresholds and evidence sources.
2. Identify ownership and change boundaries. Prefer a boundary that allows independent change and clear data stewardship; account for the cost of network, consistency, operations, and failure.
3. Develop at least two credible options, including a simpler or deferred option. Compare capability, coupling, operational load, security, cost, migration, reversibility, and failure behavior.
4. Review data flows, dependencies, resilience, observability, delivery path, and repository impact with independent specialists. Use approved prototypes or tests and preserve their assumptions and results.
5. Recommend one option or request more evidence. Define decision scope, consequences accepted, guardrails, success measures, review triggers, and rollback or migration steps.
6. Obtain human approval from the accountable owner before changing architecture records, repositories, infrastructure, or delivery commitments. Supersede prior decisions rather than erasing their history.

## Output and decision record

Return context, decision, options considered, trade-off matrix, constraints and assumptions, consequences, risks and mitigations, owners, validation evidence, approval status, review trigger, and next actions with dates.

## Uncertainty and failure handling

If a quality attribute, owner, data boundary, or operating assumption is unquantified, label the decision provisional and name the smallest discovery needed. Do not use a diagram or prototype as evidence of production readiness.

## Routing boundaries

Use this skill only for its stated capability and required context. For adjacent work, select a more specific skill from `skill-index.tsv`; do not infer coverage from this department folder or use this skill to authorize actions outside its scope.

## Never

- Never split a system or choose a vendor solely to make a diagram look cleaner.
- Never present one option without naming what it sacrifices.
- Never approve or implement an owned architecture decision without human authorization.
