# Organizational skills

Re-authored capability skills grouped by Headcount department. Existing local skills stay in their original paths; this tree contains only capabilities not covered by the local library at import time.

## Layout

```text
organizations/<department>/skills/<skill>/SKILL.md
```

Each imported skill keeps its Headcount department label for discovery. `import-matrix.tsv` is the audit record: it maps all 143 source skills to either an existing local equivalent or an imported destination.

## Import record

- Source: <https://cbrock84.github.io/headcount/org-chart.html>
- Snapshot: Headcount commit `1f3f550`
- Disposition: 19 covered locally, 124 imported
- Content: re-authored from capability concepts; external plugin wrappers, prose, code, examples, and assets are not runtime dependencies

## Activation

- `index.json` and the parent generated TSV expose every imported skill for explicit discovery.
- `disable-model-invocation: true` marks sensitive or role-oriented skills that require explicit invocation.
- OpenCode activation remains curated; imported skills do not all receive automatic trigger rules.

## Boundaries

Business, legal, finance, people, security, and executive skills provide decision support. They must surface assumptions, uncertainty, authorization, jurisdiction, and qualified-review needs; they do not confer professional authority or replace human approval.

Do not move existing skills or add compatibility symlink copies when changing this tree. Update `import-matrix.tsv` when a local equivalent is discovered or an imported capability changes disposition.
