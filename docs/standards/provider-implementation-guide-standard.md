# Provider Implementation Guide Standard

## Purpose

Define how maintained provider-specific guides map external systems to the Playbook's integration requirements without making a provider part of the normative methodology.

## Scope

This standard governs guide content, source traceability, verification evidence, ownership, and maintenance. A Provider Implementation Guide is non-normative implementation guidance for a named provider and a defined execution context. Its instructions describe an optional mapping; they do not redefine lifecycle policy or Capability Contracts.

The [Provider-independent Integration Standard](integration-standard.md) owns integration semantics, Capability Contracts, discovery, contextual support descriptions, Verification, Failure, Fallback, and Conformance. The [Execution Protocol](execution-protocol.md) owns attempt semantics. [Roles and Actor Assignment](roles-and-actor-assignment.md) owns Authority and Accountability. A guide MUST link to those sources where applicable rather than defining competing rules.

## Required guide content

A maintained guide MUST make the following content discoverable, proportionate to its scope. Existing records may be linked rather than copied; no fixed document layout, tool, or machine format is required.

- Identity and scope: named provider, intended audience, execution environment or connection, applicable versions or observation date, included capabilities, exclusions, and non-normative status.
- Governing sources: the Playbook needs and Capability Contracts being mapped, including their primary owners.
- Provider concepts: the relevant provider objects or operations, how they map to governed needs, and where the mapping is incomplete or lossy. A provider label MUST NOT silently replace a Playbook concept.
- Capability mapping: separate evidence-based descriptions of provider support and current Integration exposure, with the exact supported scope, constraints, and unresolved requirements.
- Authority and permissions: applicable scoped Authority, required approvals, provider access prerequisites, and limits. Access or a permission setting MUST NOT be represented as authorization for all exposed operations.
- Configuration: necessary setup, relevant options, environment assumptions, and how configuration can be verified. References to credential handling MUST preserve the [Security, Privacy, and Data Governance Standard](security-privacy-data-governance.md); secrets MUST NOT be included in guide content or evidence.
- Verification: expected observable results, how target identity and contract postconditions are examined, what evidence is retained, and limitations such as delayed visibility, partial reads, pagination, or truncation where relevant.
- Failure and repetition: rejected, partial, ambiguous, unavailable, and unverifiable outcomes, including the contract's repeat/idempotency and reconciliation rules where applicable.
- Manual or alternative fallback: permitted paths for each unsupported or partially exposed material capability, preserving Authority, Accountability, evidence, and governing completion criteria. When no permitted path exists, explicitly identify the unresolved obligation and governing treatment.
- Conformance evidence: the scoped evidence required by the Integration Standard, known gaps, validation performed, and the boundary between external Verification and work Validation or Completion.
- Ownership and maintenance: the maintained guide's primary source, accountable owner where required, evidence provenance, and reassessment conditions.

Missing or unknown information MUST remain explicit. A guide MUST NOT manufacture a provider capability, connector operation, completed configuration, verified external effect, approval, or conformance claim to fill a required section.

## Provider and current Integration separation

