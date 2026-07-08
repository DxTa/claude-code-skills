---
name: clean-code
description: Apply Robert C. Martin Clean Code principles and the clean-code-skills rule catalog when code quality is explicit or when an agent is reviewing, simplifying, refactoring, or cleaning touched code. Use for clean code, code smells, maintainability, readability, naming, small functions, comments/docstrings, DRY, duplication, magic numbers, boundary conditions, Boy Scout cleanup, refactor review, PR review, code quality review, test readability, boundary test coverage, test maintainability, or requests like "make this cleaner", "review for maintainability", "is this clean code", "simplify this", "remove code smells", "rename this", "split this function", "clean up comments", "clean up tests", or "review tests for clarity". For Python or TypeScript, load only the matching language reference file for files in active scope.
disable-model-invocation: true
---

# Clean Code

Use this skill to improve or review code quality without changing behavior. It consolidates the `clean-code-skills` repository taxonomy and cross-checks it against Robert C. Martin's *Clean Code* themes: meaningful names, small focused functions, minimal truthful comments, clear structure, boundary care, tests, and continuous small cleanup.

## Progressive disclosure

Core rules live here. Language-specific adaptations live in references and load only when needed:

- Python: read `references/python.md` when active scope includes `.py`, Python tests, Python APIs, or Python refactors.
- TypeScript/TSX: read `references/typescript.md` when active scope includes `.ts`, `.tsx`, TypeScript tests, React props, or TS APIs.
- Future languages: copy `references/language-extension-template.md` to `references/<language>.md`, add a short bullet above, and keep language guidance out of core unless it applies broadly.
- Sources: read `references/sources.md` when source provenance, licensing, or update traceability matters.

Load only references matching files in active scope. In mixed-language repositories, do not load Python and TypeScript references merely because both languages exist.

Do not duplicate this core catalog in language files. Language files add idioms, smells, and examples only.

## Operating stance

1. Preserve behavior first. Clean-code changes must not alter public contracts unless user asks.
2. Prefer project rules, formatter, linter, and existing conventions over generic Clean Code rules.
3. Improve touched code only unless user asks for broad refactor.
4. Apply Boy Scout rule: leave touched module slightly cleaner, not completely rewritten.
5. Report only material findings. Avoid style nits unless they affect readability, maintainability, correctness, or project standards.
6. Verify with tests, typecheck, lint, or focused inspection before claiming cleanup is safe.

## Workflow

When writing or editing code:

1. Load language reference if relevant.
2. Implement requested behavior with existing project patterns.
3. Scan touched code for nearby cleanup: names, dead code, duplication, comments, magic values, boundary handling, test gaps.
4. Make smallest coherent cleanup that preserves behavior.
5. Add/update tests for behavior and boundaries when logic changes.
6. State notable cleanup with rule IDs, e.g. `Fixed G25: replaced magic timeout with RETRY_TIMEOUT_MS`.

When reviewing code:

1. Load language reference if relevant.
2. Identify scope: diff, files, PR, or function.
3. Check correctness first, then clean-code issues.
4. Cite file path and line when possible.
5. Classify findings by impact: correctness risk, maintainability risk, readability risk, test risk.
6. Suggest concrete fixes, not vague advice.
7. Use rule IDs for traceability.

## Core rule catalog

### Comments (C)

- **C1 No metadata comments**: keep authors, dates, ticket history, and changelogs in Git or issue trackers.
- **C2 Delete obsolete comments**: stale comments mislead; remove immediately.
- **C3 No redundant comments**: do not restate obvious code.
- **C4 Write comments well when needed**: concise, precise, explains why or non-obvious constraints.
- **C5 No commented-out code**: delete it; version control preserves history.

Default move: refactor code to explain itself. Comment only when intent, domain context, workaround, security rationale, or invariant is not obvious from code.

### Environment (E)

- **E1 One command to build**: project should have a clear build/setup path.
- **E2 One command to test**: project should have a clear test path.

Flag missing or fragmented build/test workflows when they block safe changes.

### Functions (F)

- **F1 Few arguments**: prefer 0-3 arguments. Use cohesive parameter objects/value types for more.
- **F2 No output arguments**: prefer return values over mutating inputs unless mutation is idiomatic and explicit.
- **F3 No flag arguments**: boolean mode flags usually mean two behaviors; split functions or model variants.
- **F4 Delete dead functions**: no speculative helpers, unused utilities, or "just in case" code.

Function should do one thing at one abstraction level. If function name needs `and`, `or`, `handleEverything`, `process`, or `doStuff`, inspect for split.

### General design (G)

