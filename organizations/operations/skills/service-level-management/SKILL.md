---
name: service-level-management
description: Define, measure, negotiate, or remediate service levels and SLAs using customer-relevant measures, realistic targets, clear exclusions, and breach handling.
---

# Service-level management

A target recommendation is not a customer commitment. Keep recommendations separate from actions and
verify safety, service continuity, operational capacity, measurement integrity, owner approval, and
qualified contract review before changing an SLA.

## Inputs and context

Collect customer outcomes, service path, incidents, measurement location, historical percentiles,
proposed target, exclusions, internal objective, remedies, dependencies, and contractual authority.

## Workflow

### Recommendations

1. Define what customers experience, including degraded performance, resolution, and tail behavior.
2. Specify metric, start and stop events, measurement point, calculation, window, exclusions, and
   evidence source.
3. Test the target against sustained history, capacity cost, internal warning margin, and continuity
   scenarios.
4. Separate one-off incidents from repeated misses and identify whether the target is fundable.
5. Route contractual remedy language to qualified contract review while operations owns measurement
   feasibility.

### Actions

1. Obtain approval and baseline measurement before publishing or changing a service level.
2. Implement monitoring and alerting, communicate definitions, and validate the customer-visible path.
3. Report breaches promptly with cause, impact, remedy status, and evidence.
4. Review repeated breaches for funded improvement or honest renegotiation; record the decision.

## Output / decision record

Return service definition, baseline and percentile evidence, target recommendation, exclusions,
internal margin, continuity checks, breach record, remedy owner, contract-review status, and next review.

## Uncertainty and failure handling

Do not commit to an unmeasured level or rely on an inside-the-perimeter metric when customers use a
broader path. Mark missing evidence, unclear exclusions, and dependency failures before publication.

## Routing boundaries

Use this skill only for its stated capability and required context. For adjacent work, select a more specific skill from `skill-index.tsv`; do not infer coverage from this department folder or use this skill to authorize actions outside its scope.

## Never

- Use averages to hide the customer-experienced tail.
- Publish an SLA with undefined measurement rules.
- Repeatedly miss a target without funding or renegotiating it.
