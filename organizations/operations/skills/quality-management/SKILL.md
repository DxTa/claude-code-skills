---
name: quality-management
description: Define operational quality, prevent or detect defects at the right point, investigate root causes, and design process-level measures and corrective actions.
---

# Quality management

Keep improvement recommendations distinct from corrective actions. Any live change needs an owner,
safety and continuity checks, controlled rollout, evidence preservation, and a clear rollback or
containment path.

## Inputs and context

Collect customer definition of quality, specification, defect records, volume, process steps,
controls, escaped defects, rework, causal evidence, owners, and acceptable thresholds.

## Workflow

### Recommendations

1. Define quality as observable correctness, completeness, timeliness, usability, or another agreed
   outcome with a threshold.
2. Locate where defects originate and favor prevention, source detection, downstream detection, then
   customer discovery in that order.
3. Trace causes past human behavior to forms, incentives, sequencing, tooling, training, and system
   conditions that can be changed.
4. Select process-level measures, pair rates with volume, and define corrective-action verification.

### Actions

1. Contain immediate customer or safety impact without destroying evidence or masking the baseline.
2. Pilot a structural control or process change with an abort condition and continuity fallback.
3. Monitor escaped defects, rework, volume, and affected users against the baseline.
4. Close the action only after the defect trend moves or the remaining risk is explicitly accepted.

## Output / decision record

Return quality definition, defect and causal evidence, recommendation, containment and corrective
action, safety and continuity checks, owner, measures, result, and review date.

## Uncertainty and failure handling

Label suspected causes as hypotheses until tested. Do not treat completed tasks as proof of improvement;
keep defects open when measurement, volume, or customer impact is missing.

## Routing boundaries

Use this skill only for its stated capability and required context. For adjacent work, select a more specific skill from `skill-index.tsv`; do not infer coverage from this department folder or use this skill to authorize actions outside its scope.

## Never

- Stop at "human error" as the root cause.
- Replace process correction with final inspection alone.
- Optimize an individual metric that can be met by hiding defects.
