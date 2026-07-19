---
name: context-management
description: Manages context window state using pi-dcp tools and native compaction. Use after compaction events, at subtask boundaries, when context window is filling up, or when resuming prior work.
---

# Context Management

Manages context via the **pi-dcp** tools (`dcp_prune`, `dcp_distill`, `dcp_compress`) and pi's native compaction. No `context-manager` MCP is required.

## Triggers
- Session start / resume
- Before/after compaction events
- Subtask completion
- Context window >60% utilization
- Switching between unrelated tasks

## Protocol — pi-dcp tools

### dcp_distill  (replaces save_checkpoint)
Call at subtask boundaries, before expensive operations, or when 3+ key decisions have accumulated. Replaces verbose tool outputs with concise summaries that preserve key facts, paths, and evidence.
- Targets: stale file reads, resolved errors, redundant listings you still need gist of.
- Provide a distillation that captures the conclusion, not the transcript.

### dcp_prune  (replaces mark_complete)
Call when a subtask is done. Removes tool outputs no longer needed (old file reads superseded by edits, resolved errors, redundant listings). Completed-subtask context is the #1 compaction target — be aggressive.
- Safe to prune: write/edit outputs (filesystem is source of truth), reads from finished phases.

### dcp_compress  (replaces generate_compact_instructions)
Call before `/compact` or at phase boundaries. Compresses a range of conversation (tool calls + messages) into a single summary, removing the originals.
- Use for long stretches of back-and-forth that can be summarized.
- Provide a topic + summary of what was accomplished in the range.

### After compaction
pi's native compaction (settings.json: `compaction.enabled`, `reserveTokens`, `keepRecentTokens`) handles the window. dcp summaries persist through compaction. Read the active plan file (pi-plan-auto) for state — it is the canonical record across compaction events.

## Rules

1. After compaction: read the plan file (pi-plan-auto) before anything else; dcp summaries carry forward.
2. Prefix critical decisions with `[PRESERVE]` in your text output — these survive compaction.
3. Use `dcp_prune` aggressively on completed-subtask outputs — the #1 compaction target.
4. **Graduated read degradation** — apply escalating limits self-directed:
   - 1st read of a path: allowed
   - 2nd read: extract what you need now; a 3rd will be wasteful
   - 3rd+ read: use `grep` with specific patterns instead of full re-read
5. Reading resets after you Write or Edit a file — post-edit re-reads are fine.
6. **Supersede-write awareness** — after writing a file, a subsequent Read of that file is redundant; the write content is already in context. Prefer trusting your write over re-reading.
7. **Error tracking** — repeated failures of the same command: after the 2nd failure, switch strategy. Do not retry a third time.
8. **Broader dedup** — Grep, Glob, WebFetch, WebSearch are tracked; avoid 3+ accesses to the same target without progress.
9. Before long operations (multi-file refactor, large test suite): `dcp_distill` the current state so it survives.
10. When context is >65%: `dcp_compress` a completed range, then continue. If still tight, let pi's native compaction run.
11. At session end: ensure the plan file (pi-plan-auto) has current state for next-session pickup.

## Observation Masking

Self-apply these output truncation rules based on context pressure:

| Output Type | OK (<65%) | ADVISORY (65-75%) | WARNING (75-85%) | CRITICAL (>85%) |
|---|---|---|---|---|
| File >100 lines | Full | Full | Error context + 30 lines | First 20 + last 10 |
| Command success | Full | Full | Exit code + key metrics | Exit code only |
| Command error | Full | Full | Full | Full (always keep) |
| Test results | Full | All failures + stacks | Pass/fail + first 3 failures | Pass/fail counts only |
| Build logs | Full | Full | Final 10 lines | Final 5 lines |

Apply proactively — do not wait to be asked.

## Semantic Preservation

When summarizing or preparing for compaction, apply this priority ordering:

**Always keep:**
- Function signatures, class definitions, and import statements
- Error messages and the lines they reference
- In-scope variable declarations relevant to current task
- Decisions marked `[PRESERVE]` or captured in the plan file

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

- Before a tool call, scan recent turns: if the same tool with same/near-identical args already ran and returned similar results, do NOT repeat — that's a loop.
- Break it: change approach (different tool/query/scope), fall back to a known-good path, or ask the user.
- Two identical-result repeats = hard stop: escalate or surface the blocker rather than retry a third time.
- When context is CRITICAL: `dcp_compress` a completed range with `aggressive` scope to maximize reclamation before native compaction.
- For repeated command failures: after 2 failures, switch strategy immediately; after 3, stop and diagnose root cause or ask the user.