# Execution Protocol Standard

## Purpose

Define the minimum provider-independent protocol semantics required to make Playbook execution safely executable, traceable, and verifiable.

## Scope

This standard governs execution-protocol semantics without redefining Work Management, Lifecycle Phase, Work Type, Workflow State, Roles or Actor Assignments, Definition of Ready, Definition of Done, provider integrations, or delivery frameworks.

The protocol is provider-independent, tool-independent, framework-independent, and AI-optional. Existing authoritative standards retain ownership of the concepts they govern.

## Execution Protocol

Execution Protocol is the minimum provider-independent semantic contract that applies when an execution attempt is subject to governed protocol semantics. It provides a basis for making that attempt traceable and verifiable without redefining Work Management or its Execution concept.

Execution Protocol may be applied by humans, teams, AI-assisted workflows, authorized automation, hybrid execution, or future multi-agent execution; it does not require AI. It does not establish readiness, authorization, validation, approval, completion, or Work Management decisions, and it does not prescribe a delivery framework, tool, provider, platform, organizational structure, or universal workflow.

## Protocol Preconditions

Protocol Preconditions are the applicable conditions that MUST be satisfied, explicitly accepted as an authorized exception, or otherwise receive an explicit permitted disposition before a governed execution attempt proceeds.

A governed execution attempt MUST identify its applicable Protocol Preconditions before proceeding. Applicable Preconditions derive from governing requirements and the execution context; only applicable conditions are required, and this standard does not impose a universal precondition checklist. An unmet material Protocol Precondition MUST NOT be silently ignored and SHOULD remain traceable when required by applicable governance or when material to the execution decision.

Protocol Preconditions determine only whether applicable conditions for an execution attempt have been sufficiently addressed under governing standards. They do not define readiness criteria, Authority, Accountability, Assignment, capability availability, validation, approval, completion, or Work Management decisions. Satisfying Protocol Preconditions does not by itself make work Ready, selected, committed, pulled, authorized for execution, validated, approved, or complete.

## Execution Authorization Check

Execution Authorization Check is the protocol-level determination that the Actor or execution mechanism intended to perform a governed execution attempt has the applicable Authority required for that attempt before it proceeds. It checks applicable governing Authority; it does not create, grant, transfer, infer, expand, or redefine Authority.

A governed execution attempt requiring Authority MUST verify that Authority within the applicable scope before proceeding. Participation, technical capability, access, Assignment, Delegation, AI involvement, or automation MUST NOT by themselves imply Authority. Missing required Authority MUST NOT be silently ignored, and material authorization evidence or decisions SHOULD remain traceable when required by applicable governance.

A successful Execution Authorization Check means only that the applicable authorization condition has been satisfied for the attempt. It does not establish readiness, Selection, Commitment, capability availability, validation, approval, completion, or permission beyond the applicable scope. The Roles and Actor Assignment Standard remains authoritative for Authority and related responsibility semantics; AI Collaboration Standard and Security, Privacy, and Data Governance Standard remain authoritative for their applicable requirements.

## Protocol Input

Protocol Input is information, evidence, constraints, references, or other applicable material made available to a governed execution attempt for use in performing that attempt. It identifies what applicable material is available to and relevant for that attempt without changing the material's authoritative type, ownership, lifecycle, or governing requirements.

A governed execution attempt MUST identify the Protocol Inputs required by applicable governing requirements and its execution context. Protocol Inputs MAY include information, evidence, constraints, references, decisions, or governed Artifacts when applicable. Only applicable inputs are required; this standard does not prescribe a universal input schema or manifest. A Protocol Input SHOULD be sufficiently identifiable to preserve traceability when material to the attempt or its verification.

Protocol Input is an attempt-level protocol relationship, not a repository Artifact category, Work Item type, lifecycle classification, Workflow State, or Work Management Activity. Its presence does not establish readiness, authorization, capability availability, successful execution, validation, approval, or completion. It does not require every transient execution context to become a durable Artifact.

## Protocol Result

Protocol Result is the observable result produced by a governed execution attempt and identified by the Execution Protocol so that the attempt can be traced and subsequently evaluated under applicable governing requirements. It identifies what observably resulted from the attempt; it does not establish that the result was successful.

A governed execution attempt MUST make its material Protocol Result sufficiently identifiable for subsequent traceability and verification. A Protocol Result MAY include created or modified information, Artifacts, observable effects, or a recorded unsuccessful outcome when applicable. An execution attempt that does not achieve its intended outcome may still have a Protocol Result. The result SHOULD preserve enough information to distinguish what occurred from what was intended when material.

