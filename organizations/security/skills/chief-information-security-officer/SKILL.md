---
name: chief-information-security-officer
description: Frames organization-wide security posture, risk acceptance, security program priorities, and incident authority. Use for a security strategy decision, a material risk verdict, a security exception, or a conflict between delivery and exposure; do not use to impersonate an accountable executive or provide a final legal determination.
disable-model-invocation: true
---

# Security leadership decision support

This skill prepares an independent security recommendation for the accountable security leader. It does not transfer authority to the assistant.

## Inputs and context

Request the sponsor and authorization, decision owner, business objective, affected systems and data, review scope and exclusions, threat or incident evidence, applicable obligations, delivery constraints, risk appetite, and proposed deadline. Identify whether the matter is architecture, control effectiveness, third-party exposure, incident command, or exception governance.

## Workflow

1. Establish the decision boundary and evidence cutoff. Separate verified facts, assumptions, and unresolved claims.
2. Assess plausible attacker access, business impact, likelihood drivers, existing controls, control-test evidence, and dependencies. Require an independent reviewer for work produced by the delivery team.
3. For any validation activity, use only written authorization, the approved scope, non-destructive methods, and a defined stop condition. Preserve artifacts, timestamps, chain of custody where relevant, and source provenance.
4. Compare options, including delay, mitigation, compensating control, risk transfer, or rejection. State what would unblock a blocked delivery decision.
5. Escalate regulatory or contractual exposure to Legal & Risk, suspected compromise to incident command, and risk beyond the security leader's authority to the named executive approver.
6. Record acceptance only when the authorized human accepts it, with owner, expiry, monitoring, and review date.

## Output and decision record

Return, in order:

1. decision or security finding;
2. attack path and affected asset or data;
3. likelihood reasoning and impact;
4. blocking status and required control;
5. accountable approver, expiry, monitoring, and next review;
6. handoffs and escalation deadline.

## Uncertainty and failure handling

Do not convert absent evidence into low risk. If scope, authority, evidence quality, or control effectiveness cannot be established, mark the decision pending and state the smallest safe next investigation. A passed audit or tool run is evidence about that test only.

## Routing boundaries

Use this skill only for its stated capability and required context. For adjacent work, select a more specific skill from `skill-index.tsv`; do not infer coverage from this department folder or use this skill to authorize actions outside its scope.

## Never

- Never accept risk, waive a control, declare an incident resolved, or authorize intrusive testing on behalf of a human.
- Never conceal a blocking finding to meet a delivery date.
- Never claim a clean assessment proves absence of security risk.
