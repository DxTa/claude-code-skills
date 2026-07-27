# Sources and license boundaries

## Official documentation

Use official docs as source of truth. Prefer version-pinned docs when changing production guidance.

### Argo CD

- Main docs: https://argo-cd.readthedocs.io/en/stable/
- Best practices: https://argo-cd.readthedocs.io/en/stable/user-guide/best_practices/
- Sync options: https://argo-cd.readthedocs.io/en/stable/user-guide/sync-options/
- RBAC: https://argo-cd.readthedocs.io/en/stable/operator-manual/rbac/
- Declarative setup: https://argo-cd.readthedocs.io/en/stable/operator-manual/declarative-setup/
- ApplicationSet deletion: https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/Application-Deletion/

Raw GitHub fallbacks when ReadTheDocs is blocked:

- https://raw.githubusercontent.com/argoproj/argo-cd/master/docs/user-guide/best_practices.md
- https://raw.githubusercontent.com/argoproj/argo-cd/master/docs/user-guide/sync-options.md
- https://raw.githubusercontent.com/argoproj/argo-cd/master/docs/operator-manual/rbac.md

### Argo Workflows

- Main docs: https://argo-workflows.readthedocs.io/en/latest/
- Workflow concepts: https://argo-workflows.readthedocs.io/en/latest/workflow-concepts/
- Fields reference: https://argo-workflows.readthedocs.io/en/latest/fields/
- Workflow RBAC: https://argo-workflows.readthedocs.io/en/latest/workflow-rbac/
- Security: https://argo-workflows.readthedocs.io/en/latest/security/
- Workflow restrictions: https://argo-workflows.readthedocs.io/en/latest/workflow-restrictions/
- WorkflowTemplates: https://argo-workflows.readthedocs.io/en/latest/workflow-templates/
- CronWorkflows: https://argo-workflows.readthedocs.io/en/latest/cron-workflows/

Raw GitHub fallbacks:

- https://raw.githubusercontent.com/argoproj/argo-workflows/main/docs/workflow-rbac.md
- https://raw.githubusercontent.com/argoproj/argo-workflows/main/docs/security.md
- https://raw.githubusercontent.com/argoproj/argo-workflows/main/docs/workflow-restrictions.md

## Third-party research inputs

- `air-gapped/skills` `argo-cd-apps`: https://github.com/air-gapped/skills/tree/main/.claude/skills/argo-cd-apps — MIT. Used as Argo CD topic and safety-pattern input; this skill paraphrases rather than wholesale copies it.
- `TerminalSkills/skills` `argocd`: https://github.com/TerminalSkills/skills/blob/main/skills/argocd/SKILL.md — Apache-2.0. Used as broad checklist only.
- `majiayu000/claude-skill-registry` `argocd`: https://github.com/majiayu000/claude-skill-registry/blob/main/skills/data/argocd/SKILL.md — MIT. Used as registry checklist only.
- `projectbluefin/lab` `argo-workflows`: https://github.com/projectbluefin/lab/blob/main/docs/skills/argo-workflows/SKILL.md — no repo license detected during research. Inspiration only; do not copy text, examples, or files without license clearance.

## Copying rule

If substantial third-party text is copied later, add the required license notice here or create `third-party-notices.md`. Prefer paraphrase from official docs instead.
