# Troubleshooting runbooks

Use: symptom → evidence → likely causes → safest next step.

## Argo CD `OutOfSync`

Evidence:

- `argocd app get <app>`
- `argocd app diff <app>`
- `argocd app manifests <app>`
- live object `kubectl get -o yaml`

Likely causes:

- Git changed and sync has not run
- live hotfix drift
- webhook/controller mutates fields
- HPA or another controller owns replicas/status
- Helm/Kustomize rendered different output
- ignored differences too broad or too narrow

Safest next step:

- identify exact differing field and owner
- update Git or narrow ignore rules
- ask before sync/self-heal/prune

## Argo CD `Degraded` or health unknown

Evidence:

- `argocd app resources <app>`
- `kubectl describe` unhealthy resource
- pod events and logs

Likely causes:

- rollout failure, image pull, probe failure
- CRD lacks health assessment
- resource dependency not ready
- RBAC or namespace missing

Safest next step:

- fix resource root cause in Git
- add health customization only when CRD semantics are known

## `SyncFailed` or manifest generation error

Evidence:

- app conditions/events
- repo-server/render error
- Helm/Kustomize command error if reproducible locally

Likely causes:

- missing values file/path
- invalid YAML
- bad Helm dependency or chart version
- Kustomize patch target missing
- CRD absent for dry-run

Safest next step:

- reproduce render locally if possible
- fix desired source
- avoid force/replace until manifest renders cleanly

## Stuck sync, delete, or finalizer

Evidence:

- operation state in `argocd app get`
- resource finalizers and deletion timestamps
- controller logs if available

Likely causes:

- hook/job never completed
- resource deletion blocked by finalizer
- namespace deletion stuck
- controller lost permissions

Safest next step:

- terminate operation or edit finalizer only after explicit confirmation
- record rollback/backout plan first

## ApplicationSet generated wrong or missing Applications

Evidence:

- `kubectl describe applicationset <name> -n <ns>`
- generated Application list
- generator source files/clusters/labels

Likely causes:

- selector too broad/narrow
- Git file glob changed
- template missing required field
- matrix/merge input mismatch
- project/destination disallowed

Safest next step:

- fix generator input or template in Git
- check deletion impact before removing generated apps

## Workflow failed, errored, stuck, or pending

Evidence:

- `argo get <workflow>`
- `argo logs <workflow>`
- `kubectl describe pod <pod>`
- workflow node status/message

Likely causes:

- image pull failure
- bad command/script exit
- missing secret/configmap/PVC
- RBAC denied for ServiceAccount
- unschedulable resources/node selectors
- artifact repository issue

Safest next step:

- fix template/Git first
- retry only for transient infra failure
- resubmit only after confirming template revision

## WorkflowTemplate mismatch after GitOps sync

Evidence:

- Git commit/revision expected by Argo CD
- live `WorkflowTemplate` spec
- workflow creation timestamp and template reference

Likely causes:

- workflow snapshots template at submit time
- Argo CD has not synced latest Git
- controller cache stale
- workflow submitted from old template

Safest next step:

- verify Argo CD synced desired revision
- verify live template has changed field
- submit a new workflow after confirmation

## CronWorkflow skipped, duplicated, or still suspended

Evidence:

- `argo cron get <name>` or `kubectl get cronworkflow <name> -o yaml`
- last scheduled time and active workflows
- timezone/concurrency/history fields

Likely causes:

- timezone or daylight-saving behavior
- concurrency policy blocked run
- `suspend: true` still live
- controller missed schedule during outage
- history/TTL/podGC missing

Safest next step:

- fix CronWorkflow spec in Git
- ask before manual resume/backfill/terminate
