---
name: retention
description: Diagnose and reduce voluntary and involuntary churn through payment recovery, cancellation experience, at-risk signals, and product or service interventions. Use this when churn rises, cancellations are unexplained, failed payments cause loss, or a win-back flow needs evidence.
---

# Retention

Treat the cause of churn as a hypothesis and test it against cohorts and customer evidence.

## Inputs and context

Collect churn definition, voluntary/involuntary split, cohorts by tenure/plan/channel/activation, payment events, usage and support signals, cancellation reasons, save offers, baseline retention, and outcome target.

## Workflow

1. Separate failed-payment churn from chosen cancellation and quantify each against a consistent baseline.
2. Locate when the decision likely formed by cohort and event; combine funnel data with cancellation feedback, interviews, or session evidence.
3. Build at-risk signals that have an assigned intervention owner; test dunning, product fixes, service recovery, pause, or win-back separately.
4. Keep cancellation clear and capture specific reasons without coercion; offer only a remedy that matches the stated problem.
5. Measure recovered payment, retained customers at a defined horizon, churn rate, margin, complaints, and downstream product effects.

## Output and decision record

Return evidence/hypothesis table, churn diagnosis, intervention or experiment, baseline and measurable target, guardrails, cohort result, confidence, and next decision.

## Uncertainty and failure handling

A saved cancellation is not retention until the customer remains at the review horizon. If signals correlate without explaining cause, recommend targeted observation or experiment instead of broad save offers.

## Routing boundaries

Use this skill only for its stated capability and required context. For adjacent work, select a more specific skill from `skill-index.tsv`; do not infer coverage from this department folder or use this skill to authorize actions outside its scope.

## Never

- Count a deferred cancellation as retained without a later check.
- Force a customer to call to cancel.
- Treat every churn issue as a support problem.
