---
name: business-intelligence
description: Build decision-oriented reports, metric trees, dashboards, and governed self-service analytics. Use when selecting measures, designing a dashboard, creating a reporting framework, exposing trusted datasets, or diagnosing unused or disputed reporting.
---

# Business intelligence

A report earns its place by helping a named audience make a different decision.

## Inputs and context

Gather the decision, audience, action window, source systems, metric definitions, comparison period or target, refresh expectation, access needs, and evidence of existing dashboard use.

## Workflow

1. Write the question and decision before choosing a chart or tool.
2. Choose one outcome metric and map its measurable drivers into a metric tree.
3. Select the smallest set of governed metrics, comparisons, annotations, and appropriate visual forms.
4. Make freshness, source, definition, caveats, and data-quality state visible to viewers.
5. Provide curated semantic models and question templates for self-service; keep raw exploration separate.
6. Test whether representative users can find the answer and act, then retire or revise unused reports with notice.

## Output / decision record

Return decision question, audience, metric tree, dashboard or report specification, definitions and sources, comparison and action thresholds, freshness and quality status, access boundary, adoption measure, and retirement review date.

## Uncertainty and failure handling

Reconcile important figures to the system of record. Mark stale, incomplete, estimated, or conflicting data prominently and do not silently substitute it. If no action would change, reject the report request or convert it into an exploratory analysis.

## Routing boundaries

Use this skill only for its stated capability and required context. For adjacent work, select a more specific skill from `skill-index.tsv`; do not infer coverage from this department folder or use this skill to authorize actions outside its scope.

## Never

- Build a dashboard with no decision owner or intended action.
- Hide data freshness, definition, or quality failures.
- Hand raw tables to self-service users as if they were governed metrics.
