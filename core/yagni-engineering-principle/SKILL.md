---
name: yagni-engineering-principle
description: Apply YAGNI to feature planning, architecture, code review, dependency selection, and refactoring by separating committed needs from speculation and choosing the smallest clean solution. Use when evaluating future-proofing, abstractions, optional configuration, infrastructure, or over-engineering.
---

# YAGNI Engineering Principle

Build what current requirements justify. Do not encode imagined future needs before evidence makes them real.

## Workflow

1. **Separate need from speculation.** Mark each proposed behavior as required now, backed by a committed need, or hypothetical. Ask what current user, product, or operational requirement proves it.
2. **Choose the smallest clean solution.** Reuse existing code and installed dependencies before adding abstractions, providers, plugins, configuration, or infrastructure. Keep names clear, functions cohesive, tests useful, and code easy to change.
3. **Defer unproven flexibility.** Record worthwhile deferred ideas in the normal backlog or decision record, but do not build them “just in case.” Compare the cost of adding them later with the cost of maintaining them now.
4. **Refactor when evidence arrives.** When a deferred need becomes concrete, extend the tested implementation then. Do not make today’s code harder to understand to avoid a hypothetical migration.
5. **Distinguish features from foundations.** Apply YAGNI strongly to addable features and variation points. Give deliberate architectural attention to choices that are expensive or unsafe to reverse, such as data storage, trust boundaries, and deployment topology.

## Review checklist

- Is this used by a current requirement or committed deliverable?
- What concrete variation exists today? Is an abstraction solving it, or only predicting it?
- Can existing code, a standard-library/native feature, or one configured dependency solve the need?
- Can this option, wrapper, provider, endpoint, or infrastructure component be deleted until evidence requires it?
- If deferred, what is the realistic cost and incremental refactoring path?

## Safety boundary

YAGNI never justifies removing security controls, authentication, authorization, validation, error handling, data-loss protection, accessibility, observability, tests needed for confidence, or explicitly required behavior. Simplicity means less speculative surface, not lower safety or quality.
