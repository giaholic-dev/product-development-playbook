# Repository Label Standard

## Purpose

Define a consistent, lightweight label strategy that improves filtering, searchability, and automation while preserving the Playbook's required work-item model.

## Scope

This standard applies when a repository uses labels. Labels are optional implementation metadata; the underlying concepts remain technology-neutral.

## Label Principles

- A label MUST communicate one stable purpose.
- A repository SHOULD use suitable native or structured fields when they support its classification and workflow needs; a different representation needs a recorded rationale.
- Labels MAY support discovery, routing, automation, or temporary cross-cutting attention.
- Labels MAY be the primary representation of a tracked dimension only when the repository documents the dimension, allowed values, meaning, and primary record, and preserves the governing classification and workflow rules.
- When an adopted provider mapping requires a field, a label MUST NOT substitute for that field.
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

Lifecycle Phase and Work Type are required classifications. Workflow State and optional planning information retain their own meanings under [Work Item Taxonomy](work-item-taxonomy.md). A classification label can represent a dimension in a documented mapping; it does not define that dimension or make optional information mandatory. A repository MUST keep one identifiable primary record and resolve conflicting representations rather than infer a classification from a view or default label.

The [Repository Project Field Standard](repository-project-field-standard.md) applies when GitHub Projects is adopted for Playbook tracking. Its required Phase and Work Type fields remain mandatory in that context; labels or issue-body text alone do not satisfy them. A repository using issue records or another tracker without adopting GitHub Projects MAY use documented labels or explicit text records instead.

A label MAY complement a required field for discovery or automation when its mapping and synchronization responsibility are explicit. It MUST NOT become a competing source of truth. Local classification-label categories follow the documented-extension rules below.

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
