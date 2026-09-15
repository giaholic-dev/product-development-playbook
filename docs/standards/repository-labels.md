# Repository Label Standard

## Purpose

Define a consistent, lightweight label strategy that improves filtering, searchability, and automation without duplicating the Playbook's required work-item model.

## Scope

This standard applies when a repository uses labels. Labels are optional implementation metadata; the underlying concepts remain technology-neutral.

## Label Principles

- A label MUST communicate one stable purpose.
- A repository MUST use native fields for concepts that require structured classification, planning, or workflow behavior.
- Labels MAY support discovery, routing, automation, or temporary cross-cutting attention.
- A label MUST NOT be the sole record of Lifecycle Phase, Work Type, workflow state, priority, assignee, iteration, or target date when the repository tracks that concept.
- A repository SHOULD retire labels that no longer have a clear purpose or active use.

## Standard Categories

Repositories MAY use these categories:

| Category | Purpose | Naming pattern |
| --- | --- | --- |
| Area | Identify a durable product, system, or documentation area. | `area:<name>` |
| Kind | Add a lightweight operational signal not represented by Work Type. | `kind:<name>` |
| Attention | Identify a temporary or cross-cutting handling need. | `attention:<name>` |
| Source | Identify the origin of externally reported work when useful. | `source:<name>` |

A repository MUST document the meaning of every label it treats as standard.

## Naming and Color

- Label names MUST use lowercase kebab-case after an optional category prefix.
- A prefix SHOULD be used when more than one category exists or when its purpose would otherwise be unclear.
- Each category SHOULD use a consistent, accessible color family. Color is a visual aid and MUST NOT carry meaning by itself.
- Labels SHOULD have short descriptions where the platform supports them.

## Relationship to the Work-Item Model

Lifecycle Phase and Work Type are required classifications. Workflow State, priority, iteration, and target date are planning or operational fields. Repositories MUST represent those concepts through the mechanisms defined by the [Work Item Taxonomy](work-item-taxonomy.md) and [Repository Project Field Standard](repository-project-field-standard.md), not by labels alone.

A label MAY complement a required field when it expresses a separate concern, such as the affected area or an automation trigger.

## Repository-Specific Extensions

Repositories MAY add labels for local needs when they:

- use an existing category or document a new category;
- do not duplicate a required field's meaning;
- have an owner or review point; and
- are removed when no longer useful.

## References

- [Work Item Taxonomy](work-item-taxonomy.md)
- [Work Item Types](work-item-types.md)
- [Repository Project Field Standard](repository-project-field-standard.md)
- [Repository Milestone Standard](repository-milestones.md)
- [Repository Automation Standard](repository-automation.md)
