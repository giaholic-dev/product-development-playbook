# Release Strategy

## Purpose

Define how a product selects, prepares, communicates, and governs releases without prescribing a delivery platform or cadence.

## Scope

This standard governs the decision framework for a release. It does not replace detailed deployment, rollback, or release-note procedures.

## Release Decision

A release strategy MUST identify:

- the intended audience and the value or obligation served;
- the release scope and explicit exclusions;
- the release identifier or versioning approach;
- the readiness evidence and accountable release decision-maker;
- the communication, observation, and recovery expectations; and
- dependencies, constraints, and accepted risks.

A repository MAY use continuous, scheduled, staged, or event-driven releases when the approach and its suitability are documented.

## Release Readiness

Before publication, the accountable decision-maker MUST verify that the selected increment meets its release conditions, required validation has been completed, material limitations are known, and a proportionate recovery path exists.

A release MAY proceed with accepted residual risk only when the acceptance, owner, rationale, and follow-up are recorded.

## Governance and Evidence

Release evidence MUST be traceable to the released increment. It SHOULD include the release decision, included scope, validation result, release notes, and links to relevant deployment, observation, or recovery records.

## Exceptions

An emergency release MAY use an abbreviated process when delay would create greater risk. The exception MUST record the reason, decision-maker, omitted evidence, and required follow-up review.

## References

- [Release Phase](../lifecycle/06-release.md)
- [Release Notes](release-notes.md)
- [Versioning Standard](versioning-standard.md)
- [Definition of Done](definition-of-done.md)
- [Artifact Standard](artifact-standard.md)
