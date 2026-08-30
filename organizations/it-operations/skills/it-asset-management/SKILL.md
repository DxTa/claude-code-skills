---
name: it-asset-management
description: Establish or reconcile a hardware and software asset register, ownership, licensing, refresh, lifecycle state, and secure disposal evidence.
disable-model-invocation: true
---

# IT asset management

Recommendations improve inventory and lifecycle control; actions alter ownership, licenses, or
physical assets. Before action, confirm authority, data-protection safety, continuity needs, vendor
terms, rollback or recovery options, and evidence requirements.

## Inputs and context

Collect procurement and finance records, discovery and management data, asset identifiers, owner,
location, lifecycle state, support status, license entitlements and use, refresh budget, and disposal
requirements.

## Workflow

### Recommendations

1. Reconcile the register with discovery, procurement, finance, and endpoint systems.
2. Classify discrepancies, unsupported assets, unknown owners, unused licenses, and concentration risks.
3. Define lifecycle states, accountable ownership, refresh cadence, license review, and exception paths.
4. Specify secure return, wipe, destruction, certificate, and chain-of-custody requirements.

### Actions

1. Validate an asset's identity and accountable owner before assignment or state change.
2. Update the register at handoff, install, repair, retirement, or disposal; retain the evidence.
3. Reclaim or renew licenses only after usage and entitlement checks and the required approval.
4. Wipe or destroy storage under an approved procedure, verify the result, and record the certificate.

## Output / decision record

Return discrepancy list, lifecycle recommendation, owners, license or refresh decision, continuity
impact, action log, disposal evidence, and unresolved assets with escalation dates.

## Uncertainty and failure handling

Treat discovery/register mismatches as findings, not as permission to delete records. Quarantine
unknown or compromised equipment safely, preserve business data before retirement, and stop disposal
when ownership, hold, or wipe evidence is missing.

## Routing boundaries

Use this skill only for its stated capability and required context. For adjacent work, select a more specific skill from `skill-index.tsv`; do not infer coverage from this department folder or use this skill to authorize actions outside its scope.

## Never

- Treat a hand-maintained register as ground truth.
- Assign an asset to a team with no accountable person.
- Dispose of storage without verifiable wipe or destruction evidence.
