---
name: context-management
description: Manages context window state using MCP checkpoints. Use after compaction events, at subtask boundaries, when context window is filling up, or when resuming prior work.
---

# Context Management

## Triggers
- Session start / resume
- Before/after compaction events
- Subtask completion
- Context window >60% utilization
- Switching between unrelated tasks

## Protocol

You have a `context-manager` MCP server with these tools:

### save_checkpoint
Call at subtask boundaries, before expensive operations, or when 3+ key decisions
have accumulated. Include:
- `task_state`: One sentence — current objective + status
- `files_modified`: Only files YOU changed (not read)
- `decisions`: Format as "chose X over Y because Z"
- `errors`: Only unresolved blockers

### load_checkpoint
Call FIRST after any compaction event. Also useful when unsure about prior decisions
or when resuming previous work. Omit `label` to get the latest.

### mark_complete
Call when a subtask is done. The summary persists across compaction — this is the
primary mechanism for safe context reduction. Be aggressive with this.

### get_context_stats
Check periodically. If duplicate reads appear (>2x same file), stop re-reading
and extract what you need. Completed subtask count indicates compaction-safe zones.

### list_checkpoints
Enumerate saved state. Useful at session start to understand what prior work exists.

### track_tool_usage
Normally called by hooks automatically. Manual use when you want to register
a custom tracking event.

### get_context_stats (enhanced)
Pass `current_budget_remaining` from your `<budget:N>` context tag to receive
actual utilization percentage and a concrete compaction recommendation.

### generate_compact_instructions
Call before any /compact invocation. Reads session state and produces a
structured preserve/drop instruction string. Use the output as the focus
argument: `/compact <output>`. This directs the compaction model to keep
critical decisions and drop stale tool output noise.

## Rules

1. After compaction: `load_checkpoint` before anything else
2. Prefix critical decisions with `[PRESERVE]` in your text output — hooks extract these
3. Use `mark_complete` aggressively — completed work context is the #1 compaction target
4. **Graduated read degradation** — the PreToolUse hook applies escalating limits:
   - 1st read: allowed silently
   - 2nd read: warning that 3rd will be truncated — extract what you need now
   - 3rd read: allowed but output truncated to 50 lines; use Grep for specifics
   - 4th+ read: **hard deny** — use Grep or your existing knowledge
5. The hook resets the read counter when you Write or Edit a file, so post-edit re-reads work
6. **Supersede-write detection** — after writing a file, any subsequent Read of that file
   generates an advisory that the write's content in context is redundant. `generate_compact_instructions`
   will include superseded paths in the DROP list automatically.
7. **Error tracking** — repeated failures of the same command trigger an advisory after the
   2nd failure. If you see "This command has failed N times", switch strategy.
8. **Broader dedup coverage** — Grep, Glob, WebFetch, and WebSearch are now tracked.
   Advisory warnings fire at 3+ accesses (no blocking — these tools are cheap/variable).
9. Before long operations (multi-file refactor, large test suite), save a checkpoint
10. When context is >65%: call `get_context_stats` with your budget tag, then
    `generate_compact_instructions`, then run `/compact`
11. At session end, save a final checkpoint with current state for next session pickup

## Observation Masking

Self-apply these output truncation rules based on the `level` returned by `get_context_stats`:

| Output Type | OK (<65%) | ADVISORY (65-75%) | WARNING (75-85%) | CRITICAL (>85%) |
|---|---|---|---|---|
| File >100 lines | Full | Full | Error context + 30 lines | First 20 + last 10 |
| Command success | Full | Full | Exit code + key metrics | Exit code only |
| Command error | Full | Full | Full | Full (always keep) |
| Test results | Full | All failures + stacks | Pass/fail + first 3 failures | Pass/fail counts only |
| Build logs | Full | Full | Final 10 lines | Final 5 lines |

Apply these rules proactively — do not wait to be asked.

## Semantic Preservation

When summarizing or preparing for compaction, apply this priority ordering:

**Always keep:**
- Function signatures, class definitions, and import statements
- Error messages and the lines they reference
- In-scope variable declarations relevant to current task
- Decisions marked `[PRESERVE]` or recorded via `save_checkpoint`

**Safe to compress:**
- Repeated patterns (show one example, note repetition count)
- Verbose comments and extensive whitespace
- Boilerplate and scaffolding unrelated to current task
- Intermediate debugging output that preceded a fix

**Never discard:**
- Exact lines referenced in active error messages
- Function/class definitions appearing in error stack traces
- Import statements causing the current issue
- The most recent state of any modified file

## Anti-Loop and Escalation

Follow `escalation_steps` from `get_context_stats` in order — do not skip steps.

When level is CRITICAL, call `generate_compact_instructions` with `aggressive: true` to
maximize context reclamation before compaction.

For repeated command failures:
- **After 2 failures of the same command**: switch strategy immediately — do not retry.
  The hook emits `[STRATEGY-SHIFT]` to signal this.
- **After 3 failures of the same command**: stop and diagnose root cause, or ask the user.
  The hook emits `[ANTI-LOOP] BLOCKED` with the failure count and origin turn.
