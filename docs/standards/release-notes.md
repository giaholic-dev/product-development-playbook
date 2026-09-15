# Release Notes

## Purpose

Define the minimum information that communicates a released increment accurately to its intended audience.

## Scope

Release notes describe what changed in a specific release. They do not replace implementation history, operational runbooks, or backlog records.

## Required Content

Release notes MUST identify:

- the release name, version, or other stable identifier;
- publication date or release reference;
- the intended audience;
- material additions, changes, fixes, and removals relevant to that audience;
- known limitations, compatibility implications, and required action when applicable; and
- links to authoritative migration, support, or recovery information when needed.

Content MUST distinguish completed changes from planned or experimental work. Avoid claims that cannot be supported by the released scope.

## Audience and Detail

The author MUST adapt detail and vocabulary to the intended reader. User-facing notes SHOULD emphasize impact and action. Technical or operational notes MAY include implementation, compatibility, or deployment detail when it is needed to use or support the release.

A release with no audience-relevant change MAY use a concise note that states the release purpose and its stable identifier.

## Publication and Corrections

Release notes MUST be published with or be traceably linked to the release record. Corrections MUST preserve the released identifier and explain the material correction when it could affect reader decisions.

## References

- [Release Phase](../lifecycle/06-release.md)
- [Release Strategy](release-strategy.md)
- [Versioning Standard](versioning-standard.md)
- [Artifact Standard](artifact-standard.md)
