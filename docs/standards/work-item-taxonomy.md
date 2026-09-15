# Work Item Taxonomy

## Purpose

Define the standard taxonomy used to classify and organize work items across projects adopting the Product Development Playbook.

The taxonomy provides a consistent vocabulary for planning, tracking, prioritizing, and reporting work, independently of the project management tool being used.

## Scope

This document defines the classification dimensions used to describe work items throughout the product development lifecycle.

The taxonomy is independent of any specific project management platform and may be implemented using labels, custom fields, issue types, or equivalent mechanisms.

## Work Item Model

A **work item** is a trackable unit of intended work with a stated objective or outcome. Its identity is the work being tracked, not the issue, card, label, or field used to represent it in a tool. A work item may be represented by a tool record, but the record's issue type does not determine the Playbook's conceptual classification.

Each dimension answers a different question:

| Dimension | Question answered |
| --------- | ----------------- |
| Lifecycle Phase | Where in the product lifecycle is the work primarily being addressed? |
| Work Type | What is the primary nature of the work? |
| Artifact Type | What kind of primary artifact is produced, when applicable? |
| Priority | What is the work's relative planning priority? |
| Issue Type | How does the chosen management platform represent the work item? |
| Workflow State | What is the work item's current progress state? |

Lifecycle Phase and Work Type are independent dimensions: a work type does not imply a lifecycle phase, and a phase does not determine the nature of work. Artifact Type describes an output, not the kind of work or its phase. Priority describes relative planning importance, not workflow progress. Issue Type is an implementation choice rather than a Playbook Work Type; Workflow State records progress rather than classification.

This section defines responsibilities only. Primary-classification exceptions, Artifact Type multiplicity, priority decision criteria, and platform-specific field configuration are addressed in later increments and their dedicated standards.

## Primary Classification and Exceptions

A work item MUST have one primary Lifecycle Phase and one primary Work Type. Artifact Type is optional and, when used, records one primary artifact category with an optional subtype as defined by the [Artifact Standard](artifact-standard.md). Priority, Issue Type, and Workflow State use their own rules and do not replace primary classification.

A concern that spans phases or work types SHOULD be represented as related work items when the objectives, owners, or completion evidence differ. A single work item MAY carry an exception only when splitting it would obscure one inseparable objective or materially increase coordination without improving traceability.

A classification exception MUST record:

- the primary classification retained;
- the additional phase or work-type concern;
- why separate linked work items are not appropriate;
- the affected scope and traceability links;
- the owner responsible for reassessment; and
- the condition or date that ends or rechecks the exception.

The exception record follows the Repository Standards exception mechanism. It does not create a new lifecycle phase, Work Type, or Artifact Type.

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

Artifact Type is optional. When it improves planning, reporting, or traceability, it identifies the primary artifact category and optional subtype governed by the [Artifact Standard](artifact-standard.md).

The standard categories are:

- Documentation — optional subtypes include Standard, Practice, Decision Record (ADR), Specification, Guide, and Record
- Template
- Example
- Implementation evidence — optional subtypes include Configuration, Source, Test, and Automation
- External evidence

A work item MAY link additional artifacts without assigning multiple primary Artifact Types.

## Priority

Work items may be assigned a relative execution priority to support planning and scheduling.

The standard priority levels are:

- High
- Medium
- Low

## Workflow State

Workflow state is managed separately from the Playbook taxonomy.

When implemented in GitHub, the native Status field provides the operational state of a work item.

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

- [Repository Standards](repository-standards.md)
- [Work Item Types](work-item-types.md)
- [Product Backlog](product-backlog.md)
- [Project Views](project-views.md)
- [Artifact Standard](artifact-standard.md)
