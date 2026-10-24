# Playbook Upgrade Guide

## Purpose and scope

Illustrate a proportionate adoption or upgrade review under [Versioning](../standards/versioning-standard.md#adopted-playbook-baseline), [Repository Standards](../standards/repository-standards.md#conformance-declaration) and [Standards Applicability](../standards/standards-applicability.md). This optional procedure does not replace those sources or create a new mandatory artifact.

## Select and preserve a baseline

Record the source repository, release/tag and resolved immutable commit. When selecting main, record its exact commit and label it unreleased. A closed milestone, integrated PR or development target is not a published release. Preserve the previously adopted baseline and evidence before changing the declaration. A new adopter records that no previous baseline exists.

Read the release information and compare both source revisions. Version numbers alone do not enumerate obligations or demonstrate compatibility. Record uncertainty when release information or immutable source evidence is unavailable.

## Assess the change

Identify changed governing sources and their impact on the repository's product boundary, local mappings, work in progress, evidence, tools and permissions. Apply each source's scope; distinguish an unmet requirement from inapplicability. Review navigation, templates and examples as supporting material rather than additional policy owners.

For executable or served software, explicitly assess [Software Environments](../standards/software-environments.md): three existing, distinct Development, Test and Production contexts, verified isolation before implementation, same-candidate promotion, scoped approval and verification/recovery evidence. Names or planned tasks are insufficient. Existing adopters record current gaps and accountable remediation; further production promotion follows that source's requirements or its governed exception treatment. A methodology-only repository's supporting utilities do not by themselves create a runtime product.

One lightweight comparison record can use:

| Changed source/obligation | Applicable scope and rationale | Existing evidence or gap | Remediation owner and dependency | Verification / exception reference |
| --- | --- | --- | --- | --- |
| Software Environments | Runtime product, if present | Actual provisioning and isolation observations, or explicit gap | Assigned environment preparation work | Candidate, Test, approval, Production and recovery evidence |
| Classification representation | Selected work-tracking mapping | Required Project fields, or documented equivalent outside that mapping | Mapping owner | Actual field/record observations; issue text does not mutate Project fields |

These are assessment examples, not completed evidence or a universal checklist of every upgrade.

## Prepare, decide and verify

Create bounded work for material gaps with owners, acceptance evidence and dependencies. Apply existing readiness, review and completion rules. Record any permitted exception with scope, risk, approval and reassessment; an exception is not evidence that the affected requirement was met.

The accountable adoption decision identifies the exact new baseline, assessment evidence, completed remediation, remaining obligations, exceptions and next review condition. Do not claim unqualified conformance while known obligations remain unmet. The governing source determines which activity can proceed; an upgrade record does not authorize bypassing an entry or promotion gate.

Update the conformance declaration and affected local documents, then check that their baseline, issues, milestone and release information agree. Preserve the previous assessment and actual outcomes. Verify links and applicable automation; a green check proves only its declared scope. Reassess when the selected source or material operating context changes.

## Methodology repository version meaning

The Playbook repository's current 0.x sequence names reviewed methodology baselines, not a promise that existing adopters automatically remain conformant. Assess changed obligations even for a minor 0.x increment. The remediation plan's v0.6.0, v0.7.0 and v0.8.0 are planned release boundaries until their release records and immutable references are published. Historical v0.1.0 publication remains separate from later milestone acceptance and main development.

## References

- [Conformance Declaration Template](../../templates/conformance-declaration.md)
- [Repository Conformance Declaration](repository-conformance-declaration.md)
- [Playbook Remediation Plan](playbook-remediation-plan.md)
- [Definition of Ready](../standards/definition-of-ready.md)
- [Definition of Done](../standards/definition-of-done.md)


## Audit exporter upgrade candidate — v0.7.0

The [v0.7.0 candidate](../releases/v0.7.0.md) preserves v0.6.0 governing standards while upgrading optional audit coverage. Tool version 2.1.0 and package schema 2.0.0 are separate from the Playbook's 0.x release numbering. Keep old packages unchanged; use the current verifier only for supported version pairs and run a fresh explicitly authorized export for new coverage. Review committed-source sensitivity, selected repository/Project, authorized read scope and local retention/disclosure before running. A source hash is not secret detection, and a complete observable package is not provider-administration, approval or conformance certification. Preserve the prior adopted release until publication and the candidate's immutable identity are verified; record the scoped upgrade decision and remaining limits. Stateful recovery/migration obligations are excluded from the audit-only candidate and remain the separately governed M8 target.
