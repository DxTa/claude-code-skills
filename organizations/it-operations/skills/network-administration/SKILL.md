---
name: network-administration
description: Design or troubleshoot corporate network segmentation, remote access, wireless, DNS, addressing, routing, and connectivity without weakening trust boundaries.
disable-model-invocation: true
---

# Network administration

A proposed network change is not an executed change. Separate recommendations from actions and
require an owner, approved window, tested rollback, user communication, safety checks, and a
continuity path before altering routes, access, or segmentation.

## Inputs and context

Collect topology, trust zones, addressing and DNS records, affected users and services, traffic
flows, remote-access needs, monitoring, current rules, incident symptoms, and recovery access.

## Workflow

### Recommendations

1. Describe the required flow and trust boundary, separating users, servers, management, guests, and
   unmanaged equipment where appropriate.
2. Prefer narrowly scoped application access over broad network reach; identify policy decisions for
   the security owner.
3. Check address growth, DNS redundancy, dependency concentration, and observability from the user's
   path.
4. Diagnose bottom-up: physical, link/addressing, routing, name resolution, then application.

### Actions

1. Capture the current configuration and confirm out-of-band or break-glass access.
2. Pilot the rule, route, DNS, or wireless change with explicit success and abort criteria.
3. Monitor affected paths and validate expected and denied flows from representative clients.
4. Restore the previous configuration if safety, availability, or trust behavior degrades; record the
   result and update controlled documentation.

## Output / decision record

Return topology or symptom summary, recommendation, exact change scope, safety and continuity checks,
test results, rollback status, observed impact, and follow-up owner.

## Uncertainty and failure handling

Do not infer an intermittent fault from one passing test. Preserve captures and timestamps, isolate
blast radius, and stop changes when the dependency or recovery path is unknown.

## Routing boundaries

Use this skill only for its stated capability and required context. For adjacent work, select a more specific skill from `skill-index.tsv`; do not infer coverage from this department folder or use this skill to authorize actions outside its scope.

## Never

- Apply a broad allow rule to solve an unscoped symptom.
- Treat corporate network location as proof of trust.
- Make a network change without a recovery path.
