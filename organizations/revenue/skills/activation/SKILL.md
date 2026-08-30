---
name: activation
description: Improve the path from signup to a user's first meaningful value through onboarding, time-to-value, and funnel diagnosis. Use this when signups fail to become active users, onboarding is too long, or the first-value action is undefined.
---

# Activation

Treat activation as a measurable product hypothesis, not a completed tour.

## Inputs and context

Collect the target user and intended value, signup and onboarding steps, event definitions, cohort retention data, funnel baseline, session or interview evidence, constraints, and candidate activation event.

## Workflow

1. Identify the behavior that predicts retained value and label it as a hypothesis until cohort evidence supports it.
2. Instrument each step, measure completion and time-to-value, and segment by relevant user or acquisition context.
3. Observe users at the largest drop to distinguish form friction, missing value, empty states, permissions, or product mismatch.
4. Remove or defer fields and steps that do not support first value; make progress resumable and recovery clear.
5. Define an experiment with baseline, target activation rate/time, guardrails, sample or observation plan, and review date.

## Output and decision record

Return evidence versus hypotheses, activation event definition, funnel findings, proposed change or experiment, baseline and measurable target, guardrails, confidence, and next decision date.

## Uncertainty and failure handling

Do not treat login, checklist completion, or signup conversion as activation without retention evidence. If instrumentation is incomplete, state the gap and prioritize observation or event repair before causal claims.

## Routing boundaries

Use this skill only for its stated capability and required context. For adjacent work, select a more specific skill from `skill-index.tsv`; do not infer coverage from this department folder or use this skill to authorize actions outside its scope.

## Never

- Optimize signup conversion while ignoring activation quality.
- Force every user through one assumed onboarding path.
- Call an untested event the activation moment.
