---
name: markdown-preview-split
description: Open a mentioned Markdown file in a Herdr split pane as terminal/TUI preview when running inside Herdr. Use when user asks to preview, render, show, or open a `.md`/Markdown file in Herdr, terminal, split pane, side pane, or TUI instead of browser preview. Especially for requests like "preview this md in herdr", "open markdown in split pane", "show README beside editor", or "render mentioned md file in terminal".
---

# Herdr Markdown Preview Split

## Goal
Open terminal Markdown preview for mentioned `.md` file in Herdr split pane with one helper command.

## Fast path
If target Markdown path is unambiguous, run helper immediately:

```bash
~/.dotfiles/scripts/herdr-md-preview <path-to-md-file>
```

Do **not** preflight `HERDR_ENV`, `glow`, helper existence, or file existence with separate commands. Helper already validates:
- running inside Herdr
- `herdr` on PATH
- `glow` on PATH
- file path resolves and exists

Only ask user when target Markdown file is ambiguous.

## Fallback path
Use fallback only if helper script is unavailable:

```bash
FILE="/absolute/path/to/file.md"
printf -v QUOTED_FILE '%q' "$FILE"
NEW_PANE=$(herdr pane split --current --direction right --ratio 0.45 --no-focus --cwd "$(dirname "$FILE")" | python3 -c 'import json,sys; print(json.load(sys.stdin)["result"]["pane"]["pane_id"])')
herdr pane run "$NEW_PANE" "while true; do clear; glow $QUOTED_FILE || cat $QUOTED_FILE; sleep 1; done"
```

Prefer helper over fallback. Helper is source of truth for quoting, validation, and live refresh behavior.

## Response pattern
After success, say which file was opened and which pane was created.
If blocked, surface exact helper error (`HERDR_ENV!=1`, missing file, missing `glow`, etc.).

## Notes
- This is terminal preview, not browser preview.
- Use for manual preview-on-demand. Do not auto-open just because Markdown file is selected.
- If user mentions specific `.md` file, preview it. If ambiguous, ask which file.
- Avoid multi-step prerequisite probes. One helper invocation is default workflow.
