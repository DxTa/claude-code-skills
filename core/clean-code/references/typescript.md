# TypeScript Clean Code Reference

Load this when working on TypeScript or TSX code with `clean-code`.

## TypeScript-specific rules

- **TS1 Explicit stable imports**: prefer named imports and explicit dependency boundaries; avoid catch-all namespace imports unless API shape calls for it.
- **TS2 Domain variants as literal unions/enums**: replace magic strings/numbers with named constants, `as const` maps, literal unions, or enums per project style.
- **TS3 Type public boundaries**: avoid `any` in exported APIs, component props, service boundaries, and persistence/network edges; use `unknown` plus narrowing when input is untrusted.

## Idiomatic adaptations

- Use parameter object types/interfaces when F1 triggers, especially for React props, API calls, and config-heavy functions.
- Use discriminated unions for variants instead of boolean flags or selector strings.
- Prefer small pure functions for transformations; keep IO and orchestration at edges.
- Prefer `readonly` for inputs that should not mutate.
- Avoid over-abstracting React components; split when responsibilities differ, not because line count feels high.
- Use JSDoc/TSDoc for exported APIs when types alone do not explain intent, lifecycle, side effects, constraints, or non-obvious domain rules; avoid comments that restate type signatures.
- Keep async errors explicit: return typed results or throw project-standard errors, not swallowed promises.
- Follow project formatter/linter over generic style preferences.

## Common TypeScript smells

| Smell | Rule IDs | Better move |
|---|---:|---|
| `any` at exported boundary | TS3/G26 | Specific type or `unknown` + guard |
| `fn(a, b, c, d, e)` | F1/G30 | Options object/interface |
| `doThing(input, true)` | F3/G15 | Split function or discriminated union |
| Long `if (kind === ...)` chain | G23/TS2 | Strategy map or discriminated union switch |
| Magic route/status strings | G25/TS2 | `const` map or literal union |
| Nested optional access train wreck | G36/G28 | Encapsulate selector/predicate |
| Commented-out JSX/code | C5/G9 | Delete; Git preserves history |

## Test guidance

- Test behavior through public APIs/components, not implementation details.
- Add boundary tests for parsers, reducers, schema validation, permission logic, and async failure paths.
- Prefer descriptive test names and user-observable assertions.
- Use test data builders when fixture objects become noisy.
- Keep unit tests fast; isolate network, timers, and storage.

## Review examples

```text
Important: `submitOrder(order, true)` hides mode semantics (F3/G15).
Fix: split into `submitOrder` and `submitOrderDryRun`, or pass `{ mode: "dry-run" }` if shared path must remain.
```

```text
Maintainability: exported `parsePayload(payload: any)` weakens boundary safety (TS3/G26).
Fix: accept `unknown`, validate with existing schema, return typed result.
```
