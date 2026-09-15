# Documentation Navigation Standard

## Purpose

Define how a repository entry point, reading paths, and internal references make maintained documentation discoverable without duplicating its governed content.

## Scope

This standard covers navigation behavior and link verification. [Documentation Information Architecture](documentation-information-architecture.md) owns categories and placement; [Repository Standards](repository-standards.md) owns the repository-level documentation obligation. A repository may implement these rules without GitHub or a prescribed directory layout.

## Entry Point and Reading Paths

The root entry point MUST identify a starting document or a short ordered reading path appropriate to the repository's audience. It MUST link to existing primary lifecycle and standards documents, directly or through a clearly linked index. Supporting scripts and platform-specific mappings MAY be listed as optional technical reading, but MUST NOT become prerequisites for understanding the conceptual method.

A reading path SHOULD start with the project's purpose and foundation, then introduce governing standards before detailed applications. It MAY offer separate paths for distinct audiences. An index MUST distinguish existing content from planned content and MUST NOT publish a link to an absent target merely to represent a future phase.

Each maintained document MUST be reachable from the entry point through a finite sequence of documented links, unless its intentionally standalone status and discoverable reason are declared. Related-document links SHOULD direct readers to the primary source of truth rather than restating a governed rule.

## Lifecycle and Internal References

A lifecycle document SHOULD identify its place in the ordered phases and, where relevant, link to an existing previous or next phase. If a next document is planned but absent, describe it as planned text without a link. Revisiting an earlier phase does not require a second source of that phase's rules.

Use navigable Markdown links for internal references, with file paths relative to the referring document. Code-formatted paths are suitable for literal examples, not for references intended to be followed. Link text SHOULD name the destination's purpose. A reference to an external issue or specification MAY use an absolute URL. Heading fragments MAY be used when they resolve to a maintained heading.

## Link Verification

Before merging a documentation change, the reviewer MUST check its added or modified internal links against the proposed repository tree. Resolve each relative target from the referring file's directory; check that the destination exists and that any heading fragment points to its intended destination. The reviewer SHOULD recheck reachability when the change adds, moves, or removes a document or alters the entry point. The review record MAY cite manual checks or reproducible automation.

A broken internal reference MUST be corrected or identified as a planned destination without a link before the changed document is treated as conformant. Platform-specific link validation MAY automate this verification but does not change the conceptual rule.

## Adoption Evidence

A reader can follow the entry point to the maintained documents, distinguish planned destinations from available ones, and follow related-document links to their governed sources. A review can reproduce the relative-target and heading checks from the changed files and repository tree.

## References

- [Documentation Information Architecture](documentation-information-architecture.md)
- [Repository Standards](repository-standards.md)
- [Foundation Phase](../lifecycle/01-foundation.md)
- [Product Phase](../lifecycle/02-product.md)
