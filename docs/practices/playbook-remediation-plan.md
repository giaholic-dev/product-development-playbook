# Playbook Remediation Plan

## Purpose and authority

Maintain the selected response to the 2026-10-22 consistency review of baseline `330f0491b0a185a41d661cf8280f5cf0bc13e20e`. The maintainer authorized this plan's registration and the first selected implementation increment in the originating session. Accountable owner: @giaholic. AI assistance does not confer independent approval or permanent authorization.

This is a repository-specific planning record, not another standard. [Work Item Taxonomy](../standards/work-item-taxonomy.md), [Work Item Types](../standards/work-item-types.md), [Repository Milestone Standard](../standards/repository-milestones.md), [Versioning Standard](../standards/versioning-standard.md), [Definition of Ready](../standards/definition-of-ready.md), and [Definition of Done](../standards/definition-of-done.md) remain authoritative.

The review findings R01–R12 and the four follow-up research scopes are preserved in the linked work records. The original Portuguese review and implementation proposal remain historical inputs; this English record maintains repository navigation, issue identities, release boundaries, and bootstrap limits.

## Release boundaries

The last confirmed published release is v0.1.0 (2026-09-12). The closed v0.2.0–v0.5.0 milestones represent accepted delivery boundaries, not proof that those versions were published. Do not reopen them or publish historical versions merely to fill a numbering sequence.

