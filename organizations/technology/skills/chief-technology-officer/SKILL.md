---
name: chief-technology-officer
description: Prepares technology leadership decisions about architecture, engineering capacity, infrastructure, internal systems, technical debt, and build-versus-buy trade-offs. Use when a technical choice affects business scope, cost, delivery risk, or standards; do not use to impersonate an executive, approve a change, or overrule accountable security, legal, product, or repository owners.
disable-model-invocation: true
---

# Technology leadership decision support

Frame technical choices so the accountable leader can decide. The skill supplies analysis, not delegated executive authority.

## Inputs and context

Collect the decision owner, written mandate, business objective, systems and repositories affected, current architecture, constraints, capacity, budget, timeline, quality attributes, security and legal considerations, technical debt, options already considered, and approval gates. Name every team whose ownership boundary is crossed.

## Workflow

1. Define the decision and separate reversible implementation details from expensive-to-reverse commitments. Record facts, assumptions, and missing evidence.
2. Establish measurable constraints such as latency, availability, data handling, change rate, staffing, cost, and delivery date. Do not accept vague quality claims.
3. Compare at least two credible options, including buy, defer, simplify, or retain. State operational cost, failure modes, dependencies, migration or rollback path, and what each option makes harder.
4. Check architecture, delivery capacity, maintainability, security, data, compliance, and vendor risk with independent owners. Preserve repository ownership and require human approval for consequential edits.
5. Recommend a decision, pilot, or evidence-gathering step. Define success criteria, owner, review date, and the evidence that would reverse the recommendation.
6. Escalate scope, strategy, regulatory, contractual, or funding impacts to the appropriate accountable executive rather than resolving them by assumption.

## Output and decision record

Return, in order: decision or recommendation; decisive reasoning; cost and trade-offs; assumptions; reversal evidence; affected owners; next handoffs and dates; approval status. Record dissent and unresolved risks.

## Uncertainty and failure handling

If constraints, ownership, or evidence are missing, label the recommendation provisional and state the smallest safe investigation. Do not present a preferred option as inevitable. A successful pilot does not prove production readiness without operating and approval evidence.

## Routing boundaries

Use this skill only for its stated capability and required context. For adjacent work, select a more specific skill from `skill-index.tsv`; do not infer coverage from this department folder or use this skill to authorize actions outside its scope.

## Never

- Never claim executive authority or approve architecture, spend, hiring, release, or repository changes for a human.
- Never hide a delivery or security trade-off behind a technical recommendation.
- Never let an unowned exception remain open-ended.
