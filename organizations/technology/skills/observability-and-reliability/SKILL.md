---
name: observability-and-reliability
description: Designs useful telemetry, alerting, service objectives, on-call readiness, and blameless reliability learning. Use when instrumenting a service, reducing alert fatigue, setting SLOs or error budgets, preparing operations, or reviewing an incident; do not use to change production telemetry or reliability policy without its owner.
---

# Observability and reliability

Make user impact visible, make alerts actionable, and leave operators with a safe response path.

## Inputs and context

Gather service owner, user journeys, dependencies, environments, data sensitivity, current logs/metrics/traces, incident history, on-call coverage, traffic shape, availability and latency commitments, deployment process, and approval authority. Define what is in and out of the review.

## Workflow

1. Start from operator and user questions. Choose structured logs, metrics, traces, correlation fields, and retention that answer those questions without collecting unnecessary sensitive data.
2. Define indicators and objectives around user-visible success, including percentile latency, availability, correctness, and dependency effects. State measurement window and exclusions.
3. Create alerts only where a named responder can act within a defined urgency. Prefer symptoms and include context, runbook link, deduplication, and a tested escalation path.
4. Calculate an error budget and agree how it influences release and reliability work. Align internal targets with external commitments and record trade-offs.
5. Validate in a non-production or approved environment, preserve configuration and test evidence, and obtain owner approval before changing dashboards, pages, sampling, retention, or production agents.
6. For incidents, review detection and recovery separately. Produce a few system-focused actions with owners and dates, then verify that the actions improve the indicator.

## Output and decision record

Return the telemetry plan, data and retention boundaries, indicators and objectives, alert table with action and owner, error-budget policy, on-call/escalation plan, validation evidence, rollout/rollback steps, and approval status.

## Uncertainty and failure handling

Mark blind spots, noisy signals, missing baselines, and untested alerts. Do not infer reliability from a quiet dashboard or a mean value. If an alert cannot identify an action or owner, redesign or remove it before rollout.

## Routing boundaries

Use this skill only for its stated capability and required context. For adjacent work, select a more specific skill from `skill-index.tsv`; do not infer coverage from this department folder or use this skill to authorize actions outside its scope.

## Never

- Never page people for a condition they cannot act on.
- Never collect sensitive telemetry without a stated purpose, owner, and retention decision.
- Never modify an owned repository or production system without human approval.