- **G1 One language per file**: avoid mixed languages/templates unless framework demands it.
- **G2 Implement expected behavior**: code should do what name/API promises.
- **G3 Handle boundary conditions**: empty, null, zero, one, max, min, timeout, missing config, duplicate input.
- **G4 Do not override safeties**: no bypassing validation, security, type checks, lint gates, or error handling to make tests pass.
- **G5 DRY**: one authoritative representation of each business rule or algorithm.
- **G6 Consistent abstraction levels**: do not mix policy, parsing, IO, and low-level mechanics in one block.
- **G7 Base classes do not know children**: avoid parent depending on subclasses or concrete variants.
- **G8 Minimize public interface**: expose what callers need, keep internals private.
- **G9 Delete dead code**: unused branches, imports, flags, files, and feature stubs rot.
- **G10 Variables near use**: declare close to first use and smallest scope.
- **G11 Be consistent**: follow surrounding naming, layout, patterns, and error style.
- **G12 Remove clutter**: no noise comments, unused abstractions, needless wrappers, debug leftovers.
- **G13 Avoid artificial coupling**: unrelated modules should not change together.
- **G14 Avoid feature envy**: behavior belongs near data it mostly uses.
- **G15 Avoid selector arguments**: prefer explicit functions/strategies over mode selectors.
- **G16 Make intent obvious**: clarity beats cleverness.
- **G17 Put code where expected**: respect project architecture and domain ownership.
- **G18 Prefer domain/instance methods when behavior belongs to object**; avoid procedural envy when model owns logic.
- **G19 Use explanatory variables**: name intermediate concepts when expression hides intent.
- **G20 Function names say what they do**: include side effects and units.
- **G21 Understand algorithm before changing**: do not simplify code you cannot explain.
- **G22 Make dependencies physical**: imports/constructor params/config should show real dependencies.
- **G23 Prefer polymorphism/strategy over growing if/else chains** when variants are stable and likely to expand.
- **G24 Follow conventions**: formatter, linter, language idioms, project style.
- **G25 Named constants over magic numbers/strings** when value has domain meaning.
- **G26 Be precise**: types, units, names, errors, and boundaries should not be fuzzy.
- **G27 Structure over convention**: encode invariants in types/modules, not comments or naming only.
- **G28 Encapsulate conditionals**: name complex predicates.
- **G29 Avoid negative conditionals**: prefer positive predicates when possible.
- **G30 One responsibility**: module/class/function should have one reason to change.
- **G31 Make temporal coupling explicit**: ordering requirements should be visible in API or workflow.
- **G32 Do not be arbitrary**: every abstraction, name, and split needs reason.
- **G33 Encapsulate boundary conditions**: centralize edge logic instead of scattering `+1`, `-1`, slices, or limits.
- **G34 One abstraction level per function**: no mixing orchestration with byte-level/detail work.
- **G35 Config at high levels**: do not bury policy knobs deep in low-level functions.
- **G36 Law of Demeter**: avoid train-wreck chains like `a.b.c.d`; ask owner object for needed value.

### Names (N)

- **N1 Descriptive names**: reveal intent; avoid `data`, `x`, `tmp`, `proc`, `manager` unless scope makes meaning obvious.
- **N2 Right abstraction level**: name concept, not incidental representation.
- **N3 Standard nomenclature**: use domain terms and known pattern names.
- **N4 Unambiguous names**: avoid words with multiple plausible meanings.
- **N5 Length matches scope**: short names okay in tiny local scopes; long-lived names need clarity.
- **N6 No encodings**: avoid Hungarian notation, type prefixes, meaningless suffixes.
- **N7 Names describe side effects**: `getOrCreate`, `loadAndCache`, `saveAndNotify` when side effects exist.

### Tests (T)

- **T1 Test things that can break**: behavior, contracts, errors, boundaries, regressions.
- **T2 Use coverage as signal**: coverage reveals blind spots; do not chase meaningless 100%.
- **T3 Do not skip trivial behavior**: simple tests document contracts.
- **T4 Ignored/skipped test is ambiguity**: fix, delete, or document real external dependency.
- **T5 Test boundary conditions**: empty, one, many, min/max, invalid, duplicate, concurrent, timeout.
- **T6 Test near bugs exhaustively**: bugs cluster around similar paths.
- **T7 Read failure patterns**: repeated failures point to design or invariant issues.
- **T8 Coverage gaps can reveal design problems**: hard-to-test code often does too much.
- **T9 Tests should be fast, independent, repeatable, self-validating, and timely (FIRST)**.

## High-signal review heuristics

- Same business rule duplicated in multiple places (G5).
- Function takes flags or many args and branches into separate behaviors (F1/F3/G15).
- Name hides important side effect or unit (N7/G26).
- Comment explains what code does instead of why (C3).
- Magic value controls policy or boundary (G25/G33).
- Deep nesting hides primary path; guard clauses would clarify (G16/G30).
- Tests cover happy path but miss bug-prone boundary (T5/T6).
- New abstraction has one caller and no clear future pressure (G12/G32).
- Cleanup broadens scope far beyond touched code (violates Boy Scout proportionality).

## Output patterns

Review finding:

```text
Important: `retry(request, true)` hides two behaviors (F3/G15).
Path: src/client.ts:42
Risk: future callers cannot tell whether `true` means silent, forced, or cached.
Fix: split into `retryWithBackoff(request)` and `retryImmediately(request)`, or use named options object if modes share implementation.
```

Cleanup summary:

```text
Cleanups:
- Fixed N1/G25: renamed `t` to `timeoutMs`, extracted `DEFAULT_TIMEOUT_MS`.
- Fixed C3: removed redundant comment that restated `users.filter(...)`.
- Added T5: empty input and max-page boundary tests.
```

## Guardrails

Do not:

- Rewrite working code only to satisfy personal taste.
- Apply max-3-arguments mechanically to framework callbacks or conventional APIs.
- Replace simple conditionals with polymorphism when variants are few and stable.
- Extract tiny helpers that obscure more than clarify.
- Delete comments that document domain rationale, security constraints, or non-obvious workarounds.
- Rename public APIs without migration plan.
- Make cleanup mixed with risky behavior changes unless tests pin behavior.

Favor small, reversible, tested improvements.

## Source basis

This skill adapts the public MIT-licensed `ertugrul-dmr/clean-code-skills` rule taxonomy and cross-checks it against widely known principles from Robert C. Martin's *Clean Code*. See `references/sources.md` for URL, commit, license, access date, and book citation. It summarizes concepts and operational guidance; it does not reproduce book text.
