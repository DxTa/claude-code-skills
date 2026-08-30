---
name: incident-response
description: Coordinates authorized response to suspected or confirmed security incidents from triage through recovery and lessons learned. Use when compromise, data exposure, malicious activity, or an incident exercise needs a bounded response plan; do not use for unsanctioned investigation or destructive containment.
disable-model-invocation: true
---

# Incident response

Coordinate people, evidence, and decisions. The incident commander and system owners retain operational authority.

## Inputs and context

Record the reporter, declaration authority, incident commander, response scope, affected environments and accounts, detection time, known indicators, data classes, business impact, communication obligations, and available responders. Mark unknowns and exclusions immediately.

## Workflow

1. Confirm authorization and appoint one incident commander. Define severity, working channel, evidence store, update cadence, and stop conditions.
2. Triage facts without broadening access. Preserve logs, volatile state, images, alerts, and communications with timestamps, source, handler, and integrity metadata.
3. Contain with the least disruptive approved action: isolate a host, revoke a credential, restrict a route, or disable an account. Record who approved each action and its expected side effect.
4. Investigate within the written scope using non-destructive collection. Establish affected assets, initial access, persistence, lateral movement, data access, and current activity; distinguish facts from hypotheses.
5. Escalate promptly to security leadership, system owners, Legal & Risk or qualified counsel for possible personal-data or contractual impact, and executive leadership when business decisions or risk acceptance exceed delegated authority.
6. Eradicate and recover from known-good state only after evidence and containment decisions are recorded. Rotate reachable credentials, validate restored controls, and monitor for recurrence.
7. Close with a factual timeline, communications record, residual risk, and a small set of owned corrective actions. Exercise the plan separately from a live event.

## Output and decision record

Provide a timeline and current status, declared scope, evidence inventory, containment and recovery decisions, impact and notification questions, open hypotheses, owners and deadlines, and the next update time. State explicitly what remains unknown.

## Uncertainty and failure handling

If authority, scope, evidence integrity, or responder capacity is unclear, pause nonessential action and escalate to the incident commander. If evidence conflicts, retain all versions and label the conflict. Do not stand down because alerts are quiet; require scoped validation and owner approval.

## Routing boundaries

Use this skill only for its stated capability and required context. For adjacent work, select a more specific skill from `skill-index.tsv`; do not infer coverage from this department folder or use this skill to authorize actions outside its scope.

## Never

- Never delete, alter, or disclose incident evidence outside the approved response team.
- Never probe third-party or production systems without written authorization and a safe test plan.
- Never claim clean logs, containment, or recovery proves that compromise or risk is absent.
