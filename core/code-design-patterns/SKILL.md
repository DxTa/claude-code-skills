---
name: code-design-patterns
description: Language-agnostic guidance for detecting code smells, selecting behavior-preserving refactorings, and choosing or rejecting classic Refactoring.Guru design patterns. Use for requests like “review this for code smells,” “how should I refactor this long method?”, or “should I use Adapter, Strategy, or direct code?” Apply during code review, architecture, refactoring, and general application-code design when pressure, variation, coupling, lifecycle, or object structure must be evaluated. Do not replace Python-specific, frontend, backend, infrastructure, or other domain-owned pattern guidance.
---

# Code design patterns

Choose the smallest design that solves demonstrated pressure. A smell is evidence to investigate, a refactoring is a behavior-preserving move, and a pattern is a named trade-off—not a quality badge.

## Workflow

1. **Classify the work.** Load only the needed reference: [code smells](references/code-smells.md), [refactoring techniques](references/refactoring-techniques.md), or [design patterns](references/design-patterns.md). Load multiple references only when the task crosses phases.
2. **Collect evidence.** Inspect callers, ownership, lifetime, error flow, tests, change history when available, and the actual symbol/file. Do not label code from size or syntax alone.
3. **Diagnose before prescribing.** Name the smell group and observable behavior; distinguish intentional complexity, a framework constraint, a domain rule, or a one-off edge from a design problem.
4. **Prefer direct code.** Try a function, branch, map, data object, module, protocol, generator, or composition before adding a named pattern or hierarchy.
5. **Refactor safely.** Establish current behavior, make one coherent transformation, preserve public contracts and ownership, then run focused tests plus relevant static checks.
6. **Select patterns problem-first.** State the pressure, axes of variation, and simpler rejected alternative. Choose the least powerful pattern that makes the pressure clearer or safer. Define proof and a reversal condition.
7. **Keep boundaries.** Python-specific GoF implementation choices remain with `python-design-patterns`. Frontend, backend/API, persistence, distributed, infrastructure, and UI patterns remain with their owning domain skills. Use `clean-code` for naming, duplication, size, comments, and ordinary behavior-preserving cleanup.

## Smell review contract

For each finding, report:

- location and concrete evidence;
- smell name and Refactoring.Guru group;
- impact on change safety, defects, coupling, or comprehension;
- confidence and plausible intentional explanation;
- smallest suitable refactoring technique;
- whether a named design pattern is justified or explicitly unnecessary;
- focused verification and residual risk.

Do not treat a numeric rule of thumb as an automatic violation. Prefer one high-confidence finding over a catalog dump.

## Refactoring contract

Before editing, record the behavior that must remain true. Select one technique from the smallest applicable group, check variable scope, public API, ownership, error semantics, concurrency, serialization, and performance. After editing, run the narrowest proof that would fail if the transformation changed behavior. Stop when the pressure is gone; do not stack techniques or patterns speculatively.

## Pattern decision contract

For every pattern recommendation, report:

- pressure and evidence;
- direct-code/DP-00 alternative and why it is insufficient;
- chosen pattern or explicit no-pattern decision;
- participants, scope, and ownership boundary;
- trade-offs, misuse check, and domain handoff;
- one runnable or testable proof;
- exit/reversal condition.

Combine patterns only when each answers a separate pressure and has separate proof. If explanation needs more pattern names than pressures, delete patterns first.

## Reference navigation

- [Code smells](references/code-smells.md): grouped detection signals, boundaries, and first refactoring candidates.
- [Refactoring techniques](references/refactoring-techniques.md): grouped transformation steps, contract risks, and verification focus.
- [Design patterns](references/design-patterns.md): 22 catalog patterns with original compact pseudocode and rejection criteria.
- [Sources and attribution](references/sources.md): source pages, access date, and copyright boundary.
