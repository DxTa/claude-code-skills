---
name: identity-lifecycle-administration
description: Execute joiner, mover, and leaver identity changes, including provisioning, deprovisioning, group review, orphan detection, and access evidence.
disable-model-invocation: true
---

# Identity lifecycle administration

Recommendations define a safe lifecycle procedure; actions change accounts and access. Separate them
and require an approved request, accountable owner, timing, rollback or recovery plan, safety checks,
and continuity checks before execution.

## Inputs and context

Collect the role or status change, effective time, authoritative personnel record, approved access
bundles, system inventory, exceptions, service accounts, legal holds, and business-critical handoffs.

## Workflow

### Recommendations

1. Map joiner, mover, and leaver events to authoritative records and system reach.
2. Use role-based bundles defined by security policy; define exception approval and expiry.
3. Design mover handling as removal plus re-provisioning, with recertification and orphan detection.
4. Identify systems outside centralized identity, tokens, shared credentials, delegated mail, and data
   custody that need explicit continuity handling.

### Actions

1. Verify the request, effective time, approver, and affected systems before changing access.
2. Provision or revoke the approved set, recording each system result and failed endpoint.
3. Transfer required data and operational ownership without deleting records subject to a hold.
4. Reconcile completion, notify the owner, and schedule exception expiry or recertification.

## Output / decision record

Return request scope, intended access, executed changes, failed or unreachable systems, data handoff,
safety and continuity checks, evidence, exception owner, and follow-up date.

## Uncertainty and failure handling

Pause destructive action when identity, timing, authority, or legal-hold status is unclear. Isolate
partial completion, preserve a recovery path for business-critical access, and escalate policy
questions to security or people owners rather than inventing entitlement.

## Routing boundaries

Use this skill only for its stated capability and required context. For adjacent work, select a more specific skill from `skill-index.tsv`; do not infer coverage from this department folder or use this skill to authorize actions outside its scope.

## Never

- Provision by copying another person's access.
- Add mover access without removing obsolete access.
- Call a leaver complete when only the directory account changed.
