---
name: lifecycle-messaging
description: Design behavior-triggered email and SMS programs for onboarding, activation, nurture, retention, re-engagement, and transactional events. Use when creating or repairing sequences, choosing timing and segmentation, diagnosing opens, clicks, conversion, opt-outs, or deliverability.
---

# Lifecycle messaging

Send only a message that helps the recipient take the next useful step at their current stage.

## Inputs and context

Gather lifecycle states, qualifying events, user intent, consent and channel permissions, message promise, destination, suppression rules, sender reputation, baseline funnel metrics, and regional sending constraints.

## Workflow

1. Map each stage to the user's current task, desired next behavior, and exit condition.
2. Trigger from meaningful behavior where possible; define fallback timing, frequency cap, quiet hours, and suppression after completion or opt-out.
3. Write one clear action per message, deliver the promised value first, and set expectations for future messages.
4. Treat SMS as higher-intrusion, consented communication reserved for appropriate transactional or time-sensitive cases.
5. Test subject and preview as a pair, message content, destination, and segment without changing several causes at once.
6. Diagnose in order: delivery, open, click, destination conversion, downstream quality, unsubscribes, and complaint signals.

## Output / decision record

Return lifecycle map, trigger and exit rules, segment, channel and consent status, sequence copy outline, cadence, suppression policy, success and guardrail metrics, experiment plan, and retirement rule.

## Uncertainty and failure handling

Stop sending when consent, suppression, or deliverability is unclear. Do not call low opens a copy problem until delivery and list quality are checked. Remove persistently unengaged recipients through a documented policy and consult qualified counsel for jurisdiction-specific messaging rules.

## Routing boundaries

Use this skill only for its stated capability and required context. For adjacent work, select a more specific skill from `skill-index.tsv`; do not infer coverage from this department folder or use this skill to authorize actions outside its scope.

## Never

- Send marketing messages without appropriate permission or a visible opt-out.
- Continue messaging after a valid opt-out or completed journey.
- Treat higher volume as engagement when complaints and unsubscribes rise.
