# Stateful Recovery and Migration Example

## Fictional scope

Every person, product, identifier, time, number, observation, decision and approval in this example is fictional. Nothing below is an executed backup, restore, migration, environment provision or production release. The example demonstrates the [optional practice](../docs/practices/data-recovery-and-migrations.md) and [record](../templates/stateful-recovery-record.md), not conformance of real infrastructure.

Mara operates the library reservation service from the [end-to-end example](end-to-end-playbook-example.md). This later increment changes persisted reservation representation. The illustrative record uses existing architecture, recovery, deployment and incident responsibilities; it introduces no new mandatory artifact or approval role.

## State and compatibility decision

Reservation IDs, borrower references and accepted reservation changes are authoritative user state. A display cache is reconstructable from them. Provider-managed storage still needs an assessed recovery source/access/retention path; the absence of a self-managed database would not remove the concern.

Candidate `reservation-r2`, migration procedure `migrate-s1-s2-v1` and configuration `test-config-2` are identified together. Immutable artifact references stand for recorded candidate digests in a real adoption; these labels are not actual hashes.

| Application / consumer | State `s1` | State `s2` |
| --- | --- | --- |
| Current `reservation-r1` | Supported read/write. | Unsupported: legacy `status` is absent and new state meanings are not understood. |
| Candidate `reservation-r2` | No ordinary application read/write before migration. | Supported after migration and validation. |
| Migration procedure `migrate-s1-s2-v1` | Reads identified `s1` and preserves stable IDs/borrower relations. | Writes new state fields and records completed work; not a general application client. |

The change removes `status` after mapping it to new state fields. New `s2` values have no supported reverse mapping to `r1`. The record selects forward-only migration; it does not pretend an old image can use `s2`. Delayed `r1` clients/jobs must be stopped or held before migration. External notifications remain in a test sink and are disabled during recovery to avoid duplicate effects.

## Fictional recovery boundaries and protection

| Record field | Fictional decision |
| --- | --- |
| Point/loss boundary | At most 15 minutes of accepted changes could be lost in the assessed failure case; later writes must be reconciled from the retained change journal when available. Mara records the user/operational impact and the authorization required for any actual loss. |
| Time boundary | Restore usable reservation behavior within 60 minutes of the recorded recovery decision, including integrity checks, journal reconciliation and application verification. A failed restore has no successful completion time. |
| Consistent unit | Reservations, borrower references, required format/configuration references and journal checkpoint. The cache can be rebuilt after authoritative state is usable. |
| Method | Restore an identified consistent copy, reconcile accepted journal entries with stable IDs, and use the compatible application/migration sequence. Availability and identity of each input must be checked. |
| Protection | Restricted encrypted recovery copies with a fictional seven-day retention decision; authorized operator access; protected key-access reference `recovery-key-reference`, never its value. Test uses synthetic data and no production credentials. |
| Ownership / Authority | Mara has a scoped Accountable Owner Assignment for recovery readiness. Operator and any promotion/recovery Approver Assignments and Authority are separately recorded; ownership or CI alone grants no new access. |

These values are illustrative, not recommended defaults. A real record would select and verify proportionate boundaries, retention and access for its own risks, including relevant deletion obligations and provider limitations.

## Failed restore and accountable hold

At fictional 10:05, the operator begins restoring synthetic copy `test-copy-A`, identified as a 10:00 `s1` snapshot. The backup checksum passes. At 10:11, integrity checks find 20 reservation rows whose borrower references are missing because the copy did not retain the consistent recovery unit. The application cannot use the restored dataset safely.

Result: failed restoration. Six elapsed minutes is not evidence that the 60-minute restoration objective was met; there is no verified usable endpoint. The advertised snapshot time does not establish acceptable recovered state or loss exposure while linked data is missing.

Mara records the finding, holds `reservation-r2` promotion and assigns repair of copy selection/verification. No exception is accepted and no production migration occurs in this scenario. Re-running the migration or deploying `r1` would not repair missing borrowers. The existing `r1` service and its original state remain unchanged; the isolated failed test resources are retained or disposed of under the fictional test-data record.

## Corrected representative recheck

The corrected procedure selects `test-copy-B`, a consistent synthetic 10:28 copy with 1,000 reservations and their borrower references. Three later accepted synthetic changes are retained in a protected journal through sequence 1003 at fictional failure time 10:30.