Protocol Result is attempt-level and does not change the authoritative type, ownership, lifecycle, or governing requirements of any Artifact or Work Item involved. It does not establish Validation, Approval, Completion, release, or successful delivery, and it does not require every transient effect of execution to become a durable Artifact. Applicable standards determine how a Protocol Result is evaluated.

## Protocol Postconditions

Protocol Postconditions are the applicable conditions evaluated after a governed execution attempt to determine whether its Protocol Result satisfies the conditions required for the attempt's protocol-level outcome to be established. They provide the post-attempt counterpart to Protocol Preconditions.

A governed execution attempt MUST identify applicable Protocol Postconditions when governing requirements or execution context require conditions to be evaluated after the attempt. Applicable Protocol Postconditions derive from governing requirements and execution context; only applicable conditions are required, and this standard does not prescribe a universal postcondition checklist. Protocol Postconditions are evaluated against the Protocol Result and applicable evidence.

An unmet material Protocol Postcondition MUST NOT be silently treated as satisfied and SHOULD remain traceable when required for verification or governance. An unmet Protocol Postcondition does not by itself determine the subsequent Work Management action. Satisfying Protocol Postconditions does not establish Validation, Approval, Completion, release, successful delivery, or a Workflow State. Governing standards retain ownership of the criteria they supply.

## Execution Evidence Linkage

Execution Evidence Linkage is the attempt-level relationship that connects a governed execution attempt and its Protocol Result to applicable evidence needed to preserve traceability and support subsequent verification. It identifies relationships to evidence; it does not define evidence requirements, Artifact types, validation criteria, completion criteria, storage, retention, or persistence mechanisms.

A governed execution attempt MUST preserve linkage to evidence required by applicable governing standards when that evidence is material to verification. The linkage SHOULD make it possible to relate the execution attempt, applicable Protocol Inputs, Protocol Result, and applicable Protocol Postcondition evaluation when required. It MUST preserve the identity and ownership of referenced evidence rather than redefining it as a protocol Artifact type.

Evidence MAY already exist, be produced during execution, or become available after the execution action when applicable. Not every transient observation or execution detail must become durable evidence. Evidence depth and durability SHOULD remain proportional to applicable risk, governance, verification, and existing requirements. Presence of evidence or an Execution Evidence Linkage does not establish Validation, Approval, Completion, release, or successful delivery. Missing required evidence MUST NOT be silently treated as evidence that exists.

## Protocol State

Protocol State is the minimal attempt-level representation of the current protocol condition of a particular governed execution attempt. It exists only to make that attempt's current protocol condition explicit and traceable when needed for coordination or verification.

Protocol State MAY be recorded when needed for traceability, coordination, or verification. It MUST remain distinguishable from the Workflow State of any associated Work Item. It does not represent Work-in-Progress, Blocking, lifecycle progression, a Work Management Activity, Completion, or a provider's native state.

Protocol State MUST NOT imply that an associated Work Item is Ready, selected, committed, in progress, blocked, under review, validated, approved, complete, released, or re-entered. A change in Protocol State MUST NOT automatically change Workflow State, Lifecycle Phase, Work-in-Progress, Blocking, or Completion; likewise, a change in Work Management does not automatically imply a particular Protocol State.

This standard does not require a universal Protocol State catalog, transition model, or state machine. Any persisted or provider-mapped representation of Protocol State remains outside this concept.

## Handoff

Handoff is the traceable transfer of execution context from one Actor, execution mechanism, or governed execution attempt to another participant or subsequent execution context. It preserves the information necessary for continuity and verification without transferring responsibility semantics governed elsewhere.

When material, a Handoff MUST preserve sufficient execution context for the receiving participant or context to understand what is being transferred. Applicable Protocol Inputs, Protocol Result, Protocol State, Execution Evidence Linkage, unresolved conditions, and relevant governing context SHOULD remain identifiable when material to continuity or verification. A Handoff MUST preserve traceability to the originating execution attempt when required by applicable governance.

A Handoff MUST NOT silently transfer Accountability, Authority, Role, Assignment, ownership, or Approval authority. Any required reassignment, Delegation, authorization, approval, or accountability change MUST occur under the standards that govern those concepts. A Handoff does not establish acceptance, Approval, Validation, Completion, Re-entry, or a Workflow State change.

