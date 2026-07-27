# GitOps safety

## Default stance

- Git is desired state and deployment API.
- Diagnose with read-only commands first.
- Prefer PR/revert/tag change/image tag change over direct cluster mutation.
- Direct cluster edits are emergency-only; backport to Git immediately.
- Never hide drift by changing live state without reconciling Git.

## Read-only diagnostic sequence

1. Confirm kube context and namespace.
2. Inspect Argo object state.
3. Compare desired Git revision/path with live object.
4. Identify controller-owned fields, generated resources, and shared resources.
5. Propose smallest safe Git change or operator action.

## Commands that need explicit confirmation

High-risk Argo CD:

- `argocd app sync`
- `argocd app delete`
- `argocd app terminate-op`
- `argocd app rollback`
- sync options involving prune, `Force=true`, `Replace=true`, or resource deletion
- finalizer removal or edits

High-risk Workflows:

- `argo submit`
- `argo retry`
- `argo resubmit`
- `argo terminate`
- `argo stop`

High-risk Kubernetes:

- `kubectl apply`
- `kubectl delete`
- `kubectl patch`
- `kubectl replace`
- editing CRDs, namespaces, RBAC, service accounts, secrets, finalizers

## Rollback patterns

Prefer rollback through Git:

- revert manifest commit
- pin previous chart version, image tag, or Git SHA
- revert ApplicationSet generator input
- restore previous WorkflowTemplate/CronWorkflow spec
- resync Argo CD only after user confirms

Emergency rollback:

- stop stuck Argo CD operation after confirmation
- terminate runaway workflow after confirmation
- scale/patch live object only when user accepts drift and backport plan exists

## Verification after change

Argo CD:

- app reports `Synced` and `Healthy`
- expected Git revision, path, chart version, image, and destination match
- no unexpected `OutOfSync`, shared-resource, or prune candidates remain
- pods are ready and restarts are not increasing

Argo Workflows:

- workflow reaches expected phase, usually `Succeeded`
- failed/pending pods have expected reason resolved
- logs show expected step/template ran
- output parameters/artifacts exist where callers expect them
- CronWorkflow schedule/suspend/concurrency state matches Git

## Production rule

For production, include rollback and verification in same proposal before any mutating command. If rollback cannot be stated, do not mutate yet.
