---
name: spec-analyzer
description: "Analyze and enhance specs from Jira or manual input using memory-informed Socratic questioning before implementation planning"
version: "1.0.0"
license: MIT
compatibility: opencode
---

# Spec Analyzer (Memory-Informed)

## Overview

Transform vague requirements or Jira tickets into well-defined, implementation-ready specifications through memory-informed Socratic questioning.

This skill helps identify gaps, ambiguities, and edge cases BEFORE you start planning implementation. It leverages past decisions from sia-code memory to avoid re-asking resolved questions and apply project-specific patterns.

**When to use:**
- Jira ticket needs clarification ("JIRA-123")
- Vague feature request ("build a login system")
- Requirements seem incomplete or ambiguous
- User asks to grill, stress-test, or challenge a spec/plan/design before implementation
- User wants validation against `CONTEXT.md`, `CONTEXT-MAP.md`, ADRs, or project domain language
- Before T3+ tasks requiring detailed planning

## Mode Selection

Use the lightest mode that resolves the user's need:

1. **Standard Spec Analysis** - for vague requirements, Jira tickets, and feature requests that need an enhanced spec.
2. **Docs-Aware Grilling** - for stress-testing a plan/spec/design against the codebase, domain language, and recorded decisions before planning.

If requirements are already finalized and the user wants a one-shot risk review, use `self-reflect` instead. If requirements are unresolved, stay in `spec-analyzer` and grill before planning.

## Prerequisites

### Recommended: sia-code Memory Search

**Before running spec-analyzer**, search memory for context.
**Full reference:** Load skill `sia-code` | **Health check:** Load skill `sia-code/health-check`

```bash
uvx sia-code memory search "[feature keywords]"
```

Example:
```bash
# For authentication feature
uvx sia-code memory search "authentication login OAuth"

# For payment integration
uvx sia-code memory search "payment checkout Stripe"
```

**Why this matters:**
- **Past decisions:** "We use OAuth 2.1, not custom JWT"
- **Patterns:** "All forms use react-hook-form + zod"
- **Preferences:** "Mobile-first design required for all features"
- **Fixes:** "Rate limiting on all auth endpoints after JIRA-456 incident"

### Optional: mcp-atlassian (for Jira specs)

If you have mcp-atlassian configured, you can analyze Jira tickets directly. Just provide the ticket ID (e.g., "PROJ-123").

## The Process

### Phase 1: Context Gathering

**1a. Check memory context (if search was done):**
- Review sia-code memory findings
- Note relevant past decisions
- Identify applicable patterns/preferences

**1b. Get the spec:**
- **If Jira ticket ID provided:** Use `jira_get_issue` to pull ticket details
- **If manual input:** Accept user's description

**1c. Review project context:**
- Check relevant files, docs, existing patterns
- Understand current architecture where feature will live

**1d. Docs-aware context (required for grilling mode):**
- Look for `CONTEXT.md` at the repo root.
- Look for `CONTEXT-MAP.md`; if present, use it to find context-specific `CONTEXT.md` and `docs/adr/` locations.
- Look for `docs/adr/` and nearby ADR directories in the affected area.
- Search code when a question can be answered from repository state instead of asking the user.

### Phase 1b: Docs-Aware Grilling Mode

Use this mode when the user asks to "grill", "stress test", "challenge", or validate a spec/plan/design against domain docs.

**Core rule:** Interview one decision at a time until the decision tree is resolved enough for planning. Do not batch questions.

For each question:
- Ask exactly one question.
- Explain why it matters.
- Provide your recommended answer.
- State the consequence of choosing the main alternative when useful.

**Do not ask what the repo can answer.** If code, docs, memory, or ADRs can answer the question, inspect those first and present the finding.

**Challenge terminology:**
- If the user uses a vague term, propose a precise canonical term.
- If the term conflicts with `CONTEXT.md`, flag the conflict immediately.
- If code contradicts the user's stated model, surface the contradiction and ask which source should win.

**Walk dependencies in order:**
- Resolve upstream domain/user behavior decisions before downstream implementation details.
- Do not ask rollout or task-boundary questions until core behavior and constraints are clear.

**ADR candidates:**
Only mark a decision as an ADR candidate when all are true:
- hard to reverse
- surprising without context
- real trade-off with credible alternatives

Do not create or edit `CONTEXT.md` or ADR files automatically in this mode. List recommended updates for explicit follow-up.

### Phase 2: Socratic Questioning

**Ask one question at a time** to refine understanding:

