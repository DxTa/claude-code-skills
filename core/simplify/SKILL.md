---
name: simplify
description: Review changed code for reuse, clarity, efficiency, and unnecessary complexity, then apply the smallest behavior-preserving cleanup. Use when simplifying a diff, cleaning a recently changed file, or removing over-engineering without weakening required behavior.
---

# Simplify

Review changed code, then fix only material issues that make it less reusable, clear, efficient, or maintainable.

## Workflow

1. **Identify scope.** Inspect `git diff` or `git diff HEAD`. Respect any explicit file/path scope. Apply any requested focus only within that scope. If no diff exists, use files the user named or the files changed earlier in the session.
2. **Check reuse.** Search nearby and shared modules for helpers, types, utilities, and established patterns before keeping new code. Replace hand-rolled path, string, environment, or type logic when an existing solution fits.
3. **Check clarity.** Remove redundant state, parameter sprawl, copy-paste variation, leaky wrappers, stringly-typed values, unnecessary nesting, and comments that only narrate obvious code. Keep abstractions that clarify real boundaries.
4. **Check efficiency.** Look for repeated reads or computations, unnecessary sequential work, hot-path overhead, unbounded data, missing cleanup, and overly broad operations. Preserve intentional behavior and required change detection.
5. **Apply YAGNI.** Delete speculative flexibility, one-use abstractions, unused configuration, duplicate dependencies, and wrappers that add no value. Prefer the fewest files and smallest coherent diff; do not trade away safety or explicit requirements.
6. **Fix and verify.** Make behavior-preserving edits only. Re-read the resulting diff, run the narrowest relevant checks, and report skipped findings when they are false positives or not worth the risk.

## Safety boundary

Never simplify away security, validation, authorization, error handling, data-loss protection, accessibility, observability, required compatibility, or tests needed to prove behavior. Avoid clever compression that makes code harder to debug.
