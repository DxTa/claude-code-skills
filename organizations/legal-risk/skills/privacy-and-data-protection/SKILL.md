---
name: privacy-and-data-protection
description: Assess a new or changed use of personal data through data mapping, purpose and basis, vendor sharing, retention, subject rights, and breach response.
disable-model-invocation: true
---

# Privacy and data protection

This is privacy decision support, not legal advice. Preserve data-source, purpose, processing,
jurisdiction, role, date, retention, and regulatory assumptions. Qualified privacy counsel or other
qualified professionals must determine lawful basis, notification, and material compliance positions;
flag uncertainty clearly.

## Inputs and context

Inventory data categories, people, collection point, purpose, systems, access, vendors, transfers,
retention/deletion mechanism, security controls, rights requests, incident facts, and applicable
jurisdictions.

## Workflow

1. Build a data map before assessing compliance; identify unknown systems and unowned data flows.
2. Minimize collection, separate identifiers where linkage is unnecessary, and test purpose compatibility
   for any new use such as analytics or model training.
3. Record proposed basis, notice/consent needs, processor terms, transfer mechanism, retention trigger,
   deletion path, and rights-request workflow.
4. Verify vendors can support security, deletion, access, and subprocessor obligations.
5. For an incident or request, preserve evidence, verify identity safely, locate affected records, and
   route deadline and notification determinations to qualified professionals.

## Output / decision record

Return data-flow map, purpose and assumption register, control and vendor gaps, retention/deletion
plan, rights or incident steps, jurisdictional questions, decision owner, and professional-review gate.

## Uncertainty and failure handling

Do not call a processing activity compliant when its purpose, location, population, retention, or legal
basis is unknown. Restrict unnecessary access, preserve evidence, and escalate cross-border, sensitive-
data, rights-deadline, and breach-notification uncertainty.

## Routing boundaries

Use this skill only for its stated capability and required context. For adjacent work, select a more specific skill from `skill-index.tsv`; do not infer coverage from this department folder or use this skill to authorize actions outside its scope.

## Never

- Collect or reuse personal data without a defined purpose.
- Assume a vendor contract answers every privacy obligation.
- Give a lawful-basis or notification conclusion without qualified review.
