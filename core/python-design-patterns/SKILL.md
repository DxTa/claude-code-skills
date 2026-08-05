---
name: python-design-patterns
description: Problem-first guidance for choosing, rejecting, and reviewing classic design patterns in Python. Use when selecting a Python design pattern, comparing Factory vs Builder, replacing conditionals with Strategy, evaluating a Refactoring.Guru pattern, refactoring toward or away from a GoF pattern, or deciding whether an abstraction is over-engineered. Do not trigger for generic pattern words, framework patterns, backend topology, or readability-only cleanup.
---

# Python design patterns

Choose the least powerful design that solves a demonstrated problem. A named pattern is a hypothesis with cost, not a default implementation.

## Workflow

1. State the pressure: duplication, variation, lifecycle, tree shape, access control, ordering, coordination, snapshot, or algorithm choice.
2. Inspect callers, ownership, lifetime, error flow, tests, and existing domain conventions.
3. Try direct Python first: function, callable, map, branch, dataclass, enum, generator, context manager, module, protocol, or composition.
4. Read [the decision table](references/python-decision-table.md) only for the remaining pressure.
5. Record fit, avoid conditions, trade-offs, misuse risk, scope, proof, and reversal condition.
6. Keep domain ownership intact: use [backend guidance](../../backend/backend-development/SKILL.md), [frontend guidance](../../frontend/frontend-development/SKILL.md), or DeepStream guidance for framework/system patterns.
7. Return one recommendation, one rejected simpler/stronger alternative, and the smallest proof needed.

## Mandatory DP-00 gate

Start with direct code. Use a named pattern only when direct code leaves a real, recurring pressure that the pattern makes clearer or safer. Prefer:

- functions and callables over one-method classes
- dictionaries, `match`, or guard clauses over speculative strategy/chain objects
- dataclasses and keyword-only constructors over builders for plain data
- modules or explicit dependency injection over Singleton
- generators and the iterator protocol over custom iterator hierarchies
- composition and protocols over inheritance trees
- standard-library copying, context managers, `functools`, and `collections` before custom machinery

If no pressure survives this gate, stop at DP-00.

## Pattern boundaries

- **Factory Method vs factory function:** use subclass-owned creation only when subclass invariants or polymorphic ownership matter; otherwise use a function or registry.
- **Object Decorator vs `@decorator`:** use wrappers for object contracts; use callable decorators for callable concerns. Do not hide lifecycle or I/O in syntax.
- **Observer vs distributed Pub/Sub:** this skill covers explicit in-process subscribers. Queues, brokers, retries, delivery guarantees, and backpressure belong to the system/domain skill.
- **Strategy vs callable/map/match:** a Strategy class needs a meaningful contract or state; a small closed choice is usually a callable or map.
- **State objects vs enum/transition function:** object states earn their cost when transitions and behavior grow; finite small state belongs in data and a transition function.
- **Singleton vs module/global state:** both create shared lifetime. Prefer explicit ownership; never use Singleton to conceal dependency flow or make tests order-dependent.

## Output contract

For every pattern decision, report:

- pressure and evidence
- DP-00 alternative and why it is insufficient, if applicable
- chosen pattern or explicit no-pattern decision
- scope and ownership boundary
- trade-offs and misuse check
- one runnable proof
- exit/reversal condition

## Ownership handoffs

`clean-code` diagnoses smells and behavior-preserving cleanup; see its catalog for IDs such as F3, G15, G22, G23, G30, G31, G32, G34, and G36. This skill decides structural pattern trade-offs. Do not use a pattern to mask a naming, duplication, size, or control-flow problem.

Backend Repository, dependency-injection, distributed, and messaging choices remain in [backend-development](../../backend/backend-development/SKILL.md). React and UI patterns remain in [frontend-development](../../frontend/frontend-development/SKILL.md). Pipeline/runtime choices remain in the DeepStream skill.

## References

- [Python decision table](references/python-decision-table.md)
- [Sources and attribution](references/sources.md)
