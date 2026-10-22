# Audit Package Coverage and Compatibility Contract

## Decision, scope and authority

A01 / [#326](https://github.com/giaholic-dev/product-development-playbook/issues/326) selects the coverage below for the optional GitHub audit exporter and M7 / v0.7.0. Assessment: 2026-10-22, source `ce483c4d7668ceff0b1a6e831f1b1b51c1aca4c4`, exporter 1.0.1 and manifest 1.0.0. The maintainer @giaholic authorized this bounded research/decision increment. The decision takes effect through its reviewed integration; the PR/issue retains the exact head, validation and integration decision. This document does not implement the proposed collectors or publish v0.7.0.

This is a repository-specific tool contract, not a Playbook standard or methodology machine-execution schema. [Integration](../standards/integration-standard.md), [Execution Protocol](../standards/execution-protocol.md), [Artifact Standard](../standards/artifact-standard.md), [Security, Privacy, and Data Governance](../standards/security-privacy-data-governance.md), and existing work/review/release owners remain authoritative. Exporter JSON cannot supply Approval, Authority, work Completion or conformance certification.

Selected outcome: retain the declared repository source and its issue/PR/Project evidence for offline inspection, with explicit identities, coverage, integrity and observation limits. Collection is read-only against GitHub; local staging/ZIP writes are authorized separately by the export operator for the selected repository, Project, destination, data scope and retention. Access alone does not authorize redistribution or broader data collection.

## Baseline findings and alternatives

The assessed exporter copies selected working-tree documentation/configuration while its manifest names HEAD; dirty bytes may therefore differ from the declared commit. Its tree listing is not source bytes. It exports PR metadata and inline review comments, but filters PR conversations from issue comments and does not collect review submissions. Project items contain content identity but no field values. The manifest has aggregate counts and optimistic pagination flags, without retained nested-connection evidence or source-byte hashes. Optional Discussions output is outside the current manifest integrity list.

Alternatives considered:

- Retain the current scope and only improve documentation: rejected for M7 because its promised source/PR/Project outcome would remain absent.
- Copy the whole working tree and every available provider collection: rejected because it mixes source revisions, untracked credentials/generated files and unrelated data without a bounded audit need.
- Immutable tracked-source snapshot plus explicitly enumerated provider collections: selected. It supports review questions while exposing authorization, missing data and compatibility limits.

The historical 1.x implementation remains usable only within its documented limits. A01 does not retroactively certify its packages.

## Audit questions and required coverage

All required collections below are required for a successful full-profile package. A legitimately empty complete collection is retained as an empty array with positive traversal evidence, not inferred from a missing response.

| Offline audit question | Required retained evidence | Identity, relation and limit | Implementation owner |
| --- | --- | --- | --- |
| What exact repository source was assessed? | Committed tracked-file bytes, complete tracked-tree inventory, exclusions, original file modes, sizes and content hashes. Includes README, docs, templates, examples, scripts, .github and .devcontainer when tracked. | Repository host/owner/name, resolved commit and tree; working-tree edits are not represented as committed bytes. | A02 / #327 |
| Which work and planning records were observed? | All visible issues and PR metadata, issue comments/timelines, labels, open/closed milestones and release records in the selected repository, without state/date filters. | Provider IDs, repository-qualified numbers/URLs, bodies, state, supplied timestamps, issue/PR distinction and source collection. No deleted-history reconstruction. | Existing collectors, A05 / #330 |
| What was discussed and reviewed on each PR? | Separate PR conversation comments, submitted reviews and inline review comments for every collected PR. | PR relation, comment/review identities, author when available, body, state/timestamps, reviewed commit and inline file/reply/review references when supplied. Review observations do not prove current merge approval. | A03 / #328 |
| What classification/planning values did Project items actually have? | Selected Project identity, all visible active/archived items returned by its API, field definitions/options, actual item values and per-item value traversal evidence. | Project/item/field/option or iteration IDs, provider type, item kind, linked content identity and availability. Includes Phase, Work Type, Status and other configured planning fields under the policy below. | A04 / #329 |
| What Project views were observed? | View identities, numbers, names and layouts returned by the current view collector. | Project-qualified IDs and pagination. Filters, sort/group settings, workflows and access administration are excluded; layout is not classification evidence. | Existing collector, A05 |
| What local refs/history contextualize the source? | Local branch/tag inventory and recent-commit/status evidence, explicitly labeled local and bounded to the latest 100 commits. | Resolved source remains authoritative; local remote-tracking refs may be stale. No full Git history, remote-ref freshness or signature certification is promised. | A02/A05 |
| Can package claims be verified offline? | Versioned manifest, per-source/collection inventory, traversal/count/status evidence, file hashes and relationship-validation results. | Every required row must be satisfied in its declared scope; ZIP readability alone is insufficient. | A05 |
| Was optional Discussions collection selected? | Disabled/excluded disposition, or all declared visible discussion metadata/bodies when enabled, with the same status/count/integrity treatment. | Discussion comments, replies, attachments and history are excluded. Enabled collection failure cannot be hidden. | A05 |
| Does the completed implementation match live evidence? | A06 comparison record linking representative repository bytes, PR conversation/review/inline records and Project values to package observations. | Authorized interval and sampled limits; fixture and live evidence remain distinct. | A06 / #331 |

Repository issues/PR metadata include available title/body, author, state, created/updated/closed/merged timestamps, labels, assignee/milestone references and PR base/head/merge identities. Retain available review states including APPROVED, CHANGES_REQUESTED, COMMENTED and DISMISSED; preserve supplied review commit/submission timestamps. Superseded reviews remain separate observations. Pending private/draft reviews not visible to the authorized identity are not reconstructed or declared absent. Do not claim review-thread resolution history if the selected API does not supply it.

## Source snapshot and privacy policy

Resolve HEAD once at start, retain its commit/tree identities and read tracked blobs from that Git object tree. No implicit fetch, checkout, working-tree reset, submodule initialization or credential change. A dirty working tree is allowed, but the manifest must state that dirty/staged/untracked bytes are excluded and the snapshot is the selected commit. Capture initial/final HEAD and dirty status; a source-ref change during collection fails rather than mixing candidates.

Enumerate the complete selected tracked tree using an unambiguous path representation, including names containing spaces/newlines. Retain each path, Git mode/object ID, declared disposition, byte size and SHA-256 of retained content. Content hashes verify transport integrity, not trusted authorship. Preserve binary bytes and executable modes in the record. Do not follow symlinks: retain the link blob as inert regular bytes and its original symlink mode, so extraction cannot dereference it. Reject absolute/traversal/duplicate archive destinations and any extraction path escaping the package root.

Submodule gitlinks and Git LFS pointer blobs retain their original identities, explicitly identifying that referenced content was not collected. No automatic external fetch. A requested constituent requiring those missing bytes cannot be declared covered; its source needs an explicitly authorized separate scope. An inventory entry alone is not a full constituent snapshot.

Never copy .git internals, untracked files, ignored working files, audit output, downloaded caches or external attachments. A tracked file remains subject to the sensitivity policy, even inside an approved directory. Selected default exclusions are path components .git, .ssh and .aws; .env and .env.* basenames except the template candidates .env.example/.env.sample; basenames .netrc, .npmrc, .pypirc, .git-credentials, credentials.json and service-account*.json; private-key basenames id_rsa, id_dsa, id_ecdsa and id_ed25519; and suffixes .key, .pem, .p12 and .pfx. These are case-insensitive basename/component matches, not broad substring rules. Templates still require sensitivity review. Paths under the configured output directory are excluded even if tracked. Retain the exact applied list and every matching tracked path/disposition in the inventory; test the policy. Certificate/public-key false positives can require a reviewed source-policy revision, never a silent ignore. This allow/exclude policy does not guarantee that all secrets are detected.

Before copying, identify the selected source/record classes and applicable data risks. Suspected credential material or unapproved sensitive content stops collection for review; never print secret values in diagnostics. Excluding a protected tracked file records path/disposition/reason without its bytes or secret-derived payload. Required audit-source exclusion blocks the applicable coverage claim; do not silently shrink scope after a failure. Authorized redaction must record the affected fields/records and cannot be represented as byte-exact unredacted evidence.

Provider bodies can contain private data even for an otherwise public repository. Limit collection to the selected repository and Project; do not recursively fetch linked repositories, users' private profiles, attachments or secrets. Use minimum read access already authorized. Retain only provider identity metadata needed for traceability; no tokens, auth headers, full credential-bearing URLs or request environment dumps. Preserve private actor absence as null/unavailable, not a guessed identity.

Output remains owner-only under the existing umask and approved destination. The operator owns retention/deletion and disclosure decisions before an actual export; A01 sets no universal retention period and grants no publication permission. Retrying uses a new run identity/path and never overwrites a prior export or combines attempts as one complete observation.

## Project value policy

The profile covers configured scalar/planning values, not just field definitions. Each normalized value retains its Project ID, item ID, field ID, observed provider typename, typed value, supplied value ID/timestamps and origin (Project custom field or organization issue field). Never infer Phase or Work Type from a title, label, view or workflow position.

Required typed support: text, number, date, single-select, multi-select and iteration values where offered by the provider, including organization issue-field wrappers for text/number/date/select values. Retain selected option IDs/names (multiple IDs for multi-select), and iteration ID/title/start/duration when supplied. Field definitions retain the corresponding option/iteration identity, including completed iteration options if referenced. Numeric zero, empty text and an absent value are distinct.

Built-in linked metadata (repository, assignees/users, labels, milestone, linked PRs and reviewers) is retained in typed relationship records with IDs/URLs available to the authorized read, not coerced to a custom string or counted as scalar classification. Any returned nested connection included in this policy must be fully paginated. A04 may reuse repository metadata where it represents the same observed relationship and identity; it must not substitute unrelated issue state for a Project value.

Enumerate the Project once, then traverse each item's field-value connection independently. Retain an observation for every item/selected field, distinguishing value present, observed unset after complete traversal, inapplicable to that item kind, inaccessible/redacted and unsupported/unknown type. A field missing from a partial response is never "unset." Unsupported new types or wrappers affecting required coverage fail the full profile until reviewed; do not silently discard unknown union members.

The selected Project is identified by owner kind/login, number, node ID and URL. Preserve active/archived state where supplied. A visible Project may contain drafts, redacted content or items from other repositories: retain minimum item identity/disposition, not those foreign bodies or recursively collected records. References outside the selected repository are explicitly external, not dangling local issue references. Deleted, undiscoverable or access-filtered items remain outside observable history; count parity cannot prove the caller can see everything.

## Observation, pagination and completeness

Repository source is immutable; provider records form an interval observation, not an atomic snapshot. Record UTC start/end for the run and each collection, target identity, actual API version/endpoint or query fingerprint, selected principal identity without credentials, request/page counts and terminal evidence. Record material count/revision changes seen during traversal; if they make required relationships or completeness inconclusive, fail and retry as a new run.

REST collections must follow all next links until exhausted. GraphQL collections must advance each connection's own cursor until hasNextPage is false. An outer item cursor does not paginate nested values; nor does a single per-PR page cover reviews. Detect repeated/nonadvancing cursors, inconsistent terminal data, HTTP/GraphQL errors (including errors with partial data), truncation and retry exhaustion. Do not retain full request headers/secrets to prove traversal.

Keep records before deduplication and conflict checks logically distinguishable by observed counts. Identical replayed records can deduplicate by scoped provider identity; conflicting payloads under one identity fail instead of arbitrarily choosing a winner. Timeline events without provider IDs retain the existing scoped identical-payload behavior; no durable event identity is invented. Missing required IDs, invalid types, duplicate final IDs, invalid local references and mismatched counts/hashes fail validation.

Collection statuses are exporter-specific: complete, partial, unavailable, excluded. Excluded requires an explicit predeclared optional/out-of-scope reason; it cannot describe a failed required read. Successful empty is complete with count zero and terminal evidence. Inaccessible required Project, denied review access, unsupported required value, rate-limit exhaustion or unresolved required source evidence produces no successful full-profile package.

Chosen failure policy: nonzero exit, no final successful directory/ZIP/summary; clean staged sensitive data using the existing guarded cleanup scope. A sanitized diagnostic can identify collection/target/error category and the unmet need. Diagnostic-only partial packages are not introduced by M7. If archive creation or post-compression verification fails, remove/quarantine the current run's unpublished output safely and never present it as published. Do not delete prior runs. This strengthens the current publish-before-compress sequence and is part of A05 acceptance.

Completeness means all declared authorized observable collections traversed and validated within the recorded interval. It does not mean all GitHub data/history, an atomic snapshot, universal access or a full governance audit.

## Manifest and version compatibility decision

Select manifest schema 2.0.0 and exporter tool 2.0.0 for the completed coverage implementation; leave current constants unchanged in A01. The incompatible major is intentional: successful completeness now requires source/PR/value evidence absent from 1.x. v0.7.0 is the Playbook release label, not either tool/schema version.

Preserve the existing exports/<run>/ root and repository/git/github responsibilities where practical. Preserve legacy named collection files/metadata where meanings remain the same. Add separate PR conversations, submitted reviews, Project values and source/coverage inventory; do not rename inline comments into review submissions. Exact payload paths are listed once in the implemented manifest, with source-to-package path mapping. A02–A05 own serialization and fixtures, under this contract.

The schema-2 manifest must contain:

- Contract identifier audit-package-coverage/2.0.0, schema/tool versions, repository identity, selected commit/tree/ref, dirty policy, source policy/exclusions and selected Project identity.
- Observation intervals and actual collection strategy/version context.
- Every required/selected optional collection with path, required flag, status, raw/unique/retained counts as applicable, traversal evidence, explicit exclusions/unavailability and per-parent completion for nested traversal.
- Source-file inventory and SHA-256/size inventory for every retained payload file except the manifest itself; manifest coverage of its own hash is deliberately excluded to avoid self-reference. Retain a separate manifest digest beside the completed archive, without claiming tamper-proof authenticity.
- Relationship/integrity check results and overall full-profile completeness derived from required records, not a hard-coded all-true flag.

Legacy collection_counts and collection_pagination may remain as derived compatibility summaries; they cannot contradict detailed status or establish completeness by themselves. Schema-aware readers must reject unknown major versions for full validation. They may tolerate documented additive minor fields without ignoring unknown required collection/type obligations. Patch versions preserve the same contract; additions changing required coverage need a reviewed minor/major decision and migration notes.

A schema-2 reader can identify schema 1.x for limited historical inspection, but must report that the coverage contract is not satisfied. Never relabel old packages or manufacture missing evidence. Migration means a new authorized export from an explicit source and a new provider observation interval; retain the old package unchanged. No automatic converter or universal JSON Schema/parser is delivered by A01.

## Bounded acceptance for dependent work

| Work | Required acceptance scenarios |
| --- | --- |
| A02 | Clean and dirty repos yield committed bytes at the selected identity; scripts/.github/.devcontainer, binary content, unusual paths and modes are preserved; symlinks stay inert; protected/untracked/output files do not leak; missing required blobs or changed source identity fail; gitlink/LFS limits are explicit. |
| A03 | Multiple PRs/pages preserve conversations, approvals/change requests/dismissed and superseded reviews, and inline reply/review/commit links; zero reviews differs from denied/truncated access; duplicate conflicts and foreign PR references fail. No current approval is inferred. |
| A04 | More than one item and value page, all supported scalar/planning and organization issue-field types, completed iterations, nested relationship pages, null/unset/zero/empty, drafts/archived/redacted/foreign items, missing field/option and unknown types are exercised. Partial nested observations cannot claim complete. |
| A05 | Missing required source/collection, malformed/partial API data, nonadvancing cursor, duplicate/conflicting identity, invalid local reference, bad count/hash, unsupported major and ZIP failure fail safely; optional disabled/selected Discussions have explicit treatment; a legacy package is never validated as full profile. |
| A06 | Run documented checks and an authorized end-to-end export; independently compare representative real source, PR conversations/reviews/inline comments and Project values, including omission/permission limits. Record interval, privacy/retention decision, exact source/tool/schema and aggregate/release evidence. Sampling does not certify every historical record. |

Fixtures may use small page sizes to force the same traversal boundaries; include a case where item pagination finishes but value pagination does not. Include positive and intentionally invalid controls, preserving C01's false-result regression. A02–A05 are separate increments with their own readiness, validation, review and documentation; approval of this contract does not declare their implementation ready or complete.

## Decision review and maintenance

Reviewed alternatives against the v0.6.0 omissions, M7 promise and primary ownership. Conceptual cases cover committed versus dirty bytes, a required denied Project, review-history versus approval, nested pagination, foreign/redacted items, optional Discussions and schema-1 compatibility. The selected failure/coverage rules preserve missing evidence rather than turn it into absence or success.

This is source-based design/research and recorded AI-assisted self-review, not a live export, independent approval, provider-access certification or M7 completion. The reviewed PR supplies acceptance/integration evidence. @giaholic owns reassessment on contract, provider type/API, access, retention, source-policy or compatibility changes. Any reduction of M7's promised coverage requires explicit milestone/scope review, not a silently narrower collector.

## Sources

Existing implementation assessed at the pinned source: [exporter](../../scripts/export-audit.sh), [checks](../../scripts/check-export-audit.sh), [v0.6.0 limits](../releases/v0.6.0.md), [remediation plan](playbook-remediation-plan.md).

Official provider references checked on 2026-10-22: [issue/PR conversations](https://docs.github.com/en/rest/issues/comments), [review submissions](https://docs.github.com/en/rest/pulls/reviews), [Project object/value reference](https://docs.github.com/en/graphql/reference/projects), [GraphQL pagination](https://docs.github.com/en/graphql/guides/using-pagination-in-the-graphql-api). These describe provider capabilities; the selected implementation and authorized connection still need scoped verification.
