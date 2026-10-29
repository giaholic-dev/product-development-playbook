# Playbook Upgrade Guide

## Purpose and scope

Illustrate a proportionate adoption or upgrade review under [Versioning](../standards/versioning-standard.md#adopted-playbook-baseline), [Repository Standards](../standards/repository-standards.md#conformance-declaration) and [Standards Applicability](../standards/standards-applicability.md). This optional procedure does not replace those sources or create a new mandatory artifact.

## Select and preserve a baseline

Record the source repository, release/tag and resolved immutable commit. When selecting main, record its exact commit and label it unreleased. A closed milestone, integrated PR or development target is not a published release. Preserve the previously adopted baseline and evidence before changing the declaration. A new adopter records that no previous baseline exists.

Read the release information and compare both source revisions. Version numbers alone do not enumerate obligations or demonstrate compatibility. Record uncertainty when release information or immutable source evidence is unavailable.

## Assess the change

Identify changed governing sources and their impact on the repository's product boundary, local mappings, work in progress, evidence, tools and permissions. Apply each source's scope; distinguish an unmet requirement from inapplicability. Review navigation, templates and examples as supporting material rather than additional policy owners.

For executable or served software, explicitly assess [Software Environments](../standards/software-environments.md): three existing, distinct Development, Test and Production contexts, verified isolation before implementation, same-candidate promotion, scoped approval and verification/recovery evidence. Names or planned tasks are insufficient. Existing adopters record current gaps and accountable remediation; further production promotion follows that source's requirements or its governed exception treatment. A methodology-only repository's supporting utilities do not by themselves create a runtime product.

For material persistent state, assess [Rollback Strategy](../standards/rollback-strategy.md#persistent-state-and-recovery-evidence) and [Data Model](../standards/data-model.md#state-evolution-and-migration): recovered point/loss and restoration-time boundaries, compatible restoration, migration sequencing, failure/retry and later-write reconciliation evidence. Include local-only and provider-managed authoritative state. A genuinely stateless scope records its state/authority rationale; missing knowledge or a failed restore remains unresolved or a gap. Review recovery-copy access/retention and isolated verification under data governance and Software Environments. Preserve prior actual outcomes and identify accountable remediation or permitted exception before relying on future material stateful readiness; never backfill fictional historical tests. The [optional practice](data-recovery-and-migrations.md) and [record](../../templates/stateful-recovery-record.md) support existing primary owners without creating mandatory new artifacts.

One lightweight comparison record can use:

| Changed source/obligation | Applicable scope and rationale | Existing evidence or gap | Remediation owner and dependency | Verification / exception reference |
| --- | --- | --- | --- | --- |
| Software Environments | Runtime product, if present | Actual provisioning and isolation observations, or explicit gap | Assigned environment preparation work | Candidate, Test, approval, Production and recovery evidence |
| Stateful recovery / migration | Material persistent state or evidenced stateless boundary | Representative restore/compatibility evidence, or explicit gap | Recovery/data owner and dependent release work | Point/time/loss, failed/inconclusive checks, governed exception and reassessment |
| Classification representation | Selected work-tracking mapping | Required Project fields, or documented equivalent outside that mapping | Mapping owner | Actual field/record observations; issue text does not mutate Project fields |

These are assessment examples, not completed evidence or a universal checklist of every upgrade.

## Prepare, decide and verify

Create bounded work for material gaps with owners, acceptance evidence and dependencies. Apply existing readiness, review and completion rules. Record any permitted exception with scope, risk, approval and reassessment; an exception is not evidence that the affected requirement was met.

The accountable adoption decision identifies the exact new baseline, assessment evidence, completed remediation, remaining obligations, exceptions and next review condition. Do not claim unqualified conformance while known obligations remain unmet. The governing source determines which activity can proceed; an upgrade record does not authorize bypassing an entry or promotion gate.

Update the conformance declaration and affected local documents, then check that their baseline, issues, milestone and release information agree. Preserve the previous assessment and actual outcomes. Verify links and applicable automation; a green check proves only its declared scope. Reassess when the selected source or material operating context changes.

## Methodology repository version meaning

The Playbook repository's current 0.x sequence names reviewed methodology baselines, not a promise that existing adopters automatically remain conformant. Assess changed obligations even for a minor 0.x increment. The remediation plan's v0.6.0, v0.7.0 and v0.8.0 have verified publication records; later research is not a new versioned baseline until separately selected, reviewed and published. Historical v0.1.0 publication remains separate from later milestone acceptance and main development.

## References

- [Conformance Declaration Template](../../templates/conformance-declaration.md)
- [Repository Conformance Declaration](repository-conformance-declaration.md)
- [Playbook Remediation Plan](playbook-remediation-plan.md)
- [Definition of Ready](../standards/definition-of-ready.md)
- [Definition of Done](../standards/definition-of-done.md)


## Audit exporter upgrade — v0.7.0

The [published v0.7.0 baseline](../releases/v0.7.0.md) preserves v0.6.0 governing standards while upgrading optional audit coverage. Tool version 2.1.0 and package schema 2.0.0 are separate from the Playbook's 0.x release numbering. Keep old packages unchanged; use the current verifier only for supported version pairs and run a fresh explicitly authorized export for new coverage. Review committed-source sensitivity, selected repository/Project, authorized read scope and local retention/disclosure before running. A source hash is not secret detection, and a complete observable package is not provider-administration, approval or conformance certification. Use immutable v0.7.0 source `6901304985b36ecfb842d519d5ddb636f5f05698`, preserve the prior adopted release and record the scoped upgrade decision and remaining limits. Stateful recovery/migration obligations are excluded from the v0.7.0 audit-only baseline and introduced by the separately reviewed [v0.8.0 release](../releases/v0.8.0.md); assess the changed clauses and preserve actual evidence before recording adoption.

## Unreleased validation corrections — 2026-10-29

The [AP11 acceptance record](validation-reliability-acceptance-2026-10-29.md) identifies unreleased adopted source `9ac4f6027095ceeb54f425bb7333c15bec678d2d`, changes since v0.8.0, actual tests/limits and deferred work. This is not a new release. Keep the old adopted source and historical evidence. Current temporal validation may reject previously accepted malformed evidence without a schema change; record the failure and obtain separately authorized fresh observations if needed, never invented dates or a relabelled archive. A historical manifest's true flag is not a successful current verification. Also assess first-definition Markdown semantics and the documented root-relative output exclusions before relying on the corrected checker. An adopter needs its own scoped assessment; this repository's acceptance does not certify other products or real archives.

