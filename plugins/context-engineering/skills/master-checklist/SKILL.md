> **Claude Code Adapted**: This version has been adapted for Claude Code compatibility. The original OpenCode version is at the root of this repository under `core/master-checklist/SKILL.md`.

---
name: master-checklist
description: Detailed guidance for each MASTER CHECKLIST step with tier-specific requirements
version: "1.0.0"
---

# MASTER CHECKLIST Detailed Guidance

Comprehensive step-by-step guidance for all 18+ checklist steps with tier-specific requirements and best practices.

## Overview

The MASTER CHECKLIST is the core workflow for all tasks. This skill provides:
- Detailed guidance for each step
- Tier-specific variations (T1, T2, T3, T4)
- Self-reflection checkpoints (AUTO-TRIGGER)
- Common pitfalls and how to avoid them

---

## PRE-TASK Steps

### Step 1: Skill Suggestions

**Purpose:** Get AI-suggested skills relevant to the task

**Execution:**
Use the `Skill` tool or read skill SKILL.md files directly to discover relevant skills for the task at hand.

> **Note:** `@skill-suggests` is an optional workflow tool available in the full context engineering platform. In Claude Code, browse available skills manually or use the Skill tool.

**Tier Requirements:**
- T1: Optional (skip for simple tasks)
- T2+: Execute
- T3+: MANDATORY

**Skip Conditions:**
- Direct commands ("run tests", "format file X")
- Follow-up clarifications
- <30 lines, 1 file, clear solution (T1 lightweight path)

---

### Step 2: Memory / Past Decisions Search

**Purpose:** Search past decisions and patterns before starting

**Execution:**
Use `Grep` and `Glob` tools to search for relevant patterns in the codebase. Check any project-level decision logs, ADRs (Architecture Decision Records), or memory files for past decisions on the topic.

```
# Search for past decisions in the codebase
Use Grep to search decision logs, README files, or comments for relevant keywords
Use Glob to find ADR files or decision documentation
```

**Tier Requirements:**
- T1: Optional (store if useful pattern)
- T2+: MANDATORY (skip only if <30s, document why)
- T3+: MANDATORY - execute BEFORE exploration

**Recovery if no memory system is available:**
Document "No prior context found" in task_plan.md and proceed. If past decision files exist in the repo (e.g., ADRs, DECISIONS.md), check those first.

**What to look for:**
- Past decisions on similar features
- Known patterns or gotchas
- Related architecture decisions
- Configuration requirements

---

### Step 3: Generate Session Identifier

**Purpose:** Get a unique identifier for plan file naming

**Execution:**
Use a generated UUID for filenames when a session identifier is needed.

**Tier Requirements:**
- T1: Execute
- T2+: Execute
- ALL tiers: MANDATORY

**Output:**
- A unique session identifier (UUID) for naming plan and notes files

---

### Step 4: Create task_plan.md

**Purpose:** Persistent planning file for crash recovery and session continuity

**File Path:**
```
./task_plan.md (or a project-specific plans directory)
```

**Tier Requirements:**
- ALL tiers: MANDATORY (crash recovery)

**Template Structure:**
```markdown
# Task Plan: [Task Name]

**Session:** {sessionID}
**Date:** YYYY-MM-DD
**Tier:** [T1/T2/T3/T4]

## Goal
[Clear, measurable objective]

## Status
- [x] Phase 1: Planning
- [ ] Phase 2: Implementation
- [ ] Phase 3: Testing
- [ ] Phase 4: Review

## Decisions
1. [Key decision with rationale]

## Errors Encountered
[Log errors here]

## Next Steps
[Current position in task]
```

---

### Step 5: Create notes.md

**Purpose:** Offload research findings without polluting working memory

**File Path:**
```
./notes.md (or alongside task_plan.md)
```

**Tier Requirements:**
- T1: Optional (for research/analysis)
- T2: Recommended (for research/analysis)
- T3+: MANDATORY

**Use Cases:**
- API documentation summaries
- Architecture research findings
- Library usage patterns
- External resource notes

---

### Step 6: Task Tracking: Initialize Phase 1

**Purpose:** Create visible task list for live progress tracking

