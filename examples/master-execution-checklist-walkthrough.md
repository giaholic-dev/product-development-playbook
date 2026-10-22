# Master Execution Checklist Walkthrough

## Purpose

Validate the navigational coverage of the [Master Execution Checklist](../docs/standards/master-execution-checklist.md) through one fictional, bounded product increment. This example illustrates source ownership and evidence selection; it does not report a real implementation, user study, deployment, or release.

## Scope and context

The fictional increment lets a library member view a reservation status. It follows the existing software-product lifecycle and uses human-only execution. No AI, hosted work tracker, provider integration, or machine-readable format is needed to apply the checklist.

In this example, Mara has a scoped Accountable Owner Assignment for the increment's material decisions and completion declarations, and a distinct Contributor Assignment for implementation. She records a separate Reviewer Assignment for permitted solo review. Release approval Authority is explicitly granted for this increment and recorded through a separate Approver Assignment; it is not inferred from participation or checklist position. These contextual choices follow the [Roles and Actor Assignment Standard](../docs/standards/roles-and-actor-assignment.md); they do not assign universal phase Roles.

The evidence names below identify fictional records in this example, not links to files that exist. In a real application, the [record template](../templates/master-execution-checklist-record.md) identifies actual discoverable artifact locations, source revision, Assignments, Authority, results, and validation decisions.

## Foundation

