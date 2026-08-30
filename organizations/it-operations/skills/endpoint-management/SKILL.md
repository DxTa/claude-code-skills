---
name: endpoint-management
description: Plan or operate laptop, desktop, and mobile-device enrollment, configuration, patching, software rollout, and response to lost or compromised endpoints.
disable-model-invocation: true
---

# Endpoint management

Keep recommendations distinct from actions. Any fleet change needs an accountable owner, tested
rollback, user communication, safety checks, and a continuity fallback for people who cannot work.

## Inputs and context

Collect device inventory, ownership, operating systems, management status, encryption and patch
coverage, required applications, personal-device policy, user impact, and recovery options.

## Workflow

### Recommendations

1. Identify unmanaged, unsupported, unencrypted, or overdue devices and rank exposure.
2. Define a small set of standard builds, configuration controls, patch deadlines, and exception rules.
3. Choose a staged rollout cohort and success measures for enrollment, software, reboot, and recovery.
4. For lost devices, map lock, location, wipe, credential revocation, evidence preservation, and
   privacy escalation without assuming every device supports each operation.

### Actions

Before locate, lock, wipe, or credential-revoke operations, verify the exact device identifier, ownership, named authorization, BYOD consent or lawful basis, scope, and evidence-preservation decision. Confirm the command target a second time.

1. Pilot enrollment or configuration on representative devices and verify user data and recovery.
2. Communicate patch or reboot windows, then deploy to cohorts with a clear abort condition.
3. Verify device-level encryption, management heartbeat, patch state, and application availability.
4. For a loss, follow the approved incident sequence only after the authorization and target checks above, then record what was done, when, and by whom.

## Output / decision record

Return fleet gaps, proposed baseline, rollout or incident plan, safety and continuity checks,
success criteria, exceptions, action owner, and validation evidence.

## Uncertainty and failure handling

Do not force a fleet-wide change when device coverage, backups, or user impact are unknown. Isolate
failed cohorts, preserve evidence after a suspected compromise, and route personal-data exposure for
privacy assessment.

## Routing boundaries

Use this skill only for its stated capability and required context. For adjacent work, select a more specific skill from `skill-index.tsv`; do not infer coverage from this department folder or use this skill to authorize actions outside its scope.

## Never

- Locate, lock, wipe, or revoke credentials for a personal or unverified device without named authorization, lawful basis or consent, and exact-target confirmation.
- Allow unmanaged access to sensitive company data by default.
- Force a reboot without a communicated recovery path.
- Claim encryption or patch compliance from policy alone.
