---
name: planning-with-files
description: Use when Tier 2+ tasks, multi-step projects, or when tracking/recovery is needed and plan files must persist across sessions.
---

# Planning with Files + TodoWrite Integration

Work like Manus: Use persistent markdown files as your "working memory on disk" while leveraging TodoWrite for live session tracking.

## Aggressive Default

For Tier 2+ engineering work, create or update the plan file as soon as task intent is understood. Do not wait until planning is "done." The plan file is live working memory during both planning and implementation.

### Existing Active Plan File Wins

If the current session already has an active plan file from `pi-plan-auto` or another planning tool, use that file as the single source of truth. Do not create `task_plan.md`, notes files, or fallback plan files unless no active plan file exists or the user explicitly asks for a separate artifact.

Apply this skill's structure and sync discipline to the existing active plan file:

- In Plan mode: update the existing active plan via `set_plan`; never write or duplicate it with file tools.
- In implementation mode: read the active plan file path from the handoff/prefill, then keep that same file's Status, errors, phase checkboxes, and verification notes current.
- On resume: locate and read the existing active plan file before deciding whether any fallback file is needed.

Default behavior:

- In Plan mode: call `set_plan` early with a skeleton in the active plan file, then refresh it after every material change.
- In implementation mode: read the active plan file before coding, update its Status as phases/steps advance, and log errors plus verification results in that same file when `set_plan` is unavailable.
- If a task already has a plan file, resume from it before making decisions.
- If no plan file exists for a Tier 2+ task, create one unless the user explicitly asks not to.
- Prefer plan-file continuity over chat-only reasoning for anything likely to survive context reset.

## Quick Reference

| Tool | Purpose | Persistence | TUI Visible |
|------|---------|-------------|-------------|
| **TodoWrite** | Live step tracking | Session only | Yes |
| **active plan file** | Phases, goals, errors, learnings | Permanent | No |
| **notes.md** | Research findings, only when no active plan already covers them | Permanent | No |

## File Locations

Prefer the active plan file path provided by the current planning tool or implementation prefill. In Pi, this is usually the `.plan.md` file created by `pi-plan-auto` and maintained through `set_plan` during Plan mode.

Only if no active plan path exists, use the current environment's durable plan directory:

```
{planDir}/
├── {project}_{id}_task_plan.md    # Main plan (id = sessionID if available, else uuid)
├── {project}_{id}_notes.md        # Research (Tier 3+)
└── archive/                        # Optional auto-archive location
```

Suggested `planDir` by environment:

- Pi plan mode: use the active `.plan.md` path from `set_plan` / plan-mode prefill.
- Pi fallback: `~/.pi/plans/`
- OpenCode fallback: `~/.config/opencode/plans/`

## Identifier Selection (Preferred: active session ID)

**Every new task MUST have a unique identifier (`id`) used in filenames.**

**Preferred:** use the current environment's session ID and project slug if available.
- If the environment exposes `taskPlanPath` / `notesPath`, use those exact paths.
- If a plan-mode prefill names a plan file, use that path and do not create a second plan.
- Otherwise use:
  - `{planDir}/{projectSlug}_{sessionID}_task_plan.md`
  - `{planDir}/{projectSlug}_{sessionID}_notes.md`
  - If `projectSlug` is unavailable, use a short project name (e.g., cwd basename)

**Fallback only if sessionID is unavailable/empty:**
```bash
uuidgen | cut -c1-8
```

**Never use:**
- Descriptive names (e.g., `notifications_fix`)
- Dates (e.g., `20260104`)
- Mixed formats
- A second plan file when an active plan file already exists

## Tier Adaptation

| Tier | Active plan file | notes.md | TodoWrite | Re-read |
|------|------------------|----------|-----------|---------|
| T1 | Optional | Skip | Mandatory | Skip |
| T2 | **Mandatory** | If research and not covered in active plan | Mandatory | Before major decisions |
| T3+ | **Mandatory** | If research needs separate artifact | Mandatory | Before EVERY decision |

## Sync Protocol (Critical)

**Plan mode bootstrap:**
1. Reuse the active plan file if one exists; otherwise create/write a plan skeleton immediately after understanding goal.
2. Include Goal, Phases, Key Questions, Status, and expected verification.
3. Call `set_plan` before launching broad exploration or asking non-blocking questions.

**After every TodoWrite update:**
1. Update the active plan file's Status section with current position
2. Log any errors to "Errors Encountered" section

