---
name: tax
description: Map tax questions created by hiring, selling, inventory, services, or expansion into a new jurisdiction, and prepare a filing, registration, or adviser-review worklist.
disable-model-invocation: true
---

# Tax

This skill provides tax decision support, not tax advice. Preserve the facts, effective dates,
jurisdictions, filing basis, and source assumptions. Tax rules are jurisdiction-specific and change;
qualified tax advisers or CPAs must determine material positions. Flag uncertainty and do not infer
an obligation from an incomplete fact pattern.

## Inputs and context

Collect locations of workers, customers, inventory, offices, contractors, and events; products and
bundles; transaction volumes; entity structure; payroll facts; exemptions; prior registrations; and
relevant dates.

## Workflow

1. Build a fact map by jurisdiction and distinguish known facts from assumptions.
2. Classify possible corporate, sales/use, payroll, withholding, indirect, and filing obligations.
3. Check thresholds, nexus triggers, product taxability, exemptions, and registration timing with
   current qualified sources.
4. Create an obligation calendar with owner, frequency, filing, payment, evidence, and dependencies.
5. Reconcile book treatment, cash timing, and operational changes that may alter the map.
6. Prepare focused questions and evidence for qualified adviser review before taking a material position.

## Output / decision record

Return a jurisdiction matrix, fact gaps, possible obligations, deadlines, evidence needed, adviser
questions, and a decision log stating what is not yet determined.

## Uncertainty and failure handling

Do not generalize one jurisdiction's treatment to another or assume remote activity is irrelevant.
Stop when effective dates, thresholds, product classification, or entity facts are unclear; preserve
those assumptions and escalate.

## Routing boundaries

Use this skill only for its stated capability and required context. For adjacent work, select a more specific skill from `skill-index.tsv`; do not infer coverage from this department folder or use this skill to authorize actions outside its scope.

## Never

- Treat a tax checklist as a jurisdiction-specific determination.
- Assume no obligation exists without a local office.
- File or take a material position without qualified review.
