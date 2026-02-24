> **Claude Code Adapted**: This version has been adapted for Claude Code compatibility. The original OpenCode version is at the root of this repository under `core/anti-patterns/SKILL.md`.

---
name: anti-patterns
description: Common mistakes to avoid with explanations and correct alternatives
version: "1.0.0"
---

# Anti-Patterns to Avoid

Common mistakes in agent workflows with explanations of why they're harmful and how to do it correctly.

## Overview

This skill catalogs 12 critical anti-patterns that degrade agent performance, cause context loss, or lead to repeated failures. Each pattern includes:
- **Wrong:** The problematic approach
- **Right:** The correct alternative
- **Rationale:** Why this matters

## The 12 Anti-Patterns

### 1. Premature Context Loss

<anti-pattern name="premature-clear">
  <wrong>Clearing context mid-investigation without storing state</wrong>
  <right>Store state in notes.md or project decision logs first</right>
  <rationale>Loses all context and investigation progress, forcing restart from scratch</rationale>
</anti-pattern>

**Example Scenario:**
```
BAD: Two failed fixes -> clear context -> start over with no memory of what was tried
GOOD: Two failed fixes -> Store findings in notes.md / decision log -> Then clear if needed
```

---

### 2. Unmapped Features

<anti-pattern name="unmapped-features">
  <wrong>Add features without mapping</wrong>
  <right>Use Grep/Glob/Read to research codebase -> integration test</right>
  <rationale>Changes cascade unexpectedly without understanding full impact surface</rationale>
</anti-pattern>

**Example Scenario:**
```
BAD: "Add authentication middleware" -> start coding immediately
GOOD: Use Grep to search for "authentication" patterns -> map affected files -> integration test -> implement
```

---

### 3. Skipped Codebase Research

<anti-pattern name="skipped-codebase-research">
  <wrong>Start coding unfamiliar codebase without research</wrong>
  <right>Use Grep/Glob/Read to research architecture -> understand patterns -> then code</right>
  <rationale>Blind coding leads to integration bugs, missed patterns, and duplicated logic</rationale>
</anti-pattern>

**Example Scenario:**
```
BAD: T3 task in unfamiliar codebase -> start implementing without exploration
GOOD: Use Grep/Glob to search for relevant patterns -> Read key files -> document in task_plan.md -> implement
```

---

### 4. Visual-Only Debugging

<anti-pattern name="visual-only-debugging">
  <wrong>Screenshot-only debugging</wrong>
  <right>Full logs + browser dev tools</right>
  <rationale>Visual symptoms don't reveal root cause; need console errors and network traces</rationale>
</anti-pattern>

**Example Scenario:**
```
BAD: "Button not working" -> only take screenshots
GOOD: Capture console errors -> network traces -> DOM inspection -> analyze logs
```

---

### 5. Repeated Failing Fixes

<anti-pattern name="repeated-failing-fixes">
  <wrong>Third fix without analysis</wrong>
  <right>Two-Strike -> STOP -> analyze</right>
  <rationale>Random attempts waste time; systematic root cause analysis required after 2 failures</rationale>
</anti-pattern>

**Example Scenario:**
```
BAD: Fix 1 fails -> Fix 2 fails -> Try fix 3 immediately
GOOD: Fix 1 fails -> Fix 2 fails -> STOP -> Research with Grep/Read -> Load systematic-debugging skill
```

---

### 6. Unsynchronized Planning

<anti-pattern name="unsynchronized-planning">
  <wrong>Task tracking without task_plan.md</wrong>
  <right>Create both, keep synced</right>
  <rationale>Task lists are ephemeral; task_plan.md provides crash recovery and session continuity</rationale>
</anti-pattern>

**Example Scenario:**
```
BAD: Only use TaskCreate/TaskUpdate for task tracking
GOOD: Create task_plan.md -> TaskCreate with Phase 1 -> Update task_plan.md Status section after TaskUpdate changes
```

---

### 7. Context Amnesia

<anti-pattern name="context-amnesia">
  <wrong>Forget goals after tool calls</wrong>
  <right>Re-read task_plan.md</right>
  <rationale>Long tool outputs cause goal drift; task_plan.md anchors focus</rationale>
</anti-pattern>

