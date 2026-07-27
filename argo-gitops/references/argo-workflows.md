# Argo Workflows reference

Official docs:

- https://argo-workflows.readthedocs.io/en/latest/
- https://argo-workflows.readthedocs.io/en/latest/workflow-concepts/
- https://argo-workflows.readthedocs.io/en/latest/fields/
- https://argo-workflows.readthedocs.io/en/latest/workflow-rbac/
- https://argo-workflows.readthedocs.io/en/latest/security/
- https://argo-workflows.readthedocs.io/en/latest/workflow-restrictions/
- https://argo-workflows.readthedocs.io/en/latest/workflow-templates/
- https://argo-workflows.readthedocs.io/en/latest/cron-workflows/

## Core resources

- `Workflow`: one workflow run.
- `WorkflowTemplate`: reusable namespaced workflow template.
- `ClusterWorkflowTemplate`: reusable cluster-scoped template.
- `CronWorkflow`: scheduled workflow.

## Read-only commands first

```bash
argo get <workflow> -n <namespace>
argo logs <workflow> -n <namespace>
argo watch <workflow> -n <namespace>
argo list -n <namespace>
argo template list -n <namespace>
argo template get <template> -n <namespace>
kubectl get workflow,workflowtemplate,cronworkflow -n <namespace>
kubectl describe pod <pod> -n <namespace>
```

Use `kubectl describe` for scheduling, image pull, RBAC, volume, and node-pressure failures. Use `argo logs` for template/script failures.

## Authoring model

Check these fields first:

- `spec.entrypoint`
- template type: `container`, `script`, `steps`, `dag`, `resource`, `suspend`, `http`, `plugin`
- input/output parameters and artifacts
- volume mounts, secrets, artifact repository references
- `serviceAccountName`
- `retryStrategy`, `timeout`, `activeDeadlineSeconds`
- exit handler: `onExit` or lifecycle hooks where needed
- cleanup: TTL, pod GC, volume claim GC

Prefer DAG when dependencies are explicit and fan-out/fan-in matter. Prefer steps for small linear sequences.

## Parameter and output checks

- Pass parameters explicitly between templates.
- Keep output names stable; callers depend on them.
- Check whether outputs come from stdout, files, or artifacts.
- Do not embed secrets in parameters, logs, or artifact paths.
- Avoid relying on outputs from tasks that may be skipped.

## Security and RBAC

For production or multi-user clusters:

- avoid the `default` ServiceAccount
- use workflow-specific ServiceAccounts with minimal RBAC
- minimize executor permissions
- consider `automountServiceAccountToken: false` where Kubernetes API access is unnecessary
- use workflow restrictions and strict/secure template referencing where untrusted users can submit workflows
- set resource requests/limits to avoid noisy-neighbor failures
- avoid broad secret mounts; mount only what a template needs

## CronWorkflow checks

- verify schedule, timezone, and daylight-saving behavior
- check concurrency policy and missed-run behavior
- keep success/failure history bounded
- verify `suspend` live state; do not trust Git alone after manual operations
- set TTL/pod GC so scheduled runs do not accumulate pods forever

## Retry and cleanup

Use retry for transient failures, not broken manifests or deterministic script errors. Always pair retries with bounded backoff and exit criteria. For workflows that create external resources, include cleanup through exit handlers or explicit teardown workflows.
