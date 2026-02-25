> **Claude Code Adapted**: This version has been adapted for Claude Code compatibility. The original OpenCode version is at the root of this repository under `core/token-management/SKILL.md`.

---
name: token-management
description: Token budget awareness, compression strategies, and observation masking for optimal context usage
version: "1.0.0"
---

# Token Management & Compression Strategies

Comprehensive guide for managing token budget, applying tier-appropriate compression, and optimizing context window usage.

## Overview

**Context window is a public good** - every token competes with other information.

This skill provides:
- Token budget monitoring strategies
- Tier-aware compression ratios (T1: 5-10x, T2: 2-5x, T3+: minimal)
- Observation masking rules
- Semantic preservation guidelines (LLMLingua-2)
- Budget overflow protocols

---

## Token Budget Awareness (T2+)

### Monitoring

Monitor context window usage naturally by being aware of conversation length, number of tool outputs accumulated, and the complexity of the current task. There is no explicit stats command in Claude Code; instead, apply these heuristic triggers proactively.

### Budget Action Triggers

<decision-tree name="budget-action-triggers">
  <case condition="phase_boundary_reached">
    <action>Assess context usage and consider offloading to notes.md</action>
  </case>
  <case condition="long_outputs >= 3">
    <action>Consider offloading findings to notes.md</action>
  </case>
  <case condition="error_investigation > 2_attempts">
    <action>Document state in task_plan.md, assess if context reset needed</action>
  </case>
  <case condition="before_context_reset">
    <action>Store critical state in notes.md/task_plan.md, then proceed</action>
  </case>
</decision-tree>

### Heuristic Triggers

| Event | Action |
|-------|--------|
| Phase boundary | Assess context usage, summarize to task_plan.md |
| 3+ long tool outputs | Consider notes.md offload |
| Error investigation >2 attempts | Document state, check context usage |
| Research accumulated | Transfer to notes.md |
| Before context reset | Store state in plan/notes files first |

### Budget Overflow Protocol

When context feels bloated (many tool outputs, long conversation):

1. **Assess what is consuming context:**
   - Count long tool outputs still in conversation
   - Identify completed phases still fully expanded

2. **Offload research findings:**
   - Transfer to `notes.md`
   - Keep executive summary in context

3. **Summarize completed phases:**
   - Update `task_plan.md` with phase summaries
   - Archive detailed exploration notes

4. **Store key learnings in project decision log or notes:**
   ```markdown
   ## [Category]: [Decision]
   - **Context:** [trigger]
   - **Reasoning:** [why]
   - **Outcome:** [result]
   ```

5. **If still overloaded:**
   - Consider starting a fresh conversation and restoring from `task_plan.md`
   - Re-establish context from plan + notes

---

## Observation Masking (Tier-Aware)

Long outputs waste tokens. Apply tier-appropriate masking (50%+ cost savings):

### Masking Rules by Tier

| Output Type | T1 (Simple) | T2 (Moderate) | T3+ (Complex) |
|-------------|-------------|---------------|---------------|
| File >100 lines | First 20 + last 10 + matches | Error context + 20 lines | Full structure |
| Command success | Exit code only | Exit code + key metrics | Exit code + full output |
| Command error | Full error + 3 lines | Full error + 5 lines | Full error section |
| Test results | Pass/fail counts | + first 3 failures | + all failures + stacks |
| API response | Schema only | Schema + sample | Full response |
| Build logs | Final 5 lines | Final 10 lines | Full error section |

### Semantic Preservation

**Always keep:**
- Function signatures
- Error lines
- Imports
- Class definitions

**Safe to compress:**
- Repeated patterns
- Verbose comments
- Whitespace

**Never discard:**
- The exact line referenced in errors

---

## Compression Strategy (Tier-Aware)

<decision-tree name="compression-strategy">
  <description>Select compression ratio based on output type and task tier</description>

  <case condition="output.type == 'error'">
    <action>Keep FULL - errors need complete context</action>
    <rationale>Error diagnosis requires full stack traces and surrounding code</rationale>
  </case>

  <case condition="output.type != 'error'">
    <branch on="task.tier">
      <case value="T1">
        <action>5-10x compression</action>
        <rules>
          <rule>Files: First 20 + last 10 + search matches</rule>
          <rule>Commands: Exit code only</rule>
          <rule>Tests: Pass/fail counts only</rule>
        </rules>
      </case>
      <case value="T2">
        <action>2-5x compression</action>
        <rules>
          <rule>Files: Error context + 20 lines around</rule>
          <rule>Commands: Exit code + key metrics</rule>
          <rule>Tests: Pass/fail + first 3 failures</rule>
        </rules>
      </case>
      <case value="T3">
        <action>1-2x compression (semantic preservation)</action>
        <rules>
          <rule>Files: Full structure, compress comments only</rule>
          <rule>Architecture: Full file required</rule>
          <rule>Tests: Full failure details + stack traces</rule>
        </rules>
      </case>
      <case value="T4">
        <action>No compression (full fidelity)</action>
        <rationale>Critical/deployment tasks need complete context</rationale>
      </case>
    </branch>
  </case>
