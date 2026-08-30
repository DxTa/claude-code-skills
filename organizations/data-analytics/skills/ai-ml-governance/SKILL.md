---
name: ai-ml-governance
description: Assess whether a model or AI feature is appropriate for its intended use through consequence classification, representative evaluation, segment analysis, monitoring, human oversight, documentation, and retirement planning. Use before deploying or materially changing an AI system, when behavior drifts, or when a consequential use needs a governance decision.
---

# AI and ML governance

Establish accountable use and evidence before treating model performance as sufficient.

## Inputs and context

Record intended use, prohibited uses, affected people, consequence level, data provenance and permissions, baseline process, evaluation set, segments, error costs, human reviewer role, monitoring signals, fallback, owner, and applicable jurisdiction or sector.

## Workflow

1. Define what the system may do, may not do, who is affected, and what happens when it is wrong.
2. Classify it as advisory, human-reviewed assistive, or autonomous and set the corresponding review bar.
3. Evaluate against a stable representative set, a baseline, both error directions, and relevant segments.
4. Document limitations, data lineage, threshold rationale, reviewer time and override path.
5. Monitor input and output drift, delayed ground truth, segment performance, and meaningful human overrides.
6. Approve, restrict, remediate, or reject deployment; exercise the fallback and define retirement conditions.

## Output / decision record

Return intended-use statement, consequence tier, evaluation results by segment, comparison baseline, known limitations, monitoring and alert thresholds, oversight design, owner, approval status, fallback, and retirement trigger.

## Uncertainty and failure handling

Do not infer safety from aggregate accuracy or a successful demo. Pause when data permission, representative evaluation, reviewer capacity, or ground truth is missing. For employment, credit, housing, insurance, healthcare, education, or other regulated decisions, involve Legal & Risk and qualified specialists before use.

## Routing boundaries

Use this skill only for its stated capability and required context. For adjacent work, select a more specific skill from `skill-index.tsv`; do not infer coverage from this department folder or use this skill to authorize actions outside its scope.

## Never

- Deploy without a documented evaluation and monitoring plan.
- Use a model beyond its approved purpose because it appears useful.
- Treat a nominal reviewer as meaningful oversight when they cannot inspect or change the result.
