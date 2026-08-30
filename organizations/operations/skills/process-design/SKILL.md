---
name: process-design
description: Map and improve a recurring operational process by measuring touch time, elapsed time, waits, rework, handoffs, controls, and automation opportunities.
---

# Process design

A redesign is a recommendation until approved. Separate recommendations from actions and validate
worker safety, customer continuity, control coverage, ownership, and rollback before changing a live
process.

## Inputs and context

Collect a real case, current procedure, performers, systems, handoffs, queue and rework data, touch
and elapsed time, controls, failure consequences, service targets, and constraints.

## Workflow

### Recommendations

1. Trace an actual instance end to end, recording work, waits, handoffs, exceptions, and rework.
2. Measure touch time and elapsed time, then locate the constraint and evidence behind it.
3. Evaluate changes in order: remove unnecessary work, simplify flow, standardize decisions, then
   automate only what is understood.
4. Define controls, ownership, required fields, thresholds, metrics, and safe exception handling.

### Actions

1. Obtain process-owner approval and define a reversible pilot, safety checks, continuity fallback, and
   abort condition.
2. Run the pilot with affected users, preserving a path for urgent or exceptional cases.
3. Compare throughput, elapsed time, touch time, errors, rework, and customer impact with baseline.
4. Adopt, revise, or roll back based on evidence; document the new process and control owner.

## Output / decision record

Return current-state map, measured wait and work, constraint evidence, redesign, implementation cost,
pilot result, safety and continuity checks, control changes, owner, and success measure.

## Uncertainty and failure handling

Do not generalize from an idealized procedure or one case. Preserve exceptions and stop if the pilot
weakens a safety or control boundary; escalate unresolved ownership or dependency gaps.

## Routing boundaries

Use this skill only for its stated capability and required context. For adjacent work, select a more specific skill from `skill-index.tsv`; do not infer coverage from this department folder or use this skill to authorize actions outside its scope.

## Never

- Automate a process before understanding its failure modes.
- Add a step without stating the failure it prevents.
- Call a process improved without comparing evidence to baseline.