</decision-tree>

---

## Semantic Preservation Rules (LLMLingua-2)

### Core Principles

**Always keep:**
- Function signatures
- Imports
- Class definitions
- Error lines
- Variable declarations (in scope)

**Compress safely:**
- Repeated patterns
- Verbose comments
- Extensive whitespace
- Boilerplate code

**Never discard:**
- The exact line referenced in errors
- Function/class definitions in error stack
- Import statements causing issues

### Example: T1 Compression

**Original (100 lines):**
```python
# Long file with verbose comments
import os
import sys
import json

def process_data(data):
    """
    This function processes data by doing X, Y, and Z.
    It takes a data parameter and returns processed result.
    ... (50 lines of docstring) ...
    """
    # Implementation details...
    result = transform(data)
    return result

# ... 80 more lines ...
```

**T1 Compressed:**
```python
import os, sys, json
def process_data(data):
    result = transform(data)
    return result
# ... [80 lines compressed] ...
```

### Example: T3 Architecture Task

**Original:** Keep FULL

**Reasoning:** Architecture decisions require understanding full context, including:
- All class relationships
- Method signatures
- Inheritance hierarchies
- Complex logic flow

---

## Context Stability

### Keep Fixed

- System prompt and CLAUDE.md rules
- Current task goal from task_plan.md
- Active phase objectives

### Summarize at Boundaries

- Completed phases (executive summary in task_plan.md)
- Exploration findings (detailed in notes.md)
- Research notes (transfer to notes.md or project decision logs)

### Archive Aggressively

- Old tool outputs (>3 turns ago, unless actively referenced)
- Completed explorations
- Resolved error investigations

---

## Recovery Strategies

### Pre-Reset Protocol

Before starting a fresh conversation:

1. **Document current state:**
   - Update task_plan.md with exact position
   - Log next 2 steps clearly
   - Store context-critical insights in notes.md or project decision logs

2. **Assess what's important:**
   - Identify what information must survive the reset
   - Ensure task_plan.md captures current status completely

3. **Archive findings:**
   - Transfer research to notes.md
   - Store learnings in project decision logs

4. **Mark checkpoint in plan:**
   ```markdown
   ## Checkpoint: Before Context Reset
   - Position: [exact step]
   - Next: [next 2 steps]
   - Critical context: [key info]
   ```

### Post-Reset Recovery

After starting a fresh conversation:

1. **Read task_plan.md:**
   - Find "Checkpoint" or current position
   - Understand completed phases

2. **Restore task tracking:**
   - Use `TaskCreate` to initialize remaining steps
   - Use `TaskUpdate` to mark prior phases as completed

3. **Resume from position:**
   - Continue from exact step
   - Reference notes.md as needed

---

## Best Practices

### DO

- Monitor context usage naturally at phase boundaries
- Offload research to notes.md early (not when overloaded)
- Store learnings in project decision logs (not only in conversation context)
- Match compression to tier (T1: heavy, T3: light)
- Keep errors at full fidelity (always)

### DON'T

- Wait until forced context overflow (proactive offloading)
- Apply same compression to all tiers (tier-aware)
- Compress error outputs (always full)
- Lose investigation progress (store first, then reset)
- Forget to document state before context reset (tracking)

---

## Quick Reference

### When to Assess Context Usage

- Phase boundaries
- After 3+ long tool outputs
- Before context reset
- Error investigation >2 attempts

### Compression Ratios

- T1: 5-10x (aggressive)
- T2: 2-5x (moderate)
- T3: 1-2x (light)
- T4: None (full fidelity)
- Errors: FULL (always)

### Offload Targets

- Research findings -> `notes.md`
- Key learnings -> project decision logs
- Completed phases -> task_plan.md summary
- Old tool outputs -> Archive (remove from context)

---

## Usage

Load this skill when:
- Context feels bloated (offload guidance)
- Approaching context limits (overflow protocol)
- Uncertain about compression level (tier matching)
- Before context reset (recovery protocols)
- Setting up new task (budget awareness)