Follow [Foundation inventory entries](../docs/standards/master-execution-checklist.md#foundation) and the authoritative [Foundation Phase](../docs/lifecycle/01-foundation.md).

- F1 Repository Setup: the fictional repository baseline records working Git access and the chosen local work-tracking capability.
- F2 Repository Standards Adoption: a conformance declaration identifies adopted standards and applicable local choices; no exception is assumed.
- F3 Governance and Tracking: classified work records, an ordered planning view, and scoped ownership establish the selected tracking model.
- F4 Workflow Adoption: the workflow record adopts readiness, completion, branch, and review sources and deliberately chooses human-only execution.
- F5 Documentation Foundation: the root entry point declares English and provides links to the maintained documentation.

Validation examines these records against Foundation's Definition of Done. The Product entry decision checks Foundation's exit criteria and records that no unresolved Foundation decision prevents Product work. F1 and F3 use the selected access capabilities; a hosted provider is not inferred. The capability fields for F2, F4, and F5 explicitly say `No external capability required by the governing source.` Any actual attempt still evaluates its contextual requirements under the [Execution Protocol](../docs/standards/execution-protocol.md).

## Product

Follow [Product inventory entries](../docs/standards/master-execution-checklist.md#product) and the authoritative [Product Phase](../docs/lifecycle/02-product.md).

- P1 Product Vision: the vision record identifies a dependable reservation experience.
- P2 Problem Statement: the problem record distinguishes observed status confusion from assumptions about its cause.
- P3 Users: the user record identifies library members and the operational staff relevant to this increment.
- P4 Outcomes: the outcome record describes successful status interpretation and how it would be assessed.
- P5 Product Scope: the scope record includes viewing status and excludes creating or changing reservations.
- P6 Product Backlog: the initial backlog orders traceable status-view work and its acceptance evidence.

Validation checks the six linked records against Product's Definition of Done. The completion declaration is separate from the next-phase decision: UX inputs are checked before experience work begins. This does not authorize Architecture or implementation in parallel.

## UX

Follow [UX inventory entries](../docs/standards/master-execution-checklist.md#ux) and the authoritative [UX Phase](../docs/lifecycle/03-ux.md).

- U1 UX Vision: an experience-direction record connects clear status interpretation to the Product outcome.
- U2 User Understanding: a fictional research summary records member context and material assumptions. A persona is not needed for this bounded decision.
- U3 Experience Structure: a status-view flow and information-structure decision show the relevant interactions.
- U4 Experience Exploration: a paper representation explores status wording. It is a selected representation, not a universal wireframe requirement.
- U5 UX Validation: fictional observation notes, findings, and a decision record evaluate interpretation and link resulting work to the backlog.

Validation checks the evidence against UX's Definition of Done. A residual accessibility question has a recorded owner, impact, and reassessment condition. The Architecture entry decision verifies that it does not prevent the architectural decision at hand. This example does not turn a selected research method into policy.

## Architecture

Follow [Architecture inventory entries](../docs/standards/master-execution-checklist.md#architecture) and the authoritative [Architecture Phase](../docs/lifecycle/04-architecture.md). A1–A4 are checklist navigation identifiers for its four existing activity bullets.

- A1: context, data, interface, and quality records define the status-view boundary and applicable constraints.
- A2: a decision record compares material options and records the selected direction and rationale.
- A3: a risk and validation record identifies status-data freshness and accessibility checks needed before development.
- A4: architecture-enabling work is linked into the Product Backlog without becoming a separate product scope.

Validation assesses whether these records sufficiently evidence the intended development decision. Remaining uncertainty retains an owner, impact, and reassessment condition. Entry to Development checks the selected work's readiness and Architecture's exit criteria; it does not freeze all future design choices.

The fictional [three-environment preparation record](end-to-end-playbook-example.md#three-environment-preparation-record) applies to this same reservation-status increment: all three contexts exist and their access, data and external-effect isolation is observed before implementation. The Architecture-to-Development handoff links that record; a future provisioning task would not satisfy entry. The [Software Environments Standard](../docs/standards/software-environments.md) remains the owner.

## Development

Follow [Development inventory entries](../docs/standards/master-execution-checklist.md#development) and the authoritative [Development Phase](../docs/lifecycle/05-development.md).

- D1 Implementation: the fictional change record links the status-view increment to its bounded work and current constraints.
- D2 Verification: test observations record the relevant behavior, failure cases, and accessibility checks with results.
- D3 Review and Integration: a solo self-review record compares scope with the change, records validation and limitations, and states the integration decision under the adopted branch workflow. It is not independent approval.
- D4 Learning and Refinement: a follow-up record preserves findings and any accepted limitation with ownership.

The attempt result is the changed artifact, not a work-completion declaration. Work validation, review, and the [Definition of Done](../docs/standards/definition-of-done.md) are checked separately. The Release entry decision checks integrated scope, required evidence, and the treatment of unresolved risk.

The integrated candidate is immutable artifact `reservation-status-r1`, identified by its recorded digest. Test validates that artifact with isolated resources; its results and material configuration differences enter the Release handoff. The [end-to-end example](end-to-end-playbook-example.md#release) supplies the fictional evidence details.

## Release

Follow [Release inventory entries](../docs/standards/master-execution-checklist.md#release) and the authoritative [Release Phase](../docs/lifecycle/06-release.md).

- R1 Release planning: a release decision record identifies the increment, audience, identifier, and conditions.
- R2 Release readiness: readiness evidence links validation, known limitations, communications, and a recovery path.
- R3 Publication: a fictional publication record identifies the approved increment and verified availability to the intended audience. A successful request alone would not prove availability.
- R4 Communication and observation: release information and observation notes record the initial outcome and follow-up needs.
- R5 Recovery: a fictional observation finds that the first publication serves an older status label. A governed recovery record identifies the decision, corrected publication, verified availability, and follow-up. Recovery action does not retroactively make the first attempt successful.

The release-completion decision examines actual availability, release information, evidence, and accountable treatment of remaining risk. The Maintenance entry decision checks operational ownership, feedback intake, and known obligations. No provider or deployment mechanism is made mandatory by the example.

Production promotion uses the same Test-validated digest, separately scoped approval, controlled deployment identity, and observed target/configuration checks described in the [release record](end-to-end-playbook-example.md#release). The older-label observation above is a failed verification or serving drift: it does not prove a conforming promotion. Exposure is held or reduced, the discrepancy is reconciled, and any changed candidate receives affected Test validation and approval before corrected exposure. Recovery preserves both attempts and their actual results.

## Maintenance

Follow [Maintenance inventory entries](../docs/standards/master-execution-checklist.md#maintenance) and the authoritative [Maintenance Phase](../docs/lifecycle/07-maintenance.md).

- M1 Observe and assess: feedback and operational observations identify continuing confusion about one status label.
- M2 Respond and recover: an assessed support record identifies impact and a proportionate response with ownership.
- M3 Improve and evolve: a traceable improvement item records the learning and a governed decision to revisit Product and UX.
- M4 Preserve operational knowledge: ownership, relevant documentation, and linked decisions remain current.

The maintenance increment records its outcome and follow-up against Maintenance's completion and exit criteria. The active product continues to require maintenance. The [Work Management Re-entry](../docs/standards/work-management.md#re-entry) decision preserves the earlier records; it is not inferred from feedback or an attempt result and does not authorize a new attempt automatically.

## Validation outcome and ownership checks

This walkthrough accounts for all 33 inventory entries and exercises all ten fields through their governing links and contextual evidence. The ownership checks are:

- Each Lifecycle Activity, phase input/output, and phase entry/exit decision remains owned by its lifecycle document.
- Contextual Assignments, Accountability, and Authority remain owned by the Roles and Actor Assignment Standard; no checklist entry creates a fixed owner.
- Readiness and work-item completion remain owned by Definition of Ready and Definition of Done.
- Attempt requirements, capability checks, observable results, and evidence linkage remain owned by the Execution Protocol. Absence of an external requirement is explicit and is distinct from available capability or Authority.
- Validation, Completion, and Re-entry remain owned by Work Management. An attempt result, checked box, or inventory position establishes none of them.
- Artifact provenance and optionality remain owned by the applicable standards. Journeys, personas, wireframes, providers, and AI are not made mandatory.

The example validates checklist navigation and semantic boundaries. It does not establish real product execution, independent review, provider conformance, machine readiness, or completion of the later executable-protocol reference-example work.

## References

- [Master Execution Checklist](../docs/standards/master-execution-checklist.md)
- [Master Execution Checklist Record](../templates/master-execution-checklist-record.md)
- [Roles and Actor Assignment Standard](../docs/standards/roles-and-actor-assignment.md)
- [Execution Protocol Standard](../docs/standards/execution-protocol.md)
- [Work Management Standard](../docs/standards/work-management.md)
- [Definition of Ready](../docs/standards/definition-of-ready.md)
- [Definition of Done](../docs/standards/definition-of-done.md)
- [Code Review Standard](../docs/standards/code-review-standard.md)
- [Artifact Standard](../docs/standards/artifact-standard.md)
