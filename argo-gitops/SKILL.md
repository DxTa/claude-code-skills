---
name: argo-gitops
description: Argo CD, ArgoCD, and Argo Workflows GitOps operations for Kubernetes. Use for Argo CD Application, ApplicationSet, AppProject, sync, diff, health, OutOfSync, GitOps repo layout, Helm/Kustomize delivery, Argo Workflows Workflow, WorkflowTemplate, ClusterWorkflowTemplate, CronWorkflow, workflow logs, retry, terminate, and Kubernetes delivery debugging.
---

# Argo GitOps

## Contract

- Read-only first.
- Prefer Git changes or PRs over direct cluster mutation.
- Ask before all mutating commands; production changes also need rollback and verification plan.
- Produce: root cause, smallest safe action, verification, rollback.
- If live cluster and Git disagree, treat Git as desired state unless user says emergency.

## Route

| Intent | Read |
| --- | --- |
| Argo CD app drift, sync, health, ApplicationSet, AppProject | `references/argo-cd.md` |
| Workflow authoring, debugging, templates, cron, retry, logs | `references/argo-workflows.md` |
| Production promotion, rollback, direct mutation, prune/delete/force/replace | `references/gitops-safety.md` |
| Symptom-driven incident triage | `references/troubleshooting.md` |
| Source, license, attribution checks | `references/sources.md` |

## Preflight

Identify before advising or changing:

- kube context, cluster, namespace, target environment
- Argo CD app, AppProject, repo URL, path, revision, source tool: Helm/Kustomize/raw/plugin/OCI
- sync mode: manual or automated; prune, selfHeal, retry, sync windows
- workflow name, WorkflowTemplate/CronWorkflow, service account, controller namespace
- desired state in Git and observed live state

## Mutating Commands Need Confirmation

Ask before running or recommending execution of:

- `argocd app sync`, `argocd app delete`, `argocd app terminate-op`, `argocd app rollback`
- `argo submit`, `argo retry`, `argo resubmit`, `argo terminate`, `argo stop`
- `kubectl apply`, `kubectl delete`, `kubectl patch`, `kubectl replace`
- finalizer edits, prune operations, `Force=true`, `Replace=true`, broad delete/rollback
