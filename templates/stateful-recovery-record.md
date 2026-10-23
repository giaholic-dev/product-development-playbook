# Stateful Recovery and Migration Record

Optional starting material for linked architecture, recovery, migration or deployment evidence. Use existing records instead when clearer. This template adds no required artifact, universal numeric objective, approval role or exception permission. [Rollback Strategy](../docs/standards/rollback-strategy.md), [Data Model](../docs/standards/data-model.md), [Security, Privacy, and Data Governance](../docs/standards/security-privacy-data-governance.md), [Software Environments](../docs/standards/software-environments.md) and [Deployment Strategy](../docs/standards/deployment-strategy.md) govern the applicable obligations.

## Context, ownership and applicability

- Product/constituent and affected release/candidate/state/configuration identities:
- Accountable owner, decision scope, governing sources and linked work/decision:
- State inventory, authoritative inputs, provider/external dependencies and impact:
- Applicable, inapplicable or unresolved concerns, with evidence and scope:
- If genuinely stateless, rationale and remaining source/artifact/configuration obligations:

For an evidenced stateless scope, omit inapplicable state-specific detail rather than inventing a database, backup or migration. Record unknowns as unresolved, with an owner and next permitted action. Do not fill an unperformed check with an expected result.

## Recovery method and boundaries, when applicable

- Acceptable recovered point/data-loss and restoration-time boundaries, measurement conditions and rationale:
- Consistent recovery unit, source identity/version/format and availability:
- Method, safe target, dependencies/configuration and protected credential/key-access references (no secrets):
- Copy sensitivity, authorized access, retention/deletion and disposal references:
- Recovery decision-maker/operator, scoped Authority and required approval references:
- Stop/disablement, unavailable recovery, irreversible effects and later-write reconciliation treatment:

## Migration compatibility, when applicable

- Source/target state/schema/format and supported producer/consumer or application read/write combinations:
- Sequence, coexistence, delayed clients/jobs and external consumers:
- Transformation, identity/constraint and intended-behavior verification criteria:
- Interruption/partial-progress/retry treatment, recovery alternative and irreversible/loss limits:

## Observed verification

- Real, synthetic, conceptual or hypothetical evidence classification and provenance:
- Candidate/source/state/configuration/procedure identities and source links:
- Isolated target, data authorization/minimization and external-effect controls:
- Operator and start/end timestamps, duration and measurement limits:
- Recovered point/loss/reconciliation evidence, integrity/consistency and consumer/application results:
- Migration and applicable failure/retry results:
- Pass, failed or inconclusive outcome; represent expected behavior separately from observations:
- Evidence location/access/retention/disposal and unresolved risk:

## Decision, handoff and reassessment

- Actual recovery, readiness, exposure or hold decision and rationale:
- Review record and separately scoped approval/Authority, if required:
- Failed/unperformed evidence, accountable remediation and next permitted action:
- Exception only when permitted: governing permission, scope, reason, risk, accountable approval, performed/deferred validation and reassessment:
- Operational/incident handoff, communication and post-recovery reconciliation:
- Reassessment trigger/date and superseded-record links:

The record's existence or a completed template does not establish restoration, validation, approval, production access or completion. Preserve [Roles and Actor Assignment](../docs/standards/roles-and-actor-assignment.md), [Standards Applicability](../docs/standards/standards-applicability.md) and [Repository Standards](../docs/standards/repository-standards.md#exceptions-and-extensions) boundaries.
