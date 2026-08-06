# Code smells

Use smell names as investigation prompts, not automatic violations. Confirm the pressure in callers, tests, ownership, and change history before proposing a move. Source baseline: [Refactoring.Guru code-smell catalog](https://refactoring.guru/refactoring/catalog).

## Contents

- [Bloaters](#bloaters)
- [Object-Orientation Abusers](#object-orientation-abusers)
- [Change Preventers](#change-preventers)
- [Dispensables](#dispensables)
- [Couplers](#couplers)

## Bloaters

### Long Method

- **Definition/signals:** One function carries several recognizable responsibilities; deep nesting, comments that name substeps, repeated local clusters, or frequent edits make its body hard to read. Line count is only a clue.
- **Cost/boundary:** Hides control flow and duplicates; a short but dense parser may be intentional, while a long orchestration method may be the real problem.
- **First candidates:** [Extract Method](https://refactoring.guru/extract-method), [Decompose Conditional](https://refactoring.guru/decompose-conditional), [Replace Method with Method Object](https://refactoring.guru/replace-method-with-method-object).
- **Evidence/verify:** Identify a coherent fragment and its inputs/outputs; preserve ordering, mutation, exceptions, and loop behavior with focused tests.
- **Source:** [Long Method](https://refactoring.guru/smells/long-method)

### Large Class

- **Definition/signals:** A class knows or does too many unrelated things: unrelated fields, clusters of methods, multiple reasons to change, or persistent navigation across collaborators.
- **Cost/boundary:** Changes collide and invariants become unclear; a domain aggregate may legitimately be broad when it owns one cohesive invariant.
- **First candidates:** [Extract Class](https://refactoring.guru/extract-class), [Extract Subclass](https://refactoring.guru/extract-subclass), [Move Method](https://refactoring.guru/move-method), [Extract Interface](https://refactoring.guru/extract-interface).
- **Evidence/verify:** Group members by reasons for change and field usage; test each moved responsibility plus serialization, equality, and lifecycle boundaries.
- **Source:** [Large Class](https://refactoring.guru/smells/large-class)

### Primitive Obsession

- **Definition/signals:** Domain concepts are represented by raw strings, numbers, booleans, or generic collections throughout the code; validation and formatting repeat at call sites.
- **Cost/boundary:** Units, invalid states, and meaning leak across APIs; primitives remain right for genuinely simple values and stable external formats.
- **First candidates:** [Replace Data Value with Object](https://refactoring.guru/replace-data-value-with-object), [Replace Type Code with Class](https://refactoring.guru/replace-type-code-with-class), [Introduce Parameter Object](https://refactoring.guru/introduce-parameter-object), [Replace Magic Number with Symbolic Constant](https://refactoring.guru/replace-magic-number-with-symbolic-constant).
- **Evidence/verify:** Find repeated validation/conversion or unit confusion; test construction, equality, serialization, boundary validation, and migration compatibility.
- **Source:** [Primitive Obsession](https://refactoring.guru/smells/primitive-obsession)

### Long Parameter List

- **Definition/signals:** A function accepts many arguments, especially repeated clusters that travel together or are often passed in the same combinations.
- **Cost/boundary:** Call sites become positional and easy to misuse; a parameter list can be honest when the operation truly needs independent values.
- **First candidates:** [Introduce Parameter Object](https://refactoring.guru/introduce-parameter-object), [Preserve Whole Object](https://refactoring.guru/preserve-whole-object), [Replace Parameter with Method Call](https://refactoring.guru/replace-parameter-with-method-call), [Remove Parameter](https://refactoring.guru/remove-parameter).
- **Evidence/verify:** Inspect call-site clusters and parameter derivability; preserve defaults, keyword compatibility, validation order, and public API migration.
- **Source:** [Long Parameter List](https://refactoring.guru/smells/long-parameter-list)

### Data Clumps

- **Definition/signals:** The same group of fields or arguments appears together in multiple signatures, records, or calculations and is repeatedly copied or unpacked.
- **Cost/boundary:** Missing ownership causes inconsistent validation and parallel edits; repeated fields may be coincidental when their lifetimes and rules differ.
- **First candidates:** [Extract Class](https://refactoring.guru/extract-class), [Introduce Parameter Object](https://refactoring.guru/introduce-parameter-object), [Move Method](https://refactoring.guru/move-method).
- **Evidence/verify:** Confirm the values travel, change, and validate together; test construction, serialization, null/default behavior, and all affected call sites.
- **Source:** [Data Clumps](https://refactoring.guru/smells/data-clumps)

## Object-Orientation Abusers

### Switch Statements

- **Definition/signals:** The same discriminator and branches recur across methods, or a conditional keeps growing as new variants arrive.
- **Cost/boundary:** Variant behavior is scattered and every addition edits central code; a small closed decision with no independent variation may be clearer as a branch.
- **First candidates:** [Replace Conditional with Polymorphism](https://refactoring.guru/replace-conditional-with-polymorphism), [Replace Type Code with State/Strategy](https://refactoring.guru/replace-type-code-with-state-strategy), [Parameterize Method](https://refactoring.guru/parameterize-method), [Consolidate Conditional Expression](https://refactoring.guru/consolidate-conditional-expression).
- **Evidence/verify:** Map every discriminator use and default/error case; test all variants, unknown values, ordering, and persistence/API compatibility.
- **Source:** [Switch Statements](https://refactoring.guru/smells/switch-statements)

### Temporary Field

- **Definition/signals:** An object field is meaningful only during certain operations, otherwise unset, sentinel-valued, or semantically invalid.
- **Cost/boundary:** Object invariants and lifecycle become conditional; fields may be legitimate when the object explicitly models a multi-step state.
- **First candidates:** [Extract Class](https://refactoring.guru/extract-class), [Replace Method with Method Object](https://refactoring.guru/replace-method-with-method-object), [Introduce Null Object](https://refactoring.guru/introduce-null-object), [Move Field](https://refactoring.guru/move-field).
- **Evidence/verify:** Trace writes, reads, reset paths, exceptions, and concurrent reuse; test incomplete, repeated, and failed operations.
- **Source:** [Temporary Field](https://refactoring.guru/smells/temporary-field)

### Refused Bequest

- **Definition/signals:** A subclass inherits behavior or data it does not support, overrides methods to reject them, or exposes an interface broader than its contract.
- **Cost/boundary:** Substitutability is false and callers need type checks; inherited implementation can still be valid when the subtype genuinely honors the base invariant.
- **First candidates:** [Replace Inheritance with Delegation](https://refactoring.guru/replace-inheritance-with-delegation), [Push Down Method](https://refactoring.guru/push-down-method), [Push Down Field](https://refactoring.guru/push-down-field), [Extract Subclass](https://refactoring.guru/extract-subclass).
- **Evidence/verify:** Check base contract, rejected methods, and all subtype consumers; test Liskov-relevant behavior and public type compatibility.
- **Source:** [Refused Bequest](https://refactoring.guru/smells/refused-bequest)

### Alternative Classes with Different Interfaces

- **Definition/signals:** Classes serve the same conceptual role but expose different method names, argument shapes, or result conventions, forcing caller branching.
- **Cost/boundary:** Polymorphism and replacement are unavailable; differences may be intentional at an integration boundary.
- **First candidates:** [Rename Method](https://refactoring.guru/rename-method), [Extract Interface](https://refactoring.guru/extract-interface), [Adapter](https://refactoring.guru/design-patterns/adapter), [Parameterize Method](https://refactoring.guru/parameterize-method).
- **Evidence/verify:** Compare semantic contracts, not names alone; test a shared contract, error mapping, optional capability, and adapter conversions.
- **Source:** [Alternative Classes with Different Interfaces](https://refactoring.guru/smells/alternative-classes-with-different-interfaces)

## Change Preventers

### Divergent Change

- **Definition/signals:** One module or class is repeatedly edited for unrelated causes such as storage, formatting, policy, and transport changes.
- **Cost/boundary:** Responsibilities have separate volatility and changes interfere; a cohesive boundary can still have several legitimate callers.
- **First candidates:** [Extract Class](https://refactoring.guru/extract-class), [Move Method](https://refactoring.guru/move-method), [Move Field](https://refactoring.guru/move-field), [Extract Interface](https://refactoring.guru/extract-interface).
- **Evidence/verify:** Group recent changes by reason and owner; test behavior at each extracted boundary and dependency direction.
- **Source:** [Divergent Change](https://refactoring.guru/smells/divergent-change)

### Shotgun Surgery

- **Definition/signals:** One conceptual change requires small edits across many classes, files, branches, or duplicated schemas.
- **Cost/boundary:** Changes are easy to miss and hard to review; distributed ownership may be intentional for independent deployable components.
- **First candidates:** [Move Method](https://refactoring.guru/move-method), [Move Field](https://refactoring.guru/move-field), [Extract Class](https://refactoring.guru/extract-class), [Pull Up Method](https://refactoring.guru/pull-up-method), [Encapsulate Collection](https://refactoring.guru/encapsulate-collection).
- **Evidence/verify:** Trace one real change request and all touched locations; use contract tests and search-based completeness checks before/after.
- **Source:** [Shotgun Surgery](https://refactoring.guru/smells/shotgun-surgery)

### Parallel Inheritance Hierarchies

- **Definition/signals:** Adding one subclass in one hierarchy repeatedly requires a corresponding subclass in another hierarchy.
- **Cost/boundary:** Variant axes multiply classes and synchronization work; paired hierarchies can be valid when both axes are stable and explicit.
- **First candidates:** [Move Method](https://refactoring.guru/move-method), [Move Field](https://refactoring.guru/move-field), [Replace Inheritance with Delegation](https://refactoring.guru/replace-inheritance-with-delegation), [Bridge](https://refactoring.guru/design-patterns/bridge).
- **Evidence/verify:** Identify independent axes and creation rules; test the full variant matrix and absence of invalid combinations.
- **Source:** [Parallel Inheritance Hierarchies](https://refactoring.guru/smells/parallel-inheritance-hierarchies)

## Dispensables

### Comments

- **Definition/signals:** Comments explain what tangled code does, compensate for unclear names, or preserve obsolete intent instead of documenting a real external constraint.
- **Cost/boundary:** Stale explanations mislead and hide extractable behavior; comments are valuable for why, legal, safety, compatibility, and non-obvious invariants.
- **First candidates:** [Extract Method](https://refactoring.guru/extract-method), [Rename Method](https://refactoring.guru/rename-method), [Introduce Assertion](https://refactoring.guru/introduce-assertion), [Replace Magic Number with Symbolic Constant](https://refactoring.guru/replace-magic-number-with-symbolic-constant).
- **Evidence/verify:** Classify each comment as why, contract, warning, or narration; after cleanup, verify the code and durable rationale still communicate intent.
- **Source:** [Comments](https://refactoring.guru/smells/comments)

### Duplicate Code

- **Definition/signals:** Equivalent or near-equivalent logic, including bug fixes and validation, appears in multiple locations.
- **Cost/boundary:** Fixes drift and behavior diverges; repetition may be safer when abstractions would couple unrelated policies or contexts.
- **First candidates:** [Extract Method](https://refactoring.guru/extract-method), [Pull Up Method](https://refactoring.guru/pull-up-method), [Form Template Method](https://refactoring.guru/form-template-method), [Parameterize Method](https://refactoring.guru/parameterize-method), [Substitute Algorithm](https://refactoring.guru/substitute-algorithm).
- **Evidence/verify:** Compare semantics and change reasons, not text similarity; test shared cases plus deliberately different cases so over-generalization is caught.
- **Source:** [Duplicate Code](https://refactoring.guru/smells/duplicate-code)

### Lazy Class

- **Definition/signals:** A class, wrapper, or hierarchy adds little behavior, ownership, or protection relative to its ceremony and maintenance cost.
- **Cost/boundary:** Increases navigation and indirection; a small class may be a valuable stable boundary, plugin seam, or future-proofing with explicit evidence.
- **First candidates:** [Inline Class](https://refactoring.guru/inline-class), [Collapse Hierarchy](https://refactoring.guru/collapse-hierarchy), [Remove Middle Man](https://refactoring.guru/remove-middle-man).
- **Evidence/verify:** Measure callers, invariants, extension points, and change ownership; preserve public imports, lifecycle hooks, and serialization when inlining.
- **Source:** [Lazy Class](https://refactoring.guru/smells/lazy-class)

### Data Class

- **Definition/signals:** A class mostly exposes fields and accessors while behavior that should enforce its data invariants lives elsewhere.
- **Cost/boundary:** Callers duplicate rules and can create invalid states; DTOs, persistence records, messages, and API schemas are intentionally data-oriented.
- **First candidates:** [Move Method](https://refactoring.guru/move-method), [Encapsulate Field](https://refactoring.guru/encapsulate-field), [Replace Data Value with Object](https://refactoring.guru/replace-data-value-with-object), [Remove Setting Method](https://refactoring.guru/remove-setting-method).
- **Evidence/verify:** Find repeated consumers and invariant logic; test construction, mutation, serialization, equality, and domain behavior after moving it.
- **Source:** [Data Class](https://refactoring.guru/smells/data-class)

### Dead Code

- **Definition/signals:** Unreachable branches, unused declarations, obsolete flags, ignored results, or code no build/test/runtime path exercises.
- **Cost/boundary:** Adds misleading surface and hides real behavior; generated code, feature-flagged paths, public extension points, and migration shims need explicit proof before deletion.
- **First candidates:** Delete after search/build evidence; otherwise [Inline Method](https://refactoring.guru/inline-method), [Remove Parameter](https://refactoring.guru/remove-parameter), [Collapse Hierarchy](https://refactoring.guru/collapse-hierarchy), or flag cleanup.
- **Evidence/verify:** Search references, exports, reflection, configuration, dynamic loading, and deployment manifests; run build, tests, and relevant smoke checks after deletion.
- **Source:** [Dead Code](https://refactoring.guru/smells/dead-code)

### Speculative Generality

- **Definition/signals:** Hooks, abstractions, parameters, subclasses, or extension points exist for imagined future variation and have no current pressure.
- **Cost/boundary:** Adds concepts and paths users must understand; a proven plugin contract or compatibility seam is not speculative merely because it is small.
- **First candidates:** [Inline Class](https://refactoring.guru/inline-class), [Remove Parameter](https://refactoring.guru/remove-parameter), [Collapse Hierarchy](https://refactoring.guru/collapse-hierarchy), [Remove Setting Method](https://refactoring.guru/remove-setting-method).
- **Evidence/verify:** Identify unused variability and current callers; simplify while preserving documented extension contracts and compile-time/API compatibility.
- **Source:** [Speculative Generality](https://refactoring.guru/smells/speculative-generality)

## Couplers

### Feature Envy

- **Definition/signals:** A method reads or manipulates another object’s data far more than its own and effectively owns that object’s behavior.
- **Cost/boundary:** Rules sit away from the data they protect and coupling grows; orchestration and reporting may legitimately coordinate several objects.
- **First candidates:** [Move Method](https://refactoring.guru/move-method), [Extract Method](https://refactoring.guru/extract-method), [Move Field](https://refactoring.guru/move-field), [Extract Class](https://refactoring.guru/extract-class).
- **Evidence/verify:** Count meaningful data accesses and ask which object owns the invariant; test authorization, transaction, lazy-loading, and dependency direction after moving.
- **Source:** [Feature Envy](https://refactoring.guru/smells/feature-envy)

### Inappropriate Intimacy

- **Definition/signals:** Two modules reach into private details, depend on internal ordering, or mutually know implementation details rather than a stable contract.
- **Cost/boundary:** Small internal changes ripple across boundaries and cycles become likely; tightly coupled aggregate internals can be deliberate within one ownership boundary.
- **First candidates:** [Move Method](https://refactoring.guru/move-method), [Move Field](https://refactoring.guru/move-field), [Hide Delegate](https://refactoring.guru/hide-delegate), [Extract Class](https://refactoring.guru/extract-class), [Replace Inheritance with Delegation](https://refactoring.guru/replace-inheritance-with-delegation).
- **Evidence/verify:** Map private access, cycles, and order assumptions; test public contract behavior, failure propagation, and ownership after the boundary is tightened.
- **Source:** [Inappropriate Intimacy](https://refactoring.guru/smells/inappropriate-intimacy)

### Message Chains

- **Definition/signals:** Callers navigate a long sequence of getters/delegates to reach a result, exposing object graph structure.
- **Cost/boundary:** Intermediate changes break distant callers and null/error handling spreads; a short fluent API can be the intended contract when each link is stable.
- **First candidates:** [Hide Delegate](https://refactoring.guru/hide-delegate), [Extract Method](https://refactoring.guru/extract-method), [Move Method](https://refactoring.guru/move-method), [Introduce Parameter Object](https://refactoring.guru/introduce-parameter-object).
- **Evidence/verify:** Trace the full chain and ownership of the requested operation; test missing links, permissions, lazy loading, and stable facade behavior.
- **Source:** [Message Chains](https://refactoring.guru/smells/message-chains)

### Middle Man

- **Definition/signals:** A class forwards most calls to another object and contributes little policy, validation, or lifecycle ownership.
- **Cost/boundary:** Clients must navigate an unnecessary layer; a facade, security boundary, compatibility adapter, or stable port is not a middle man merely because it delegates.
- **First candidates:** [Remove Middle Man](https://refactoring.guru/remove-middle-man), [Hide Delegate](https://refactoring.guru/hide-delegate), [Inline Class](https://refactoring.guru/inline-class), [Facade](https://refactoring.guru/design-patterns/facade) when the boundary is intentional.
- **Evidence/verify:** Compare forwarded surface with actual policy and ownership; test callers, API compatibility, instrumentation, authorization, and lifecycle effects before removal.
- **Source:** [Middle Man](https://refactoring.guru/smells/middle-man)

### Incomplete Library Class

- **Definition/signals:** A third-party or standard class is almost sufficient, but repeated callers add the same missing operation or conversion around it.
- **Cost/boundary:** Workarounds duplicate policy and leak vendor details; modifying or subclassing an external type may be unsafe or impossible.
- **First candidates:** [Introduce Foreign Method](https://refactoring.guru/introduce-foreign-method), [Introduce Local Extension](https://refactoring.guru/introduce-local-extension), [Adapter](https://refactoring.guru/design-patterns/adapter), [Facade](https://refactoring.guru/design-patterns/facade).
- **Evidence/verify:** Confirm ownership/license/version constraints and repeated semantics; test the wrapper against supported dependency versions and conversion failures.
- **Source:** [Incomplete Library Class](https://refactoring.guru/smells/incomplete-library-class)
