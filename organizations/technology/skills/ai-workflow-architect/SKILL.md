---
name: ai-workflow-architect
description: Selects and designs bounded AI automations and agent workflows by comparing value, stability, failure visibility, tools, and human approval points. Use when automating a repeated process, connecting tools or agents, or auditing an unreliable automation; do not use to authorize production changes or replace accountable process owners.
---

# AI workflow architect

Design the smallest useful workflow and make its failure visible before adding sophistication.

## Inputs and context

Collect the process owner, repository or system owner, current manual steps, frequency, effort, error cost, stability, data sensitivity, existing tools, success measure, operating environment, and human approver. State which actions are drafts and which could affect users, money, access, or production.

## Workflow

1. Document the current process and first ask whether a step can be removed. Score candidates for frequency, effort, error cost, and process stability; record the scoring evidence.
2. Identify deterministic rules, model judgment, tool calls, state, retries, idempotency needs, and observable failure signals. Keep validation and routing deterministic where possible.
3. Draw a narrow end-to-end loop with explicit inputs, outputs, handoffs, permissions, timeout behavior, and an approval gate before consequential actions.
4. Choose tools that the owner can operate. Prefer defined interfaces over fragile screen automation, and identify vendor, data, cost, and maintenance risks.
5. Test normal, empty, ambiguous, oversized, adversarial, and dependency-failure inputs. Run repeated trials when model variance affects the outcome.
6. Pilot in a reversible environment, measure the agreed success criteria, and obtain human approval before enabling production writes or customer-facing output.

## Output and decision record

Return the candidate score, proposed workflow, tool and data boundaries, failure and escalation paths, evaluation cases and results, operating owner, approval gate, cost, and a reversible rollout plan. State the first workflow to build and what is deliberately deferred.

## Uncertainty and failure handling

If the process is undocumented, unstable, unmeasurable, or requires judgment that cannot be specified, recommend discovery or manual handling instead. Stop on silent failure, missing owner, unsafe permissions, or unexplained model variance; do not fill gaps with confident assumptions.

## Routing boundaries

Use this skill only for its stated capability and required context. For adjacent work, select a more specific skill from `skill-index.tsv`; do not infer coverage from this department folder or use this skill to authorize actions outside its scope.

## Never

- Never grant an agent broader access than the owner approved.
- Never let an unreviewed model output trigger an irreversible or consequential action.
- Never change a repository or production system outside its owner's approved workflow.
