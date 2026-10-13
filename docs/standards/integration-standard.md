# Provider-independent Integration Standard

## Purpose

Define the boundary for using external systems during Playbook execution while preserving human-only execution, scoped Authority, and accountable Verification.

## Scope

This standard owns Integration, Capability, Capability Contract, Capability Discovery, contextual support descriptions, integration Verification, Failure handling, Fallback boundaries, and integration Conformance. It does not require an Integration, provider, adapter, execution application, or machine-readable representation.

The [Execution Protocol Standard](execution-protocol.md) retains ownership of attempt-level Capability Requirement, Capability Availability, authorization checks, Protocol Results, evidence linkage, and Execution Dispositions. [Roles and Actor Assignment](roles-and-actor-assignment.md) owns Authority and Accountability; [Work Management](work-management.md) owns Blocking, Validation, Completion, and Re-entry. Integration evidence does not replace those decisions.

## Definitions

### Integration

An Integration is an arrangement through which an execution context accesses an external system's capabilities for governed Playbook work. It may involve a connector, interface, or human-mediated exchange; these are implementation choices, not prerequisites.

### Capability

A Capability is an action or result that a system or execution arrangement can support within a defined scope. A provider is the external system or service offering capabilities. Provider support describes what that provider offers; current Integration support describes what the particular connection or arrangement exposes in its actual context.

Provider support MUST NOT be treated as evidence that a current Integration exposes the same Capability. Integration support MUST NOT be treated as Authority to use it or as proof that an attempt will succeed. Attempt-level Capability Availability remains governed by the Execution Protocol.

### Capability Contract

A Capability Contract is the provider-independent description of the conditions, expected observable result, and evidence necessary to use and verify a Capability within a defined scope. It describes meaning and boundaries rather than an API, vendor object, or implementation mechanism.

### Capability Discovery

Capability Discovery is the evidence-based identification of the Capabilities exposed by a particular Integration, including their scope, limitations, and unresolved support. Discovery is contextual; it does not authorize execution or replace the attempt-level availability check.

### Integration Verification

Integration Verification is examination of an observable external result or state against the applicable Capability Contract. It establishes only the result and scope actually evidenced. It is distinct from Work Management Validation, Approval, Completion, or release.

### Integration Failure and Integration Fallback

An Integration Failure is an observed inability to fulfill an applicable Capability Contract, including a rejected request, incomplete result, or failed Verification. An ambiguous outcome is unresolved, not automatically proof of failure or success.

Integration Fallback is an alternative permitted approach to fulfilling the governed need when the chosen Integration cannot do so. The protocol-level `Fallback` disposition remains owned by the Execution Protocol; this standard governs the external-capability boundary of the alternative approach.

### Integration Conformance

Integration Conformance is evidence that a scoped Integration use satisfies this standard and its applicable Capability Contracts. It is not a global certification of a provider or a declaration that a Work Item is complete.

## Capability domains

Derive applicable domains from governed work, rather than selecting a vendor's object model as the methodology. Examples of domains and their primary sources are:

- Repository and change tracking: [Repository Standards](repository-standards.md) and [Branch Workflow](branch-workflow.md).
- Work and planning records: [Work Management](work-management.md), [Work Item Taxonomy](work-item-taxonomy.md), and [Project Views](project-views.md).
- Documentation and evidence: [Artifact Standard](artifact-standard.md) and [Documentation Navigation](documentation-navigation.md).
- Review records: [Code Review Standard](code-review-standard.md).
- Release and operational records: [Release Phase](../lifecycle/06-release.md) and [Maintenance Phase](../lifecycle/07-maintenance.md).
- Authorized automation: [Repository Automation](repository-automation.md) and [AI Collaboration](ai-collaboration.md).

These examples do not require every Integration to implement every domain. A chosen Capability MUST map to its governing need and applicable sources; provider-specific mappings MUST NOT redefine those sources.

## Capability contract content

Each relied-upon Capability MUST have an identifiable contract proportionate to its risk and scope. A contract may be a concise record with links to existing sources; no separate document or format is mandatory. It MUST identify:

