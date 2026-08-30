---
name: capacity-and-demand-planning
description: Match staffing, service, fulfillment, or operational-system capacity to expected demand, queues, variability, and bottlenecks before deciding to add resources.
---

# Capacity and demand planning

A recommendation to add capacity is not an execution order. Keep recommendations and actions separate;
validate safety, service continuity, workload sustainability, budget ownership, and rollback before
changing staffing, queues, or production limits.

## Inputs and context

Collect arrival volume in work units, baseline and trend, known spikes, service times, available
hours, interruption rate, skills, queue age, target service level, dependencies, and current capacity.

## Workflow

### Recommendations

1. Forecast baseline, trend, and spikes separately in the unit work actually arrives in.
2. Convert headcount or machine count into effective capacity after leave, training, meetings, and
   other non-productive time.
3. Examine utilization, oldest queue age, rework, handoffs, and wait time to locate the constraint.
4. Distinguish an arrival-rate shortfall from a flow problem before proposing hiring, tooling, or
   outsourcing.
5. Compare scenarios with safety and continuity headroom rather than planning at nominal maximum.

### Actions

1. Pilot the smallest approved change to staffing, routing, hours, or throughput limit.
2. Confirm service safeguards, workload limits, communications, and fallback coverage before rollout.
3. Monitor arrival rate, effective capacity, queue age, quality, and staff or customer impact.
4. Revert or pause if the change increases unsafe load, rework, or continuity risk; record evidence.

## Output / decision record

Return demand forecast, effective-capacity calculation, bottleneck evidence, scenario comparison,
recommendation, action owner, safety and continuity checks, success threshold, and review date.

## Uncertainty and failure handling

Use ranges for volatile demand and identify data gaps. Do not add resources to an unmeasured flow
problem; escalate when capacity claims conflict with quality, safety, or service evidence.

## Routing boundaries

Use this skill only for its stated capability and required context. For adjacent work, select a more specific skill from `skill-index.tsv`; do not infer coverage from this department folder or use this skill to authorize actions outside its scope.

## Never

- Plan at 100% nominal utilization.
- Add capacity before identifying the constraint.
- Hide queue aging behind an average queue length.
