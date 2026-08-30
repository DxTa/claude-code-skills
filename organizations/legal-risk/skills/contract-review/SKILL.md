---
name: contract-review
description: Review or negotiate an MSA, SOW, order form, NDA, vendor agreement, or data-processing term by prioritizing material exposure, operational feasibility, fallback positions, and approval thresholds.
disable-model-invocation: true
---

# Contract review

This produces legal decision support, not legal advice. Preserve the exact draft, parties, effective
dates, governing law, jurisdiction, commercial assumptions, and negotiation history. Qualified counsel
must determine legal effect, especially for material, novel, regulated, employment, financing, or
litigation matters; flag uncertainty.

## Inputs and context

Collect the agreement and exhibits, business purpose, promised service, data and IP flows, price and
term, implementation capability, negotiation leverage, internal thresholds, and relevant jurisdictions.
Use an approved processing environment, minimize and redact irrelevant personal data or account
identifiers, exclude credentials and secrets, and mark outputs for controlled need-to-know retention.

## Workflow

1. Confirm version, parties, precedence among documents, side communications, and missing schedules.
2. Triage liability, indemnity, IP/data rights, term/termination, payment/change, warranty, and service
   obligations by realistic impact.
3. For each material point, state the exposure, preferred position, acceptable fallback, walk-away
   condition, and operational owner.
4. Check that engineering, security, finance, privacy, and operations can fulfill every commitment.
5. Route jurisdiction-specific and high-consequence issues to qualified counsel before signature.

## Output / decision record

Return issue register, negotiation positions, operational feasibility findings, approval threshold,
open assumptions, recommended path, counsel questions, signature blocker status, and post-signature
owner for obligations and renewal dates.

## Uncertainty and failure handling

Do not infer terms from a summary or marketing promise. Mark missing exhibits, conflicting clauses,
uncertain governing law, unreviewed side letters, and obligations without an owner; pause signature
until the appropriate professional resolves material ambiguity.

## Routing boundaries

Use this skill only for its stated capability and required context. For adjacent work, select a more specific skill from `skill-index.tsv`; do not infer coverage from this department folder or use this skill to authorize actions outside its scope.

## Never

- Approve an obligation no operational owner has accepted.
- Treat urgency as a substitute for review.
- State legal effect as certain without qualified counsel.
