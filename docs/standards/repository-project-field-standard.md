# Repository Project Field Standard

## Purpose

Define how a project may implement the Playbook work-item model in GitHub Projects without making GitHub configuration part of the conceptual taxonomy.

This standard is an implementation mapping. The [Work Item Taxonomy](work-item-taxonomy.md) remains applicable when a project uses another tool.

## Scope

This standard covers a GitHub Projects mapping of the Playbook work-item model. It does not make GitHub configuration a requirement for adopting the conceptual taxonomy.

## Configuration Principles

- A GitHub Project does not automatically contain every field named by this Playbook.
- Use GitHub-provided item metadata when it has the required semantics; do not duplicate it as a custom field.
- Create a project custom field only when the project needs the corresponding Playbook dimension and GitHub does not already provide it.
- Keep required classification distinct from optional planning and reporting information.
- An organization MAY use organization-level issue fields where consistent metadata across its repositories is needed. This is a configuration choice, not a prerequisite for adoption.

## Field Inventory

GitHub Projects can expose built-in or issue-derived metadata such as item title, assignees, issue type, linked pull requests, pull-request reviewers, and workflow status. Availability can depend on the item kind and organization configuration.

GitHub Project custom field types include single select, date, iteration, text, and number. A project creates and names these fields; their presence in one project or template does not imply their presence in another.

## Playbook Mapping

| Playbook concept | GitHub Projects implementation | Adoption requirement |
| --- | --- | --- |
| Lifecycle Phase | Create a **Phase** single-select field. | Required for each tracked work item. |
| Work Type | Create a **Work Type** single-select field. | Required for each tracked work item. |
| Artifact Type | Create an optional **Artifact Category** single-select field; capture an optional subtype in a separate field or the linked artifact record. | Optional. |
| Priority | Create an optional **Priority** single-select field, or use an organization-level issue field with equivalent semantics. | Optional. |
| Workflow State | Use the GitHub Projects **Status** field where available. | Required as an operational workflow choice, not a taxonomy classification. |
| Assignee | Use GitHub issue assignees where applicable. | Optional operational metadata. |
| Issue Type | If the organization uses GitHub issue types, expose **Type** as issue metadata. It does not replace Work Type. | Optional platform mapping. |
| Iteration | Create an **Iteration** field when timebox planning is used. | Optional. |
| Target Date | Create a **Target Date** date field when date-based commitments are used. | Optional. |
| Pull request visibility | Enable **Linked pull requests** and, when useful, **Reviewers**. | Optional view-level metadata. |

## Required Field Definitions

A GitHub Project that tracks Playbook work items MUST create these single-select fields and use the stated values:

| Field | Values |
| --- | --- |
| Phase | Foundation, Product, UX, Architecture, Development, Release, Maintenance |
| Work Type | Feature, Bug, Improvement, Research, Technical Debt, Operational Maintenance |

The project MAY set a default for either field, but it MUST correct the value when the item is classified. Each work item has one primary value in each field. Cross-cutting concerns use the exception record defined by the Work Item Taxonomy rather than multiple values in one field.

## Optional Field Definitions

When a project uses these fields, it MUST preserve the associated Playbook meaning:

| Field | Configuration |
| --- | --- |
| Artifact Category | Documentation, Template, Example, Implementation evidence, External evidence. Record the primary category only; use the Artifact Standard for subtypes and additional linked artifacts. |
| Priority | High, Medium, Low, or an explicitly documented equivalent scale. Priority remains a relative planning decision, not backlog order, urgency, committed sequence, or target date. |
| Iteration | A repeating timebox. Its duration, breaks, and cadence are local planning choices. |
| Target Date | A date-based milestone or commitment; it does not assign priority or workflow state. |

## View Consumption

Project views consume fields for a stated management purpose. A planning view may show Phase, Work Type, Priority, Iteration, and Target Date; an operational view normally shows Status and Assignees; an integration-oriented view may also show Linked pull requests and Reviewers.

A view MUST NOT infer a taxonomy value from its layout, filter, grouping, or sort order. The [Project Views](project-views.md) standard owns view purpose and composition rules.

## References

- [Work Item Taxonomy](work-item-taxonomy.md)
- [Work Item Types](work-item-types.md)
- [Artifact Standard](artifact-standard.md)
- [Project Views](project-views.md)
- [Repository Standards](repository-standards.md)
