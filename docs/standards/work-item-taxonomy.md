# Work Item Taxonomy

## Purpose

Define the standard taxonomy used to classify and organize work items across projects adopting the Product Development Playbook.

The taxonomy provides a consistent vocabulary for planning, tracking, prioritizing, and reporting work, independently of the project management tool being used.

## Scope

This document defines the classification dimensions used to describe work items throughout the product development lifecycle.

The taxonomy is independent of any specific project management platform and may be implemented using labels, custom fields, issue types, or equivalent mechanisms.

## Lifecycle Phase

Every work item should be associated with exactly one phase of the product development lifecycle.

The standard lifecycle phases are:

- Foundation
- Product
- UX
- Architecture
- Development
- Release
- Maintenance

## Work Type

Every work item should describe a single primary type of work.

The standard work types are:

- Feature
- Bug
- Improvement
- Research
- Technical Debt
- Maintenance

## Artifact Type

Some work items produce a primary project artifact.

When applicable, the artifact should be classified using one of the following types:

- Documentation
- Standard
- Practice
- Template
- Example
- ADR

## Priority

Work items may be assigned a relative execution priority to support planning and scheduling.

The standard priority levels are:

- High
- Medium
- Low

## GitHub Field Mapping

The Work Item Taxonomy is tool-agnostic.

When implemented in GitHub Projects, taxonomy dimensions should reuse native fields whenever they accurately represent the same concept. Custom fields should be introduced only when the native platform does not provide an equivalent.

| Taxonomy Dimension | GitHub Implementation |
| ------------------ | --------------------- |
| Lifecycle Phase | Custom field: **Phase** |
| Work Type | Custom field: **Work Type** |
| Artifact Type | Custom field: **Artifact Type** |
| Priority | Native field: **Priority** |
| Status | Native field: **Status** |
| Assignee | Native field: **Assignees** |
| Iteration *(optional)* | Native field: **Iteration** |
| Target Date *(optional)* | Native field: **Date** |

The Playbook favors native GitHub capabilities over custom fields whenever they provide equivalent semantics. This minimizes duplication while preserving a consistent, tool-independent taxonomy.

## References

- `docs/standards/repository-standards.md`
- `docs/standards/work-item-types.md`
- `docs/standards/project-views.md`
