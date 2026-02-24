#!/usr/bin/env bash
#
# sync-plugins.sh - Regenerate plugin skills/ symlinks from root skill directories
#
# Usage: ./scripts/sync-plugins.sh [--dry-run]
#
# Reads the plugin list from .claude-plugin/marketplace.json and recreates
# all skills/ symlinks in each plugin directory, pointing back to the
# canonical root skill directories. Skips context-engineering (real files).

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MARKETPLACE="${REPO_ROOT}/.claude-plugin/marketplace.json"
DRY_RUN=false

if [[ "${1:-}" == "--dry-run" ]]; then
    DRY_RUN=true
    echo "[dry-run] No changes will be made."
    echo
fi

if [[ ! -f "$MARKETPLACE" ]]; then
    echo "ERROR: marketplace.json not found at ${MARKETPLACE}" >&2
    exit 1
fi

# ---------------------------------------------------------------------------
# Plugin -> root skill path mapping
#
# Each key is a plugin name from marketplace.json.
# Values are space-separated "root_dir/skill_name" relative to REPO_ROOT.
# ---------------------------------------------------------------------------
declare -A PLUGIN_SKILLS

PLUGIN_SKILLS[core-thinking]="
    core/collision-zone-thinking
    core/defense-in-depth
    core/inversion-exercise
    core/meta-pattern-recognition
    core/root-cause-tracing
    core/scale-game
    core/simplification-cascades
    core/when-stuck
    core/reasoning-tools
"

PLUGIN_SKILLS[core-workflow]="
    core/code-review
    core/planning-with-files
    core/push-all
    core/skill-creator
    core/spec-analyzer
"

# context-engineering is skipped (uses real files, not symlinks)

PLUGIN_SKILLS[frontend]="
    frontend/frontend-design
    frontend/frontend-development
    frontend/ui-styling
    frontend/web-artifacts-builder
    frontend/web-frameworks
"

PLUGIN_SKILLS[backend]="
    backend/backend-development
    backend/databases
"

PLUGIN_SKILLS[quality]="
    quality/chaos-engineering-toolkit
    quality/code-review-plugin
    quality/performance-test-suite
    quality/pr-review-toolkit
    quality/test-coverage-analyzer
    quality/webapp-testing
"

PLUGIN_SKILLS[devops]="
    devops/ansible-playbook-creator
    devops/ci-cd-pipeline-builder
    devops/cloud-cost-optimizer
    devops/infrastructure-as-code-generator
"

PLUGIN_SKILLS[docs]="
    docs/api-documentation-generator
    docs/docx
    docs/pdf
    docs/pptx
    docs/xlsx
"

PLUGIN_SKILLS[design]="
    design/algorithmic-art
    design/artifacts-builder
    design/brand-guidelines
    design/canvas-design
    design/theme-factory
"

PLUGIN_SKILLS[security]="
    security/security-pro-pack
    security/security-test-scanner
"

PLUGIN_SKILLS[comms]="
    comms/gcal
    comms/gdrive
    comms/github-operations
    comms/glab-operations
    comms/gmail
    comms/internal-comms
"

PLUGIN_SKILLS[media-and-data]="
    media/media-processing
    media/slack-gif-creator
    data/memvid
    data/pkm
"

PLUGIN_SKILLS[tools-and-integrations]="
    tools/chrome-devtools
    integration/mcp-builder
"

# ---------------------------------------------------------------------------
# Counters
# ---------------------------------------------------------------------------
total_removed=0
total_created=0
total_broken=0
plugins_processed=0
plugins_skipped=0

# ---------------------------------------------------------------------------
# Process each plugin
# ---------------------------------------------------------------------------
for plugin in $(echo "${!PLUGIN_SKILLS[@]}" | tr ' ' '\n' | sort); do
    plugin_dir="${REPO_ROOT}/plugins/${plugin}"
    skills_dir="${plugin_dir}/skills"

    if [[ ! -d "$plugin_dir" ]]; then
        echo "WARNING: Plugin directory missing: ${plugin_dir}" >&2
        plugins_skipped=$((plugins_skipped + 1))
        continue
    fi

    echo "--- ${plugin} ---"

    # 1. Remove existing symlinks in skills/
    if [[ -d "$skills_dir" ]]; then
        while IFS= read -r -d '' link; do
            if $DRY_RUN; then
                echo "  [dry-run] would remove symlink: $(basename "$link")"
            else
                rm "$link"
            fi
            total_removed=$((total_removed + 1))
        done < <(find "$skills_dir" -maxdepth 1 -type l -print0)
    else
        if $DRY_RUN; then
            echo "  [dry-run] would create directory: skills/"
        else
            mkdir -p "$skills_dir"
        fi
    fi

    # 2. Recreate symlinks from mapping
    for skill_path in ${PLUGIN_SKILLS[$plugin]}; do
        skill_name="$(basename "$skill_path")"
        source_abs="${REPO_ROOT}/${skill_path}"
        # Symlink target is relative: ../../../<root_dir>/<skill_name>
        root_dir="$(dirname "$skill_path")"
        link_target="../../../${root_dir}/${skill_name}"
        link_path="${skills_dir}/${skill_name}"

        if [[ ! -d "$source_abs" ]]; then
            echo "  WARNING: Source directory missing: ${skill_path}" >&2
            total_broken=$((total_broken + 1))
            continue
        fi

        if $DRY_RUN; then
            echo "  [dry-run] would link: ${skill_name} -> ${link_target}"
        else
            ln -s "$link_target" "$link_path"
            echo "  linked: ${skill_name} -> ${link_target}"
        fi
        total_created=$((total_created + 1))
    done

    plugins_processed=$((plugins_processed + 1))
done

# ---------------------------------------------------------------------------
# Verify no broken symlinks across all plugin skills/ directories
# ---------------------------------------------------------------------------
echo
echo "=== Verification ==="

broken_links=()
while IFS= read -r -d '' link; do
    if [[ ! -e "$link" ]]; then
        broken_links+=("$link")
    fi
done < <(find "${REPO_ROOT}/plugins" -path "*/skills/*" -type l -print0)

if [[ ${#broken_links[@]} -gt 0 ]]; then
    echo "BROKEN SYMLINKS FOUND:"
    for bl in "${broken_links[@]}"; do
        echo "  ${bl} -> $(readlink "$bl")"
    done
    total_broken=$((total_broken + ${#broken_links[@]}))
else
    echo "All symlinks valid."
fi

# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------
echo
echo "=== Summary ==="
echo "Plugins processed : ${plugins_processed}"
echo "Plugins skipped   : ${plugins_skipped}"
echo "Symlinks removed  : ${total_removed}"
echo "Symlinks created  : ${total_created}"
echo "Broken/missing    : ${total_broken}"
echo "Skipped plugins   : context-engineering (uses real files)"

if $DRY_RUN; then
    echo
    echo "[dry-run] No changes were made. Re-run without --dry-run to apply."
fi

if [[ $total_broken -gt 0 ]]; then
    exit 1
fi