A Handoff MAY occur between humans, teams, AI agents, automations, hybrid Actors, or execution contexts when otherwise permitted. This standard does not prescribe a communication channel, document format, provider, queue, event system, or transport mechanism, nor does it require a handoff template or workflow.

## Capability Requirement

Capability Requirement is an attempt-level statement of a capability that must be available for a governed execution attempt to perform an applicable action or produce an applicable result. It identifies what must be possible for the attempt, not how the capability is implemented.

A governed execution attempt MUST identify any Capability Requirement material to its applicable execution action. Capability Requirements SHOULD be expressed at the minimum level of specificity necessary to determine whether execution can proceed. A Capability Requirement MAY be satisfied by a human, team, AI agent, automation, tool, integration, hybrid Actor, or other permitted mechanism.

A Capability Requirement does not establish that the capability is available. Possessing or exposing a capability does not establish Authority to use it; authorization and capability are independent conditions. Identifying a Capability Requirement does not establish readiness, execution success, Validation, Approval, Completion, or release.

This standard does not require a particular provider, API, tool, framework, AI model, integration, or implementation mechanism. Capability availability, discovery, provider availability semantics, integration contracts, adapters, provider authorization mechanisms, and provider mappings remain outside this concept and belong to their applicable standards, including future integration concerns.

## Capability Availability

Capability Availability is the attempt-level determination of whether a required capability can actually be performed in the applicable execution context. It distinguishes a Capability Requirement from whether that requirement can currently be satisfied.

When a governed execution attempt has a material Capability Requirement, the protocol MUST determine whether that capability is available in the applicable execution context before relying on it. Capability Availability MUST be evaluated for the particular attempt and context rather than assumed globally. An available capability does not imply Authority to use it, and applicable Authority does not imply that the required capability is available.

Capability Availability does not establish readiness, successful execution, Validation, Approval, Completion, or release. An unavailable required capability MUST NOT be silently treated as available and MUST remain explicit and traceable when material. This concept identifies availability or unavailability only; it does not determine the disposition that follows.

Capability Availability is not capability discovery. This standard does not define capability support classifications, provider capability catalogs, integration contracts, adapters, provider mappings, APIs, or provider-specific availability mechanisms; those remain outside this concept and belong to applicable standards, including future integration concerns. Blocking remains governed by Work Management.

## Execution Disposition

Execution Disposition is the explicit protocol-level determination of how a governed execution attempt is to be treated when its current conditions do not permit ordinary progression or when its result requires an explicit protocol outcome. It makes that treatment explicit without defining a universal workflow, state machine, recovery algorithm, provider behavior, or Work Management decision model.

When a material protocol condition prevents ordinary progression, a governed execution attempt MUST receive an explicit Execution Disposition rather than silently proceeding. When applicable governing requirements require explicit treatment of an execution result or unmet condition, that treatment MUST remain identifiable and traceable. An Execution Disposition records only how the attempt is to be treated at the protocol level; it does not prove that the underlying condition has been resolved.

An Execution Disposition MUST NOT silently change Workflow State, Lifecycle Phase, Work-in-Progress, Blocking, Assignment, Authority, Accountability, Validation, Approval, Completion, or release status. Any resulting Work Management action remains governed by Work Management, and any required authorization or approval remains governed by the standards that own those concepts. The protocol does not prescribe a universal sequence of dispositions.

The permitted generic protocol-level dispositions are:

- `Proceed` — the attempt may continue under the applicable protocol conditions.
- `Defer` — progression is intentionally postponed pending later treatment.
- `Fallback` — progression may continue through another permitted execution approach.
- `Block` — the attempt cannot currently progress under the applicable conditions.
- `Exception` — progression or treatment depends on a governed exception.

These dispositions are not Workflow States or Work Management Activities. They do not define internal procedures. An unavailable required capability MUST receive an applicable Execution Disposition rather than be silently ignored; this standard does not define how fallback is selected, blocking is managed, deferment is scheduled, an exception is authorized, or capability discovery operates.

## Exception

Exception is an explicit, governed protocol-level treatment used when an applicable requirement or normal execution condition cannot be satisfied as ordinarily required, but applicable governance permits exceptional treatment. It is an Execution Disposition; it is not a silent bypass, implicit waiver, automatic permission to proceed, generic failure, provider error, or replacement for Authority, Approval, Validation, or Completion criteria.

An Exception MUST be explicit and MUST identify the applicable requirement or condition receiving exceptional treatment when material. It MUST be permitted by applicable governance. Required Authority or Approval for an Exception MUST be established under the standards that govern those concepts. The rationale for a material Exception MUST remain traceable when required by applicable governance, and applicable supporting evidence SHOULD remain linked when required.

