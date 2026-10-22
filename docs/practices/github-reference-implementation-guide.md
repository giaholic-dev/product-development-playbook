# GitHub Reference Implementation Guide

## Purpose

Map optional GitHub implementation choices to governed Playbook needs under the [Provider Implementation Guide Standard](../standards/provider-implementation-guide-standard.md) and [Provider-independent Integration Standard](../standards/integration-standard.md). GitHub is replaceable implementation guidance, not a required provider or the owner of methodology.

## Scope and observation context

This guide covers repository, work, planning, change, review, release, and automation records. Its connection observations apply to the GitHub connector exposed to this Codex chat on 2026-10-13, targeting `giaholic-dev/product-development-playbook`. They do not describe all ChatGPT accounts, other connectors, native GitHub UI access, or every future execution context.

Provider support is evidenced by the official sources linked below. Connector exposure is separately evidenced by the callable tool inventory and bounded observations in this chat. Exposed operations do not establish authorization or guaranteed runtime success. The connector's generic fetch operation permits approved GET endpoints only; it is not an arbitrary REST or GraphQL client. This guide does not configure a Project, create a milestone or release, or implement an adapter.

## Concept mapping

- A repository stores source-controlled Artifacts and traceable history; GitHub objects do not determine Artifact classification.
- An issue may represent a Work Item; its labels, type, and fields are optional mappings of governed dimensions, not their definitions.
- A Project item or view represents planning information. Its status field does not define Lifecycle Phase, Work Type, or protocol state.
- A milestone groups a governed delivery or decision boundary; a milestone's closed state does not prove that all governing completion criteria were assessed.
- A Pull Request records a proposed change, review, and integration. It is not a replacement for the associated Work Item.
- A release record and source tag represent publication evidence. A merged PR or closed milestone does not publish a release.
- A workflow run is automation evidence for its actual checked scope; success does not certify unexecuted checks or all work Completion.

## Optional small-repository setup recipe

This recipe applies the concept mapping above; it adds no required GitHub Project, field, status name, or automation.

1. Read the adopted taxonomy, work-item types, field, view, and milestone standards. Identify the dimensions needed for the product before configuring GitHub.
2. Inspect the actual repository, Project (if selected), existing fields/options, issues, and milestones. Reuse suitable configuration; record any mapping gap rather than inventing identifiers.
3. Prepare a mapping from each selected governed dimension to its issue metadata, Project field, or documented body record. Preserve Lifecycle Phase, Work Type, and workflow status as distinct dimensions. An issue update does not update a custom Project field.
4. Configure the selected fields and views through an authorized supported channel. If milestones are used, record their outcome, scope, owner, included-work rule, and criteria. Use the capability matrix below to distinguish provider support from this connector's exposure.
5. Try a representative work record and verify its issue metadata, Project values, planning view, and milestone membership where applicable. Record actual observed values and any collection or access limits.
6. Link the maintained mapping from the repository's governance or conformance record. Check that the first Product item can be represented without requiring capabilities the project has not established.

For closure, record acceptance, validation, review, integration, and remaining obligations before updating issue status. Separately use the [milestone and phase boundary review](milestone-boundary-review.md) to assess the combined result. A closed issue or populated Project view does not establish that boundary's completion.

## Capability matrix

The support descriptions use the Integration Standard's meanings. Supported denotes exposed scope, not a blanket runtime guarantee. This table is a dated snapshot; recheck the inventory and context before relying on it.

