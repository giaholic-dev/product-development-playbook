# Audit evidence validation — 2026-10-24

## Scope and accountable decision

A06 / [#331](https://github.com/giaholic-dev/product-development-playbook/issues/331), M7, owner @giaholic. The maintainer authorized continued implementation and the selected local export in the originating session. This record reports actual execution and bounded independent source/API sampling, not independent human approval or an exhaustive historical certification. The [coverage contract](audit-package-contract.md) governs the result.

Live-tested source: `3a46275f0888af9b0ed489730c956266986d0fb1`, tool 2.1.0, manifest 2.0.0, Project evidence 1.3.0, selected organization `giaholic-dev` Project 1 / `PVT_kwDOE410Wc4BjOE0`. Discussions were explicitly excluded. The local operator used authenticated gh and Python 3.13.5. Earlier failed attempts were not combined with this run or represented as successful packages; #364–#366 retain their fixes and tests.

The run archived main, which also contained unreleased O01–O03 work. It is validation evidence for the unchanged audit implementation, not the v0.7.0 distributable. The audit-only release branch starts at A05 merge `824abd3c2393012ff46518f451eb7fa2e88e4201` and selects the exact reviewed audit implementation/test/contract bytes from the live-tested source. The candidate review verifies that byte comparison and separately runs its checks. Release notes, source identity and publication observation must identify that candidate rather than relabel this package as a release archive.

## Actual observation interval and counts

Times below are UTC on 2026-10-24; provider observations are not atomic.

| Collection | Start | End / final observation |
| --- | --- | --- |
| Committed source | 10:13:50.364515 | 10:13:53.426566 |
| Repository REST records | 10:13:53.660128 | 10:16:10.724899 |
| Project GraphQL evidence | 10:16:12.602863 | 10:26:35.538682 |
| PR evidence | Identity at 10:26:38.252381 | Latest collection at 10:33:40.397100 |

| Retained collection | Count |
| --- | ---: |
| Committed source entries, all retained | 141 |
| Issues / issue comments / issue timeline events | 147 / 1 / 1353 |
| Pull requests | 198 |
| PR conversations / reviews / inline comments | 9 / 115 / 0 |
| Labels / milestones / releases | 11 / 8 / 2 |
| Project items / fields / views | 344 / 17 / 2 |
| Normalized item/field dispositions | 5848 |

All 344 observed Project items were local references in this run. All 594 PR collection observations were complete with terminal traversal evidence. All 115 actual reviews were COMMENTED. Positive approval/change-request/dismissal/supersession, positive inline replies, and absent Project kinds/types are covered by synthetic tests, not falsely claimed as actual live observations. The 5848 values include present, observed-unset and inapplicable dispositions; they are not 5848 non-null scalar values.

## Package integrity and privacy

The operator's completed exporter and a separate offline verification passed. The assistant then read the saved package locally and independently used Python's standard library, without importing exporter verification helpers, to check ZIP membership, CRC, every archived byte against the saved directory, and the manifest sidecar. All 284 entries matched. Size: 3,452,973 bytes.

- Archive: `product-development-playbook-audit-2026-10-24T10-13-48Z.zip`.
- Archive SHA-256: `74032d6b25eae059c949b0dfeefe6215b01c8373e53cdabdfe9b393ec6b1d76e`.
- Manifest SHA-256: `6c1b25ff26a1d97ef4a192f044a31f93e03a7808c4722cff6c0bbf9cac5db970`, matching the saved sidecar.

Observed permissions: package directory 0700, ZIP and manifest 0600. The operator selected a separate local clone and retained the package locally for release validation; no public ZIP attachment, repository copy of provider bodies, credential change or broader access was authorized or performed. The maintainer owns subsequent retention/deletion/disclosure. This record publishes only scoped public source/provider references, non-sensitive counts and digests. Bounded secret/path checks do not guarantee secret-free source or provider bodies.

## Independent comparisons

| Sample | Comparison and result |
| --- | --- |
| README.md, scripts/export-audit.sh, docs/standards/rollback-strategy.md | Independent GitHub connector content at the pinned live-tested commit matches local immutable Git objects and package source bytes. |
| PR #286 conversation 5703062899; PR #351 conversation 6350565528 | Independent REST reads match body, actor identity, target and timestamps. |
| PR #144 review 5205876816; PR #145 review 5205881008 | Independent REST reads match body, actor identity, state, reviewed commit, target and timestamps. |
| Repository-wide inline comments | Independent successful REST pulls/comments response is an empty array, matching the retained zero. This is an observable absence, not an access failure. |
| Issue #9 and PR #6 | Independent REST Node IDs and created/updated/closed timestamps match the linked Project content. The operator's separate GraphQL sample matches Project-item timestamps, nullable direct built-in reads, parent and progress summary observations. |
| Issue #9 Project item `PVTI_lADOE410Wc4BjOE0zg6kuoE` | Fresh operator GraphQL read: Phase Foundation / `b7d09690`; Work Type Improvement / `dedea8ac`; organization Priority Medium / `IFSSO_kgDOBOJKYw`. IDs and names match normalized values and definitions. Project-item created/updated times match the package. |

The independent REST projection had differences limited to user.avatar_url, application.client_id and an added null pin property. The comparison explicitly excluded only those public profile/API projection differences and the exporter's added PR-number annotation; it did not claim full cross-API byte equivalence or suppress substantive changes. The retained snapshot remains unchanged.

The Project sample is independently executed by the maintainer; the assistant compared its returned values against the saved package. It does not prove all 5848 normalized dispositions against the live UI. Computed built-ins retain direct null observations and separately attributed provider metadata; no exact rendered display value, descendant list or inaccessible history is reconstructed. Created/Updated retain both Project-item and linked-content times because they differ. A missing or changed required observation still fails collection rather than becoming unset.

## Aggregate disposition and follow-up

No blocking mismatch was found within the selected observable profile. Readiness evidence combines A01–A05, live corrections #363–#366, 78 audit regressions, seven documentation-checker regressions, actual export/offline validation and the comparisons above. Exact candidate checks and publication remain separately recorded in A06 and the release-preparation PR. Review is AI-assisted self-review; no independent approval, current PR approval decision, provider-administration certification or product conformance follows from this result.

The maintainer owns revalidation after provider/API/schema, access, source-policy, retention or material implementation changes. Sampling cannot establish undiscoverable/deleted records or universal future endpoint availability. Preserve the original package and previous immutable release; use a fresh run for future observations and a corrective release for material defects.
