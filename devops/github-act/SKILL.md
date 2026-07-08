---
name: github-act
description: Test GitHub Actions locally with nektos/act through the GitHub CLI extension `gh act`. Use when running, debugging, listing, or simulating GitHub Actions workflows on a local machine; when a user mentions `gh act`, nektos/act, local Actions testing, `.actrc`, event payloads, workflow_dispatch inputs, local CI reproduction, GitHub Enterprise/GHE remotes such as `*.ghe`, or testing `.github/workflows/*.yml` before pushing. Proactively detect repo remote host and add `--github-instance` when origin uses a `*.ghe` domain.
disable-model-invocation: true
---

# GitHub Act

Use `gh act` to run GitHub Actions workflows locally through the nektos/act GitHub CLI extension.

## Setup Check

Run these checks from repository root before debugging workflows:

```sh
cd "$(git rev-parse --show-toplevel)"
test -d .github/workflows
gh --version
gh auth status
gh extension list | grep -E 'nektos/gh-act|gh-act'
gh act -h
docker info >/dev/null
```

If extension is missing, install it with the docs command:

```sh
gh extension install https://github.com/nektos/gh-act
```

If `docker info` fails, start Docker Desktop, Colima, OrbStack, or the configured Docker daemon before running `gh act`.

After installation, call act through `gh`:

```sh
gh act push
gh act -l pull_request
```

## Proactive GHE Detection

Before forming any `gh act` command, inspect the repo remote host. If `origin` uses a `*.ghe` domain, add `--github-instance <host>` to every `gh act` invocation.

```sh
origin_url="$(git remote get-url origin)"
repo_host="$(
  printf '%s\n' "$origin_url" |
  sed -E 's#^[a-zA-Z]+://([^/:]+).*#\1#; s#^[^@]+@([^:]+):.*#\1#'
)"

case "$repo_host" in
  *.ghe) echo "Use: --github-instance $repo_host" ;;
  *) echo "No GHE instance flag needed" ;;
esac
```

GHE run pattern:

```sh
gh act pull_request --github-instance "$repo_host" -W .github/workflows/ci.yml -j test
```

If GHE requires auth, `act` uses `GITHUB_TOKEN`. Prefer secure prompt:

```sh
gh act pull_request --github-instance "$repo_host" -s GITHUB_TOKEN
```

Or pass the token from `gh` without writing the secret into shell history:

```sh
GITHUB_TOKEN="$(gh auth token --hostname "$repo_host")" \
  gh act pull_request --github-instance "$repo_host" -s GITHUB_TOKEN
```

## Local Test Workflow

1. Inspect workflows under `.github/workflows/`.
2. Pick event, workflow file, and job instead of running everything blindly.
3. List matching jobs first.
4. Run smallest useful job with needed payload, vars, and secrets.
5. Compare local failure with GitHub-hosted behavior before editing workflow logic.

Common commands:

```sh
# Docs default to push when no event is passed. Prefer explicit events.
gh act push

# Run specific events.
gh act push
gh act pull_request
gh act schedule

# List jobs for event.
gh act -l pull_request

# Run one workflow file and one job.
gh act push -W .github/workflows/ci.yml -j test

# Run all workflows in directory for push.
gh act push -W .github/workflows/
```

## Event Payloads

Use `-e <file>` when workflow logic reads `github.event.*` or needs fields not inferable from local git state.

Pull request payload minimum:

```json
{
  "pull_request": {
    "head": { "ref": "feature-branch" },
    "base": { "ref": "main" }
  }
}
```

Run it:

```sh
gh act pull_request -e event.json
```

Tag push payload:

```json
{
  "ref": "refs/tags/v1.2.3"
}
```

Manual `workflow_dispatch` payload:

```json
{
  "inputs": {
    "NAME": "Manual Workflow",
    "SOME_VALUE": "ABC"
  }
}
```

Run it:

```sh
gh act workflow_dispatch -e payload.json
```

For simple workflow dispatch inputs, use:

