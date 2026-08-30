---
name: access-and-identity
description: Designs and reviews authentication, authorization, privileged access, and identity lifecycle controls. Use when scoping an access review, reducing standing privilege, planning SSO or MFA, handling joiner-mover-leaver changes, or governing service credentials; do not use for unsanctioned account probing or incident response.
disable-model-invocation: true
---

# Access and identity

Use this skill to produce a bounded, reviewable access decision—not to operate an identity system without its owner.

## Inputs and context

Collect the requesting owner, written authorization, review scope, systems and environments, identity populations, sensitive data, current role/group exports, credential owners, and the required completion date. Mark exclusions explicitly. Treat production changes as a separate approved activity.

## Workflow

1. Confirm the authority and inventory in-scope human, contractor, service, and machine identities. Record source timestamps and gaps.
2. Map each entitlement to a business purpose, accountable data/system owner, role or group, privilege level, and expiry or review date.
3. Check joiner, mover, and leaver paths separately. Look for retained grants, shared accounts, dormant identities, unowned credentials, and administrative access without time limits.
4. Prefer role-based, least-privilege grants, short-lived elevation, phishing-resistant MFA for sensitive access, and a documented credential rotation path.
5. Test only with approved read-only queries, a staging tenant, or a maintenance window. Preserve exports, request IDs, timestamps, and relevant hashes; do not alter evidence during review.
6. Escalate suspected compromise, unapproved access, material data exposure, or an inability to verify scope to the security owner and incident process. Obtain system-owner approval before remediation.

## Output and decision record

Return:

- scope, authority, systems reviewed, and evidence timestamp;
- findings grouped by excessive, stale, missing, or unowned access;
- recommended grant, revoke, review, or time-bound elevation with an accountable owner;
- test limitations and residual uncertainty;
- approval, due date, and escalation path for each consequential action.

## Uncertainty and failure handling

Stop if authorization, ownership, or a reliable inventory is absent. Label partial coverage instead of inferring that unreviewed systems are safe. If exports conflict, retain both versions, identify the authoritative source, and escalate the discrepancy.

## Routing boundaries

Use this skill only for its stated capability and required context. For adjacent work, select a more specific skill from `skill-index.tsv`; do not infer coverage from this department folder or use this skill to authorize actions outside its scope.

## Never

- Never test credentials, bypass MFA, disable controls, or revoke access without explicit authority.
- Never treat a clean review as proof that unauthorized access or security risk is absent.
- Never approve access for an unnamed owner or leave an exception without an expiry.