An Exception MUST NOT silently transfer Authority, Accountability, Assignment, ownership, or responsibility. It MUST NOT establish Validation, Approval, Completion, release, successful delivery, or a Workflow State, and it MUST NOT be interpreted as permanently changing the underlying governing requirement. The absence of a permitted Exception MUST NOT be treated as permission to ignore an unmet material requirement.

Applicable governance standards retain ownership of the requirements receiving exceptional treatment and of any specific exception authority, criteria, evidence, or approval they require. This standard defines only the generic protocol semantics that make exceptional treatment explicit and traceable.

## Escalation

Escalation is the explicit raising of an unresolved material execution condition to an Actor, Role, authority context, or governance mechanism capable of determining its treatment. It makes conditions requiring a decision beyond the current execution context explicit and traceable.

An unresolved material execution condition SHOULD be escalated when its treatment requires Authority, information, judgment, or governance outside the current execution context. An Escalation MUST identify the material condition being raised when required for meaningful treatment, and its target MUST be appropriate to the applicable governing context.

When material, an Escalation SHOULD preserve relevant Protocol Inputs, Protocol Result, Protocol State, Execution Evidence Linkage, prior Execution Disposition, and Exception context. It MUST preserve traceability to the originating governed execution attempt when material. Escalation MUST NOT silently transfer Assignment, Authority, Accountability, ownership, or responsibility.

Escalation does not establish Approval, Exception, Validation, Completion, release, Re-entry, or a Workflow State. The response to an Escalation is governed by the standards and Authority applicable to that response; absence of immediate resolution MUST NOT be treated as successful resolution. This standard defines no escalation hierarchy, level, severity, timeout, SLA, notification mechanism, queue, routing algorithm, or workflow.

## Re-entry Boundary

Re-entry remains a Work Management decision governed by the Work Management Standard. This standard defines only the attempt-level traceability boundary: when Work Management determines that Re-entry is required, relevant execution context SHOULD remain traceable when material.

A governed execution attempt MUST NOT automatically cause Re-entry solely because it failed, produced an unexpected result, received an Execution Disposition, encountered an Exception, or was escalated. Relevant context MAY include applicable Protocol Inputs, Protocol Result, Protocol State, Execution Evidence Linkage, Execution Disposition, Exception, Escalation, and Handoff information.

Re-entry MUST NOT erase or replace traceability of the originating execution attempt. A re-entered Work Item or context does not retroactively alter the historical Protocol Result or evidence of that attempt. This standard does not determine where work re-enters, which activity follows, whether a new Work Item is created, or how Workflow State changes.

Re-entry does not authorize another execution attempt. Any subsequent governed execution attempt MUST independently satisfy its applicable protocol requirements.

## Non-normative execution traces

The following example illustrates one valid, provider-independent execution path. It does not prescribe a universal sequence, require every illustrated element for every attempt, or establish a workflow.

### Normal execution trace

A governed execution attempt updates an existing documentation Artifact. Applicable Protocol Preconditions are addressed, and an Execution Authorization Check independently verifies the applicable Authority. The attempt identifies its relevant Protocol Inputs and a material Capability Requirement; Capability Availability then determines that the required capability is available in the applicable context.

The attempt performs the governed execution action and identifies the updated Artifact as its observable Protocol Result. Applicable Protocol Postconditions are evaluated against that result, and material Execution Evidence Linkage preserves traceability to the inputs, result, and evaluation. The result and linked evidence remain available for subsequent Work Management Validation or other applicable governance; this trace does not establish Validation, Approval, Completion, release, or Workflow State.

## References

- [Work Management Standard](work-management.md)
- [Roles and Actor Assignment Standard](roles-and-actor-assignment.md)
- [Definition of Ready](definition-of-ready.md)
- [Definition of Done](definition-of-done.md)
- [Work Item Taxonomy](work-item-taxonomy.md)
- [Work Item Types](work-item-types.md)
- [Artifact Standard](artifact-standard.md)
- [AI Collaboration Standard](ai-collaboration.md)
- [Security, Privacy, and Data Governance Standard](security-privacy-data-governance.md)
- [Code Review Standard](code-review-standard.md)
- [Testing Strategy](testing-strategy.md)
- [Release Strategy](release-strategy.md)
- [Maintenance Phase](../lifecycle/07-maintenance.md)
