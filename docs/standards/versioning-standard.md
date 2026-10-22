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

## Adopted Playbook baseline

An adopting repository MUST identify the Playbook source repository and an immutable adopted revision in its conformance declaration, with the release version/tag when one exists. A branch name or retrieval date alone is insufficient. If adopting an unreleased revision, the record MUST label it as unreleased rather than implying publication. The declaration MUST identify assessment date, accountable owner, applicable standards/local mappings, unresolved gaps, exceptions and the next review condition.

An upgrade MUST compare the previous and proposed immutable baselines, identify changed applicable obligations and affected evidence, and record the adoption decision and required remediation or governed exceptions. Merely pulling source changes or changing a version label does not establish conformance. Preserve historical baseline and migration evidence. Detailed working steps are illustrated by the optional [Playbook Upgrade Guide](../practices/playbook-upgrade-guide.md).

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