**Focus areas:**
1. **Purpose & Success Criteria**
   - What problem does this solve?
   - How do we know it's working?
   - What's the expected user flow?

2. **Constraints & Requirements**
   - Performance requirements?
   - Security considerations?
   - Browser/device support?
   - Accessibility requirements?

3. **Edge Cases & Error Handling**
   - What happens when things go wrong?
   - Boundary conditions?
   - Rate limiting needed?
   - Timeout handling?

4. **Integration Points**
   - What existing code does this touch?
   - Dependencies on other features?
   - API contracts?
   - Database changes?

5. **Testing Strategy**
   - How will this be tested?
   - What are the test cases?
   - Manual testing steps?

**Questioning style:**
- **Prefer multiple choice** when applicable
- **One question per message** - don't overwhelm
- **Skip resolved questions** if memory shows past decisions
- **Apply project patterns** from memory (e.g., "Use react-hook-form as standard?")

**Example memory-informed question:**
```
Bad:  "What authentication method should we use?"
Good: "Per memory, we use OAuth 2.1 for all auth. Should this follow the same pattern as login (JIRA-789), or does it need custom handling?"
```

### Phase 3: Explore Approaches

**Once you understand the requirements**, propose 2-3 approaches:

```markdown
## Approach Options

### Option 1: [Name] (Recommended)
- **Description:** [Brief explanation]
- **Pros:** [Why this is best]
- **Cons:** [Trade-offs]
- **Effort:** [Relative complexity]

### Option 2: [Alternative]
- **Description:** [Brief explanation]
- **Pros:** [Advantages]
- **Cons:** [Why not recommended]
- **Effort:** [Relative complexity]

### Recommendation
I recommend Option 1 because [reasoning based on requirements and constraints].
```

### Phase 4: Present Enhanced Spec

**Present the enhanced spec in sections** (200-300 words each):
- Validate each section before moving to next
- Ask: "Does this section look right so far?"

**Sections to cover:**
1. **Feature Summary**
   - Purpose and success criteria
   - User personas/use cases
   
2. **Functional Requirements**
   - Core functionality
   - User flows
   - Business logic
   
3. **Technical Requirements**
   - Architecture approach
   - Integration points
   - Data model changes
   
4. **Edge Cases & Error Handling**
   - Boundary conditions
   - Error scenarios
   - Fallback behavior
   
5. **Testing Strategy**
   - Test cases
   - Acceptance criteria
   - Manual testing steps

6. **Docs-Aware Grilling Addendum** (only when grilling mode was used)
   - Domain terms
   - Resolved decisions
   - ADR candidates
   - Remaining open questions
   - Ready for planning: yes/no

## Output Format

### Store Enhanced Spec in notes.md

```markdown
## Enhanced Spec: [Feature Name]

**Source:** [JIRA-123 OR Manual input]
**Date:** YYYY-MM-DD
**Memory Context Applied:** [Yes/No - list key findings]

### Summary
[1-2 sentences]

### Purpose & Success Criteria
[What problem this solves and how we measure success]

### Functional Requirements
[Core functionality, user flows]

### Technical Requirements
[Architecture, integrations, data changes]

### Edge Cases & Error Handling
[Boundary conditions, error scenarios]

### Testing Strategy
[Test cases, acceptance criteria]

### Domain Terms
[Existing terms used, fuzzy/conflicting terms resolved, terms to record later]

### Resolved Decisions
[Decision, rationale, alternatives considered]

### ADR Candidates
[Only hard-to-reverse, surprising, trade-off decisions]

### Open Questions
[Any unresolved items]

### Ready For Planning
[Yes/No with reason]

---

**Next Steps:**
1. Review this spec
2. If approved: Create task_plan.md with phases
3. Proceed with implementation (T1-T4 tiers)
```

## Integration with AGENTS.md Workflow

### When to Use

| Scenario | Use spec-analyzer? |
|----------|-------------------|
| Vague requirement ("add login") | ✅ YES |
| Jira ticket with unclear acceptance criteria | ✅ YES |
| T3+ task before planning | ✅ RECOMMENDED |
| Well-defined task with clear spec | ❌ Skip, go to task_plan.md |
| Follow-up on existing work | ❌ Skip |

### Workflow Integration

```
User request → @skill-suggests detects spec-analyzer
     ↓
sia-code memory search (get past context)
     ↓
spec-analyzer (memory-informed analysis)
     ↓
Enhanced spec → notes.md
     ↓
Continue with MASTER CHECKLIST → task_plan.md
```

## Key Principles

