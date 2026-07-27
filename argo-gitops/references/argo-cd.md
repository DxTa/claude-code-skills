# Argo CD reference

Official docs:

- https://argo-cd.readthedocs.io/en/stable/
- https://argo-cd.readthedocs.io/en/stable/user-guide/best_practices/
- https://argo-cd.readthedocs.io/en/stable/user-guide/sync-options/
- https://argo-cd.readthedocs.io/en/stable/operator-manual/rbac/
- https://argo-cd.readthedocs.io/en/stable/operator-manual/declarative-setup/
- https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/Application-Deletion/

## Core resources

- `Application`: desired source, destination, project, sync policy.
- `ApplicationSet`: generator plus template that creates many Applications.
- `AppProject`: tenancy boundary for repos, destinations, resource kinds, roles, sync windows.

## Read-only commands first

```bash
argocd app get <app>
argocd app diff <app>
argocd app history <app>
argocd app manifests <app>
argocd app resources <app>
kubectl get application,applicationset,appproject -A
kubectl describe application <app> -n <argocd-namespace>
```

Use `--refresh` or hard refresh only when stale cache is plausible; do not use sync as diagnostic shortcut.

## Source patterns

Check which source mode is active before editing:

- raw directory: path contains Kubernetes YAML/Jsonnet/plugin output
- Helm chart from repo, Git, or OCI
- Kustomize overlay
- OCI manifest bundle
- multi-source app, often chart plus `$values` repo
- config management plugin

Prefer pinned chart versions, image tags/digests, or Git SHAs for production. Floating branches and remote bases can create silent drift.

## Sync policy

Review before proposing sync:

- manual vs `automated`
- `prune`: may delete resources no longer in Git
- `selfHeal`: may undo live hotfixes
- retry/backoff: may hide repeated bad manifests
- sync waves/hooks: ordering and migration jobs
- sync windows: deployment calendar gate
- sync options: server-side apply, create namespace, prune behavior

Treat `Force=true`, `Replace=true`, deletion finalizers, and prune as destructive. Prefer safer options such as confirming prune/delete and `FailOnSharedResource=true` where applicable.

## ApplicationSet safety

Before changing generators/templates:

- confirm generator input scope: clusters, Git dirs/files, list, matrix, merge, PR/SCM
- preview names/destinations if possible
- check `goTemplate` missing-key behavior when templating critical fields
- understand deletion cascade: deleting ApplicationSet can delete Applications and managed resources unless preservation is configured
- avoid templating `project` from untrusted input in multi-tenant setups

## AppProject and RBAC

For multi-tenant clusters:

- avoid broad `default` project for real teams
- restrict `sourceRepos`
- restrict `destinations`
- restrict cluster-scoped and namespace-scoped resource kinds
- define project roles intentionally
- verify logs/access permissions separately where required
- keep secrets out of Application manifests; use secret managers or references

## Common authoring checks

- `metadata.namespace` is Argo CD namespace unless using applications-in-any-namespace intentionally
- destination namespace exists or `CreateNamespace=true` is intentional
- Helm values file paths match repo layout
- Kustomize overlay path exists
- app name and instance labels do not collide with other controllers
- ignored differences are narrow and documented
- repo credentials and project allowlists permit source/destination
