---
name: supply-chain-and-logistics
description: Plan inventory, lead times, fulfillment, supplier alternatives, and supply risk when stockouts, excess stock, unreliable delivery, or concentration threaten operations.
---

# Supply chain and logistics

Recommendations about inventory or suppliers are not execution orders. Separate actions and require
safety, continuity, quality, cash, storage, and customer-impact checks before changing orders, stock,
routes, or fulfillment commitments.

## Inputs and context

Collect demand history and variability, lead-time distribution, inventory by stage, service target,
reorder settings, supplier tiers, capacity, ports or regions, substitution options, orders in flight,
and fulfillment outcomes.

## Workflow

### Recommendations

1. Model demand and replenishment variability, not only averages; define the unit and service target.
2. Set reorder logic using measured lead-time demand, safety buffer, constraints, and obsolescence risk.
3. Trace supplier dependencies beyond the first tier and assess alternate qualification time and design
   lock-in.
4. Diagnose fulfillment misses by supply, capacity, information, or process and compare total trade-offs.
5. Coordinate supplier terms and exit with vendor owners and continuity planning.

### Actions

1. Validate approved quantities, quality requirements, storage, cash, and continuity fallback before
   placing or changing an order.
2. Pilot revised reorder, routing, or alternate-supplier controls with traceability and an abort rule.
3. Monitor on-time-in-full, stockout, excess, lead-time spread, defects, and customer impact.
4. Quarantine unsafe or nonconforming goods, preserve records, and escalate a supply interruption early.

## Output / decision record

Return demand and lead-time assumptions, inventory recommendation, concentration map, fulfillment
baseline, action plan, safety and continuity checks, owners, thresholds, and review date.

## Uncertainty and failure handling

Use ranges when demand or lead-time evidence is thin. Do not count suppliers as independent without
tracing shared dependencies; stop a change that threatens product safety, quality, or essential supply.

## Routing boundaries

Use this skill only for its stated capability and required context. For adjacent work, select a more specific skill from `skill-index.tsv`; do not infer coverage from this department folder or use this skill to authorize actions outside its scope.

## Never

- Size buffers from averages while ignoring variability.
- Treat a quoted lead time as measured reliability.
- Count converged suppliers as true redundancy.