```sh
gh act workflow_dispatch --input NAME='Manual Workflow' --input SOME_VALUE=ABC
gh act workflow_dispatch --input-file .act/inputs.env
```

## Vars, Secrets, and Token

Repository variables:

```sh
gh act --var NODE_ENV=test
gh act --var-file .act/vars.env
```

Secrets:

```sh
# Preferred for sensitive values: secure prompt; avoids shell history.
gh act -s MY_SECRET

# Load dotenv-style file. Keep out of git.
gh act --secret-file .act/secrets.env
```

`GITHUB_TOKEN` is not auto-created locally. If workflow needs it:

```sh
# Secure prompt, safest for history.
gh act -s GITHUB_TOKEN

# Convenient, but token may enter shell history depending shell config.
gh act -s GITHUB_TOKEN="$(gh auth token)"
```

Never commit `.act/secrets.env`. Add local act files to `.gitignore` when creating them:

```gitignore
.act/secrets.env
.act/*.secrets
.act/vars.env
.act/*.local.env
.act/*payload*.json
.artifacts/
```

## `.actrc` Defaults

Use `.actrc` for repeated local flags. Act reads arguments in order: XDG config, home `.actrc`, cwd `.actrc`, CLI args. Format: one argument per line, no comments.

Useful project `.actrc`:

```text
--container-architecture=linux/amd64
```

Use `--container-architecture=linux/amd64` on Apple Silicon when runner images or actions expect amd64. Add `--action-offline-mode` only after actions and images have been cached by at least one online run.

## Matrix Selection

Narrow matrix jobs with `--matrix key:value`; repeat flag for multiple dimensions.

```sh
gh act push -W .github/workflows/ci.yml -j test --matrix node:20
gh act push --matrix node:20 --matrix os:ubuntu-latest
```

`--matrix` only selects values already present in workflow matrix. It cannot add new matrix values. Workflow `exclude` rules still win.

## Skipping Local-Unsafe Work

For steps, use act's `ACT` environment variable:

```yaml
- name: Publish release
  if: ${{ !env.ACT }}
  run: ./scripts/publish.sh
```

For whole jobs, do not use `env.ACT` in a job-level `if`. Add a custom event property instead:

```yaml
jobs:
  deploy:
    if: ${{ !github.event.act }}
    runs-on: ubuntu-latest
    steps:
      - run: ./scripts/deploy.sh
```

Use payload:

```json
{ "act": true }
```

Run:

```sh
gh act push -e event.json
```

## Artifacts and Offline Mode

Enable local artifact upload/download support when workflows use `actions/upload-artifact` or `actions/download-artifact`:

```sh
gh act push --artifact-server-path "$PWD/.artifacts"
```

Use offline mode after at least one successful online run to reuse cached actions/images and reduce registry/network flakiness:

```sh
gh act --action-offline-mode
```

## Troubleshooting Pattern

1. Reproduce with narrow scope:

   ```sh
   gh act pull_request -W .github/workflows/ci.yml -j test -e event.json
   ```

2. Add only required vars/secrets.
3. If action download or image pull is flaky, retry once online, then use `--action-offline-mode`.
4. If artifacts are blank or unavailable, add `--artifact-server-path "$PWD/.artifacts"`.
5. If local run differs from GitHub, check event payload, runner image/architecture, unavailable secrets, job-level skip conditions, and services requiring Docker/network behavior. If a command exists on GitHub-hosted runners but not locally, check the act runner image and use `-P ubuntu-latest=<image>` or document a project-specific platform mapping in `.actrc`.
6. Treat `gh act` as fast local feedback, not final CI authority. Still verify critical workflow changes on GitHub Actions.

## Safety Rules

- Prefer `-j <job>` and `-W <workflow>` before running all workflows.
- Do not run deploy/release jobs locally unless workflow explicitly guards them for act.
- Prefer secure secret prompt (`-s NAME`) over inline secret assignment.
- Keep local payloads, vars, secrets, and artifacts out of git unless intentionally shared and non-sensitive.