| Fictional observation | Result and limit |
| --- | --- |
| 10:30 recovery decision/start; correct copy, format, configuration and journal checkpoint identified. | Scope is this synthetic dataset and procedure, not production scale. |
| Copy restored; stable IDs, borrower references and required constraints checked. | 1,000 consistent reservations before replay; a checksum alone is not the result. |
| Three accepted journal changes replayed with their original IDs and checked for duplicates. | 1,003 reservations at sequence 1003; these simulated later changes are preserved. The copy was two minutes old, but measured loss for the modeled journaled changes is zero after reconciliation. |
| Migration interruption at a recorded checkpoint, followed by controlled resume. | The ledger distinguishes completed IDs and partial work; constraints and counts are rechecked. This is not permission to rerun any arbitrary migration blindly. |
| `r2` reads/writes `s2`; IDs and relationships match; cache rebuild and synthetic reservation behavior verified; notifications stay in the sink. | Compatibility and external-effect checks cover the modeled candidate/configuration and representative inputs only. |
| 10:42 verification completes with usable behavior. | Twelve minutes includes the modeled restore, replay, migration and application checks, within the fictional 60-minute boundary. No real timing measurement occurred. |

The repaired copy/procedure and affected migration/candidate conditions receive the applicable Test validation again. The successful fictional recheck replaces neither the failed observation nor the need to assess production-specific differences and scale. It does not prove that every possible outage meets the objectives.

## Recovery and promotion disposition

The record permits a separately scoped promotion decision only after the relevant evidence and configuration differences are reviewed by an identified Approver with production-promotion Authority. No actual promotion is claimed here. The deployment plan references the consistent-copy/journal prerequisites, paused old jobs, migration sequence, verification and stop points.

If `s2` later becomes unsafe, the planned response is to hold writes and outbound effects, assess the incident, and select a verified compatible forward repair or the recorded restore/replay/re-migration sequence. Restoring an old `s1` copy without reconciling later accepted changes is not loss-free rollback. If the inputs or loss/time boundaries cannot be met, record the failed/inconclusive outcome and accountable next decision rather than expand exposure or silently downgrade requirements. Any exception follows its governing permission and scoped approval; none is manufactured by this example.

Reassessment triggers include changed schema, copy/retention provider, journal coverage, data scale, key-access path, compatibility, objective, material incident or failed restoration. Credential values and real user records do not belong in the evidence.

## Stateless contrast

A separate fictional informational site serves immutable pages/assets and has no forms, user accounts, saved preferences, uploads, queues or provider-managed user records. Its assessed source of truth is the versioned content and deployment configuration; operational access logs have separate security/retention governance and are not an undeclared application database.

The owner records state-specific backup/migration concerns as inapplicable for that scoped runtime, with the inventory and rationale. The site still needs identifiable source/artifact/configuration recovery, the applicable three isolated software environments, candidate validation and scoped promotion approval. It does not need a fictional database or restore test merely to fill a template. Adding saved preferences or a registration provider triggers reassessment. Missing knowledge about external stored state would remain unresolved, not stateless.

## Governing references and evidence classification

- [Rollback Strategy](../docs/standards/rollback-strategy.md#persistent-state-and-recovery-evidence): point/time boundaries, method, restoration evidence and accountable response.
- [Data Model](../docs/standards/data-model.md#state-evolution-and-migration): compatible state/consumer versions, migration and failure/retry/loss evidence.
- [Security, Privacy, and Data Governance](../docs/standards/security-privacy-data-governance.md#recovery-copies-and-restore-data): recovery-copy access, retention and restore data.
- [Software Environments](../docs/standards/software-environments.md) and [Deployment Strategy](../docs/standards/deployment-strategy.md): isolation, candidate/configuration fidelity, promotion and actual execution evidence.
- [Roles and Actor Assignment](../docs/standards/roles-and-actor-assignment.md), [Standards Applicability](../docs/standards/standards-applicability.md), [Incident Management](../docs/standards/incident-management.md): scoped Authority, applicability and incident decisions.

This is conceptual review material. The failed/pass observations, decisions and records are deliberately fictional; no completed template, checklist mark, source example or AI explanation certifies an actual product's recoverability.
