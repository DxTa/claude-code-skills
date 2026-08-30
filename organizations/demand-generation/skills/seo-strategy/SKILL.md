---
name: seo-strategy
description: Audit and prioritize organic search work across crawlability, indexation, intent, site architecture, internal links, structured data, performance, and authority. Use when pages do not rank, traffic falls, pages are deindexed, URLs or navigation need planning, or SEO fixes need sequencing by business impact.
---

# SEO strategy

Find the earliest break in the search path before producing more content.

## Inputs and context

Gather target queries and pages, intended audience and business value, crawl and index reports, robots and canonical directives, site architecture, internal links, structured data, field performance, mobile behavior, content evidence, and competitor results.

## Workflow

1. Check crawl access, accidental noindex, blocked resources, duplicate URLs, canonicals, and actual index coverage.
2. Test search intent and page usefulness for priority queries before diagnosing authority.
3. Review stable readable URLs, navigation depth, internal-link paths, mobile parity, loading, responsiveness, and layout stability using field data where available.
4. Add structured data only for visible factual content and validate it after template changes.
5. Rank fixes by traffic or conversion at risk, expected effect, evidence, effort, and time to observe.
6. Define implementation owner, validation method, monitoring window, and what is intentionally deferred.

## Output / decision record

Return findings by severity, affected URLs and evidence, root-cause hypothesis, sequenced fixes, expected impact and timing, validation checks, ownership, confidence, and deferred work.

## Uncertainty and failure handling

Separate crawl, indexation, relevance, authority, and measurement problems. Use representative samples when logs are incomplete and label causality as unproven after a change. Do not infer a ranking cause from one query or lab performance score.

## Routing boundaries

Use this skill only for its stated capability and required context. For adjacent work, select a more specific skill from `skill-index.tsv`; do not infer coverage from this department folder or use this skill to authorize actions outside its scope.

## Never

- Mark up claims, ratings, prices, or events that are not visible and real.
- Rewrite content before checking crawlability and indexation.
- Change stable URLs without an explicit migration and redirect plan.