**Execution:**
Use `TaskCreate` to create initial phase steps. Use `TaskUpdate` to mark progress and `TaskList`/`TaskGet` to review status.

**Tier Requirements:**
- ALL tiers: MANDATORY

**Best Practices:**
- Break into specific, actionable items
- One task in_progress at a time
- Mark complete IMMEDIATELY after finishing (don't batch)
- Keep synced with task_plan.md Status section

---

### Step 7: Exploration

**Purpose:** Understand codebase architecture before code changes

**Tier Requirements:**
- T1: Skip for simple tasks
- T2+: If triggers hit (unfamiliar code, cross-file, "how does X work", post Two-Strike)
- T3+: MANDATORY before code changes

#### Step 7a: Codebase Research

**Trigger Check:**
- Unfamiliar codebase area (haven't worked in past 30 days)?
- Cross-file changes (Integration Changes pattern)?
- Task involves "how does X work" or "trace dependencies"?
- After Two-Strike Rule triggered?

**If YES:**

1. **Search the codebase for relevant patterns:**
   Use `Grep` to search for keywords, patterns, and function names across the codebase.
   Use `Glob` to find files matching relevant naming patterns.
   Use `Read` to examine key files in detail.

2. **Map the architecture:**
   Read relevant source files, configuration, and tests to understand the structure and dependencies.

3. **Document in task_plan.md:**
   - **T2:** Optional: "Research findings: [summary]" OR "Research skipped: [reason]"
   - **T3+:** MANDATORY: Must document findings or skip reason

**If NO:**
Document in task_plan.md ("Familiar codebase: [reason]") for T3+ tasks

#### Step 7b: Tool / Agent Selection

**Use decision tree, not all tools at once**

Read skill: `agent-selection/SKILL.md` for full decision tree.

**Core Tools:**
- `Grep` / `Glob` for file pattern matching, code search, keyword lookup
- `Read` for examining specific files in detail
- `Task` tool with appropriate agent prompt for multi-step analysis or specialist work

**Additional specialist prompts based on domain:**
- Use Task tool with a frontend specialist prompt (React/Vue/CSS/UI)
- Use Task tool with a backend specialist prompt (API/DB/Auth)
- Use Task tool with a security-focused prompt (security implications)
- Use Task tool with a DevOps prompt (infrastructure, CI/CD)

**MUST complete exploration before any code changes**
**Re-run exploration if task scope changes**

---

## DURING Steps

### Step 8: Task Tracking: Update as steps complete

**Purpose:** Keep task list current

**Tier Requirements:**
- ALL tiers: Execute

**Best Practices:**
- Use `TaskUpdate` to mark tasks complete IMMEDIATELY after finishing each step
- Don't batch completions
- Only ONE task in_progress at a time

---

### Step 9: Sync task_plan.md Status

**Purpose:** Keep persistent plan synced with task tracking

**Tier Requirements:**
- ALL tiers: Execute after each task status change

**Sync Protocol:**
| Event | Action |
|-------|--------|
| Task status update | Update task_plan.md Status section |
| Error occurs | Log to task_plan.md "Errors Encountered" |
| Phase complete | Mark task_plan.md [x] -> Reset task tracking |

---

### Step 9a: TDD Cycle (T2+ MANDATORY)

**Purpose:** Ensure test-first development

**Tier Requirements:**
- T1: Optional (but encouraged)
- T2+: **MANDATORY** - Code before test? DELETE IT. Start over.

**Iron Law:**
```
NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST
```

**RED-GREEN-REFACTOR Cycle:**
- [ ] **RED:** Write ONE failing test
- [ ] **Verify RED:** Watch it fail (correct reason - "feature missing" not typo)
- [ ] **GREEN:** Write MINIMAL code to pass
- [ ] **Verify GREEN:** All tests pass (no regressions)
- [ ] **REFACTOR:** Clean up (stay green)
- [ ] **COMMIT:** Atomic commit per behavior

**Read skill:** `test-driven-development/SKILL.md` for full guidance

---

### Step 10: Re-read task_plan.md before major decisions

**Purpose:** Prevent context amnesia and goal drift

**Tier Requirements:**
- T1: Before major decisions
- T2: Before major decisions
- T3+: Before EVERY major decision

**What qualifies as "major decision":**
- Choosing implementation approach
- Refactoring existing code
- Adding new dependencies
- Changing architecture

**Action:** Confirm trimmed context is irrelevant to next 2 steps

---

### Step 11: Self-reflection

**Purpose:** Validate approach, identify risks, find simpler alternatives

**Tier Requirements:**
- T1: Quick mental check (skip agent)
- T2: Use self-reflection (recommended)
- T3+: Use self-reflection (MANDATORY)
- T4: Use self-reflection (NON-SKIPPABLE)

**Self-Reflection Checkpoints (AUTO-TRIGGER):**
- [ ] After creating task_plan.md (T2+: recommended, T3+: run self-reflection)
- [ ] Before first code change (T3+: MANDATORY self-reflection on approach)
- [ ] After Two-Strike Rule triggered (run self-reflection for root cause)
- [ ] Before claiming "task complete" (T2+: self-reflection verification gate)

**Invocation:**
Use the `mcp__code-reasoning__code-reasoning` or `mcp__shannon-thinking__shannonthinking` MCP reasoning tools, or use `Task` tool with a self-reflection prompt to review the plan for edge cases, production risks, and missing considerations.

**What self-reflection validates:**
- Edge cases and error scenarios
- Production risks and scalability concerns
- Missing considerations and requirements gaps
- Simpler alternative approaches
- Unstated assumptions that need verification

**Validation approach:** Antagonistic QA mindset from a Senior Technical Lead perspective - **assume broken until proven.**

---

### Step 12: Log errors to task_plan.md

**Purpose:** Track investigation progress for crash recovery

**Tier Requirements:**
- ALL tiers: Execute

**Format:**
```markdown
## Errors Encountered

### Error 1: TypeError at line 42
- **When:** 2026-01-27 14:30
- **What:** Cannot read property 'foo' of undefined
- **Fix Attempted:** Added null check
- **Result:** Still failing
```

---

## POST-TASK Steps

### Step 13: External LLM validation

**Purpose:** Get second opinion on approach and implementation

**Tier Requirements:**
- T1/T2: Skip
- T3+: MANDATORY
- T4: NON-SKIPPABLE

**How:** Use external LLM (ChatGPT, Claude web) to review:
- Architecture decisions
- Security implications
- Edge cases
- Performance concerns

---

### Step 14: Task Tracking: Mark all completed

**Purpose:** Clean up task list

**Tier Requirements:**
- ALL tiers: Use `TaskUpdate` to mark all tasks as completed

---

### Step 15: task_plan.md: Mark all phases [x]

**Purpose:** Update persistent plan to show completion

**Tier Requirements:**
- ALL tiers: Execute

---

### Step 16: Store Learnings

**Purpose:** Preserve knowledge for future tasks

**Tier Requirements:**
- T1: Optional (store if useful pattern)
- T2+: MANDATORY

**What new insight did we capture?**

**Search for related past decisions first:**
Use `Grep` to search decision logs, ADRs, or notes files for the topic. If the project maintains memory files or decision records, check those.

**If exists:** Update with "Updated [date]: [new insight]"
**If new:** Use appropriate category prefix

**Categories:**
- `Procedure:` Step-by-step how-to instructions
- `Fact:` Verified assertion about the codebase
- `Pattern:` Reusable approach with conditions for use
- `Fix:` Root cause -> solution mapping
- `Preference:` User or project-specific choice

**Store as decision in project decision log or notes:**
```markdown
## [Category]: [Decision]
- **Context:** [trigger]
- **Reasoning:** [why]
- **Outcome:** [result]
```

**Examples:**
```markdown
## Procedure: How to debug X
- **Context:** Recurring issue in module Y
- **Reasoning:** Stack trace pointed to Z
- **Outcome:** Documented for future sessions

## Fact: Module Y requires Z
- **Context:** Discovered during feature implementation
- **Reasoning:** Missing config caused silent failure
- **Outcome:** Added to setup checklist
```
- Do NOT store bare outcomes: `"Fix: Added retry logic"`
- ALWAYS include Context + Reasoning to preserve decision history

---

### Step 17: Code Simplification

**Purpose:** Clean up code for clarity and maintainability

**Tier Requirements:**
- T1: Optional
- T2+: Recommended (before final testing)

**Invocation:**
Use `Task` tool with a code simplification prompt to review and simplify modified files.

---

### Step 17a: Two-Stage Review (T2+)

**Purpose:** Systematic code review: spec compliance FIRST, then code quality

**Tier Requirements:**
- T1: Skip
- T2+: Execute

**STAGE 1: Spec Compliance**
Use `Task` tool with a spec-reviewer prompt to verify implementation matches requirements.

**Loop until pass:**
- [ ] Run spec review
- [ ] Fix issues
- [ ] Re-run spec review
- [ ] Repeat until spec compliant

**STAGE 2: Code Quality** (only after Stage 1 passes)
Use `Task` tool with a code-review prompt to check quality.

**Loop until pass:**
- [ ] Run code review
- [ ] Fix issues (Critical = BLOCKING)
- [ ] Re-run code review
- [ ] Repeat until quality approved

---

### Step 18: Validation: run tests, verify changes

**Purpose:** Evidence-based completion verification

**Tier Requirements:**
- ALL tiers: Execute

**Read skill:** `verification-before-completion/SKILL.md`

**Iron Law:**
```
NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE
```

**Before ANY claim of success:**
1. IDENTIFY: What command proves this claim?
2. RUN: Execute the command (fresh, complete)
3. READ: Full output, check exit code
4. VERIFY: Does output confirm claim?
5. ONLY THEN: Make the claim

**Red Flags:** "should work", "probably", "seems to"

---

### Step 18a: Branch Completion

**Purpose:** Systematically finish development branch with quality gates

**Tier Requirements:**
- ALL tiers: Execute when branch work complete

**Read skill:** `finishing-a-development-branch/SKILL.md`

**Workflow:**
- [ ] Tests pass (verification gate)
- [ ] Choose option (PR/merge/keep/discard)
- [ ] For PR/merge: Run quality gates
- [ ] Execute choice

**Options:**
1. **Create PR:** Push and `gh pr create`
2. **Merge locally:** Checkout main and merge
3. **Keep as-is:** No action
4. **Discard:** Require "discard" confirmation

---

## Tier-Specific Summary

### T1 Requirements
**MANDATORY steps:** 3, 4, 6
**Skip:** Step 1 (skill-suggests), Step 2 (memory search), Step 7 (exploration)
**Optional:** Step 16 (store learnings)

### T2 Requirements
**MANDATORY steps:** 1-6, 8-12, 14-18
**Step 7:** If triggers hit (unfamiliar, cross-file, "how does X work", post Two-Strike)
**Step 9a (TDD):** MANDATORY
**Step 11 (self-reflection):** Recommended
**Step 16 (store learnings):** MANDATORY

### T3 Requirements
**ALL steps MANDATORY** except where noted
**Step 5 (notes.md):** MANDATORY
**Step 7 (exploration):** Codebase research MANDATORY before code changes
**Step 10 (Re-read plan):** Before EVERY major decision
**Step 11 (self-reflection):** MANDATORY
**Step 13 (External LLM):** MANDATORY
**Step 16 (store learnings):** MANDATORY

### T4 Additions
- All T3 requirements
- External LLM validation NON-SKIPPABLE
- task_plan.md must include deployment checklist phase
- task_plan.md must include rollback plan in Decisions section
- Antagonistic QA before marking complete

---

## Common Pitfalls

| Pitfall | Detection | Fix |
|---------|-----------|-----|
| Skipping task_plan.md | No persistent plan exists | Create immediately (Step 4) |
| Task tracking without plan | Tasks exist but no plan file | Create plan, sync Status |
| Forgetting to store learnings | Task complete, no learnings stored | Run Step 16 before marking done |
| Code before test (T2+) | Writing implementation before test | DELETE code, write test first |
| No self-reflection (T3+) | About to code without self-reflection | Stop, run self-reflection first |
| Claiming complete without verification | Using "should work" language | Run Step 18 verification |

---

## Usage

Load this skill when:
- Starting a new task (review full checklist)
- Uncertain about a specific step (find step number)
- Debugging why a step failed (read detailed guidance)
- Explaining workflow to others (comprehensive reference)
