# Data Recovery and Migrations

## Purpose and authority

Help a small product apply the state-specific rules without creating another standard, approval gate or required document. O03 / [#334](https://github.com/giaholic-dev/product-development-playbook/issues/334) follows the [O01 decision](stateful-recovery-decision.md) and O02's integration into the existing primary owners.

[Rollback Strategy](../standards/rollback-strategy.md#persistent-state-and-recovery-evidence) owns recovery readiness and restoration evidence; [Data Model](../standards/data-model.md#state-evolution-and-migration) owns compatibility and migration evidence. [Security, Privacy, and Data Governance](../standards/security-privacy-data-governance.md#recovery-copies-and-restore-data), [Software Environments](../standards/software-environments.md) and [Deployment Strategy](../standards/deployment-strategy.md) retain their data, isolation, promotion and execution responsibilities. This guide does not waive those sources.

## A compact working sequence

1. Identify the affected state and its authoritative inputs. Include local-only or provider-managed data and linked files/queues where they materially affect recovery. Distinguish reconstructable caches from irreplaceable records.
2. Record applicable state/recovery concerns and their impact. For a genuinely stateless scope, explain the state/authority boundary; do not invent a database. A missing assessment or inaccessible restore is unresolved or a gap, not inapplicability.
3. Choose acceptable data-point/loss and restoration-time boundaries, with measurement conditions and rationale. Identify a feasible source/method and recovery decision/operator. Keep the decision proportionate; no universal numbers or backup tool are required.
4. For a migration, identify source/target formats and the producer/consumer or application/state combinations that work. Plan ordering, interruptions, retry, partial progress, irreversible effects and reconciliation of later legitimate writes. Do not assume that an old executable can use migrated data.
5. Examine representative restore/reconstruction and migration evidence in isolated resources. Record what was actually checked, the result and limits. A checksum or backup job alone cannot establish usable restoration.
6. Give failed or inconclusive evidence an accountable disposition before dependent exposure. Repair and revalidate, select another verified method, or use an applicable governed exception; do not relabel failure as a passed exercise. Keep incident/rollback and approval decisions with their primary owners.
7. Link the evidence to the candidate, deployment sequence, approval and operational handoff where applicable. Reassess changed state, procedures, dependencies, objectives or material risks. Retain/dispose of sensitive copies under the recorded data-governance decision.

Existing architecture, decision, deployment and incident records can contain this information. The [optional record](../../templates/stateful-recovery-record.md) is a starting point using existing documentation/evidence categories, not a mandatory new artifact or an executable recovery procedure.

## Worked illustrations and reading points

The [fictional walkthrough](../../examples/stateful-recovery-and-migration-example.md) includes a failed restore, a held forward-only migration, a corrected recheck, subsequent-write reconciliation and a stateless contrast. Its numbers, people, identifiers, timestamps and observations are invented to show record quality; they are not infrastructure tests or evidence that an adopting product is ready.

In the [Master Execution Checklist](../standards/master-execution-checklist.md), Architecture's data/decision activities point to the governing model, Release readiness links state recovery and compatibility, and Recovery links the source-owned response evidence. Checklist completion does not itself supply state verification, scoped Authority or approval. The [end-to-end example](../../examples/end-to-end-playbook-example.md) shows how data recovery accompanies artifact/configuration recovery without changing the seven-phase lifecycle.

## Common insufficient evidence

| Observation | What remains to establish under the governing source |
| --- | --- |
| A backup job or checksum passed. | Recover the required consistent state, use it with the relevant application/consumer, and assess the point/time boundary. |
| An old artifact is available. | Show compatibility with the current or recovered state and handle irreversible/external effects. |
| The provider advertises recovery. | Establish authorized access, retained scope/point, compatibility, actual verification or explicit gap/exception. |
| No server database exists. | Assess local files/device or provider state before declaring the product stateless. |
| A migration ran once. | Examine relevant constraints, partial progress, interruption/retry and loss/reconciliation behavior. |
| CI is green or the owner wrote the record. | Retain the distinct review, approval/Authority and actual execution evidence required by their owners. |

An operator's inability to run a restore does not authorize broader data access or production side effects. An AI-generated record does not replace observed results. Use the [Integration Standard](../standards/integration-standard.md) and [Execution Protocol](../standards/execution-protocol.md) for unavailable capabilities and permitted fallback while preserving the unmet need.
