---
name: backup-and-recovery
description: Design, assess, or test data backup and restoration, including coverage, retention, immutability, recovery objectives, and evidence that a restore is usable.
disable-model-invocation: true
---

# Backup and recovery

Recommendations describe a recovery design; they are not permission to alter production or delete
retained data. Before any action, verify ownership, safety, continuity impact, credentials, rollback,
and the recovery objectives set by the business.

## Inputs and context

Collect the asset register, data owners, dependency map, critical processes, target RTO/RPO, backup
scope, retention rules, provider commitments, access model, and evidence from recent restore tests.

## Workflow

### Recommendations

1. Compare protected assets with the authoritative inventory, including SaaS data and configuration.
2. Identify copy, platform, location, immutability, credential, retention, and deletion gaps.
3. Propose recovery tiers and a test schedule based on business impact, not backup-job status.
4. Size restore paths against measured recovery time and document dependencies that may fail together.

### Actions

1. Obtain the change owner and maintenance window before modifying backup policy or infrastructure.
2. Run a representative restore in an isolated environment; validate application behavior and data
   completeness, not only file presence.
3. Record duration, integrity checks, missing prerequisites, and cleanup of the test environment.
4. Remediate approved gaps with least-privilege access and verify that immutable or offline copies
   remain recoverable.

## Output / decision record

Return a coverage matrix, recovery recommendation, test evidence, measured RTO/RPO, exceptions,
owners, next test date, and any action requiring explicit approval.

## Uncertainty and failure handling

Treat an untested backup as unproven. Stop if a restore could overwrite live data, expose sensitive
data, or consume shared capacity without an isolation and cleanup plan. Escalate retention conflicts
to legal/privacy owners.

## Routing boundaries

Use this skill only for its stated capability and required context. For adjacent work, select a more specific skill from `skill-index.tsv`; do not infer coverage from this department folder or use this skill to authorize actions outside its scope.

## Never

- Declare recovery from successful backup jobs alone.
- Test by overwriting production data.
- Remove retained copies without an approved policy and owner.
