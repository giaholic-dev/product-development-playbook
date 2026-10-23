# Rollback Strategy

## Purpose

Define how a product restores a safe, acceptable state when a release or deployment does not meet its conditions.

## Scope

This standard governs rollback decisions, preparation, execution, and evidence. It does not prescribe a specific recovery mechanism or replace incident management.

## Rollback Readiness

For a release with material operational risk, the responsible party MUST define before deployment:

- the conditions that trigger rollback assessment;
- the accountable rollback decision-maker;
- the safe target state and recovery method;
- the evidence required to decide and verify recovery;
- the communication responsibilities; and
- the follow-up work required after a rollback.

The recovery method MAY be a prior release, a compensating change, controlled disablement, or another documented safe state.

## Persistent State and Recovery Evidence

Before relying on recovery readiness for a release, the responsible party MUST assess material persistent state and its authoritative source, affected scope, dependencies and credible loss or availability impact. The assessment includes applicable local-device, file, database, queued/event and provider-managed state; absence of a self-managed database does not establish statelessness.

For material persistent state, the recovery record MUST identify:

- the acceptable recovered point or data-loss boundary and restoration-time boundary, their measurement conditions and impact-based rationale;
- the consistent recovery unit, identified recovery source/method, safe target and required configuration, access, retention or dependency prerequisites;
- the accountable recovery decision-maker, authorized operator and verification criteria; and
- the disposition of unavailable recovery, unmet objectives, irreversible effects and subsequent legitimate changes requiring reconciliation.

The method MAY use backup/restore, authoritative replay, reconstruction, provider-supported recovery, or an explicitly authorized loss/disablement strategy within the accepted boundary. This standard does not require a particular database, provider, tool, backup schedule or universal numeric objective. A prior executable or source revision MUST NOT be treated as sufficient recovery evidence unless its compatibility with the affected state and safe target is demonstrated. Reverting software does not by itself reverse a schema change, restore deleted data or undo external effects.

Before a recovery method is relied on for a material stateful release, representative restoration or reconstruction verification MUST demonstrate that the required state can be recovered and used within the recorded boundary, or an applicable governed exception MUST identify the unverified obligation and risk. Evidence MUST identify the source/version or format, procedure, isolated target, operator, timestamps/duration, recovered point or loss boundary, relevant integrity/consistency and application-compatibility checks, result and unresolved risk. A backup's existence, successful job, checksum or provider claim alone is not restoration verification.

Verification data, environment isolation and privileged recovery-task access MUST follow [Software Environments](software-environments.md) and [Security, Privacy, and Data Governance](security-privacy-data-governance.md). Evidence MUST reference credentials or key-access prerequisites without exposing secret values. A restore exercise does not itself grant production access or promotion Authority.

A genuinely stateless product or constituent MUST record why no material persistent application state requires restoration or migration, including relevant state/authority and reconstruction assumptions. No database backup or data-migration obligation is imposed solely to fill that record. Applicable source/artifact/configuration recovery and other governing obligations remain. Unavailable recovery, missing evidence or unknown state is a gap or unresolved determination, not stateless inapplicability; [Standards Applicability](standards-applicability.md) governs that distinction.

Reassess the affected recovery evidence when state, format/schema, provider/dependencies, retention, method, objectives or material risk changes, and after a failed recovery or material incident. Material schema/data evolution and application/state compatibility follow [Data Model](data-model.md). Exceptions MUST use the applicable permission and recorded scope, reason, risk, accountable approval, validation and reassessment under [Repository Standards](repository-standards.md#exceptions-and-extensions); a recovery record does not create exception or production-promotion Authority.

## Decision and Execution

Rollback MUST be considered when release verification or observation shows that the agreed release conditions are not met and mitigation cannot restore an acceptable state within the applicable risk boundary.

The decision, rationale, affected release, execution result, and verification outcome MUST be recorded. A rollback MUST not obscure the evidence needed to understand the release outcome.

## Follow-up

After a rollback, record the customer or operational impact, unresolved risk, and accountable follow-up. A subsequent release MUST not reuse the failed approach without reassessing the relevant evidence and conditions.

## References

- [Release Phase](../lifecycle/06-release.md)
- [Release Strategy](release-strategy.md)
- [Deployment Strategy](deployment-strategy.md)
- [Incident Management](incident-management.md)
- [Definition of Done](definition-of-done.md)
- [Artifact Standard](artifact-standard.md)
- [Data Model](data-model.md)
- [Software Environments Standard](software-environments.md)
- [Security, Privacy, and Data Governance Standard](security-privacy-data-governance.md)
- [Standards Applicability](standards-applicability.md)
- [Roles and Actor Assignment Standard](roles-and-actor-assignment.md)
