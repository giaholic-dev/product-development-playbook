# Versioning Standard

## Purpose

Define how a repository communicates published releases and any explicitly established development version without treating a working-tree label as a release.

## Scope

This standard covers version meaning and change communication for a repository or product. It does not prescribe a release cadence or distribution platform.

## Versioning Approach

A repository MUST choose a versioning approach appropriate to its product type and audience. Semantic Versioning is suitable when consumers depend on compatibility promises. A documentation repository, internal service, or experimental product MAY use another approach when it documents the meaning of its versions.

A version identifies a released or explicitly declared development state; it does not by itself prove completion of a lifecycle phase.

## Published Releases

A published version MUST correspond to a release record and immutable source reference, normally a tag. The release record SHOULD state the included scope, material changes, known limitations, and any relevant migration or compatibility information.

The README MAY link to the latest published release. It MUST NOT present an unpublished development label as the latest release.

## Development Versions

A repository MAY establish a development target separately from the latest published release. When it does, the target MUST be labeled as in development, identify its intended scope or decision boundary, and be updated when the plan materially changes.

If no development target is explicitly established, the README MUST say so or omit it.

## Update Rules

Update version information when:

- publishing a release;
- establishing, changing, or retiring an explicit development target; or
- discovering that reported version information no longer matches the release record.

Do not create a release or tag solely to make an existing document claim true.

## References

- [Repository Standards](repository-standards.md)
- [Branch Workflow](branch-workflow.md)
- [Definition of Done](definition-of-done.md)
