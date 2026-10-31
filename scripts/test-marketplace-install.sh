#!/usr/bin/env bash
# End-to-end: install every plugin from a clean copy of the repo (git-tracked
# and untracked-but-not-ignored files only, i.e. what a push would publish)
# into a throwaway HOME, then check every listed skill is present after install.
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
work="$(mktemp -d)"
trap 'rm -rf "$work"' EXIT

repo="$work/repo"
mkdir -p "$repo" "$work/home"
(cd "$root" && git ls-files -z --cached --others --exclude-standard) \
  | (cd "$root" && xargs -0 cp --parents -t "$repo")

export HOME="$work/home"
claude plugin marketplace add "$repo" >/dev/null

marketplace="$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["name"])' "$repo/.claude-plugin/marketplace.json")"
failed=0
while IFS=$'\t' read -r plugin _source skill; do
  if [[ "$skill" == "-" ]]; then
    if ! claude plugin install "$plugin@$marketplace" >"$work/out" 2>&1; then
      echo "FAIL install $plugin"; cat "$work/out"; failed=1
    fi
    continue
  fi
  # Check the installed copy in the plugin cache, not the source tree.
  found="$(find "$HOME/.claude/plugins/cache/$marketplace/$plugin" -path "*/${skill#./}/SKILL.md" -print -quit 2>/dev/null || true)"
  if [[ -z "$found" ]]; then
    echo "FAIL $plugin: $skill missing after install"; failed=1
  fi
done < <(python3 - "$repo/.claude-plugin/marketplace.json" <<'EOF'
import json, sys
for p in json.load(open(sys.argv[1]))["plugins"]:
    print(f"{p['name']}\t{p['source']}\t-")
    for s in p["skills"]:
        print(f"{p['name']}\t{p['source']}\t{s}")
EOF
)

claude plugin list >"$work/list" 2>&1
count="$(grep -c "@$marketplace" "$work/list" || true)"
expected="$(python3 -c 'import json,sys; print(len(json.load(open(sys.argv[1]))["plugins"]))' "$repo/.claude-plugin/marketplace.json")"
if [[ "$count" != "$expected" ]]; then
  echo "FAIL: $count of $expected plugins installed"; failed=1
fi

if [[ $failed -ne 0 ]]; then exit 1; fi
echo "OK: $expected plugins installed from $marketplace"
