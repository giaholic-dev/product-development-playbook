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
