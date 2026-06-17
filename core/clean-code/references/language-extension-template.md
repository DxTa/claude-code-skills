# Clean Code Language Extension Template

Use this file when adding support for another language. Keep language-specific guidance in one `references/<language>.md` file and link it from `SKILL.md`.

## File naming

- Use lowercase language name: `go.md`, `rust.md`, `java.md`, `kotlin.md`, `csharp.md`.
- Keep file one level under `references/`; avoid nested reference trees.

## Required sections

```markdown
# <Language> Clean Code Reference

Load this when working on <language> code with `clean-code`.

## <Language>-specific rules

- **<ID1> <Rule name>**: <language adaptation>.
- **<ID2> <Rule name>**: <language adaptation>.

## Idiomatic adaptations

- <How core C/F/G/N/T rules translate into language idioms.>

## Common <Language> smells

| Smell | Rule IDs | Better move |
|---|---:|---|
| <smell> | <core/lang IDs> | <fix> |

## Test guidance

- <Framework-agnostic or dominant-framework guidance.>

## Review examples

```text
Important: <specific finding> (<rule IDs>).
Fix: <concrete fix>.
```
```

## Extension rules

- Keep core Clean Code taxonomy in `SKILL.md`; put only language adaptations here.
- Prefer language idioms over mechanical Java-derived advice.
- Add 2-5 language-specific rules only when core rules do not cover the issue.
- Use stable rule prefixes: `GO1`, `RS1`, `JAVA1`, `KT1`, `CS1`, etc.
- Avoid duplicating full core catalog in each language file.
- Add high-signal smells and examples over exhaustive style-guide content.
- Respect project conventions, linters, and formatters above generic language advice.
