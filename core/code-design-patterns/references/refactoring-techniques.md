# Refactoring techniques

Apply one behavior-preserving transformation at a time. Confirm current behavior first, keep contracts explicit, and select the smallest move that removes a demonstrated pressure. Source baseline: [Refactoring.Guru refactoring techniques](https://refactoring.guru/refactoring/techniques).

## Contents

- [Composing Methods](#composing-methods)
- [Moving Features between Objects](#moving-features-between-objects)
- [Organizing Data](#organizing-data)
- [Simplifying Conditional Expressions](#simplifying-conditional-expressions)
- [Simplifying Method Calls](#simplifying-method-calls)
- [Dealing with Generalization](#dealing-with-generalization)

## Composing Methods

### Extract Method

- **Signal:** A fragment has a nameable purpose, repeated logic, or its own comment/branch/loop.
- **Move:** Create a small named function, pass inputs explicitly, return values that used to escape, and replace the fragment with one call.
- **Risk/check:** Preserve evaluation order, mutation, exceptions, closure state, and variable scope; test the old path and extracted boundaries.
- **Related:** Long Method, Duplicate Code, Feature Envy; often precedes Move Method or Parameter Object. [Source](https://refactoring.guru/extract-method)

### Inline Method

- **Signal:** A wrapper’s body is as clear as its name, or indirection hides no independent contract.
- **Move:** Replace calls with the body, adjust parameters/returns, then remove the wrapper after checking all callers.
- **Risk/check:** Preserve dynamic dispatch, recursion, instrumentation, visibility, stack-sensitive behavior, and side-effect order; run caller tests.
- **Related:** Lazy Class, Speculative Generality; inverse of Extract Method. [Source](https://refactoring.guru/inline-method)

### Extract Variable

- **Signal:** An expression is complex, repeated, or carries an important domain meaning.
- **Move:** Bind it once to an intention-revealing name and replace equivalent uses within the same scope.
- **Risk/check:** Preserve evaluation count, short-circuiting, laziness, mutation, and type narrowing; test branches where expression inputs differ.
- **Related:** Comments, Long Method, Primitive Obsession; may lead to Replace Temp with Query. [Source](https://refactoring.guru/extract-variable)

### Inline Temp

- **Signal:** A temporary only aliases an expression and adds no meaning or is blocking a later transformation.
- **Move:** Replace each use with the expression, then delete the binding after confirming it is evaluated the same number of times.
- **Risk/check:** Do not duplicate expensive, stateful, non-idempotent, or lazily evaluated work; use characterization tests and a performance check when relevant.
- **Related:** Speculative Generality; inverse of Extract Variable. [Source](https://refactoring.guru/inline-temp)

### Replace Temp with Query

- **Signal:** A computed temporary is reused, obscures intent, or would be useful to other methods.
- **Move:** Extract the computation into a query, replace reads with calls, and remove the temporary when no longer needed.
- **Risk/check:** Preserve snapshot-vs-live semantics, caching, side effects, and visibility; test repeated calls and changed dependencies.
- **Related:** Long Method, Temporary Field, Extract Method. [Source](https://refactoring.guru/replace-temp-with-query)

### Split Temporary Variable

- **Signal:** One variable is assigned for unrelated meanings or changes role across phases.
- **Move:** Give each assignment purpose-specific immutable/local names; update later uses by phase.
- **Risk/check:** Preserve aliasing, scope, loop behavior, and assignment order; test every phase and ensure no use still refers to the wrong meaning.
- **Related:** Long Method, Temporary Field; supports Extract Method and Replace Temp with Query. [Source](https://refactoring.guru/split-temporary-variable)

### Remove Assignments to Parameters

- **Signal:** A parameter is overwritten, so callers cannot tell input from evolving local state.
- **Move:** Introduce a local with the new value, use it for subsequent work, and leave parameters as inputs.
- **Risk/check:** Preserve reference/value semantics, mutation visible through aliases, and return behavior; test null/default and reassignment branches.
- **Related:** Long Method, Data Class; supports Extract Method. [Source](https://refactoring.guru/remove-assignments-to-parameters)

### Replace Method with Method Object

- **Signal:** A method is too tangled to extract because many locals and parameters cross its fragments.
- **Move:** Create an object holding the method inputs and evolving locals, move the algorithm into one operation, then split/move pieces there.
- **Risk/check:** Preserve lifetime, visibility, mutation, and exception behavior; test the original call contract before deleting the old implementation.
- **Related:** Long Method, Temporary Field, Large Class; fallback before larger extraction. [Source](https://refactoring.guru/replace-method-with-method-object)

### Substitute Algorithm

- **Signal:** An algorithm is hard to understand, slower, duplicated, or replaced by a clearer equivalent.
- **Move:** Implement the replacement beside the old version, compare results on representative and boundary inputs, then swap and delete old code.
- **Risk/check:** Preserve ordering, numeric precision, error behavior, mutation, complexity expectations, and side effects; use differential/property tests and benchmarks.
- **Related:** Duplicate Code, Long Method, Strategy; do not change semantics under a readability-only request. [Source](https://refactoring.guru/substitute-algorithm)

## Moving Features between Objects

### Move Method

- **Signal:** A method uses another object’s data more than its owner’s or is a better fit elsewhere.
- **Move:** Copy to the target, adjust references and visibility, delegate temporarily if needed, migrate callers, then remove the old method.
- **Risk/check:** Recheck polymorphism, transaction/session ownership, lazy loading, subclass overrides, and public API; run caller and contract tests.
- **Related:** Feature Envy, Large Class, Divergent Change; may use Extract Method first. [Source](https://refactoring.guru/move-method)

### Move Field

- **Signal:** A field is read/updated mostly by another object or belongs to another invariant.
- **Move:** Add it to the target, migrate reads/writes through explicit access, update construction/serialization, then delete the source field.
- **Risk/check:** Preserve identity, defaults, persistence, thread safety, and observers; test all creators and mutation paths.
- **Related:** Feature Envy, Divergent Change, Parallel Inheritance Hierarchies. [Source](https://refactoring.guru/move-field)

### Extract Class

- **Signal:** One class has independent responsibility clusters, field groups, or reasons to change.
- **Move:** Create a cohesive class, move selected data/behavior, expose the smallest boundary, and update callers incrementally.
- **Risk/check:** Preserve invariants, equality, serialization, lifecycle, and dependency direction; test old and new boundaries before deleting delegation.
- **Related:** Large Class, Data Clumps, Divergent Change, Inappropriate Intimacy. [Source](https://refactoring.guru/extract-class)

### Inline Class

- **Signal:** A class no longer owns meaningful behavior or boundary and merely forwards data/calls.
- **Move:** Move its fields and operations into the dominant client, update all references, then remove the class.
- **Risk/check:** Preserve imports, public types, extension hooks, identity, serialization, and instrumentation; search dynamic references before deletion.
- **Related:** Lazy Class, Middle Man, Speculative Generality; inverse of Extract Class. [Source](https://refactoring.guru/inline-class)

### Hide Delegate

- **Signal:** Callers navigate through an object to reach its collaborator and learn internal graph structure.
- **Move:** Add a focused operation on the owner that delegates, migrate callers, and keep the collaborator private where possible.
- **Risk/check:** Avoid a broad forwarding surface; preserve null/error, transaction, authorization, and lazy-loading semantics; test missing delegate cases.
- **Related:** Message Chains, Inappropriate Intimacy; can create Middle Man if overused. [Source](https://refactoring.guru/hide-delegate)

### Remove Middle Man

- **Signal:** A wrapper forwards most operations without policy, validation, lifecycle, or stable boundary value.
- **Move:** Expose the real collaborator or move meaningful behavior to the caller, update callers, and delete forwarding methods/class if safe.
- **Risk/check:** Check access control, metrics, compatibility, mocking seams, and ownership before bypassing; run API and integration tests.
- **Related:** Middle Man, Lazy Class; inverse of Hide Delegate. [Source](https://refactoring.guru/remove-middle-man)

### Introduce Foreign Method

- **Signal:** An external class needs one missing operation and cannot be changed or safely extended.
- **Move:** Add a local helper taking the foreign object as its first argument; keep conversion and policy near the caller boundary.
- **Risk/check:** Version and ownership remain external; test null/error and dependency-version behavior, and avoid pretending the method is part of the vendor API.
- **Related:** Incomplete Library Class, Primitive Obsession; use a local extension when several operations accumulate. [Source](https://refactoring.guru/introduce-foreign-method)

### Introduce Local Extension

- **Signal:** Several missing operations or a coherent policy are needed around an external type.
- **Move:** Wrap/subclass the external type behind a local type, expose only supported operations, and migrate callers.
- **Risk/check:** Preserve substitutability, construction, equality, serialization, version compatibility, and external ownership; contract-test the wrapper.
- **Related:** Incomplete Library Class, Adapter, Facade; stop before wrapper becomes a second framework. [Source](https://refactoring.guru/introduce-local-extension)

## Organizing Data

### Self Encapsulate Field

- **Signal:** Direct field access prevents validation, lazy computation, subclass override, or consistent mutation policy.
- **Move:** Route reads/writes through accessors, then add policy or replace the field representation behind that boundary.
- **Risk/check:** Preserve initialization order, recursion avoidance, visibility, and identity; test reads during construction and subclass behavior.
- **Related:** Data Class, Temporary Field; supports Replace Data Value with Object. [Source](https://refactoring.guru/self-encapsulate-field)

### Replace Data Value with Object

- **Signal:** A primitive or record value has repeated validation, formatting, comparison, or related operations.
- **Move:** Create a value object, move validation/behavior into it, migrate construction and comparisons, then tighten the old representation.
- **Risk/check:** Define equality, immutability, units, serialization, and invalid-input behavior; test boundaries and compatibility adapters.
- **Related:** Primitive Obsession, Data Clumps, Long Parameter List. [Source](https://refactoring.guru/replace-data-value-with-object)

### Change Value to Reference

- **Signal:** Equal-looking values must share identity and updates should be visible to all users.
- **Move:** Introduce a registry/repository or canonical lookup and replace duplicate value construction with reference retrieval.
- **Risk/check:** Define ownership, lifetime, concurrency, mutability, cache misses, and persistence identity; test same-instance and update visibility.
- **Related:** Primitive Obsession, Data Class; inverse of Change Reference to Value. [Source](https://refactoring.guru/change-value-to-reference)

### Change Reference to Value

- **Signal:** A shared reference creates unwanted coupling, mutation visibility, or lifecycle complexity, while the data is small and independent.
- **Move:** Copy into an immutable/value object, define value equality, and remove unnecessary shared identity.
- **Risk/check:** Preserve update semantics only where intended; test alias isolation, equality, serialization, and performance of copying.
- **Related:** Inappropriate Intimacy, Data Class; inverse of Change Value to Reference. [Source](https://refactoring.guru/change-reference-to-value)

### Replace Array with Object

- **Signal:** Array positions have stable meanings and callers remember indexes rather than names.
- **Move:** Create a record/object with named fields, migrate construction and reads, then remove positional access.
- **Risk/check:** Preserve ordering and external wire formats at adapters; test missing/default fields, equality, and serialization.
- **Related:** Primitive Obsession, Data Clumps, Long Parameter List. [Source](https://refactoring.guru/replace-array-with-object)

### Duplicate Observed Data

- **Signal:** UI/transport/persistence representation must mirror domain state but should not own domain behavior.
- **Move:** Create a separate representation, define explicit synchronization/update paths, and keep one authoritative owner.
- **Risk/check:** Prevent stale or partial copies; test initial load, every update path, failure/retry, ordering, and concurrent changes.
- **Related:** Inappropriate Intimacy, Data Class; often pairs with Observer but does not require it. [Source](https://refactoring.guru/duplicate-observed-data)

### Change Unidirectional Association to Bidirectional

- **Signal:** The reverse lookup is repeatedly reconstructed and is a real navigation requirement.
- **Move:** Add the reverse reference and centralize both-side add/remove/update operations.
- **Risk/check:** Maintain consistency, cycles, ownership, persistence, and garbage-collection behavior; test add, remove, replace, and failed update paths.
- **Related:** Message Chains, Inappropriate Intimacy; do not add reverse links for convenience alone. [Source](https://refactoring.guru/change-unidirectional-association-to-bidirectional)

### Change Bidirectional Association to Unidirectional

- **Signal:** Reverse navigation is unused or creates synchronization, lifecycle, or serialization cost.
- **Move:** Remove the reverse reference, replace needed queries with an owner/repository lookup, and update persistence mappings.
- **Risk/check:** Find reflection, serializers, equality, cascade, and query users before deletion; test deletion and reload semantics.
- **Related:** Inappropriate Intimacy, Message Chains; inverse of the bidirectional change. [Source](https://refactoring.guru/change-bidirectional-association-to-unidirectional)

### Replace Magic Number with Symbolic Constant

- **Signal:** A literal encodes a domain limit, unit, protocol value, or algorithm choice without visible meaning.
- **Move:** Name it at the narrowest correct scope, replace uses, and document unit/source when not self-evident.
- **Risk/check:** Do not merge numerically equal values with different meanings; test boundary behavior and serialization/API exactness.
- **Related:** Primitive Obsession, Comments, Duplicate Code. [Source](https://refactoring.guru/replace-magic-number-with-symbolic-constant)

### Encapsulate Field

- **Signal:** Public field access allows invalid mutation or makes representation part of the contract.
- **Move:** Make representation private, add the smallest read/write operations, migrate callers, then add validation or immutability.
- **Risk/check:** Preserve API compatibility deliberately, aliasing, subclass behavior, and serialization; test invalid writes and direct consumers.
- **Related:** Data Class, Temporary Field; often follows Self Encapsulate Field. [Source](https://refactoring.guru/encapsulate-field)

### Encapsulate Collection

- **Signal:** Callers can replace or mutate an owned collection, bypassing invariants or notification.
- **Move:** Return a read-only view/copy and expose intent-named add/remove/bulk operations owned by the aggregate.
- **Risk/check:** Define copy/view semantics, ordering, duplicates, concurrency, and serialization; test mutation attempts and all update notifications.
- **Related:** Data Class, Inappropriate Intimacy, Change Reference to Value. [Source](https://refactoring.guru/encapsulate-collection)

### Replace Type Code with Class

- **Signal:** A primitive discriminator has a fixed set of named values but no behavior of its own.
- **Move:** Introduce a type/value object, migrate comparisons and validation, and keep wire conversion at the boundary.
- **Risk/check:** Preserve equality, persistence, unknown-value behavior, and serialization; test old/new inputs during migration.
- **Related:** Primitive Obsession, Switch Statements; may precede subclasses or State/Strategy. [Source](https://refactoring.guru/replace-type-code-with-class)

### Replace Type Code with Subclasses

- **Signal:** Type-specific behavior and data are stable, substantial, and chosen at object creation.
- **Move:** Create subclasses with a common contract, move type branches, update factories/deserialization, and remove the discriminator.
- **Risk/check:** Preserve substitutability, equality, serialization, and construction; test every type and invalid transitions.
- **Related:** Switch Statements, Parallel Inheritance Hierarchies, Refused Bequest. [Source](https://refactoring.guru/replace-type-code-with-subclasses)

### Replace Type Code with State/Strategy

- **Signal:** Type-specific behavior changes during an object’s life or algorithm choice is runtime-configurable.
- **Move:** Extract a focused state/strategy contract, put variant behavior behind it, delegate from the context, and define transitions/selection.
- **Risk/check:** Make ownership, transition legality, persistence, and handler identity explicit; test all states/strategies and runtime switches.
- **Related:** Switch Statements, Temporary Field; links to [State](https://refactoring.guru/design-patterns/state) and [Strategy](https://refactoring.guru/design-patterns/strategy). [Source](https://refactoring.guru/replace-type-code-with-state-strategy)

### Replace Subclass with Fields

- **Signal:** Subclasses differ only by constant data and do not add meaningful behavior or invariants.
- **Move:** Put the varying values in the base object, replace subclass construction with named factories/data, and remove hierarchy.
- **Risk/check:** Preserve type checks, serialization, factory APIs, and equality; search subtype consumers before collapsing.
- **Related:** Lazy Class, Speculative Generality, Parallel Inheritance Hierarchies; inverse of subclass extraction. [Source](https://refactoring.guru/replace-subclass-with-fields)

## Simplifying Conditional Expressions

### Decompose Conditional

- **Signal:** Condition, true branch, and false branch each express a distinct business concept.
- **Move:** Extract intention-named query/action functions and keep the top-level decision readable.
- **Risk/check:** Preserve short-circuiting, evaluation order, mutation, time reads, and exception behavior; test each branch and boundary.
- **Related:** Long Method, Comments, Switch Statements. [Source](https://refactoring.guru/decompose-conditional)

### Consolidate Conditional Expression

- **Signal:** Several conditions produce the same result or guard the same action and represent one rule.
- **Move:** Combine into a named predicate or decision function, then use it once while preserving short-circuit/error semantics.
- **Risk/check:** Do not combine conditions with different side effects or error policy; test each predicate, precedence, and unknown input.
- **Related:** Switch Statements, Duplicate Code; can precede Introduce Assertion or Null Object. [Source](https://refactoring.guru/consolidate-conditional-expression)

### Consolidate Duplicate Conditional Fragments

- **Signal:** The same setup/cleanup/action appears in multiple conditional branches.
- **Move:** Move invariant code before/after the branch or into one helper, leaving only the varying part conditional.
- **Risk/check:** Preserve branch-specific ordering and exception/cleanup behavior; test success, failure, and early-return paths.
- **Related:** Duplicate Code, Long Method, Remove Control Flag. [Source](https://refactoring.guru/consolidate-duplicate-conditional-fragments)

### Remove Control Flag

- **Signal:** A boolean variable exists solely to stop/skip loops or communicate a branch exit.
- **Move:** Use `break`, `return`, `continue`, exceptions, or a named predicate appropriate to the contract.
- **Risk/check:** Preserve nested-loop scope, cleanup, and caller-visible returns; test early and late exits plus no-match behavior.
- **Related:** Long Method, Switch Statements; avoid replacing a meaningful domain state with control flow. [Source](https://refactoring.guru/remove-control-flag)

### Replace Nested Conditional with Guard Clauses

- **Signal:** Main logic is buried under repeated success nesting and exceptional cases are hard to see.
- **Move:** Return/raise early for invalid or exceptional cases, then leave the normal path flat.
- **Risk/check:** Preserve exception types, cleanup, authorization order, and side effects; test every guard and normal path.
- **Related:** Long Method, Comments, Remove Control Flag. [Source](https://refactoring.guru/replace-nested-conditional-with-guard-clauses)

### Replace Conditional with Polymorphism

- **Signal:** A discriminator repeatedly selects behavior that belongs to separate variants.
- **Move:** Define a common contract, move each branch into a variant, delegate from the context, and retain explicit selection.
- **Risk/check:** Prove substitutability, lifecycle, serialization, default/unknown behavior, and variant completeness; do not create a hierarchy for one stable branch.
- **Related:** Switch Statements, Refused Bequest, Type Code; may use State/Strategy. [Source](https://refactoring.guru/replace-conditional-with-polymorphism)

### Introduce Null Object

- **Signal:** Callers repeat null checks for a legitimate “no behavior/no result” case.
- **Move:** Define the same contract for an explicit neutral object and replace null branches with it at the boundary.
- **Risk/check:** Make absence observable where required, avoid hiding errors, and preserve equality/serialization; test absent, present, and invalid cases.
- **Related:** Switch Statements, Temporary Field, Message Chains. [Source](https://refactoring.guru/introduce-null-object)

### Introduce Assertion

- **Signal:** A required invariant is assumed but not checked near the point where it must hold.
- **Move:** Add an executable assertion or domain-specific validation with a useful failure message at the narrowest boundary.
- **Risk/check:** Never use assertions for recoverable user input or security checks that must run when assertions are disabled; test enabled failure behavior.
- **Related:** Comments, Primitive Obsession, Temporary Field. [Source](https://refactoring.guru/introduce-assertion)

## Simplifying Method Calls

### Rename Method

- **Signal:** Name does not state intent, uses inconsistent vocabulary, or hides whether operation queries or mutates.
- **Move:** Choose a domain-accurate name, update declarations/callers/docs, and keep a compatibility alias only when migration needs it.
- **Risk/check:** Preserve public API, reflection, serialization, overrides, and metrics; search dynamic references and run contract tests.
- **Related:** Comments, Alternative Classes with Different Interfaces, Middle Man. [Source](https://refactoring.guru/rename-method)

### Add Parameter

- **Signal:** A method needs context currently obtained implicitly or cannot satisfy a new explicit contract.
- **Move:** Add the parameter with a safe migration/default at the boundary, update callers, then remove the compatibility path when safe.
- **Risk/check:** Preserve overload resolution, defaults, positional callers, serialization, and dependency flow; test old/new call shapes.
- **Related:** Long Parameter List, Primitive Obsession; consider Parameter Object if additions continue. [Source](https://refactoring.guru/add-parameter)

### Remove Parameter

- **Signal:** A parameter is unused, derivable, duplicated, or no longer part of the operation’s contract.
- **Move:** Delete it from declaration and every call, then remove stale docs/adapters and verify dynamic/reflection callers.
- **Risk/check:** Do not remove a parameter whose side-effectful expression was relied on; preserve API migration deliberately and test defaults.
- **Related:** Long Parameter List, Speculative Generality, Dead Code. [Source](https://refactoring.guru/remove-parameter)

### Separate Query from Modifier

- **Signal:** One method both returns information and changes state, making retries and reasoning unsafe.
- **Move:** Split read and write operations; let a command call the query explicitly when both are needed.
- **Risk/check:** Preserve atomicity, caching, transaction boundaries, and evaluation order; test repeated queries and failed modifications.
- **Related:** Data Class, Comments, Long Method; supports Command and event boundaries. [Source](https://refactoring.guru/separate-query-from-modifier)

### Parameterize Method

- **Signal:** Several methods differ only by a small value or condition and duplicate the same algorithm.
- **Move:** Introduce a parameter for the varying value, update callers, and name the policy clearly.
- **Risk/check:** Avoid a boolean parameter that hides unrelated modes; preserve defaults, validation, and branch semantics with representative tests.
- **Related:** Duplicate Code, Switch Statements, Long Parameter List; inverse may be Replace Parameter with Explicit Methods. [Source](https://refactoring.guru/parameterize-method)

### Replace Parameter with Explicit Methods

- **Signal:** A parameter selects a few fixed behaviors and callers pass opaque flags/values.
- **Move:** Create intention-named methods that call a shared implementation or pass explicit policy.
- **Risk/check:** Prevent combinatorial method growth and preserve validation/error differences; test each named operation and shared path.
- **Related:** Switch Statements, Primitive Obsession; inverse of Parameterize Method. [Source](https://refactoring.guru/replace-parameter-with-explicit-methods)

### Preserve Whole Object

- **Signal:** Callers unpack several fields from one object only to pass them together to another method.
- **Move:** Pass the source object, derive fields at the callee boundary, and remove redundant parameters.
- **Risk/check:** Preserve snapshot timing, encapsulation, mutation visibility, null/default behavior, and API compatibility; test changed source state.
- **Related:** Data Clumps, Long Parameter List, Feature Envy. [Source](https://refactoring.guru/preserve-whole-object)

### Replace Parameter with Method Call

- **Signal:** A caller computes a value the callee can derive from stable state or another parameter.
- **Move:** Remove the redundant parameter and calculate it inside the callee through a named query.
- **Risk/check:** Preserve calculation timing, override behavior, side effects, caching, and error context; test changed state between calls.
- **Related:** Long Parameter List, Feature Envy, Replace Temp with Query. [Source](https://refactoring.guru/replace-parameter-with-method-call)

### Introduce Parameter Object

- **Signal:** Several parameters travel together, have shared validation, or form a meaningful request/context.
- **Move:** Create a value/request object, move validation and related behavior into it, then migrate callers.
- **Risk/check:** Define immutability, defaults, equality, versioning, and serialization; test old/new request shapes and invalid combinations.
- **Related:** Data Clumps, Long Parameter List, Primitive Obsession. [Source](https://refactoring.guru/introduce-parameter-object)

### Remove Setting Method

- **Signal:** A setter permits invalid transitions or mutation after construction when the value should be fixed.
- **Move:** Set through constructor/factory or an intent-specific command, remove the generic setter, and update callers.
- **Risk/check:** Preserve deserialization, ORM/framework hooks, subclass behavior, and migration; test construction and rejected mutation.
- **Related:** Data Class, Temporary Field, Speculative Generality. [Source](https://refactoring.guru/remove-setting-method)

### Hide Method

- **Signal:** A method is implementation detail but has broader visibility than its callers require.
- **Move:** Narrow visibility, update internal call sites, and expose a higher-level operation only if a real contract exists.
- **Risk/check:** Search reflection, subclass, plugin, serialization, and external consumers; compile and contract-test before narrowing.
- **Related:** Inappropriate Intimacy, Middle Man, Large Class. [Source](https://refactoring.guru/hide-method)

### Replace Constructor with Factory Method

- **Signal:** Construction needs a meaningful name, variant selection, validation, caching, or subclass-specific creation.
- **Move:** Add a named factory, migrate callers, make direct construction private/uncommon where the language permits, and keep ownership explicit.
- **Risk/check:** Preserve identity, initialization order, exceptions, subclassing, serialization, and dependency injection; test every variant.
- **Related:** Primitive Obsession, Switch Statements, Factory Method pattern; do not add it for a plain record constructor. [Source](https://refactoring.guru/replace-constructor-with-factory-method)

### Replace Error Code with Exception

- **Signal:** Callers must remember to inspect return codes and normal values can be confused with failure.
- **Move:** Raise a specific exception at the failure boundary, catch it where recovery belongs, and remove sentinel plumbing.
- **Risk/check:** Preserve transaction/cleanup, retry, public error contract, and exception taxonomy; test success, expected failure, and unexpected failure.
- **Related:** Long Method, Primitive Obsession, Separate Query from Modifier. [Source](https://refactoring.guru/replace-error-code-with-exception)

### Replace Exception with Test

- **Signal:** An exception is used for ordinary branching where a cheap precondition can decide safely.
- **Move:** Test the expected condition first, reserve exceptions for abnormal failures, and keep race-prone checks inside the operation when required.
- **Risk/check:** Avoid time-of-check/time-of-use bugs and duplicated expensive work; test races/concurrency, invalid input, and exception propagation.
- **Related:** Introduce Assertion, Replace Error Code with Exception, Long Method. [Source](https://refactoring.guru/replace-exception-with-test)

## Dealing with Generalization

### Pull Up Field

- **Signal:** Sibling subclasses duplicate the same field, initialization, or invariant.
- **Move:** Add the field to the common base, migrate constructors/access, and delete duplicates after all subclasses compile and test.
- **Risk/check:** Preserve visibility, defaults, storage mapping, initialization order, and subtype-specific meaning; run every subtype contract test.
- **Related:** Parallel Inheritance Hierarchies, Duplicate Code, Divergent Change. [Source](https://refactoring.guru/pull-up-field)

### Pull Up Method

- **Signal:** Sibling subclasses implement equivalent behavior under different or identical names.
- **Move:** align signatures, move shared implementation to the base, retain explicit hooks only for real variation, and delete duplicates.
- **Risk/check:** Prove semantic equivalence, dispatch, access, exception, and side-effect order; test all subclasses and overrides.
- **Related:** Duplicate Code, Alternative Classes with Different Interfaces, Form Template Method. [Source](https://refactoring.guru/pull-up-method)

### Pull Up Constructor Body

- **Signal:** Subclass constructors repeat common initialization before variant-specific work.
- **Move:** Move common initialization into the base constructor/factory, leaving explicit subclass extension points.
- **Risk/check:** Preserve virtual-dispatch safety, initialization order, defaults, and failure cleanup; test construction for each subtype.
- **Related:** Duplicate Code, Parallel Inheritance Hierarchies, Pull Up Field. [Source](https://refactoring.guru/pull-up-constructor-body)

### Push Down Method

- **Signal:** A base method is meaningful to only some subclasses and forces unrelated subtypes to inherit it.
- **Move:** Move the method to the owning subtype(s), narrow the base contract, and update polymorphic callers if needed.
- **Risk/check:** Check dynamic dispatch, external base consumers, visibility, and duplicate behavior; test supported and unsupported subtype calls.
- **Related:** Refused Bequest, Speculative Generality, Extract Subclass. [Source](https://refactoring.guru/push-down-method)

### Push Down Field

- **Signal:** A base field is meaningful to only one or a few subclasses.
- **Move:** Move storage and access to those subtypes, update construction/serialization, and remove the base field.
- **Risk/check:** Preserve base invariants, reflection, persistence, and subtype initialization; test every consumer and absent-field case.
- **Related:** Refused Bequest, Temporary Field, Extract Subclass. [Source](https://refactoring.guru/push-down-field)

### Extract Subclass

- **Signal:** One subtype-specific feature set is conditional, optional, or makes the base awkward for other instances.
- **Move:** Create a subtype, move data/behavior and creation rules, then replace flags/conditionals with subtype selection.
- **Risk/check:** Preserve substitutability, serialization, equality, factories, and valid construction; test base-only and subtype paths.
- **Related:** Temporary Field, Switch Statements, Replace Type Code with Subclasses. [Source](https://refactoring.guru/extract-subclass)

### Extract Superclass

- **Signal:** Classes share meaningful state/behavior and a stable common contract, but duplication is costly.
- **Move:** Create a base, pull up only proven common members, migrate callers, and keep variant behavior explicit.
- **Risk/check:** Avoid false abstraction and refused bequest; test substitutability, initialization, visibility, and all subclasses.
- **Related:** Duplicate Code, Alternative Classes with Different Interfaces, Pull Up Method. [Source](https://refactoring.guru/extract-superclass)

### Extract Interface

- **Signal:** Clients need a smaller stable contract or multiple implementations must be substitutable without sharing implementation.
- **Move:** Define the minimal interface from actual clients, implement it, type callers against it, and keep unsupported operations out.
- **Risk/check:** Preserve semantic contracts, error behavior, variance, and dependency injection; contract-test each implementation.
- **Related:** Alternative Classes with Different Interfaces, Large Class, Adapter. [Source](https://refactoring.guru/extract-interface)

### Collapse Hierarchy

- **Signal:** A subclass adds no meaningful behavior/state or hierarchy variation has disappeared.
- **Move:** Move useful members into the remaining class, update constructors/type checks, and delete the empty subtype.
- **Risk/check:** Search serialization, reflection, public imports, factories, and external subclasses; test identity/equality and compatibility.
- **Related:** Lazy Class, Speculative Generality, Replace Subclass with Fields. [Source](https://refactoring.guru/collapse-hierarchy)

### Form Template Method

- **Signal:** Sibling methods perform the same ordered algorithm with a few varying steps.
- **Move:** Extract the invariant skeleton into a shared operation and expose only explicit hooks for variation.
- **Risk/check:** Preserve ordering, hook count, exceptions, transaction boundaries, and subclass contracts; test sequence and each hook combination.
- **Related:** Duplicate Code, Pull Up Method, Template Method pattern. [Source](https://refactoring.guru/form-template-method)

### Replace Inheritance with Delegation

- **Signal:** Inheritance is used for reuse but subtype substitution, protected coupling, or inherited surface is unsafe.
- **Move:** Hold the former base object, forward only needed operations, and expose an explicit local contract.
- **Risk/check:** Preserve polymorphic behavior, identity, callbacks, lifecycle, and extension semantics; test clients that relied on inherited members.
- **Related:** Refused Bequest, Inappropriate Intimacy, Bridge/Decorator/Adapter. [Source](https://refactoring.guru/replace-inheritance-with-delegation)

### Replace Delegation with Inheritance

- **Signal:** A wrapper forwards nearly the full stable contract of a type and is intended to be substitutable for it.
- **Move:** Inherit from the delegated type only when the subtype contract is true, remove redundant forwarding, and preserve overrides.
- **Risk/check:** Check Liskov substitution, future base changes, identity, security, and lifecycle; test full inherited contract and rejected operations.
- **Related:** Middle Man, Lazy Class, Refused Bequest; inverse of Replace Inheritance with Delegation. [Source](https://refactoring.guru/replace-delegation-with-inheritance)