For each material mapped Capability, use the [Integration Standard support descriptions](integration-standard.md#discovery-and-support-descriptions) for the provider and current Integration separately. Record their evidence sources, date or revision, context, limitations, and reassessment trigger. An absent exposed operation establishes only the evidenced limitation of that context; it does not establish that the provider lacks the feature.

Provider documentation may evidence native support. It does not alone evidence connector exposure, permissions, or attempt-level Capability Availability. A read-only interface inspection may evidence exposure but not the outcome of a write. A hypothetical demonstration MUST be labeled hypothetical; an unperformed action MUST NOT appear as live validation.

Support descriptions remain contextual. A guide MUST distinguish Unsupported from Unknown and identify the usable subset of Partially supported behavior. The guide MUST NOT map these descriptions into Workflow States, Protocol States, or automatic completion decisions.

## Instructions and verification boundaries

Instructions MUST identify their intended target and scope, required preconditions and Authority sources, expected result, verification method, and failure/fallback references. They MUST preserve the relevant Capability Contract rather than copying or changing its semantics.

Consequential instructions MUST make their effects and approval boundaries understandable before execution. A guide is not authorization to perform its instructions. Request acceptance remains distinct from verified external state change; following documented steps does not establish that they succeeded.

If provider behavior cannot fulfill a governing requirement, identify the gap and permitted treatment. Do not weaken the requirement through a provider-specific workaround. Manual procedures and another provider may replace the mapping where they satisfy the same applicable requirements; adopting the Playbook does not require adopting this guide.

## Maintenance and evidence

The guide MUST have one discoverable maintained source. Identify its owner, scoped validation evidence, and relevant provider/interface/configuration revision or observation date. Follow the [Artifact Standard](artifact-standard.md) for provenance and the [Code Review Standard](code-review-standard.md) for repository changes.

Reassess affected mappings when governing sources, provider behavior, exposed interfaces, permissions, configuration, or the execution environment change, or when observed results contradict the guide. Preserve the provenance of earlier observations without presenting them as current verification. Stale or inconclusive support becomes explicit uncertainty pending reassessment.

An update MUST distinguish changed guidance from changed normative rules. Any proposed normative change belongs to its primary owner and normal repository governance. This standard does not prescribe a universal maintenance interval or certify every future use of a connection.

## Guide conformance review

Before treating a guide as maintained implementation guidance, review its required content and applicable mappings against this standard and the Integration Standard. Record the examined scope, sources, evidence, outcome, unresolved gaps, and reassessment condition. A partial guide MUST identify its incomplete scope; it MUST NOT claim conformance for missing obligations.

Verify internal references and discoverability under the [Documentation Navigation Standard](documentation-navigation.md). A reviewer assesses the mapping and evidence, not whether the guide makes the provider mandatory. Each guide remains replaceable while the governing needs and contracts remain authoritative.

Use the [Provider Implementation Guide template](../../templates/provider-implementation-guide.md) as optional starting material. The template is not itself proof of conformance.

## Non-normative hypothetical review

Consider a hypothetical provider called Record Service and a connection called Read/Update Session. These names describe an invented scenario, not real software or live capability evidence.

The hypothetical guide maps a provider document object to a governed documentation Artifact. The mapping preserves the Artifact's owner and evidence obligations; it does not treat the provider's object type as the Playbook's Artifact classification.

For document reads and updates, the scenario assumes provider support is Supported. The session exposes read and revision-checked update but no approval operation. The guide records separate support descriptions: Supported for read, Supported for the bounded update, and Unsupported for session approval despite assumed provider support. A permissions summary identifies read/update access separately from the Actor's scoped Authority and any governing approval requirement.

The guide records a configured target and expected revision as hypothetical prerequisites. Its update instructions identify the content boundary, result, and readback check; an acknowledgment alone does not verify the content. A partial read cannot evidence a contract requiring the complete document. A timeout requires reconciliation against the current revision before repetition. The guide links to the governing failure and disposition rules rather than defining retry states.

For approval, an authorized human may use a separate permitted channel and retain the decision evidence. If this is unavailable or unauthorized, the obligation remains unresolved and receives governed treatment. The guide does not claim that content update or manual fallback establishes work Completion.

The review checks the scope, concept mapping, contracts, two support descriptions, permissions, hypothetical configuration, Verification, failures, fallback, and conformance evidence. Its conclusion is that the scenario illustrates conformant guide structure and ownership boundaries; it does not verify an actual provider or connection. A real maintained guide would require dated provider and connection evidence and actual scoped validation. Its named maintainer would reassess the guide on interface, configuration, permission, or governing-standard changes. The same contracts remain usable through another provider or permitted manual approach.

## References

- [Provider-independent Integration Standard](integration-standard.md)
- [Execution Protocol Standard](execution-protocol.md)
- [Roles and Actor Assignment Standard](roles-and-actor-assignment.md)
- [Work Management Standard](work-management.md)
- [Artifact Standard](artifact-standard.md)
- [Security, Privacy, and Data Governance Standard](security-privacy-data-governance.md)
- [Code Review Standard](code-review-standard.md)
- [Documentation Navigation Standard](documentation-navigation.md)
