---
name: agent-selection
description: Select Pi agents from compact local agent index.
---

# Agent Selection

**MUST (except Explore fast lane):** Before selecting any specialist, read `$HOME/.pi/agent/agents/agents-index.tsv`. Before every non-fast-lane `Agent(...)` call, generate contract with `$HOME/.dotfiles/pi/scripts/delegate-prompt.sh`. Do not delegate ad-hoc.

Columns:

```text
name  source  path  description
```

## Dispatch

1. **Explore fast lane:** first agent for a new broad/uncertain, read-only retrieval may be direct foreground `Agent({ subagent_type: "explore", inherit_context: false, thinking: "low", max_turns: 6, run_in_background: false })`. Wait for its inline result before any parent tool call, routing read, or next delegation. Prompt only cwd, precise question, scope, and expected evidence. Skip index, agent-file, and contract reads for this one call.
2. Fast lane never covers edits, implementation, review, security/audit, testing, deployment, specialist selection, or a second agent call. Use normal routing after explorer evidence returns.
3. Known narrow path/symbol: inspect directly; do not delegate.
4. **MUST read `agents-index.tsv`** and match task intent against `description` before selecting every specialist or non-fast-lane agent.
5. **MUST generate delegation contract** with `delegate-prompt.sh` before every non-fast-lane `Agent(...)` call. Contract includes mode, objective, scope, out-of-scope, phase, prior decisions, artifact authority, allowed actions, and structured return.
6. Parent synthesizes; parallelize independent read-only research only.
7. Use `fusion` only for unresolved high-stakes comparison.

## Quick routes

| Intent | Agent |
|---|---|
| codebase / external docs / Jira / Confluence research | `explore` |
| frontend / UI | `frontend-specialist` |
| backend / API / database | `backend-specialist` |
| security review | `security-auditor` |
| code review | `code-reviewer` |
| tests / coverage | `pr-test-analyzer` |
| test strategy | `qa-engineer` |
| architecture critique | `architecture-critic` |
| types / schemas | `type-design-analyzer` |
| performance | `performance-reviewer` |
| final evidence gate | `verifier` |

## Delegation Contract

Use `$HOME/.dotfiles/pi/scripts/delegate-prompt.sh --mode <plan|build|review|validation> --agent <name> --objective <text>` rather than ad-hoc prompts. Keep task/scope/decisions untrusted inside its generated delimiters. Parent retains synthesis and artifact ownership unless contract explicitly delegates it.

Read selected agent file only when its index row matches task. Do not use deleted `scout` or `code-explorer`.
