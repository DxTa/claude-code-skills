# Python Clean Code Reference

Load this when working on Python code with `clean-code`.

## Python-specific rules

- **P1 Explicit imports**: avoid `from module import *`; import named symbols or modules explicitly.
- **P2 Domain constants as Enums/literals**: use `Enum`, `Literal`, or named constants for meaningful variants instead of scattered strings/numbers.
- **P3 Type public interfaces**: add type hints to public functions, methods, and return values; keep internal typing proportional.
- **P4 Reject pytest `monkeypatch`**: do not use the `monkeypatch` fixture. Prefer explicit dependency injection, local fakes, `tmp_path`, or a focused fixture that supplies config/env/dependency values.
- **P5 Minimal pytest fixtures**: keep fixtures small, explicit, and scoped to the nearest useful place. Use local setup for one test, module-local fixtures for one file, and the closest folder `conftest.py` only when multiple test modules share setup.

## Idiomatic adaptations

- Use `dataclass`, `TypedDict`, Pydantic models, or small value objects for cohesive argument groups when F1 triggers.
- Use context managers for resource lifetime instead of manual open/close pairs.
- Prefer exceptions with specific types and helpful messages over broad `Exception` or silent `None`.
- Keep module-level constants uppercase when project style agrees.
- Prefer guard clauses for validation-heavy code.
- Keep comprehensions readable; switch to loops when conditions or transformations get dense.
- Write docstrings for public APIs when signatures/types do not fully explain behavior, parameters, returns, raised exceptions, side effects, or domain constraints; avoid docstrings that restate implementation.
- Avoid clever descriptor/metaclass/dynamic import patterns unless project already uses them and need is real.

## Common Python smells

| Smell | Rule IDs | Better move |
|---|---:|---|
| `from x import *` | P1/G22 | Named imports |
| `def fn(a, b, c, d, e)` | F1/G30 | Dataclass/options object |
| Mutable default args | G3/G26 | Use `None`, construct inside |
| Broad `except Exception: pass` | G4/G16 | Catch specific exception, log/raise |
| `dict` with unknown shape crossing boundary | P3/G26 | TypedDict/dataclass/Pydantic |
| Pytest `monkeypatch` fixture | P4/G22 | Inject dependency/config/env via arguments, fakes, `tmp_path`, or focused fixture |
| Global `conftest.py` fixture graph | P5/G16/G30 | Move fixture to nearest folder/module, or inline setup if single-use |
| `# TODO remove later` old code | C2/C5/G9 | Delete or create tracked issue |
| Boolean flag parameter | F3/G15 | Split functions or explicit strategy |

## Test guidance

- Use pytest names that describe behavior: `test_rejects_empty_email`.
- Add parametrized boundary cases for validators and parsers.
- Reject `monkeypatch`; it hides dependencies and mutates global state. Refactor toward injectable collaborators/config/env, local fakes, `tmp_path`, or focused fixtures.
- Prefer minimal fixtures. Keep fixture definitions closest to use: inline setup for one test, module-local fixture for one file, nearest folder `conftest.py` only for setup shared across multiple test modules.
- Avoid broad `conftest.py` fixture graphs, autouse fixtures, and fixtures that hide assertions or behavior.
- Prefer fakes/in-memory objects over real services for unit tests.
- Use `pytest.raises(..., match=...)` for meaningful error contracts.

## Review examples

```text
Important: `load_config(path, create=True)` hides a write side effect (F3/N7).
Fix: split into `load_config(path)` and `load_or_create_config(path)`.
```

```text
Maintainability: public `parse_user(data: dict)` loses boundary type information (P3/G26).
Fix: introduce `TypedDict`/dataclass or validate through existing schema type.
```