The current development target is **v0.6.0 — Consistency, Environments and Adoption**. v0.7.0 and v0.8.0 are subsequent planned delivery boundaries, not published releases or date commitments. The selected 0.x versions identify reviewed adoption baselines; they do not establish a full external Semantic Versioning compatibility promise. [C09 / #323](https://github.com/giaholic-dev/product-development-playbook/issues/323) documents the detailed adoption/upgrade policy before publication.

| Local boundary | Intended version and outcome | Included records |
| --- | --- | --- |
| M6 | v0.6.0 — coherent standards, practical three-environment guidance, regression/documentation validation, and adopter upgrades. | C01–C11 |
| M7 | v0.7.0 — offline audit evidence coverage under an approved contract, with explicit completeness and compatibility limits. | A01–A06 |
| M8 | v0.8.0 — approved stateful recovery and migration requirements with proportionate examples. | O01–O04 |
| Research backlog | No release assigned; implementation depends on evidence and a separate scope decision. | F01–F04 |

All three environments remain mandatory for in-scope executable products under [Software Environments](../standards/software-environments.md). This plan neither provisions adopting-product environments nor changes the methodology repository's recorded applicability.

## Work records and dependencies

The IDs below are local planning references; the linked issue numbers are GitHub identities. Each record has one primary Lifecycle Phase and Work Type. Classification concerns the work's intended outcome, not the title of the document being edited. Priorities remain relative planning information, not execution order or workflow state.

| ID | Finding | Work record | Phase | Work Type | Priority | Dependencies |
| --- | --- | --- | --- | --- | --- | --- |
| C01 | R01 | [#315 — Fix false-positive audit comment regression assertion](https://github.com/giaholic-dev/product-development-playbook/issues/315) | Maintenance | Bug | High | None established |
| C02 | R02 | [#316 — Reconcile work classification representation and label rules](https://github.com/giaholic-dev/product-development-playbook/issues/316) | Maintenance | Bug | High | None established |
| C03 | R04 | [#317 — Align Artifact Catalog categories with Artifact Standard](https://github.com/giaholic-dev/product-development-playbook/issues/317) | Maintenance | Bug | Medium | None established |
| C04 | R05 | [#318 — Clarify glossary catalog ownership and definition ownership](https://github.com/giaholic-dev/product-development-playbook/issues/318) | Maintenance | Bug | Medium | None established |
| C05 | R06 | [#319 — Replace obsolete future references in governing standards](https://github.com/giaholic-dev/product-development-playbook/issues/319) | Maintenance | Bug | Medium | None established |
| C06 | R08 | [#320 — Clarify application and deployment identity boundaries](https://github.com/giaholic-dev/product-development-playbook/issues/320) | Maintenance | Improvement | Medium | None established |
| C07 | R07 | [#321 — Demonstrate three-environment preparation and promotion end to end](https://github.com/giaholic-dev/product-development-playbook/issues/321) | Maintenance | Improvement | Medium | [#320](https://github.com/giaholic-dev/product-development-playbook/issues/320) |
| C08 | R10 | [#322 — Add scoped documentation validation to CI](https://github.com/giaholic-dev/product-development-playbook/issues/322) | Development | Feature | Medium | [#317](https://github.com/giaholic-dev/product-development-playbook/issues/317), [#318](https://github.com/giaholic-dev/product-development-playbook/issues/318), [#319](https://github.com/giaholic-dev/product-development-playbook/issues/319) |
| C09 | R11 | [#323 — Document adoption baselines and Playbook upgrade procedure](https://github.com/giaholic-dev/product-development-playbook/issues/323) | Release | Improvement | Medium | [#316](https://github.com/giaholic-dev/product-development-playbook/issues/316), [#317](https://github.com/giaholic-dev/product-development-playbook/issues/317), [#318](https://github.com/giaholic-dev/product-development-playbook/issues/318), [#319](https://github.com/giaholic-dev/product-development-playbook/issues/319), [#320](https://github.com/giaholic-dev/product-development-playbook/issues/320), [#321](https://github.com/giaholic-dev/product-development-playbook/issues/321) |
| C10 | R12 | [#324 — Reconcile integrated branch retention with Branch Workflow](https://github.com/giaholic-dev/product-development-playbook/issues/324) | Maintenance | Operational Maintenance | Low | None established |
| C11 | R01,R02,R04–R08,R10–R12 | [#325 — Validate and publish v0.6.0 consistency and adoption baseline](https://github.com/giaholic-dev/product-development-playbook/issues/325) | Release | Operational Maintenance | Medium | [#315](https://github.com/giaholic-dev/product-development-playbook/issues/315), [#316](https://github.com/giaholic-dev/product-development-playbook/issues/316), [#317](https://github.com/giaholic-dev/product-development-playbook/issues/317), [#318](https://github.com/giaholic-dev/product-development-playbook/issues/318), [#319](https://github.com/giaholic-dev/product-development-playbook/issues/319), [#320](https://github.com/giaholic-dev/product-development-playbook/issues/320), [#321](https://github.com/giaholic-dev/product-development-playbook/issues/321), [#322](https://github.com/giaholic-dev/product-development-playbook/issues/322), [#323](https://github.com/giaholic-dev/product-development-playbook/issues/323), [#324](https://github.com/giaholic-dev/product-development-playbook/issues/324) |
| A01 | R03 | [#326 — Define audit package coverage and compatibility contract](https://github.com/giaholic-dev/product-development-playbook/issues/326) | Architecture | Research | High | [#315](https://github.com/giaholic-dev/product-development-playbook/issues/315) |
| A02 | R03 | [#327 — Export the declared repository source snapshot](https://github.com/giaholic-dev/product-development-playbook/issues/327) | Development | Feature | Medium | [#326](https://github.com/giaholic-dev/product-development-playbook/issues/326) |
| A03 | R03 | [#328 — Export PR conversations and review submissions](https://github.com/giaholic-dev/product-development-playbook/issues/328) | Development | Feature | Medium | [#326](https://github.com/giaholic-dev/product-development-playbook/issues/326) |
| A04 | R03 | [#329 — Export Project item field values with completeness evidence](https://github.com/giaholic-dev/product-development-playbook/issues/329) | Development | Feature | Medium | [#326](https://github.com/giaholic-dev/product-development-playbook/issues/326) |
| A05 | R03 | [#330 — Enforce audit manifest coverage and integrity checks](https://github.com/giaholic-dev/product-development-playbook/issues/330) | Development | Improvement | Medium | [#327](https://github.com/giaholic-dev/product-development-playbook/issues/327), [#328](https://github.com/giaholic-dev/product-development-playbook/issues/328), [#329](https://github.com/giaholic-dev/product-development-playbook/issues/329) |
| A06 | R03 | [#331 — Validate and publish v0.7.0 audit evidence coverage](https://github.com/giaholic-dev/product-development-playbook/issues/331) | Release | Operational Maintenance | Medium | [#326](https://github.com/giaholic-dev/product-development-playbook/issues/326), [#327](https://github.com/giaholic-dev/product-development-playbook/issues/327), [#328](https://github.com/giaholic-dev/product-development-playbook/issues/328), [#329](https://github.com/giaholic-dev/product-development-playbook/issues/329), [#330](https://github.com/giaholic-dev/product-development-playbook/issues/330), [#325](https://github.com/giaholic-dev/product-development-playbook/issues/325) |
| O01 | R09 | [#332 — Define stateful recovery and migration requirements](https://github.com/giaholic-dev/product-development-playbook/issues/332) | Architecture | Research | Medium | None established |
| O02 | R09 | [#333 — Establish stateful recovery and migration evidence rules](https://github.com/giaholic-dev/product-development-playbook/issues/333) | Architecture | Feature | Medium | [#332](https://github.com/giaholic-dev/product-development-playbook/issues/332) |
| O03 | R09 | [#334 — Demonstrate data recovery and migration decisions](https://github.com/giaholic-dev/product-development-playbook/issues/334) | Maintenance | Improvement | Medium | [#333](https://github.com/giaholic-dev/product-development-playbook/issues/333) |
| O04 | R09 | [#335 — Validate and publish v0.8.0 stateful recovery guidance](https://github.com/giaholic-dev/product-development-playbook/issues/335) | Release | Operational Maintenance | Medium | [#332](https://github.com/giaholic-dev/product-development-playbook/issues/332), [#333](https://github.com/giaholic-dev/product-development-playbook/issues/333), [#334](https://github.com/giaholic-dev/product-development-playbook/issues/334), [#331](https://github.com/giaholic-dev/product-development-playbook/issues/331) |
| F01 | Evolution 1 | [#336 — Select the first non-software specialization and pilot](https://github.com/giaholic-dev/product-development-playbook/issues/336) | Product | Research | Low | None established |
| F02 | Evolution 2 | [#337 — Reassess machine-readable execution representation for a concrete consumer](https://github.com/giaholic-dev/product-development-playbook/issues/337) | Architecture | Research | Low | None established |
| F03 | Evolution 3 | [#338 — Assess product retirement and decommissioning scope](https://github.com/giaholic-dev/product-development-playbook/issues/338) | Product | Research | Low | None established |
| F04 | Evolution 4 | [#339 — Validate lifecycle guidance usability with an adopter](https://github.com/giaholic-dev/product-development-playbook/issues/339) | UX | Research | Low | [#321](https://github.com/giaholic-dev/product-development-playbook/issues/321), [#323](https://github.com/giaholic-dev/product-development-playbook/issues/323) |

Issue intake does not establish readiness or commitment. Evaluate current scope, acceptance evidence, source revision, access, capabilities, Assignments, Authority, and the next action before execution. A01 and O01 determine the approved scope for their dependent implementation. F01 needs a selected non-software pilot; F02 needs a concrete consumer; F03 needs a confirmed retirement need; F04 needs an adopter/task and an evidence approach.

The first selected implementation is C01 / #315. C02–C06 and branch-retention assessment can be prepared independently. C07 consumes C06; documentation CI consumes the corrected structure; C09 consolidates adoption guidance before C11's aggregate release review. A01 can be prepared after C01, but M7 publication follows M6. O01 may gather evidence separately; O02–O04 remain conditional on its decision. Research completion does not automatically complete a promised implementation boundary.

## Milestone contracts

Milestone creation and assignment were **not completed at registration time (2026-10-22)**: the connected GitHub operations do not expose milestone creation, local CLI network access is unavailable, and the browser GitHub session is signed out. The visible milestone page showed zero open and five closed milestones. The issue bodies explicitly retain their intended milestone rather than claiming an association.

The contracts below are prepared for an authorized native/CLI operation. Reconcile the actual collection before creating, then verify the new milestone identities and assign the selected issues. This is an outstanding bootstrap obligation, not an approved exception or completed configuration. Native GitHub Project field values also remain unverified; body classification is not evidence of a Project-field update.

### v0.6.0 — Consistency, Environments and Adoption

**Intended outcome**

Establish a coherent, verifiable Playbook adoption baseline by correcting confirmed validation and semantic defects, completing practical three-environment guidance, and documenting baseline upgrades.

**Scope and included work**

C01–C11: assertion regression fix; classification representation; artifact categories; terminology ownership; obsolete governing references; deployment-identity clarification; environment examples/template/navigation; scoped documentation CI; adopter upgrade guidance; branch-retention reconciliation; aggregate release review and publication.

Excluded: expanded audit data collection, new stateful recovery requirements, non-software methods, a machine-execution schema, real adopter infrastructure, and product decommissioning.

**Accountable owner:** @giaholic.

**Completion criteria**

- All selected correction and integration outcomes are evidenced in the reviewed default-branch source.
- Positive/negative exporter checks and the selected documentation checks behave as intended; skipped checks are not claimed successful.
- Primary sources, classification, examples and environment promotion guidance are consistent.
- Upgrade guidance identifies the adopted baseline, changed obligations, remediation and exceptions.
- Reviewed branch cleanup or retention is evidenced without deleting active work.
- Aggregate milestone review records scope, source revision, evidence, residual obligations and decision.
- The approved v0.6.0 source is tagged and its release record/notes and audience availability are verified through C11.

### v0.7.0 — Audit Evidence Coverage

**Intended outcome**

Provide an offline audit package whose repository, Pull Request and Project evidence satisfies an explicit, verifiable coverage contract.

**Scope and included work**

A01–A06: coverage/compatibility decision; repository source snapshot; PR conversations and review submissions; Project item field values; manifest/integrity enforcement; end-to-end verification and release publication.

Excluded: provider administration certification, unapproved data disclosure, a methodology machine-execution schema, a universal guarantee that every external collection is available, and unrelated new integrations.

**Accountable owner:** @giaholic.

**Completion criteria**

- A01 defines and approves required coverage, exclusions, source identity, pagination and partial/unavailable-result treatment.
- Required source bytes and governance records are retained and linked to their identities/revisions.
- Fixtures exercise missing data, nested pagination, duplicates, inaccessible collections and invalid references.
- Manifest and verification results do not classify a partial required result as complete.
- Authorized end-to-end observation checks package coverage against actual selected repository/PR/Project evidence and records its time interval and limits.
- Aggregate acceptance, compatibility notes and verified v0.7.0 publication are retained.

If A01 selects a narrower scope than the promised outcome, change the milestone explicitly with reason and affected work; a completed research decision alone does not complete M7.

### v0.8.0 — Stateful Recovery Guidance

**Intended outcome**

Enable software adopters to evidence recoverability of material persistent state and safe migration decisions, in proportion to risk.

**Scope and included work**

O01–O04: requirement/ownership research; approved recovery and migration rules through existing primary owners; stateful/stateless examples and optional reusable record; aggregate adoption review and release.

Excluded: operating or restoring actual production data, mandatory databases for stateless products, non-software manufacturing recovery, a new lifecycle phase, and product retirement policy.

**Accountable owner:** @giaholic.

**Completion criteria**

- O01 approves applicable triggers, ownership, required evidence and exceptions.
- Rules distinguish code rollback from state restoration and migration compatibility.
- Stateful and stateless examples demonstrate correct applicability and accountable disposition.
- New obligations and adopter migration consequences are documented without duplicated definition ownership.
- Aggregate review and verified v0.8.0 publication are retained.

O02–O04 are not ready for implementation before O01. If O01 concludes that normative implementation should be deferred, revise or cancel the unfulfilled delivery boundary explicitly instead of marking its original outcome delivered.


## Documentation implementation

Keep one primary source per rule. Existing standards own classification, artifact hierarchy, terminology, readiness, completion, release, security and recovery. Practices and examples apply those rules rather than duplicate them.

- C02–C05 reconcile the existing taxonomy, labels, artifact catalog, terminology and obsolete governing references. Preserve historical assessment baselines.
- C06 clarifies application versus deployment identities in Software Environments and its related owners. It must preserve isolation and scoped production approval.
- C07 updates the three existing full-lifecycle examples, relevant Master Execution Checklist references, and an optional `templates/software-environment-record.md`.
- C08 selects a repository-toolchain implementation for documentation checks; `scripts/check-documentation.*` and `.github/workflows/documentation-checks.yml` are proposed targets, not files claimed to exist.
- C09 maintains the Versioning Standard and conformance template and adds the proposed `docs/practices/playbook-upgrade-guide.md`.
- A01 defines the proposed `docs/practices/audit-package-contract.md`; A02–A05 update the exporter, fixtures and manifest according to that contract. Exporter JSON is not a Playbook machine-execution schema.
- O01 chooses primary ownership for stateful recovery/migration rules before O02 edits governing sources. O03 adds the proposed `docs/practices/data-recovery-and-migrations.md` and proportionate examples/optional records.
- C11, A06 and O04 prepare release notes at proposed `docs/releases/v0.6.0.md`, `v0.7.0.md` and `v0.8.0.md`, linked to actual releases only when published.

Proposed paths are not empty placeholders or existing destinations. Update README, index, glossary, relationship map and activity navigation only when their actual maintained content changes. Record current self-adoption evidence in the existing conformance declaration without rewriting earlier observations.

## Review, completion and publication

Use short-lived branches and reviewed increments with traceability to the governing issue. One issue may need multiple PRs; its tests and documentation belong to that outcome. No empty parent issue is required merely to duplicate milestone grouping.

Before work completion, retain the scoped outcome, required validation/review evidence, integrated source where applicable, and the governed disposition of remaining obligations. Assess the combined milestone with [Milestone and Phase Boundary Review](milestone-boundary-review.md), separately from individual issue statuses.

For each proposed release: select an exact source, prepare audience/compatibility/migration notes, record the release decision and Authority, publish through an available authorized channel, and verify the tag, source, release information and availability. Update the latest published release in README only afterward. The milestone contracts include verified publication, so closing them follows that observation. v0.6.0 notes must cover material integrated changes since v0.1.0, including the three-environment requirement and current audit coverage limits.

Release publication is not exposed by the current connector. Until an authorized native/CLI publication is performed and verified, the version remains in development. Missing capability does not establish release success.

## Maintenance and status ownership

Issue and milestone records own their current operational status; this document owns the selected planning boundaries and identity map. Reassess it when accepted scope, dependencies, applicable rules, capability access or release decisions materially change. Retain prior reasons and source revisions. Do not mark future research implemented because an issue was created or a study completed.
