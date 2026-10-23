# Playbook Remediation Plan

## Purpose and authority

Maintain the selected response to the 2026-10-22 consistency review of baseline `330f0491b0a185a41d661cf8280f5cf0bc13e20e`. The maintainer authorized this plan's registration and the first selected implementation increment in the originating session. Accountable owner: @giaholic. AI assistance does not confer independent approval or permanent authorization.

This is a repository-specific planning record, not another standard. [Work Item Taxonomy](../standards/work-item-taxonomy.md), [Work Item Types](../standards/work-item-types.md), [Repository Milestone Standard](../standards/repository-milestones.md), [Versioning Standard](../standards/versioning-standard.md), [Definition of Ready](../standards/definition-of-ready.md), and [Definition of Done](../standards/definition-of-done.md) remain authoritative.

The review findings R01–R12 and the four follow-up research scopes are preserved in the linked work records. The original Portuguese review and implementation proposal remain historical inputs; this English record maintains repository navigation, issue identities, release boundaries, and bootstrap limits.

## Release boundaries

The latest verified published release is [v0.6.0](https://github.com/giaholic-dev/product-development-playbook/releases/tag/v0.6.0) (2026-10-22), from immutable commit `c7c0bc67b53433e4a549d807bb04f37c4c9f0002`. The historical v0.1.0 release remains published (2026-09-12). The closed v0.2.0–v0.5.0 milestones represent accepted delivery boundaries, not proof that those versions were published. Do not reopen them or publish historical versions merely to fill a numbering sequence.

The current development target is **v0.7.0 — Audit Evidence Coverage**. v0.7.0 and v0.8.0 remain planned delivery boundaries, not published releases or date commitments. The selected 0.x versions identify reviewed adoption baselines; they do not establish a full external Semantic Versioning compatibility promise. [C09 / #323](https://github.com/giaholic-dev/product-development-playbook/issues/323) documents the detailed adoption/upgrade policy before publication.

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
- C08 implements Python-standard-library documentation checks in `scripts/check-documentation.py`, behavioral cases in `scripts/test_check_documentation.py`, and the read-only `.github/workflows/documentation-checks.yml`. README records the parser contract and manual reachability/index boundary.
- C09 maintains the Versioning Standard and conformance template and adds `docs/practices/playbook-upgrade-guide.md`, with immutable-baseline and migration evidence requirements.
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


## Execution checkpoint — 2026-10-22

This is a dated evidence checkpoint after integrated revision `621529b83ffcbdbb8286fad0ee16971e51213638`, not a replacement for live issue status. The original Portuguese implementation plan is preserved; the selected release boundaries and dependencies above remain unchanged.

| Work | Integrated evidence | Outcome at this checkpoint |
| --- | --- | --- |
| C01 / [#315](https://github.com/giaholic-dev/product-development-playbook/issues/315) | [PR #341](https://github.com/giaholic-dev/product-development-playbook/pull/341) | Closed: jq exit-status regression and negative fixture verified. |
| C02 / [#316](https://github.com/giaholic-dev/product-development-playbook/issues/316) | [PR #342](https://github.com/giaholic-dev/product-development-playbook/pull/342) | Closed: portable classification and adopted Project requirements reconciled. |
| C03 / [#317](https://github.com/giaholic-dev/product-development-playbook/issues/317) | [PR #343](https://github.com/giaholic-dev/product-development-playbook/pull/343) | Closed: catalog categories aligned with Artifact Standard. |
| C04 / [#318](https://github.com/giaholic-dev/product-development-playbook/issues/318) | [PR #344](https://github.com/giaholic-dev/product-development-playbook/pull/344) | Closed: glossary navigation distinguished from definition ownership. |
| C05 / [#319](https://github.com/giaholic-dev/product-development-playbook/issues/319) | [PR #345](https://github.com/giaholic-dev/product-development-playbook/pull/345) | Closed: obsolete future references replaced with current owners. |
| C06 / [#320](https://github.com/giaholic-dev/product-development-playbook/issues/320) | [PR #346](https://github.com/giaholic-dev/product-development-playbook/pull/346) | Closed: application/deployment identity boundaries clarified. |
| C07 / [#321](https://github.com/giaholic-dev/product-development-playbook/issues/321) | [PR #347](https://github.com/giaholic-dev/product-development-playbook/pull/347) | Closed: three lifecycle examples, six checklist entries and optional environment record updated. |
| C08 / [#322](https://github.com/giaholic-dev/product-development-playbook/issues/322) | [PR #348](https://github.com/giaholic-dev/product-development-playbook/pull/348) | Closed: documentation checker, seven behavioral tests and GitHub Actions validation passed. |
| C09 / [#323](https://github.com/giaholic-dev/product-development-playbook/issues/323) | [PR #349](https://github.com/giaholic-dev/product-development-playbook/pull/349) | Closed: immutable adoption baseline, upgrade procedure and scoped conformance update integrated; Documentation checks passed. |

PRs retain exact reviewed heads, changed-file readback, scoped validation and recorded AI-assisted self-review. No independent approval is inferred. The maintainer authorized continuation of these bounded changes in the work session. The examples are explicitly fictional and do not provision an adopter's environments.

### Remaining release and capability obligations

- C10 [#324](https://github.com/giaholic-dev/product-development-playbook/issues/324) remains open: reviewed obsolete branch deletion/retention must be executed and verified without touching active work. Integrated PRs alone are not deletion evidence. No branch deletion is claimed by this checkpoint.
- C11 [#325](https://github.com/giaholic-dev/product-development-playbook/issues/325) remains open and depends on C10 plus aggregate readiness and verified publication. No v0.6.0 tag or release has been published by this work.
- The three native milestones and issue associations remain unperformed. The connected interface exposes no milestone-creation operation; the available native browser is signed out. A milestone title in this plan or an issue body is not a native milestone.
- Required Phase/Work Type field updates for the adopted GitHub Project mapping remain unverified/unperformed through the current connection. Body classifications preserve intended values only; they do not satisfy that mapping's mutation/evidence requirement.
- Release publication and branch-ref deletion are not exposed by the current connector. Native fallback requires an authenticated, authorized session and post-action verification. Missing capability is an open obligation, not an exception or successful result.

M7, M8 and the four unversioned research issues retain their original boundaries. A01 may proceed after C01 under its recorded dependency, but exporter expansion requires its coverage decision; stateful rules require O01. This checkpoint does not report any of them implemented or approve their research conclusions in advance.

## Reconciled governance checkpoint — 2026-10-22

This checkpoint supersedes the earlier pending-capability observations for the operations explicitly verified below. Historical observations remain dated evidence; they are not current blockers.

- Native milestones [#6](https://github.com/giaholic-dev/product-development-playbook/milestone/6), [#7](https://github.com/giaholic-dev/product-development-playbook/milestone/7) and [#8](https://github.com/giaholic-dev/product-development-playbook/milestone/8) exist. All 21 delivery issues (#315–#335) have their intended native milestone association; the four research candidates remain unversioned.
- C10 / [#324](https://github.com/giaholic-dev/product-development-playbook/issues/324) retains the completed review of 149 original refs and verified removal of 147 integrated branches. A fresh branch inventory in this continuation confirmed only `main` and `docs/define-execution-protocol-standard` before creation of this checkpoint's short-lived branch. No further original branch was deleted in this continuation.
- The retained branch at `1a970af8a24141ad45d9a2710bf68c36299b499b` preserves 23 commits outside main associated with closed, unmerged [PR #286](https://github.com/giaholic-dev/product-development-playbook/pull/286). Owner: @giaholic. Reassess before reuse or by 2026-11-05; remove only after its preservation/equivalence needs and disposition are verified. This is documented audit retention permitted by Branch Workflow, not an active feature or an exception.
- Authenticated native access to Organization Project #1 now works. Phase and Work Type were populated and read back for all 25 plan issues (#315–#339) against the identity/classification table above. The existing Work Type option `Maintenance` was renamed `Operational Maintenance` to match the governing standard, preserving the option identity and existing assignments. No workflow commitment, optional artifact classification or research acceptance is inferred from these updates.
- C01–C09 retain their integrated evidence. C10 completion follows integration of this reconciled record. C11 / [#325](https://github.com/giaholic-dev/product-development-playbook/issues/325) remains the release work item: aggregate boundary review, exact candidate/check verification, substantive notes covering material changes since v0.1.0, release decision and verified tag/publication remain required. Resolving the mapping does not publish v0.6.0.
- A01–A06, O01–O04 and F01–F04 remain pending under their recorded dependencies. This checkpoint neither expands exporter coverage nor approves stateful recovery requirements.

## v0.6.0 publication verified — 2026-10-22

[PR #352](https://github.com/giaholic-dev/product-development-playbook/pull/352) integrated the [release notes and M6 aggregate review](../releases/v0.6.0.md). The reviewed head passed Documentation checks; its merge candidate `c7c0bc67b53433e4a549d807bb04f37c4c9f0002` had no file differences from that head. C11 records the scoped release decision, validation and known limits.

The native GitHub Release is published, labeled Latest and linked to the approved exact commit. Tag comparison against that commit is identical; the release-note bytes fetched through v0.6.0 match the reviewed source. The release page exposes the notes, adopter actions, known exporter omissions and content-recovery guidance. No earlier release/tag was rewritten. This checkpoint resolves the earlier pending-publication and capability observations for M6; it does not claim publication of v0.7.0 or v0.8.0.

C01–C10 are complete. C11 closure and native M6 closure follow verification of this post-publication README/evidence update. The next selected development boundary is M7; start with A01 / #326 to approve audit coverage before A02–A05 implementation. O01 and unversioned research retain their own readiness/decision conditions. Audit-retention reassessment before reuse or by 2026-11-05 remains a non-blocking operational obligation owned by @giaholic.

## A01 coverage decision — 2026-10-22

A01 / #326 selects the [Audit Package Coverage and Compatibility Contract](audit-package-contract.md) for A02–A05: committed tracked-source bytes with explicit sensitivity/exclusion and dirty-state semantics; distinct PR conversations/review submissions/inline comments; actual typed Project planning values; nested traversal, interval observation and fail-closed completeness. The completed implementation targets manifest 2.0.0 / tool 2.0.0, while the current script remains 1.0.1 / schema 1.0.0. Historical packages are not upgraded by relabeling.

This is the bounded contract research outcome, effective through its reviewed integration. It does not change collector code, execute a live export, certify API access, complete M7 or publish v0.7.0. A02–A05 must evaluate their own current readiness against the contract and retain exact-source/fixture evidence; A06 still requires authorized end-to-end comparison and release verification. The M7 outcome is preserved rather than narrowed.

## A02 committed-source increment — 2026-10-22

A02 / #327 adds the standard-library source helper and isolated Git fixtures, integrated with the Bash exporter and CI. Tool/manifest 1.1.0 describes this additive source increment and explicitly leaves full-profile completeness false. It is not schema/tool 2, expanded PR/Project collection or M7 acceptance. Source bytes are pinned to the selected commit with tracked inventory, mode/size/hash records, explicit protected/pointer exclusions and final verification; dirty working-tree content is excluded. A03/A04/A05 retain their own scope and gates.

## A03 PR-evidence increment — 2026-10-22

A03 / #328 adds per-PR conversation comments, review submissions and inline comments/replies as distinct retained collections. The read-only REST helper validates selected-repository identity, paginates each PR/collection through validated response headers, records page/count/interval evidence and fails on partial/error/conflicting or unresolvable parent evidence. Synthetic fixtures cover pagination, empty results, review history, replies, failure boundaries and Bash/CLI integration without a live export. Tool/manifest 1.2.0 remains an intermediate profile with `full_profile_complete=false`; actual Project values, aggregate integrity/finalization and authorized live comparison remain A04–A06 obligations. Retained review states do not establish current approval or lifecycle acceptance.

## A04 Project-value increment — 2026-10-23

A04 / #329 adds a read-only typed Project collector and offline transcript replay: Project identity, field definitions/options, active/archived item identities, each item's independently paginated values, nested relationship connections and views. Every item/field pair retains present, observed-unset, inapplicable or inaccessible-redacted status; unsupported types, partial/error responses, missing relations and detected revision/count drift fail. Owner kind/login/number are explicitly selectable. Synthetic fixtures exercise the contract boundaries without a live GitHub export. Tool/manifest 1.3.0 is an intermediate additive profile with `full_profile_complete=false`; A05 aggregate integrity/finalization and A06 authorized live comparison/release evidence remain pending. Implementation/validation does not establish independent approval or M7 completion.

## A05 aggregate coverage/integrity increment — 2026-10-23

A05 / #330 implements tool/manifest 2.0.0 under the existing A01 contract. Required repository collections now retain read-only page/count/interval evidence and scoped responses; optional Discussions is explicitly excluded or collected/validated. Schema-2 completeness is derived after source Git tree/blob reconstruction, all payload hashes/sizes, collection replay, PR/Project relations, cross-collector conversation consistency and local work references pass. ZIP bytes are verified before no-overwrite publication; current-run outputs roll back on finalization failure. A separate manifest digest is retained beside the archive. Legacy packages are not relabeled or converted. Synthetic fixtures cover positive, malformed, incomplete, conflicting, foreign, hash/count/version and ZIP/copy failure cases. A06 still owns authorized real-data comparison, aggregate release review and v0.7.0 publication; implementation does not establish independent approval, universal provider visibility or M7 completion.

## O01 stateful-recovery decision — 2026-10-23

O01 / #332 selects proportionate recovery/migration evidence through existing primary owners, recorded in the [Stateful Recovery and Migration Decision](stateful-recovery-decision.md). Applicability covers material persistent state, including local-only/provider-managed state, with evidence-backed stateless inapplicability. Recovery point/time boundaries, representative restoration evidence, schema/application compatibility and failure/retry/loss treatment are selected for O02 integration; no universal database, backup tool/schedule or numerical objective is imposed. Conceptual cases exercise stateful/stateless/managed/cache/irreversible/hybrid boundaries. O02 normative integration, O03 fictional walkthrough and O04 release acceptance remain separate. O01 has no established issue dependency; progress does not imply that A06 or v0.7.0 live acceptance is complete.

## O02 stateful-recovery integration — 2026-10-23

O02 / #333 implements the selected [O01 decision](stateful-recovery-decision.md) through existing primary owners. Rollback Strategy owns persistent-state assessment, recovery boundaries/method, representative restoration evidence, gaps/exceptions and reassessment. Data Model owns source/target state, producer/consumer or application compatibility and migration failure/retry/loss evidence. Security/Privacy/Data Governance covers recovery copies and restore data; Software Environments and Deployment reference the affected state validation while retaining isolation and scoped promotion Authority. No new role, backup provider, universal numerical objective, mandatory database or competing exception source is introduced. O03 walkthrough and O04 aggregate release acceptance remain pending; no actual backup/restore or v0.8.0 publication is claimed.

## O03 recovery/migration illustration — 2026-10-23

O03 / #334 adds the [optional practice](data-recovery-and-migrations.md), [reusable optional record](../../templates/stateful-recovery-record.md) and [fictional walkthrough](../../examples/stateful-recovery-and-migration-example.md). A failed restore holds a forward-only migration; a modeled corrected recheck exposes recovery point/time, compatibility, interruption/resume, later-write reconciliation and accountable disposition. A stateless contrast preserves source/configuration and environment obligations without inventing database backups. The existing end-to-end example now distinguishes data recovery from artifact/configuration recovery; R2/R5 checklist entries link to their primary evidence owners without introducing a required template or new gate. All example observations are fictional, not tested infrastructure. O04 aggregate/release acceptance and A06 live-export acceptance remain pending.

## A06 reviewer preflight correction — 2026-10-23

A source-based preflight against GitHub's current [RequestedReviewer union](https://docs.github.com/en/graphql/reference/pulls#requestedreviewer) found that the A04 query selected identity fields for User/Team/Mannequin but omitted Bot and EnterpriseTeam. The bounded correction retains their Node IDs and available identity metadata, rejects unknown reviewer actor types and independently paginates the same existing relationship. Tool 2.0.1 retains manifest 2.0.0; Project evidence 1.1.0 distinguishes the changed query, with offline compatibility for original Project evidence 1.0.0/tool 2.0.0 and no package rewriting. This repairs the already-required reviewer coverage; it does not reduce scope, add access or satisfy A06 live-export/release acceptance. A retrieved Octokit schema snapshot predates the current Project schema additions, so it was not treated as proof of current endpoint support; authorized live query/coverage verification remains mandatory in A06.