**After every material planning change:**
1. Update Decisions Made, Key Questions, Risks/Open Questions, and Status
2. Call `set_plan` with the full latest plan while in Plan mode

**During implementation:**
1. Re-read the active plan file before each major decision or phase transition
2. Mark completed steps/phases as work lands
3. Update Status with the exact next action
4. Append errors, blockers, verification commands, and results to the same active plan file

**At phase boundaries:**
1. Mark phase [x] in the active plan file
2. Update Status to next phase
3. Reset TodoWrite with next phase's steps

**Before /clear or session end:**
1. Ensure the active plan file Status reflects exact position
2. Note any in-progress items

**On session resume:**
1. Read the existing active plan file when available; otherwise read the fallback plan file
2. Identify current phase from Status
3. TodoWrite: Recreate items for current phase

## Tool Fallbacks (Write/Edit Unavailable)

If `write`/`edit` tools are not available:
1. In Pi Plan mode, use `set_plan` for the active plan file instead of shell/file writes.
2. If no active plan file exists and no plan-writing tool exists, ask the user for permission to create a fallback file via bash heredoc/redirect.
3. If `apply_patch` is available, use it to add or update the fallback file with full content.
4. If approved, create the fallback file with a single command:
   ```bash
   cat <<'EOF' > /absolute/path/to/task_plan.md
   [template contents]
   EOF
   ```
5. If not approved, ask the user to create the file manually and provide the template.
6. Never use `echo` or partial writes for multi-line files.

## Active Plan File Template

```markdown
# Task Plan: [Brief Description]

## Goal
[One sentence describing to end state]

## Phases
- [ ] Phase 1: Plan and setup
- [ ] Phase 2: Research/gather information
- [ ] Phase 3: Execute/build
- [ ] Phase 4: Review and deliver

## Key Questions
1. [Question to answer]

## Decisions Made
- [Decision]: [Rationale]

## Delegation Summary
Include only when subagents are dispatched.
- [agent-name]: [objective] - [key finding or status]

## Errors Encountered
- [Timestamp] [Error]: [Resolution]

## Learnings for Graphiti
- [Procedure/Preference/Fact]: [Learning to store after task]

## Status
**Currently in Phase X** - [What I'm doing now]
**TodoWrite sync:** [Last synced step]
```

## notes.md Template (Tier 3+)

```markdown
# Notes: [Task Brief]

## Research Findings

### Source 1: [Name]
- URL: [link]
- Key points:
  - [Finding]

### Source 2: [Name]
...

## Synthesized Insights
- [Category]: [Insight]

## Open Questions
- [Question still to resolve]
```

## Critical Rules

### 1. Dual-Layer Tracking
- TodoWrite = live visibility (TUI)
- active plan file = persistence + recovery

### 2. Sync After Every TodoWrite Update
Keep the active plan file Status current. This enables recovery after context reset.

### 2a. Sync After Every Material Change
In Plan mode, `set_plan` is mandatory after material changes. In implementation mode, update the plan file directly with normal file edit tools. Material changes include new requirements, decisions, delegated findings, phase transitions, blockers, errors, verification results, and scope changes.

### 3. Re-read Before Decisions (Tier 2+)
Read the active plan file before major decisions to bring goals into attention window.

### 4. Log All Errors
Every error goes in the active plan file. TodoWrite doesn't track error history.

### 5. Bridge to Graphiti
At task end, extract learnings from the active plan file to store in Graphiti memory.

### 6. Record Delegation Only When Used
If any subagent was dispatched, add a `Delegation Summary` section to the active plan file with the selected agents, objectives, and key findings. If no delegation happened for a qualifying task, note the skip rationale in the plan status or decisions section.

## Recovery Scenario

```
Context reset or /clear happens...

1. Read the active plan file
   → Status: "Currently in Phase 2 - Implementing auth middleware"
   → TodoWrite sync: "Completed JWT validation, working on user service"

2. Restore TodoWrite:
   - [x] Create auth middleware file
   - [x] Add JWT validation logic
   - [in_progress] Connect to user service
   - [pending] Add error handling

3. Continue from exact position
```

## Why This Works

| Problem | TodoWrite Alone | With active plan file |
|---------|-----------------|-----------------------|
| Context reset | **Lost** | Recoverable |
| 50+ tool calls | Goal drift | Re-read refreshes goals |
| Error patterns | Not tracked | Logged for learning |
| Cross-session | Must restart | Resume exactly |
| Graphiti sync | Manual | "Learnings" section |
