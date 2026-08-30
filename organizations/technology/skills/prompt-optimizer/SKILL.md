---
name: prompt-optimizer
description: Improves prompts by diagnosing underspecification, conflicting constraints, output shape, evaluation criteria, and model-specific behavior. Use when an AI task is inconsistent, a reusable prompt needs design, or a prompt must move between models; do not use to guarantee model behavior or to make consequential changes without human review.
---

# Prompt optimizer

Optimize against the task's observed failure, not against a preference for longer instructions.

## Inputs and context

Request the original prompt, representative inputs, actual outputs, target audience, purpose, model and tool context, desired output shape, quality criteria, constraints, and examples. Identify private or sensitive material and obtain permission before including it in tests.

## Workflow

1. Inspect the failed output and classify the main cause: missing detail, conflicting detail, wrong format, absent success test, buried instruction, insufficient context, or a problem no prompt can solve.
2. State the task first, separate fixed instructions from variable input, define audience and purpose, and specify output sections, limits, examples, and an explicit fallback for insufficient information.
3. Prefer precise positive instructions. Remove duplicate or competing constraints and keep role framing limited to useful perspective rather than authority claims.
4. Produce materially different candidates when the prompt matters: concise, structured, example-led, or role-framed. Keep the evaluation criteria constant.
5. Test each candidate repeatedly on the same input and on empty, long, ambiguous, adversarial, and model-transfer cases. Record variance, failures, cost, and latency.
6. Select or revise based on the worst important failure. Human-review any prompt whose output can affect users, access, money, safety, or repository state before adoption.

## Output and decision record

Return the diagnosed failure, candidate prompts, test set, scoring rubric, trial results, known limitations, selected version, model assumptions, owner, review date, and approval status.

## Uncertainty and failure handling

Say when missing knowledge, tool limits, or task complexity—not wording—is the blocker. Do not generalize from one successful run. If tests contain sensitive data or results vary materially, stop adoption and escalate to the owner.

## Routing boundaries

Use this skill only for its stated capability and required context. For adjacent work, select a more specific skill from `skill-index.tsv`; do not infer coverage from this department folder or use this skill to authorize actions outside its scope.

## Never

- Never include secrets or personal data in a prompt test without authorization and minimization.
- Never claim a prompt guarantees correctness, consistency, or transfer across models.
- Never change an owned prompt library, workflow, or repository without human approval.