- Purpose and scope: the governed need, action, target, and relevant boundaries.
- Inputs: required identifiers, data, source revision or expected state where relevant, and input constraints.
- Outputs: the expected observable result, identifiers, and distinction between an acknowledgment and a fulfilled outcome.
- Preconditions and postconditions: the conditions for reliance and the state or result to examine afterward.
- Authority: the applicable source of scoped permission and any required approval, without inventing a Role or transferring Accountability.
- Evidence: how results, target identity, limitations, and material execution context remain discoverable under applicable artifact and data-governance rules.
- Failure and uncertainty: rejected, partial, unavailable, ambiguous, or unverifiable outcomes and their applicable treatment sources.
- Verification and Validation: the external observation that verifies the contract, its limits, and the separate governing criteria for work Validation.
- Repeat and idempotency behavior where relevant: whether repetition may duplicate an effect, how an earlier effect can be detected, and applicable reconciliation or recovery boundaries. If not relevant, record why.

A contract MUST preserve the linked Protocol Preconditions, Protocol Postconditions, Authority, and evidence obligations rather than defining competing meanings. [Security, Privacy, and Data Governance](security-privacy-data-governance.md) governs applicable data, credential, access, retention, and risk decisions. Credentials do not belong in a capability description or evidence record.

## Discovery and support descriptions

Before relying on an Integration, identify its exposed operations, relevant permissions, limits, and evidence source. Documentation, exposed interfaces, configuration, or bounded observations may supply evidence. Discovery MUST NOT perform a consequential mutation solely to infer support without applicable Authority.

For each material Capability, record provider support and current Integration support separately. Each description MUST identify the context, evidence, observation date or revision, material limits, and reassessment trigger. Use the following support meanings:

- `Supported`: evidence shows that the described scope is exposed in that context; attempt-level availability and authorization still need checking.
- `Partially supported`: evidence shows that a defined subset is exposed, with explicit missing or constrained behavior. The supported subset and unmet contract obligations MUST be identifiable.
- `Unsupported`: evidence establishes that the Capability is not exposed in that context.
- `Unknown`: sufficient evidence to determine support is absent, inaccessible, outdated for the intended use, or inconclusive. Unknown MUST NOT be silently treated as Supported or Unsupported.

The two descriptions may differ. A supported provider Capability may be unsupported or unknown in a current Integration. These are contextual support descriptions, not Protocol States, Workflow States, or replacements for Capability Availability. A runtime outage alone does not establish that a provider never supports the Capability.

Reassess material support when the interface, permissions, configuration, relevant provider behavior, or execution environment changes, or when observed behavior contradicts the record. Unverified historical support MUST NOT be presented as confirmed current support.

## Authorization boundary

