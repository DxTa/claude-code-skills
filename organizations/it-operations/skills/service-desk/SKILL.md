---
name: service-desk
description: Design or improve IT service-desk intake, triage, priority, escalation, knowledge, and service metrics for incidents and requests.
---

# Service desk

Recommendations improve the service model; actions alter queues, priorities, communications, or user
access. Keep them separate and require an owner, safety check, continuity fallback, and a reversible
pilot for material workflow changes.

## Inputs and context

Collect intake channels, incident and request types, affected users, business impact, urgency,
current queues, escalation timers, knowledge gaps, resolution data, and supported hours.

## Workflow

### Recommendations

1. Define one observable intake path and the minimum context needed for routing and first response.
2. Set priority from impact and urgency, separating incidents from routine requests.
3. Design time-based escalation, handoff ownership, user communication, and continuity for outages.
4. Measure first-contact resolution, percentile resolution time, reopen rate, and recurring causes rather
   than individual ticket volume.
5. Convert repeated demand into source fixes or user-facing knowledge.

### Actions

1. Classify the case, capture symptoms and expected outcome, and assign accountable ownership.
2. Apply the approved priority and escalation clock; notify affected users through the fallback channel
   when the normal channel is unavailable.
3. Test a knowledge article or queue change with a small cohort and monitor misrouting and reopen rate.
4. Close only after the requester or defined evidence confirms resolution; log recurring causes.

## Output / decision record

Return service-model recommendation, case classification, priority rationale, action owner, user and
continuity communications, metrics baseline, test result, and next improvement date.

## Uncertainty and failure handling

When impact or urgency is unclear, preserve the case at the safer priority until clarified. Keep a
visible record for unofficial requests, avoid exposing private user data, and escalate active safety
or widespread availability issues through the incident path.

## Routing boundaries

Use this skill only for its stated capability and required context. For adjacent work, select a more specific skill from `skill-index.tsv`; do not infer coverage from this department folder or use this skill to authorize actions outside its scope.

## Never

- Let loudness replace impact-based priority.
- Merge incidents and requests without distinct clocks.
- Close recurring failures without a problem-elimination owner.
