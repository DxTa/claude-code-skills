---
name: security-architecture-review
description: Reviews a system design, change, dependency, or delivery plan for security exposure before approval. Use for authentication and authorization review, data-flow and secrets analysis, secure-development controls, or third-party integration assessment; do not use as a substitute for authorized testing or final security-risk acceptance.
disable-model-invocation: true
---

# Security architecture review

Produce findings that connect a concrete attack path to a specific remediation. Keep the review independent of the team proposing the change.

## Inputs and context

Obtain the design or diff, data-flow and trust boundaries, environments, assets, identities, dependencies, deployment path, threat assumptions, written review authorization, test scope, applicable obligations, and release decision owner. List omitted components and requested evidence.

## Workflow

1. Confirm scope, authorization, review window, and safe-test limits. Classify assets and identify where an attacker-controlled value crosses a boundary.
2. Review identity establishment, session and recovery paths, object-level authorization, tenant isolation, data collection and retention, logging, secrets, inputs, outputs, cryptography usage, dependencies, and third-party access.
3. Check that proposed controls are testable and owned. Use static analysis, dependency checks, secret scanning, or bounded dynamic tests only when approved; preserve tool versions, outputs, timestamps, and samples.
4. Separate blocking findings, required fixes, accepted residual risk, and observations. Describe the attacker's capability, target, consequence, and evidence for each finding.
5. Escalate suspected active exploitation, material data exposure, regulatory or contractual impact, and exceptions beyond the reviewer's authority to the appropriate security, incident, or legal owner.
6. Re-review changed boundaries or mitigations before release. Require human approval for release, exception, and any intrusive test.

## Output and decision record

Return findings by severity with attack path, affected asset, evidence, blocking status, remediation, owner, due date, retest method, and residual uncertainty. End with a release recommendation that names the approving human and any expiry on accepted risk.

## Uncertainty and failure handling

If architecture, scope, evidence, or authorization is incomplete, mark the review incomplete and identify the minimum evidence needed. A scanner pass is limited evidence; absence of a finding is not evidence that the design is safe.

## Routing boundaries

Use this skill only for its stated capability and required context. For adjacent work, select a more specific skill from `skill-index.tsv`; do not infer coverage from this department folder or use this skill to authorize actions outside its scope.

## Never

- Never approve an exception, release, or intrusive test on behalf of the accountable owner.
- Never invent assurances about unreviewed paths, dependencies, tenants, or environments.
- Never claim a clean review proves absence of security risk.
