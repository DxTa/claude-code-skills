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

## Semantic ranking

After reading index, use semantic search to produce advisory candidates:

```bash
node "$HOME/.dotfiles/pi/scripts/agent-semantic-search.mjs" search --catalog agents --query "<one-sentence task>" --top-k 5
```

Treat returned names as candidates only. Read matching agent files and apply explicit task fit, safety, and routing rules. If command fails because model, cache, or index is unavailable, continue with manual index selection; never use stale output.

## Dispatch

1. **Explore fast lane:** first agent for a new broad/uncertain, read-only retrieval. For one direction, use foreground `Agent({ subagent_type: "explore", inherit_context: false, thinking: "low", max_turns: 6, run_in_background: false })`; wait for its inline result before any parent tool call, routing read, or next delegation. For two or more independent directions, issue all `Agent({ subagent_type: "explore", inherit_context: false, run_in_background: true })` calls in one parallel tool turn. Stop task-specific work and wait for every completion notification/result before synthesis, dependent inspection, routing, or another delegation; do not poll or sleep. Prompt each agent only cwd, precise question, scope, and expected evidence. Skip index, agent-file, and contract reads for these fast-lane calls.
2. Fast lane covers read-only exploration only; not edits, implementation, review, security/audit, testing, deployment, specialist selection, or coupled directions. Use normal routing after all required Explore evidence returns.
3. Known narrow path/symbol: inspect directly; do not delegate.
4. **MUST read `agents-index.tsv`** and match task intent against `description` before selecting every specialist or non-fast-lane agent.
5. **MUST generate delegation contract** with `delegate-prompt.sh` before every non-fast-lane `Agent(...)` call. Contract includes mode, objective, scope, out-of-scope, phase, prior decisions, artifact authority, allowed actions, and structured return.
6. Parent synthesizes all required Explore results; parallelize independent read-only research only.
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
