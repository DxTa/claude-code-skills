---
name: support-operations
description: Design or diagnose support channels, queues, routing, staffing, service levels, quality review, and cost per contact. Use when setting up support, sizing coverage, reducing backlog, renegotiating service commitments, choosing automation, or investigating poor resolution quality.
---

# Support operations

Design the system around solving customer problems, not maximizing tickets closed.

## Inputs and context

Gather a representative contact sample, arrival pattern, severity and customer tiers, channel expectations, staffing and shrinkage, service commitments, backlog age, reopen rate, resolution outcomes, and quality rubric.

## Workflow

1. Categorize contacts to identify preventable causes and demand peaks before changing staffing.
2. Choose the lowest-cost effective intervention: product elimination, in-product guidance, self-service, automation, or assisted handling.
3. Select channels whose response expectations can be staffed, then define severity-based routing and ownership.
4. Size coverage to peak concurrency and realistic availability; model investigation time separately from first response.
5. Set measurable service levels, quality sampling, escalation rules, and customer-effort checks.
6. Review contacts per active customer, first-contact resolution, backlog age distribution, reopen rate, and downstream customer impact.

## Output / decision record

Return demand profile, preventable causes, channel and routing design, staffing assumptions, service-level proposal, quality rubric, metrics with definitions, automation boundaries, and review date.

## Uncertainty and failure handling

Do not infer demand from daily averages when peaks drive queues. Show sampling limitations and test proposed capacity against worst normal periods. Investigate a metric change for definition or mix changes before declaring improvement.

## Routing boundaries

Use this skill only for its stated capability and required context. For adjacent work, select a more specific skill from `skill-index.tsv`; do not infer coverage from this department folder or use this skill to authorize actions outside its scope.

## Never

- Promise a service level without checking capacity.
- Optimize time-to-close while reopened or unresolved contacts rise.
- Launch an unstaffed synchronous channel or an automation that blocks human help.
