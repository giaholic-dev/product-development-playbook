# Stateful Recovery and Migration Decision

## Context

O01 / [#332](https://github.com/giaholic-dev/product-development-playbook/issues/332) addresses R09 in the [remediation plan](playbook-remediation-plan.md). Assessment: 2026-10-23 at `824abd3c2393012ff46518f451eb7fa2e88e4201`. The maintainer @giaholic authorized continued plan execution. This decision is Architecture / Research, with no established issue dependency; it does not depend on claiming that the pending v0.7.0 live-export acceptance has completed.

The existing [Rollback Strategy](../standards/rollback-strategy.md) covers a safe target, decision-maker, recovery method and verification, but does not explicitly distinguish restoring software from restoring compatible persistent state. [Data Model](../standards/data-model.md) identifies information ownership/constraints and informs migration without specifying migration compatibility evidence. [Security, Privacy, and Data Governance](../standards/security-privacy-data-governance.md) already owns access, retention, risk and exceptions. [Software Environments](../standards/software-environments.md) already owns isolation, test fidelity and production-promotion approval. [Deployment Strategy](../standards/deployment-strategy.md) owns prerequisites and execution evidence. Add the missing recovery/migration detail through these owners rather than creating a parallel authority.

Status: selected design input, effective through reviewed integration of O01. The proposed normative extensions below require O02 / [#333](https://github.com/giaholic-dev/product-development-playbook/issues/333). This practice records the decision; it does not itself amend the primary standards, operate a backup service or certify an adopting product.

## Decision

Select proportionate, evidence-based recovery obligations for affected persistent state. Retain one recovery decision and linked evidence in existing architecture, deployment or operational records; a new standalone file, database, provider or paid service is not required.

### Applicability and triggers

Assess state that materially affects users, operations or obligations and cannot be safely recreated from identified authoritative inputs within the accepted recovery boundary. This includes local-device state, files/object storage, databases, queues/events and provider-managed state where relevant. A product's lack of a self-managed database does not establish statelessness. Reconstructable caches and indexes can have different recovery treatment when their authoritative inputs and reconstruction evidence are identified.

Reassess before a release materially changes stored information, schema/format, read/write compatibility, retention/deletion, recovery mechanism, provider or external-state dependency; also reassess after a failed recovery, material incident or changed recovery objective. The boundary is the affected product or constituent, not every repository file or every resource the team can access.

For genuinely stateless runtime behavior, record the inventory/authority rationale for why no material persistent application state needs restoration or migration. Do not invent a database, backup schedule, restore exercise or data migration. Source/artifact/configuration recovery and applicable software environment/promotion requirements still apply. A missing state assessment, untested restoration or unavailable mechanism is a gap or accepted exception, not evidence of statelessness.

For physical/non-software products, assess relevant information and operational continuity through their applicable standards and specialization. This decision does not turn physical production into software deployment or require software environments for a purely non-software product. A hybrid product scopes software-state obligations to the affected constituent and records cross-constituent dependencies.

### Recovery objectives and method

For material persistent state, the selected O02 rule is to record the acceptable recovery point/data-loss boundary and restoration-time boundary, with measurement start/end conditions and a rationale linked to user/operational impact. Recovery point objective (RPO) and recovery time objective (RTO) are useful names, not mandatory jargon or universal numeric targets. A solo project can use a short decision when its impact is low; an unknown or unachievable objective remains an explicit risk/gap.

Identify the authoritative state, scope and consistent recovery unit; the recovery source/method; its identity, availability, retention and access prerequisites; the safe target; the recovery operator/decision-maker; verification criteria; and the response when restoration cannot meet the boundary. A method can be backup/restore, replay from a protected authoritative log, reconstruction from retained inputs, provider-supported recovery/export, or an explicitly accepted loss/disablement strategy. The choice must preserve its actual limits rather than relabel a missing backup as a tested recovery method.

A prior executable or source revision is sufficient only when evidence shows the target state remains readable/writable and acceptable. It does not by itself undo schema changes, data corruption, deletion, queued effects or external side effects. Code redeployment and state restoration can be separate controlled steps.

### Restoration evidence

Before relying on a recovery method for a material stateful release, retain a representative restoration/reconstruction verification or a governed exception. Evidence identifies the source and version/format, recovery procedure, target and isolation, operator, timestamps/duration, recovered point or loss boundary, relevant integrity/consistency checks, application usability/compatibility checks, result and unresolved risk.

Backup-file existence, a successful backup job, an advertised provider feature or a checksum alone does not show that the required state can be restored and used within the objective. Verify representative protected/linked state and required configuration, key-access references or external dependencies without putting credentials in evidence. Providers' own recovery promises need a scoped assessment of access, retention, export and restoration limitations; do not claim an unavailable verification was performed.

Use isolated data/resources and representative failure conditions. Production-derived restore data, privileged recovery-task identities and disposal follow the existing environment and data-governance boundaries. A restore test does not authorize a non-production application to access or mutate production, broaden secret access, or send real external effects. Reassess evidence when its source, procedure, scale, dependency, risk or compatibility assumptions materially change; no universal exercise frequency is selected.

### Migration compatibility and failure treatment

For a material schema, format or data migration, record the identified source/target versions and state; supported application/state read/write combinations; sequencing and prerequisites; transformation/validation criteria; failure/interruption/retry treatment; preservation of identities, constraints and required data; and the feasible recovery path. Include coexistence, delayed clients/jobs and external consumers when they affect compatibility. A forward-only migration is permitted when its irreversibility, safe recovery alternative, loss exposure and required authorization are explicit.

Use representative synthetic or authorized minimized data to verify transformation, integrity and intended behavior, including applicable interruption/retry/partial-progress cases. Do not presume every migration is transactional, reversible or safe to rerun. If reverting software cannot read/write the migrated state, record that limitation and the tested alternative before exposure expands. Do not silently restore an older state and lose later legitimate changes without an authorized loss boundary and reconciliation treatment.

## Primary ownership and integration map

| Concern | Primary source | O02 integration boundary |
| --- | --- | --- |
| Recovery triggers, acceptable target, objectives/method and restoration verification | [Rollback Strategy](../standards/rollback-strategy.md) | Add state-aware recovery readiness/evidence; preserve existing rollback decision/response ownership. |
| State authority, schema/format evolution and application/data compatibility | [Data Model](../standards/data-model.md) | Add migration decision and validation evidence; reference recovery ownership. |
| Backup/recovery-copy access, sensitivity, retention, deletion and key references | [Security, Privacy, and Data Governance](../standards/security-privacy-data-governance.md) | Clarify that retained recovery copies and restore data fall within existing controls; do not invent a compliance regime. |
| Isolated restore/migration validation, configuration fidelity and promotion Authority | [Software Environments](../standards/software-environments.md) | Cross-reference affected state validation; retain existing identity and approval rules. |
| Candidate/configuration/state sequence, prerequisites and observed result | [Deployment Strategy](../standards/deployment-strategy.md) | Require applicable recovery/migration evidence in the existing plan, without duplicating recovery semantics. |
| Scoped Assignments, Approver and Authority | [Roles and Actor Assignment](../standards/roles-and-actor-assignment.md) | No new role, automatic approval or delegated production access. |
| Incident coordination and follow-up | [Incident Management](../standards/incident-management.md) | Existing owner; do not create a competing incident process. |
| Inapplicability, exceptions and reassessment | [Standards Applicability](../standards/standards-applicability.md), [Repository Standards](../standards/repository-standards.md) | Evidence-backed inapplicability differs from a gap/exception. Keep the existing accountable approval and reassessment rules. |

The [Decision Record Template](../../templates/decision-record.md) is already adequate for context, alternatives, evidence, consequences and accountability. No mandatory new template/schema is selected. O03 / [#334](https://github.com/giaholic-dev/product-development-playbook/issues/334) can demonstrate a compact use of existing records after O02 is integrated.

## Options and evidence

- Keep generic rollback wording only: rejected because an old executable can coexist with incompatible or lost data, leaving readiness ambiguous.
- Require a database, identical backup tool, fixed schedule and fixed objectives for every product: rejected because applicability and loss/availability impact differ, including genuinely stateless and provider-managed products.
- Add a new universal disaster-recovery standard and approval role: rejected for this increment because existing sources already own the decisions and evidence.
- Extend existing primary owners with proportionate state/recovery/migration evidence: selected; preserves conceptual ownership and lets small products use concise records without erasing material risks.

The NIST [RPO](https://csrc.nist.gov/glossary/term/recovery_point_objective) and [RTO](https://csrc.nist.gov/glossary/term/Recovery_Time_Objective) references distinguish recoverable data point from recovery duration. They inform terminology; their federal-system planning context is not imposed as a framework or certification. PostgreSQL's [backup verifier documentation](https://www.postgresql.org/docs/18/app-pgverifybackup.html) distinguishes backup integrity checks from test restoration/application verification; its [upgrade guidance](https://www.postgresql.org/docs/18/upgrading.html) illustrates version/tool and client compatibility concerns. These primary sources were checked on 2026-10-23 as concrete evidence, not as required product technology or an implementation prescription.

## Decision validation cases

| Case | Selected treatment | Evidence that would be insufficient |
| --- | --- | --- |
| Stateful service changes a persisted field meaning | Source/target semantics, supported code/state combinations, representative migration and recovery verification. | Reverting a container image without checking migrated data. |
| Local-only application stores the sole copy of user work | Scope recoverability/export or accepted loss, device/format compatibility and isolated verification. | Calling the app stateless because no server database exists. |
| Static informational site with immutable source/assets and no material stored user state | Documented stateless rationale; artifact/configuration recovery and normal environment/promotion evidence. | Adding a fictional database backup obligation. |
| Managed provider owns authoritative records | Scoped provider recovery/export/retention/access assessment and verified method or explicit gap/exception. | Assuming a paid plan or provider claim proves a completed restore. |
| Cache can be rebuilt from preserved authoritative records | Record inputs, dependencies, time boundary and representative rebuild verification; assess source-state protection separately. | Treating a cache as disposable when its supposed source is missing. |
| Destructive/forward-only migration with later legitimate writes | Explicit irreversibility, compatible forward recovery or accepted point/loss and reconciliation, with scoped authorization. | Presenting an old backup as loss-free rollback. |
| Hybrid physical/digital product | Scope state obligations and cross-constituent dependencies; use non-software specialization for physical recovery. | Applying software-deployment mechanics to the whole physical production process. |

The cases check scope, ownership, stateless inapplicability, operational limits and migration failure paths. They are conceptual acceptance evidence for the research decision, not actual restoration tests. O02 must integrate the rules into their owners; O03 must demonstrate them; O04 / [#335](https://github.com/giaholic-dev/product-development-playbook/issues/335) retains aggregate review and release acceptance.

## Consequences, accountability and reassessment

Owner: @giaholic. Review: proportionate recorded AI-assisted self-review through the O01 PR, not independent approval or production-promotion Authority. The integration record identifies the reviewed head, validation, unresolved findings and merge decision under the existing [Code Review Standard](../standards/code-review-standard.md).

Reassess on evidence of an unaddressed stateful/stateless case, conflicting primary ownership, changed product/provider or data risk, or inability to produce proportionate acceptance evidence. Accepted risk and exceptions remain governed records; an AI output or passing documentation check cannot supply approval. No backup system, live dataset, credential change, production recovery, universal recovery objective or compliance certification is delivered by this methodology decision.