1. **Memory-first:** Check sia-code memory before asking questions
2. **One question at a time:** Don't overwhelm with multiple questions
3. **Multiple choice preferred:** Easier to answer when possible
4. **Skip resolved questions:** If memory shows "we always use X", don't ask
5. **Apply project patterns:** Reference past decisions (e.g., "per JIRA-789 pattern")
6. **Repo answers first:** If code/docs can answer a question, inspect them instead of asking
7. **Domain language discipline:** Use `CONTEXT.md` terms and flag conflicts
8. **ADR discipline:** Suggest ADRs only for hard-to-reverse, surprising trade-offs
9. **YAGNI ruthlessly:** Remove unnecessary features from all designs
10. **Explore alternatives:** Always propose 2-3 approaches before settling
11. **Incremental validation:** Present spec in sections, validate each
12. **Be flexible:** Go back and clarify when something doesn't make sense

## Examples

### Example 1: Memory-Informed Jira Analysis

**User:** "Analyze JIRA-456"

**Agent Actions:**
1. Check if sia-code memory was searched (prompt if not)
2. Pull ticket via mcp-atlassian
3. Review memory findings (example: "OAuth 2.1 standard, react-hook-form pattern")
4. Start questioning:
   - ✅ "The ticket mentions login. Per memory, we use OAuth 2.1 (JIRA-123). Should this follow the same flow?"
   - ❌ "What authentication method?" (memory already answered this)

### Example 2: Manual Input with Memory

**User:** "Build a payment checkout flow"

**sia-code memory findings:**
- "Payment: Use Stripe, webhook validation required (JIRA-789)"
- "Forms: react-hook-form + zod validation (all features)"

**Agent Questions:**
1. ✅ "Per memory, we use Stripe with webhook validation. Should this follow the JIRA-789 pattern, or need custom handling?"
2. ✅ "For the checkout form, should we use react-hook-form + zod as standard, or different validation?"
3. ❌ "What payment provider?" (memory answered)

### Example 3: No Memory Context

**User:** "Create a new reporting dashboard"

**No memory findings for "reporting dashboard"**

**Agent Questions (start from scratch):**
1. "What type of reports will this show? (a) Financial metrics, (b) User analytics, (c) System performance, (d) Custom"
2. "Who are the primary users? (a) Executives, (b) Analysts, (c) Developers, (d) All"
3. ... (continue standard questioning)

### Example 4: Docs-Aware Grilling

**User:** "Grill this plan against our domain docs before I split it into tasks."

**Agent Actions:**
1. Read the plan and relevant code/docs.
2. Check `CONTEXT.md`, `CONTEXT-MAP.md`, and `docs/adr/` when present.
3. Ask one decision question at a time:
   - ✅ "Your plan says 'account', but `CONTEXT.md` distinguishes Customer from User. I recommend using User here because this touches authentication state. Do you mean User?"
   - ❌ "What are the domain terms, rollout plan, testing strategy, and data model?"
4. Record resolved terms, decisions, ADR candidates, and whether the spec is ready for planning.

## After Spec Analysis

1. **Store enhanced spec** in notes.md
2. **Ask:** "Does this spec capture everything? Any changes needed?"
3. **When approved:**
   - "Ready to create task_plan.md with implementation phases?"
   - Continue with your normal AGENTS.md workflow (get-session-info, task_plan.md, TodoWrite)

## Common Pitfalls to Avoid

❌ **Asking resolved questions:**
```
Bad:  "What form validation library should we use?"
Good: "Per memory, we use react-hook-form + zod. Apply this pattern?"
```

❌ **Overwhelming with multiple questions:**
```
Bad:  "What authentication method, what database, what UI library, and what testing framework?"
Good: "Let's start with authentication. Per memory, we use OAuth 2.1. Confirm this applies here?"
```

❌ **Skipping memory search:**
```
Bad:  [Jump straight to questions without checking memory]
Good: [Prompt user to run memory search if not done, or check for past findings]
```

❌ **Creating spec without exploration:**
```
Bad:  [Immediately write spec based on vague input]
Good: [Ask clarifying questions first, explore approaches, then present spec]
```

## Notes

- **Not a planning tool:** This skill refines REQUIREMENTS, not implementation plans
- **Use before task_plan.md:** Enhanced spec feeds into your normal planning workflow
- **Works standalone or with Jira:** Flexible input sources
- **Memory-aware:** Leverages past decisions for consistency
- **Integrates seamlessly:** Fits into your existing AGENTS.md MASTER CHECKLIST