| Governed need and primary source | GitHub provider support | Current connector exposure | Limitation and permitted alternative |
| --- | --- | --- | --- |
| Repository reads and documentation changes — [Repository Standards](../standards/repository-standards.md), [Artifact Standard](../standards/artifact-standard.md) | Supported for repository contents and Git objects; [contents API](https://docs.github.com/en/rest/repos/contents) and [Git database API](https://docs.github.com/en/rest/git). | Supported for exposed file reads, file changes, tree/commit creation, branch creation, and ref updates. | Limited to installed repository access and tool arguments. Missing administration access is not repository administration support. An authorized human may use the native interface or another permitted Git client. |
| Work records — [Work Management](../standards/work-management.md), [Work Item Taxonomy](../standards/work-item-taxonomy.md) | Supported for issues and their metadata; [issues API](https://docs.github.com/en/rest/issues/issues). | Supported for exposed issue create/update, assignee and label operations, and reading/searching records. | Do not infer complete taxonomy-field support from issue mutation. Use a governed body record or authorized native edit for unexposed dimensions. |
| Milestone creation and lifecycle changes — [Repository Milestone Standard](../standards/repository-milestones.md) | Supported; [milestone API](https://docs.github.com/en/rest/issues/milestones). | Unsupported for create/update/close/delete: no milestone mutation tool is exposed. Issue assignment to an existing milestone is exposed through issue create/update. | Authorized human creates or updates the milestone natively, then verifies its identifier, scope, criteria, owner record, and state. Embedded issue milestone data is only partial read evidence; it does not certify the whole milestone collection. |
| Project fields, items, and views — [Project Views](../standards/project-views.md), [Repository Project Field Standard](../standards/repository-project-field-standard.md) | Supported within documented Project API scope; [Projects API guide](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-api-to-manage-projects). | Unsupported for Project-field mutation and Project configuration: no Project operation or arbitrary GraphQL execution tool is exposed. Project read completeness is Unknown in this context. | Authorized human configures or updates the native Project and records readback evidence; no update is inferred from issue changes. Issue-backed assignees, labels, milestone, and repository are distinct from Project field-value mutations. |
| Proposed changes and integration — [Branch Workflow](../standards/branch-workflow.md) | Supported; [pull request API](https://docs.github.com/en/rest/pulls/pulls). | Supported for exposed create/update/read/compare and merge operations. | Merge requires governing review and explicit scoped authorization; use expected head revision where available. If blocked, preserve the PR and use authorized native integration or defer. |
| Review records — [Code Review Standard](../standards/code-review-standard.md) | Supported; [reviews API](https://docs.github.com/en/rest/pulls/reviews). | Supported for exposed review reads/submission, reviewer requests, comments, and review-thread operations. | Tool exposure does not make the Actor an independent reviewer or authorized Approver. Missing required review uses an assigned qualified reviewer or governed recorded solo review where permitted. |
| Release publication — [Versioning Standard](../standards/versioning-standard.md), [Release Strategy](../standards/release-strategy.md) | Supported; [releases API](https://docs.github.com/en/rest/releases/releases). | Partially supported: release reads are exposed through approved fetch; release create/update/delete is not exposed. | Authorized human publishes the approved immutable source and release record natively, then verifies tag, source, notes, audience availability, and applicable criteria. No publication is claimed from a read or merge. |
| Automation evidence and invocation — [Repository Automation Standard](../standards/repository-automation.md) | Supported for documented workflow-run operations; [workflow runs API](https://docs.github.com/en/rest/actions/workflow-runs). | Partially supported: run/job/log/artifact reads and selected reruns are exposed; dispatch and permission administration are not exposed. | Read success covers only returned scope. An authorized human may invoke the appropriate native workflow; reassess permissions and duplicate effects before a rerun. Preserve unavailable evidence or deferred validation explicitly. |

## Scoped contracts, Authority, and verification

Use the [Capability Contract content](../standards/integration-standard.md#capability-contract-content) for each selected operation. The following mapping records identify the minimum implementation context without replacing those contracts:

- Repository/content: identify repository, path, branch or immutable ref, expected old revision, authorized content boundary, and intended resulting revision. Verify returned or fetched content and source reference; inspect ambiguous writes before repetition.
- Work record: identify repository and issue number, intended fields, unchanged boundaries, and applicable classification sources. Verify the issue body/metadata and state. A closed issue does not replace acceptance review or default-branch integration evidence.
- Milestone: identify repository, milestone number or intended unique boundary, included work, owner, and completion criteria. Verify existence and state after authorized native mutation. Reconcile an existing milestone before repeating creation.
- Project: identify the Project, item, field and allowed value by their actual identities. Verify the value on the intended item and preserve its governing dimension. Project access and field definitions are unverified until observed; no numeric identifiers or configuration are invented here.
- PR/review: identify repository, PR number, base/head revisions, reviewed scope, findings, and the applicable Reviewer/Approver Assignment. Verify actual merge state and default-branch revision, or the recorded review result. A request for review is not completed review.
- Release: identify approved source, release identifier, notes, audience, and publication conditions. Verify the immutable reference and published release record; inspect existing tags/releases before retrying publication.
- Automation: identify workflow/run/job, inputs, approved effects, checked scope, and retained evidence. Verify final result and material downstream effects; a rerun may repeat effects and requires the applicable contract's reconciliation rules.

For every mapping, authentication and provider permissions are access prerequisites, separate from the [Execution Authorization Check](../standards/execution-protocol.md#execution-authorization-check). The permission needed depends on the selected endpoint and credential type; consult the endpoint's current official documentation rather than assuming that a connection grants all listed capabilities. Configuration records retain only non-secret context and follow [Security, Privacy, and Data Governance](../standards/security-privacy-data-governance.md).

## Failure and bootstrap records

Rejected, partial, ambiguous, or unverified outcomes retain their evidence and use the [Integration Standard's failure and repetition rules](../standards/integration-standard.md#failure-uncertainty-and-repetition). Do not continue dependent actions on an unverified postcondition. API pagination, truncated tool responses, restricted endpoints, and unavailable observations remain explicit limits.

The following bootstrap obligations are currently outside the connector's exposed mutation scope:

- Milestones: prepare the scope, owner, criteria, and intended state; an authorized human performs the native operation and records its verified result. Until then, an intended milestone or requested closure remains pending.
- Project configuration and field mutation: prepare the governed dimensions and values; an authorized human applies them and records the Project/item/field observations. Existing issue metadata does not prove Project configuration.
- Release publication: prepare approved source, notes, and conditions; an authorized human publishes and verifies the result. An unpublished version remains an intended target.
- Unexposed automation dispatch or administration: identify the approved workflow and effects; an authorized human executes or configures it and retains run and state evidence.

If native access, required Authority, or verification is unavailable, preserve the obligation and apply governed Defer, Block, or permitted Exception treatment. Another authorized provider or manual record may fulfill a need only when it satisfies the same governing contract. Switching channels does not expand Authority.

## Evidence and conformance review

This snapshot was validated by reading official GitHub documentation and separately inspecting exposed connector schemas on 2026-10-13. Schema inspection found content/Git, issue, PR/review, selected workflow evidence/rerun operations, but no milestone mutation, Project-field mutation, release publication, or arbitrary GraphQL execution tool. This absence is scoped to the exposed connector inventory, not native GitHub.

Bounded live evidence includes [PR #293](https://github.com/giaholic-dev/product-development-playbook/pull/293), [PR #294](https://github.com/giaholic-dev/product-development-playbook/pull/294), and [PR #295](https://github.com/giaholic-dev/product-development-playbook/pull/295): authorized content publication, merge, issue updates, and subsequent reads were observed. No milestone, Project configuration, release publication, or workflow dispatch was performed to test this guide. Historical exporter evidence is not proof of current connector Project exposure.

The review checks each mapping against its governing need, separate provider/connector support, scope, Authority, expected result, verification evidence, failure treatment, and fallback. It establishes documentation mapping coverage; it does not globally certify a provider, execute every mapped operation, or complete adopting product work.

## Ownership and maintenance

This file is the maintained source for this GitHub mapping. The adopting repository identifies its accountable maintainer under the [Roles and Actor Assignment Standard](../standards/roles-and-actor-assignment.md); authorship alone does not establish permanent Accountability. The governing work and review record identify responsibility and validation for each revision.

Reassess affected mappings whenever exposed tools, installation access, permissions, provider behavior, configuration, governing standards, or execution context change. Before reuse, compare the dated snapshot to the current interface. Preserve prior observations as history and mark unresolved current support Unknown. Another provider guide can replace this file without redefining the core standards.

## References

- [Provider Implementation Guide Standard](../standards/provider-implementation-guide-standard.md)
- [Provider-independent Integration Standard](../standards/integration-standard.md)
- [Execution Protocol Standard](../standards/execution-protocol.md)
- [GitHub REST API documentation](https://docs.github.com/en/rest)
