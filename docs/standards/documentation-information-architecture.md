# Documentation Information Architecture

## Purpose

Define how Playbook-adopting repositories organize documentation by responsibility, so readers can locate maintained content without treating a preferred directory layout as a conformance requirement.

## Scope

This standard governs documentation categories, placement, relationships, and the representation of current and planned content. Writing conventions belong to the [Documentation Style Guide](documentation-style-guide.md); reading paths and links belong to the [Documentation Navigation Standard](documentation-navigation.md). Neither GitHub nor a fixed directory tree is required by this conceptual architecture.

## Category Responsibilities

| Category | Responsibility |
| -------- | -------------- |
| Entry point | State repository purpose, documentation language, current top-level structure, and where primary content is found. |
| Core concepts | Explain enduring purpose, principles, and conceptual boundaries. |
| Lifecycle | Define phase objectives, progression, responsibilities, and exit conditions. |
| Standards | Define reusable rules and the evidence needed to apply them. |
| Practices | Explain optional or recommended ways to carry out the standards without redefining them. |
| Templates | Provide reusable starting material; a template is not the governing rule. |
| Examples | Demonstrate concrete applications without becoming the source of a rule. |
| Supporting automation | Implement or check a process; record tool prerequisites and limitations separately from conceptual rules. |

A repository MUST provide a root entry point and document its applicable categories. It MUST include only categories needed for its purpose; absence of an inapplicable category does not require a placeholder. These responsibilities MAY use different directory names or nesting. A document SHOULD have one primary responsibility and be placed where a reader would expect to find its governing content.

## Placement and Relationships

The entry point MUST distinguish content that exists now from categories or documents planned for later. It MUST NOT present a planned path as an existing destination or create an empty directory solely to satisfy a category list.

Each governed concept MUST have one primary source of truth. Related categories SHOULD refer to that source rather than repeat its rules. Lifecycle documents MAY adopt a standard or link to a practice, but MUST NOT silently redefine the reusable standard. Supporting automation MAY map conceptual responsibilities to a chosen tool; the tool implementation does not make the conceptual method vendor-dependent.

Every maintained document MUST be reachable from the declared documentation architecture or explicitly identified as intentionally standalone with a discoverable reason. The entry point MUST identify where the primary documentation language is declared. Detailed link form, reading order, and reachability checks are owned by the Documentation Navigation Standard; detailed writing style is owned by the Documentation Style Guide.

## Adoption Evidence

A reader can inspect the root entry point and find: the current repository categories and their purposes, planned categories clearly marked as planned, the declared language, and the location of primary content. A change that adds, removes, or moves a category SHOULD update the entry point in the same change.

## References

- [Repository Standards](repository-standards.md)
- [Foundation Phase](../lifecycle/01-foundation.md)
- [Documentation Style Guide](documentation-style-guide.md)
- [Documentation Navigation Standard](documentation-navigation.md)
