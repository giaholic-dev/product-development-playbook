# Artifact Standard

## Purpose

Define what an artifact is, how it provides evidence of work, and how artifact types are classified without conflating an artifact with a work item, workflow state, or platform record.

## Scope

An **artifact** is an inspectable record, deliverable, or durable result created, adopted, or materially changed by product work. It may be a document, source-controlled configuration, decision record, template, example, or another medium appropriate to the product.

This standard governs artifact identity, type hierarchy, multiplicity, ownership, and evidence. It does not prescribe a directory layout, tool, file format, or lifecycle phase. The [Work Item Taxonomy](work-item-taxonomy.md) may reference an Artifact Type when an artifact is relevant to tracking the work.

## Artifact Model

A work item MAY produce no artifact, one primary artifact, or multiple artifacts. Where a work item is classified with Artifact Type, the field describes its primary intended artifact; additional artifacts SHOULD be recorded through links or equivalent traceability rather than by assigning conflicting primary types.

An artifact MAY be created before, during, or after the work item it evidences. It does not determine Work Type, Lifecycle Phase, Priority, Issue Type, or Workflow State.

Each governed artifact MUST have a discoverable primary source of truth. If an artifact is intentionally temporary, generated, or external, the responsible work item or governing document MUST identify its location or the reason it is not retained.

## Type Hierarchy

Artifact Type uses a category and optional subtype. A repository MAY extend the subtype list when it preserves these category meanings.

| Category | Optional subtype | Purpose |
| --- | --- | --- |
| Documentation | Standard, Practice, Decision Record (ADR), Specification, Guide, Record | Communicates or governs a concept, decision, process, or state. |
| Template | — | Provides reusable starting material without becoming the governing rule. |
| Example | — | Demonstrates an application of a rule or concept without defining it. |
| Implementation evidence | Configuration, Source, Test, Automation | Records an implemented technical or operational result. |
| External evidence | — | Identifies evidence retained outside the repository, with a discoverable location or reference. |

A **Standard** and a **Practice** are Documentation subtypes. An **ADR** is the established name for a Decision Record subtype. A type MUST NOT be used both as a category and as its own subtype.

## Ownership and Evidence

The artifact's primary owner is the document, repository location, or external system that maintains it. The work item that creates or changes it SHOULD link to that owner. Artifact classification is optional when it adds no useful planning, reporting, or traceability value.

A project can demonstrate conformance by showing that each governed artifact has a discoverable source, an appropriate category, and links from relevant work or decision records when traceability is required.

## References

- [Repository Standards](repository-standards.md)
- [Terminology Standard](terminology-standard.md)
- [Work Item Taxonomy](work-item-taxonomy.md)
- [Work Item Types](work-item-types.md)
- [Documentation Information Architecture](documentation-information-architecture.md)
