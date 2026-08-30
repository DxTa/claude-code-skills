---
name: self-service-and-knowledge
description: Improve customer help content, in-product guidance, and knowledge-base findability so people can complete a task without contacting support. Use to plan or audit a help center, interpret failed searches, reduce avoidable contacts, or choose between documentation and a product fix.
---

# Self-service and knowledge

Optimize for successful customer task completion, not article volume or page views.

## Inputs and context

Collect contact categories, help-search queries, failed searches, article analytics, product labels, customer vocabulary, known defects, and content owners. Include the support path for customers who cannot self-serve.

## Workflow

1. Rank problems by contact volume, customer effort, and business impact.
2. Decide whether each problem needs a product correction, in-product guidance, a help article, or human support.
3. Write one task-focused answer using the labels customers see, with the action first and recovery steps included.
4. Connect relevant in-product entry points and search terms; keep one primary task per article.
5. Test the path with representative users and inspect contact-after-view behavior.
6. Assign an owner, review date, interface-change trigger, and retirement process.

## Output / decision record

Return prioritized content or product findings, target audience and task, draft outline or fix, entry points, evidence, expected contact impact, owner, review date, and escalation path.

## Uncertainty and failure handling

Treat high views with continued contact as a failure signal, not success. If search or contact data is incomplete, label the sample bias and validate with a small usability test. When interface labels differ by version or locale, document the variance or route to product owners.

## Routing boundaries

Use this skill only for its stated capability and required context. For adjacent work, select a more specific skill from `skill-index.tsv`; do not infer coverage from this department folder or use this skill to authorize actions outside its scope.

## Never

- Use an article to conceal a repeatable product defect.
- Publish steps for an interface that has not been checked.
- Make human support difficult when self-service fails.
