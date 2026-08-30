---
name: data-modeling
description: Design warehouse and semantic-layer structures with explicit grain, raw-to-staging-to-mart separation, dimensional history, executable metrics, and query-aware performance choices. Use when modeling a source, restructuring tables, defining a metric layer, or debugging inflated joins and slow analytics queries.
---

# Data modeling

Make grain and meaning explicit before optimizing table shape.

## Inputs and context

Collect source schemas, business questions, required history, privacy constraints, expected query patterns, metric definitions, consumers, volume, latency, and retention requirements.

## Workflow

1. Define raw, staging, and business-facing layers; retain permitted source detail and isolate business logic from ingestion.
2. State every table's grain as one row per entity or event, including time and version semantics.
3. Choose fact and dimension structures, conformed entities, keys, and history handling for each changing attribute.
4. Put reusable metric logic in the semantic layer and link it to the metric definition and source lineage.
5. Test joins for fan-out, reconciliation, nulls, history correctness, and representative query results.
6. Optimize based on real access patterns with partitions, clustering, pre-aggregation, or deliberate denormalization documented as decisions.

## Output / decision record

Return layer diagram or table map, grain statements, keys and relationships, history policy, metric definitions, privacy controls, validation queries, performance assumptions, and migration or rollback plan.

## Uncertainty and failure handling

Use sample data and reconciliation to expose unknown grain or history behavior before publishing. If a source cannot support required history or freshness, state the limitation and propose a bounded alternative. Treat unexplained row multiplication as a modeling defect until disproven.

## Routing boundaries

Use this skill only for its stated capability and required context. For adjacent work, select a more specific skill from `skill-index.tsv`; do not infer coverage from this department folder or use this skill to authorize actions outside its scope.

## Never

- Build business-facing marts directly on unstable raw data.
- Mix grains in one fact table without an explicit contract.
- Hide business logic in an unversioned dashboard query.
