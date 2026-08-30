---
name: behavioral-marketing
description: "Use when a marketing or product decision appears blocked by choice friction, framing, defaults, attention, or perceived risk; build ethical, evidence-based behavior hypotheses and tests, not psychological diagnoses or coercive persuasion."
---

# Behavioral marketing

## Inputs and context

Collect the decision being made, the audience and their context, the current journey or offer, observed funnel or research evidence, constraints, and the business outcome. Record whether the evidence is behavioral, reported, or inferred. Note consent, privacy, accessibility, and platform requirements before proposing a change.

## Workflow

1. State the customer decision and the observable point where it stalls.
2. Identify the smallest plausible constraint: comprehension, trust, effort, timing, risk, or competing priorities.
3. Map a small number of behavior hypotheses to the evidence. Explain how each change should help the customer make an informed choice.
4. Design a controlled test or qualitative check with a baseline, success metric, downstream guardrails, and a stop condition.
5. Review the variant for clarity, reversibility, accessibility, and compliance before release.
6. Inspect outcomes beyond the immediate conversion, including cancellations, complaints, refunds, and retention.

## Output / decision record

Return:

- decision point and evidence classification;
- selected hypothesis and proposed variant;
- primary metric, guardrails, sample or observation plan, and stop rule;
- expected customer benefit and possible harm;
- approval owner, test window, and follow-up date.

## Uncertainty and failure handling

Treat behavioral research as directional rather than predictive. Mark assumptions, confounders, and insufficient sample sizes. If evidence is weak, recommend a low-risk discovery step instead of claiming a bias explains behavior. If conversion rises while trust, retention, or complaint signals worsen, reject the variant and record the trade-off.

## Routing boundaries

Use this skill only for its stated capability and required context. For adjacent work, select a more specific skill from `skill-index.tsv`; do not infer coverage from this department folder or use this skill to authorize actions outside its scope.

## Never

- Never use fake scarcity, hidden defaults, obstructed cancellation, or confusing consent.
- Never infer a person’s vulnerability or intent from a single action.
- Never use personal or sensitive data outside its documented permission and purpose.
