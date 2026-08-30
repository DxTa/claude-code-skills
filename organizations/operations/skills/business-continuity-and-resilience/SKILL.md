---
name: business-continuity-and-resilience
description: Run a business-impact analysis, set recovery objectives, create or exercise continuity plans, or assess disruption from a supplier, site, system, or people dependency.
---

# Business continuity and resilience

Keep recommendations separate from actions. Any exercise, failover, or operational change needs an
accountable owner, safety review, communications, continuity fallback, and a recovery path that does
not depend on the failed service.

## Inputs and context

Collect critical processes, customers and consequences, dependencies, process owners, maximum
outage, proposed RTO/RPO, alternate methods, suppliers, facilities, staffing, and prior exercise
findings.

## Workflow

### Recommendations

1. Start from customer and business impact, then map the systems, people, sites, and suppliers the
   process needs.
2. Agree outage tolerance, RTO, and RPO with the accountable process owner and state their cost.
3. Design a short first-response sequence, decision authority, role-based contacts, alternatives, and
   assumptions that may fail together.
4. Choose walkthrough, tabletop, or live test based on risk and measure the capability being claimed.

### Actions

1. Obtain approval, communications plan, safety checks, and an isolated or controlled test environment.
2. Run the selected exercise or failover without endangering production or people.
3. Record decisions, elapsed recovery, missing dependencies, unsafe steps, and customer impact.
4. Assign findings, retest failed scenarios, and update owners and runbooks.

## Output / decision record

Return impact analysis, agreed objectives, dependency map, recommendation, exercise evidence,
continuity gaps, action owners, fallback status, and next test date.

## Uncertainty and failure handling

Treat unsigned RTO/RPO values as aspirations. Stop if the alternate path shares the same dependency,
if the exercise could cause uncontrolled service impact, or if decision authority is absent; escalate
and preserve the last known safe state.

## Routing boundaries

Use this skill only for its stated capability and required context. For adjacent work, select a more specific skill from `skill-index.tsv`; do not infer coverage from this department folder or use this skill to authorize actions outside its scope.

## Never

- Call a reviewed document a tested capability.
- Put a failed system on the first recovery step.
- Set recovery objectives without the process owner's agreement.