Before an external action, the governed attempt MUST satisfy the [Execution Authorization Check](execution-protocol.md#execution-authorization-check) against applicable [Authority](roles-and-actor-assignment.md#accountability-and-authority). Access, authenticated connection, discovered support, or an assigned Role alone does not establish permission for the intended action.

The contract MUST make the relevant action and target scope identifiable. Required approval remains owned by its governing source. Delegation, switching providers, or choosing a fallback MUST NOT silently expand Authority or transfer Accountability.

## Verification and evidence

A request acknowledgment or success response MUST NOT, by itself, be represented as a verified external state change. Evaluate the returned evidence against the contract. A response may suffice when it directly and reliably evidences the required result; otherwise use an authorized observation of the affected external state.

Verification MUST identify the target, intended outcome, observed result, observation context, and material limits. For reads, check the requested identity, scope, completeness, pagination, revision or currentness where relevant, and truncation. For writes, check the intended target and postconditions; distinguish accepted requests, completed actions, partial effects, and verified outcomes.

Delayed visibility, unavailable observations, or conflicting evidence MUST remain explicit. Record the outcome as unresolved until sufficient evidence exists; do not manufacture certainty or assume that a retry is safe. Evidence retention and disclosure follow the Artifact and Security, Privacy, and Data Governance standards.

Verification of an external result does not establish all applicable work Validation, review, Approval, Completion, or release conditions. Those remain separately evaluated under their governing sources.

## Failure, uncertainty, and repetition

When a request is rejected or produces partial, ambiguous, or unverifiable results, preserve material evidence of what was requested, what was observed, and what remains unknown. Do not run dependent actions that assume an unverified postcondition.

Before repeating a potentially effectful action, inspect whether the original action may already have taken effect and apply its repeat/idempotency contract. A timeout does not prove that no mutation occurred. When reconciliation cannot establish a safe next action, preserve the unresolved condition and use applicable protocol treatment and Work Management decisions. This standard prescribes no retry count, delay, recovery algorithm, or universal failure state.

## Unavailable capabilities and manual execution

An unmet material Capability Requirement MUST receive explicit treatment under the [Execution Disposition](execution-protocol.md#execution-disposition) rules. Identify the unresolved contract obligation and applicable evidence; do not infer that partial support satisfies the whole need.

Where permitted, an authorized manual or alternative approach may fulfill the same governed need. A fallback MUST preserve applicable Authority, Accountability, evidence, Verification, Validation, and completion requirements. Record the change in approach when material to traceability. Fallback is a new applicable execution context, not proof that the unavailable operation succeeded.

If no permitted alternative exists, use applicable `Defer`, `Block`, or `Exception` treatment rather than silently bypassing the requirement. Work Management owns resulting Blocking, ordering, or Re-entry decisions; the applicable governance owns exception permission. Unavailability does not authorize an Exception automatically.

Without any Integration, people can use the lifecycle, standards, checklist, and evidence records directly. An external need may be handled manually when governing requirements permit. If a need cannot be fulfilled manually or externally, it remains explicit and receives governed treatment; human-only execution does not waive mandatory outcomes.

## Conformance evidence

A scoped conformance record MUST make the following evidence discoverable, proportionate to the use:

- Governing need, sources, and applicable Capability Contracts.
- Separate provider and current Integration support descriptions, including uncertainty and limits.
- Applicable Assignments, Authority, and risk/data-handling decisions.
- Verification method, observed results, and unresolved conditions for material attempts.
- Failure, repeat/idempotency, and permitted fallback treatment where relevant.
- The boundary between Integration Verification and work Validation, Approval, and Completion.
- An identifiable accountable owner where required by governing rules, and a reassessment condition.

A missing requirement MUST remain visible rather than being concealed by a broad conformance claim. Existing work, artifact, or review records may carry this evidence; this standard does not require another tracking system.

## Non-normative validation examples

The following examples apply the contracts without prescribing a provider, adapter, mandatory format, or actual production execution.

### Read a work record

A human has scoped permission to read a selected work record. The contract identifies its immutable identity, required fields, observation context, and completeness check; repetition has no intended external mutation. Provider and current Integration support are separately evidenced as Supported for that read scope. The returned record is examined for identity, required fields, and truncation. Missing discussion pages make the result partial when the contract requires the full discussion. Verification records only the retrieved scope and limits; it does not declare the work complete.

### Update a documentation record

The contract identifies the target and expected revision, authorized content scope, postcondition, and verification observation. Provider support is Supported, while current Integration support is Partially supported: it exposes content update and readback but no approval operation. The authorized attempt can update content; it cannot claim approval through that operation. The response acknowledges acceptance, and an authorized readback verifies the intended revision and content. An ambiguous timeout would require inspection of existing content before repetition to avoid duplicate effects or overwriting another revision. Work Validation, review, and Completion are separate decisions.

### Unavailable planning capability

A contract requires a planning-field update. Provider evidence establishes support, but discovery establishes that the current Integration does not expose the operation: its support is Unsupported. The attempt-level required capability is unavailable, and no update is claimed. If an authorized human can perform and verify the same update, a permitted Fallback preserves ownership and evidence. Otherwise an explicit Defer or Block disposition preserves the unresolved obligation; a governed Exception is used only if permitted. When discovery evidence is absent rather than negative, support is Unknown and remains unresolved until assessed. Neither case automatically changes Work Management state.

## References

- [Execution Protocol Standard](execution-protocol.md)
- [Roles and Actor Assignment Standard](roles-and-actor-assignment.md)
- [Work Management Standard](work-management.md)
- [Definition of Ready](definition-of-ready.md)
- [Definition of Done](definition-of-done.md)
- [Artifact Standard](artifact-standard.md)
- [Repository Standards](repository-standards.md)
- [Security, Privacy, and Data Governance Standard](security-privacy-data-governance.md)
- [Repository Automation Standard](repository-automation.md)
- [AI Collaboration Standard](ai-collaboration.md)