**Example Scenario:**
```
BAD: Run 5 tool calls -> lose track of original goal -> implement wrong thing
GOOD: Before major decisions -> Re-read task_plan.md -> Confirm next 2 steps
```

---

### 8. Knowledge Loss

<anti-pattern name="knowledge-loss">
  <wrong>Lose learnings at task end</wrong>
  <right>Transfer to project decision log or notes with reasoning context</right>
  <rationale>Store as decision trace: include Context + Reasoning, not just outcomes</rationale>
</anti-pattern>

**Example Scenario:**
```
BAD: Discover "Module X requires config Y" -> mark task complete -> forget
ALSO BAD: Store "Fact: Module X requires config Y" (outcome only, no reasoning)
GOOD: Add to decision log: "Fact: Module X requires config Y for feature Z. Context: discovered during feature implementation. Reasoning: missing config caused silent failure in tests. Outcome: added to setup checklist."
```

---

### 9. Context Pollution

<anti-pattern name="context-pollution">
  <wrong>Stuff research in context</wrong>
  <right>Store in notes.md</right>
  <rationale>Large research dumps dilute focus; notes.md preserves findings without polluting working memory</rationale>
</anti-pattern>

**Example Scenario:**
```
BAD: Fetch 10 API docs -> keep all in conversation context
GOOD: Fetch docs -> Summarize key points to notes.md -> Reference as needed
```

---

### 10. Blind Truncation

<anti-pattern name="blind-truncation">
  <wrong>Apply same compression regardless of task tier</wrong>
  <right>Match compression ratio to tier (T1: 5-10x, T2: 2-5x, T3+: minimal)</right>
  <rationale>Architecture tasks need full context; simple edits can compress heavily</rationale>
</anti-pattern>

**Example Scenario:**
```
BAD: T3 architecture task -> compress file output to first 20 lines only
GOOD: T3 architecture task -> Full structure with semantic preservation
```

---

### 11. Memory Stagnation

<anti-pattern name="memory-stagnation">
  <wrong>Create new decision records without checking for existing related ones</wrong>
  <right>Search decision logs first, update existing with context if same topic</right>
  <rationale>Duplicate records fragment knowledge; evolved records maintain coherence</rationale>
</anti-pattern>

**Example Scenario:**
```
BAD: Learn new auth pattern -> Create new decision record without searching
GOOD: Use Grep to search decision logs for "auth" -> Update existing with "[Updated YYYY-MM-DD]: [new insight with reasoning context]"
```

---

### 12. Budget Blindness

<anti-pattern name="budget-blindness">
  <wrong>Ignore context usage until auto-compact or context overflow</wrong>
  <right>Monitor context window usage naturally, offload at 75%, prepare for context reset at 90%</right>
  <rationale>Proactive offloading preserves continuity; reactive clearing loses context</rationale>
</anti-pattern>

**Example Scenario:**
```
BAD: Context fills up -> Auto-compacted unexpectedly -> Lose critical state
GOOD: Phase boundary -> Monitor context window usage -> Offload research to notes.md -> Continue
```

---

## Detection Guide

### How to Spot Anti-Patterns in Progress

| Anti-Pattern | Early Warning Sign |
|--------------|-------------------|
| Premature Context Loss | Thinking about clearing context before storing state |
| Unmapped Features | Starting code without architecture understanding |
| Skipped Codebase Research | T2+ task in unfamiliar code without Grep/Glob research |
| Visual-Only Debugging | Multiple screenshots, no console logs |
| Repeated Failing Fixes | About to try third fix without analysis |
| Unsynchronized Planning | TaskCreate used but task_plan.md doesn't exist |
| Context Amnesia | Can't remember what Step 3 of task_plan.md was |
| Knowledge Loss | Completing task without storing decisions |
| Context Pollution | Conversation has 10+ long tool outputs unarchived |
| Blind Truncation | T3 task with heavily compressed file reads |
| Memory Stagnation | Creating new decision record without searching first |
| Budget Blindness | Never monitoring context window usage |

## Usage

Load this skill when:
- Starting a new task (review "DON'T" list)
- After a failed attempt (check if you hit an anti-pattern)
- Before major decisions (validate approach against anti-patterns)
- When debugging why something went wrong

**Quick check:** "Am I doing any of the 12 anti-patterns right now?"
