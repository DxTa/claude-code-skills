---
name: systems-administration
description: Operate servers and corporate systems through configuration baselines, patch cadence, change control, capacity checks, and recovery-aware maintenance.
disable-model-invocation: true
---

# Systems administration

Recommendations describe intended operations; actions change systems. Require an accountable owner,
maintenance window, backup or recovery check, safety validation, communications, and a tested rollback
before execution.

## Inputs and context

Collect system inventory, service owner, baseline, exposure, patch state, dependencies, capacity,
change history, maintenance constraints, backup status, monitoring, and emergency authority.

## Workflow

### Recommendations

1. Compare running systems with the approved baseline and classify drift, exposure, and unsupported
   ownership.
2. Set patch cadence by exposure, distinguishing routine, emergency, and deferred exceptions.
3. Choose change control proportional to risk; every change has owner, back-out method, and evidence.
4. Check capacity and dependency behavior under maintenance or failover, not just nominal health.

### Actions

1. Confirm inventory, backup/recovery evidence, access, approval, and rollback before changing a system.
2. Capture current state, apply the smallest approved change, and monitor service and dependent paths.
3. Validate configuration, patch coverage, logs, capacity, and user-visible behavior after the window.
4. Roll back when success criteria or continuity checks fail, then record the incident and correct the
   baseline or change procedure that allowed the failure.

## Output / decision record

Return baseline and drift findings, patch or change recommendation, action record, safety and
continuity checks, validation evidence, exceptions, rollback result, and next review date.

## Uncertainty and failure handling

Do not repair an unknown system from memory. Stop when ownership, recovery, dependency, or emergency
authority is unclear; isolate the system safely, preserve evidence, and escalate rather than guessing.

## Routing boundaries

Use this skill only for its stated capability and required context. For adjacent work, select a more specific skill from `skill-index.tsv`; do not infer coverage from this department folder or use this skill to authorize actions outside its scope.

## Never

- Make a system change without a back-out plan.
- Treat patch activity as coverage evidence.
- Leave an unmanaged or drifted system without an owner and due date.
