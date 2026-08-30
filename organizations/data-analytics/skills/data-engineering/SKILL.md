---
name: data-engineering
description: Design, operate, and debug reliable data pipelines covering ingestion, transformation, orchestration, late data, idempotent recovery, and data-quality checks. Use when building a batch or streaming pipeline, investigating changed numbers, or preventing stale or duplicated data from reaching reports.
---

# Data engineering

Treat data movement as production infrastructure whose failures can look plausible.

## Inputs and context

Collect source contracts, event or processing time, expected volume and lateness, schema, destination grain, transformation rules, replay needs, service-level target, privacy constraints, and downstream consumers.

## Workflow

1. Preserve an immutable permitted raw landing layer and document any privacy minimization performed at ingestion.
2. Keep business transformations downstream, visible, versioned, and testable.
3. Define deterministic keys, merge or overwrite behavior, partitioning, and replay semantics so reruns have one effect.
4. Decide acceptance windows and duplicate handling for late or out-of-order records using event time where available.
5. Add checks for volume, freshness, uniqueness, referential integrity, nulls, and meaningful distribution changes.
6. Fail loudly or quarantine suspect data, alert owners, and verify recovery before republishing downstream.

## Output / decision record

Return pipeline design, source and destination contracts, data lineage, grain and replay policy, lateness and duplicate rules, quality checks and thresholds, failure behavior, owner, and operational SLO.

## Uncertainty and failure handling

Separate source defects from transformation defects and report which records or partitions are affected. If raw retention or replay is impossible, state the recovery limit and use a controlled backfill rather than guessing. Do not label data current until freshness checks pass.

## Routing boundaries

Use this skill only for its stated capability and required context. For adjacent work, select a more specific skill from `skill-index.tsv`; do not infer coverage from this department folder or use this skill to authorize actions outside its scope.

## Never

- Discard the permitted raw record to hide a business transformation mistake.
- Make reruns double-count.
- Publish stale or unvalidated data as current.
