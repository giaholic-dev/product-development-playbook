# Master Execution Checklist

## Purpose

Define the governing contract and stable entry structure for the cross-lifecycle operational index spanning Foundation through Maintenance.

The Master Execution Checklist makes applicable sources and execution boundaries discoverable for each lifecycle activity. It links to authoritative Playbook content rather than duplicating that content.

## Scope

This standard governs how Master Execution Checklist entries are structured and how they reference their authoritative sources. It does not replace lifecycle documents, Work Management, the Execution Protocol, readiness or completion standards, or artifact governance.

The checklist is provider-independent and directly usable by humans. It does not define a workflow, state model, execution mechanism, provider integration, or machine-readable execution format.

The operational inventory below covers every activity currently listed by the seven lifecycle documents. It is a navigational index, not evidence that a project has performed those activities.

## Authority and source-of-truth boundaries

The checklist exposes concise operational labels and links while preserving the following ownership boundaries:

- Lifecycle documents own lifecycle activities, phase inputs and outputs, and entry and exit criteria.
- The [Roles and Actor Assignment Standard](roles-and-actor-assignment.md) owns Role, Actor, Assignment, Accountability, and Reviewer and Approver responsibility semantics.
- The [Work Management Standard](work-management.md) owns work progression, Blocking, Review, Validation, Completion, and Re-entry.
- The [Execution Protocol Standard](execution-protocol.md) owns attempt semantics, authorization checks, capability checks, Execution Dispositions, Protocol Results, and Execution Evidence Linkage.
- The [Definition of Ready](definition-of-ready.md) owns readiness criteria.
- The [Definition of Done](definition-of-done.md) owns completion criteria.
- The [Artifact Standard](artifact-standard.md) owns artifact classification and provenance; the [Artifact Catalog](artifact-catalog.md) owns catalog navigation.

The checklist MUST NOT redefine a concept owned by another source. A concise label in an entry is navigational context, not a parallel definition or rule.

## Stable entry structure

Each populated lifecycle activity entry MUST expose the following fields consistently:

| Field | Required content |
| --- | --- |
| Phase | The applicable Lifecycle Phase and a link to its authoritative lifecycle document. |
| Lifecycle Activity | The activity name used by the authoritative lifecycle document and a link to that source. |
| Role / Assignment Source | The applicable source for contextual Role or Assignment information without inventing a universal owner. |
| Inputs | Concise identification of applicable inputs with links to their governing sources. |
| Governing Standards | Links to the standards that govern the activity or its required decisions. |
| Outputs / Artifacts | Concise identification of applicable outputs or Artifacts with links to their authoritative sources. |
| Capability Requirement | A linked authoritative Capability Requirement when one exists, or an explicit statement that the governing source requires no external capability. |
| Validation / Evidence | Links to applicable Validation and evidence requirements. |
| Completion Condition | Links to the applicable phase, work, or artifact completion requirements. |
| Next-action / Entry-Exit Boundary | The linked authoritative condition governing the applicable next action or lifecycle entry or exit boundary. |

The fixed fields establish consistent navigation. They do not establish universal values, requirements, or execution semantics for every activity.

## Linking and non-duplication rules

A populated entry MUST link to the document that owns each applicable rule. It MAY use a concise source-aligned label only when the label helps the reader identify what the link governs.

An entry MUST NOT:

- copy normative rules from an authoritative source;
- create an alternate definition for an established concept;
- convert an example into a requirement;
- convert an optional output or representation into a mandatory Artifact;
- invent a Role, Assignment, accountable owner, or approval requirement;
- invent a Capability Requirement;
- invent a Workflow State, Protocol State, Execution Disposition, or transition; or
- treat checklist position as evidence of readiness, authorization, execution, validation, approval, or Completion.

When an authoritative source does not provide information for a field, the entry MUST make that absence explicit or link to the governing contextual rule. It MUST NOT manufacture content to make the entry appear complete.

## Contextual role handling

Roles are not universally assigned to Lifecycle Activities. The `Role / Assignment Source` field MUST preserve contextual Assignment under the [Roles and Actor Assignment Standard](roles-and-actor-assignment.md).

An entry MAY link to an applicable lifecycle-specific responsibility or governed Assignment when one exists. Otherwise, it MUST point to the source that requires an applicable Assignment to be established. The checklist MUST NOT create fixed phase Roles or universal activity owners.

## Capability handling

When an authoritative source establishes a Capability Requirement for an activity, the `Capability Requirement` field MAY expose that requirement and MUST link to its source.

When no authoritative source requires an external capability, the field MUST explicitly state: `No external capability required by the governing source.` This statement records the absence of an external requirement; it does not create a capability category, provider model, or claim about every execution context.

The checklist MUST NOT infer capability availability, Authority to use a capability, or an Execution Disposition. Those determinations remain governed by their authoritative standards and the applicable execution context.

## Human and future machine use

The checklist MUST remain directly usable by humans as portable Markdown. Consistent headings and fields MAY support future machine interpretation, but they do not make the checklist machine-authoritative.

This standard does not define a schema, manifest, structured execution format, provider contract, automation representation, or machine-execution source. Any machine-readable representation belongs to later architectural work and MUST preserve the human-readable authoritative sources.

## Using the operational inventory

Start with the applicable phase inputs and readiness sources, then follow the entries for the bounded work under consideration. Role Assignments, Authority, capability checks, evidence, and completion remain contextual and governed by the linked sources. Phase-level inputs, outputs, and criteria are shared references; the lifecycle does not define separate mandatory gates or input sets for every activity.

Activity labels follow the lifecycle sources. The four Architecture navigation identifiers (`A1` through `A4`) identify the existing activity bullets in source order; they add no lifecycle activity or rule. Supporting standards help readers locate detail without making every artifact or representation mandatory.

Use the [Master Execution Checklist Record template](../../templates/master-execution-checklist-record.md) to retain context and evidence for a bounded application. The [fictional validation walkthrough](../../examples/master-execution-checklist-walkthrough.md) illustrates all seven phases and the separation between navigation and completion evidence.

## Operational inventory

### Foundation

#### F1 Repository Setup

- **Phase:** [Foundation](../lifecycle/01-foundation.md)
- **Lifecycle Activity:** [F1 Repository Setup](../lifecycle/01-foundation.md#activities)
- **Role / Assignment Source:** [Contextual Assignment](roles-and-actor-assignment.md#assignment-model) and [Accountability and Authority](roles-and-actor-assignment.md#accountability-and-authority); no fixed phase Role is assigned here.
- **Inputs:** [Foundation inputs](../lifecycle/01-foundation.md#inputs) and [work readiness](definition-of-ready.md). Activity-specific inputs remain contextual where the lifecycle lists only phase inputs.
- **Governing Standards:** [Foundation activity source](../lifecycle/01-foundation.md#activities); [Repository Standards](repository-standards.md); [Execution Protocol Standard](execution-protocol.md); [Work Management Standard](work-management.md)
- **Outputs / Artifacts:** [Repository and version-control baseline](../lifecycle/01-foundation.md#artifacts-and-evidence); [Repository Standards](repository-standards.md). These sources retain applicable selection and optionality.
- **Capability Requirement:** [Selected version-control and work-tracking access](../lifecycle/01-foundation.md#inputs); [Git baseline](repository-standards.md#git-baseline). The selected context determines any external capability required for this activity.
- **Validation / Evidence:** [Foundation completion evidence](../lifecycle/01-foundation.md#definition-of-done), [work validation](work-management.md#validation), and [execution evidence linkage](execution-protocol.md#execution-evidence-linkage).
- **Completion Condition:** [Foundation Definition of Done](../lifecycle/01-foundation.md#definition-of-done) and [work-item completion](definition-of-done.md).
- **Next-action / Entry-Exit Boundary:** [Foundation exit criteria](../lifecycle/01-foundation.md#exit-criteria), [work readiness](definition-of-ready.md), and [Re-entry](work-management.md#re-entry). Entry order alone does not authorize progression.

#### F2 Repository Standards Adoption

- **Phase:** [Foundation](../lifecycle/01-foundation.md)
- **Lifecycle Activity:** [F2 Repository Standards Adoption](../lifecycle/01-foundation.md#activities)
- **Role / Assignment Source:** [Contextual Assignment](roles-and-actor-assignment.md#assignment-model) and [Accountability and Authority](roles-and-actor-assignment.md#accountability-and-authority); no fixed phase Role is assigned here.
- **Inputs:** [Foundation inputs](../lifecycle/01-foundation.md#inputs) and [work readiness](definition-of-ready.md). Activity-specific inputs remain contextual where the lifecycle lists only phase inputs.
- **Governing Standards:** [Foundation activity source](../lifecycle/01-foundation.md#activities); [Repository Standards](repository-standards.md); [Execution Protocol Standard](execution-protocol.md); [Work Management Standard](work-management.md)
- **Outputs / Artifacts:** [Standards adoption and applicable extension or exception records](../lifecycle/01-foundation.md#artifacts-and-evidence); [Repository Standards](repository-standards.md). These sources retain applicable selection and optionality.
- **Capability Requirement:** No external capability required by the governing source.
- **Validation / Evidence:** [Foundation completion evidence](../lifecycle/01-foundation.md#definition-of-done), [work validation](work-management.md#validation), and [execution evidence linkage](execution-protocol.md#execution-evidence-linkage).
- **Completion Condition:** [Foundation Definition of Done](../lifecycle/01-foundation.md#definition-of-done) and [work-item completion](definition-of-done.md).
- **Next-action / Entry-Exit Boundary:** [Foundation exit criteria](../lifecycle/01-foundation.md#exit-criteria), [work readiness](definition-of-ready.md), and [Re-entry](work-management.md#re-entry). Entry order alone does not authorize progression.

#### F3 Governance and Tracking

- **Phase:** [Foundation](../lifecycle/01-foundation.md)
- **Lifecycle Activity:** [F3 Governance and Tracking](../lifecycle/01-foundation.md#activities)
- **Role / Assignment Source:** [Contextual Assignment](roles-and-actor-assignment.md#assignment-model) and [Accountability and Authority](roles-and-actor-assignment.md#accountability-and-authority); no fixed phase Role is assigned here.
- **Inputs:** [Foundation inputs](../lifecycle/01-foundation.md#inputs) and [work readiness](definition-of-ready.md). Activity-specific inputs remain contextual where the lifecycle lists only phase inputs.
- **Governing Standards:** [Foundation activity source](../lifecycle/01-foundation.md#activities); [Work Item Taxonomy](work-item-taxonomy.md); [Work Item Types](work-item-types.md); [Project Views](project-views.md); [Repository Milestone Standard](repository-milestones.md); [Work Management Standard](work-management.md); [Execution Protocol Standard](execution-protocol.md)
- **Outputs / Artifacts:** [Work-tracking configuration, planning model, and ownership evidence](../lifecycle/01-foundation.md#artifacts-and-evidence); [Work Item Taxonomy](work-item-taxonomy.md); [Work Item Types](work-item-types.md); [Project Views](project-views.md); [Repository Milestone Standard](repository-milestones.md); [Work Management Standard](work-management.md). These sources retain applicable selection and optionality.
- **Capability Requirement:** [Selected version-control and work-tracking access](../lifecycle/01-foundation.md#inputs); [Git baseline](repository-standards.md#git-baseline). The selected context determines any external capability required for this activity.
- **Validation / Evidence:** [Foundation completion evidence](../lifecycle/01-foundation.md#definition-of-done), [work validation](work-management.md#validation), and [execution evidence linkage](execution-protocol.md#execution-evidence-linkage).
- **Completion Condition:** [Foundation Definition of Done](../lifecycle/01-foundation.md#definition-of-done) and [work-item completion](definition-of-done.md).
- **Next-action / Entry-Exit Boundary:** [Foundation exit criteria](../lifecycle/01-foundation.md#exit-criteria), [work readiness](definition-of-ready.md), and [Re-entry](work-management.md#re-entry). Entry order alone does not authorize progression.

#### F4 Workflow Adoption

- **Phase:** [Foundation](../lifecycle/01-foundation.md)
- **Lifecycle Activity:** [F4 Workflow Adoption](../lifecycle/01-foundation.md#activities)
- **Role / Assignment Source:** [Contextual Assignment](roles-and-actor-assignment.md#assignment-model) and [Accountability and Authority](roles-and-actor-assignment.md#accountability-and-authority); no fixed phase Role is assigned here.
- **Inputs:** [Foundation inputs](../lifecycle/01-foundation.md#inputs) and [work readiness](definition-of-ready.md). Activity-specific inputs remain contextual where the lifecycle lists only phase inputs.
- **Governing Standards:** [Foundation activity source](../lifecycle/01-foundation.md#activities); [Branch Workflow](branch-workflow.md); [Definition of Ready](definition-of-ready.md); [Code Review Standard](code-review-standard.md); [Definition of Done](definition-of-done.md); [AI Collaboration Standard](ai-collaboration.md); [Execution Protocol Standard](execution-protocol.md); [Work Management Standard](work-management.md)
- **Outputs / Artifacts:** [Workflow configuration, gates, and manual-only or AI authority record](../lifecycle/01-foundation.md#artifacts-and-evidence); [Branch Workflow](branch-workflow.md); [Definition of Ready](definition-of-ready.md); [Code Review Standard](code-review-standard.md); [Definition of Done](definition-of-done.md); [AI Collaboration Standard](ai-collaboration.md); [Execution Protocol Standard](execution-protocol.md). These sources retain applicable selection and optionality.
- **Capability Requirement:** No external capability required by the governing source.
- **Validation / Evidence:** [Foundation completion evidence](../lifecycle/01-foundation.md#definition-of-done), [work validation](work-management.md#validation), and [execution evidence linkage](execution-protocol.md#execution-evidence-linkage).
- **Completion Condition:** [Foundation Definition of Done](../lifecycle/01-foundation.md#definition-of-done) and [work-item completion](definition-of-done.md).
- **Next-action / Entry-Exit Boundary:** [Foundation exit criteria](../lifecycle/01-foundation.md#exit-criteria), [work readiness](definition-of-ready.md), and [Re-entry](work-management.md#re-entry). Entry order alone does not authorize progression.

#### F5 Documentation Foundation

- **Phase:** [Foundation](../lifecycle/01-foundation.md)
- **Lifecycle Activity:** [F5 Documentation Foundation](../lifecycle/01-foundation.md#activities)
- **Role / Assignment Source:** [Contextual Assignment](roles-and-actor-assignment.md#assignment-model) and [Accountability and Authority](roles-and-actor-assignment.md#accountability-and-authority); no fixed phase Role is assigned here.
- **Inputs:** [Foundation inputs](../lifecycle/01-foundation.md#inputs) and [work readiness](definition-of-ready.md). Activity-specific inputs remain contextual where the lifecycle lists only phase inputs.
- **Governing Standards:** [Foundation activity source](../lifecycle/01-foundation.md#activities); [Documentation Information Architecture](documentation-information-architecture.md); [Documentation Navigation Standard](documentation-navigation.md); [Documentation Style Guide](documentation-style-guide.md); [Execution Protocol Standard](execution-protocol.md); [Work Management Standard](work-management.md)
- **Outputs / Artifacts:** [Root entry point, language declaration, architecture, and navigation](../lifecycle/01-foundation.md#artifacts-and-evidence); [Documentation Information Architecture](documentation-information-architecture.md); [Documentation Navigation Standard](documentation-navigation.md); [Documentation Style Guide](documentation-style-guide.md). These sources retain applicable selection and optionality.
- **Capability Requirement:** No external capability required by the governing source.
- **Validation / Evidence:** [Foundation completion evidence](../lifecycle/01-foundation.md#definition-of-done), [work validation](work-management.md#validation), and [execution evidence linkage](execution-protocol.md#execution-evidence-linkage).
- **Completion Condition:** [Foundation Definition of Done](../lifecycle/01-foundation.md#definition-of-done) and [work-item completion](definition-of-done.md).
- **Next-action / Entry-Exit Boundary:** [Foundation exit criteria](../lifecycle/01-foundation.md#exit-criteria), [work readiness](definition-of-ready.md), and [Re-entry](work-management.md#re-entry). Entry order alone does not authorize progression.

### Product

#### P1 Product Vision

- **Phase:** [Product](../lifecycle/02-product.md)
- **Lifecycle Activity:** [P1 Product Vision](../lifecycle/02-product.md#activities)
- **Role / Assignment Source:** [Contextual Assignment](roles-and-actor-assignment.md#assignment-model) and [Accountability and Authority](roles-and-actor-assignment.md#accountability-and-authority); no fixed phase Role is assigned here.
- **Inputs:** [Product inputs](../lifecycle/02-product.md#inputs) and [work readiness](definition-of-ready.md). Activity-specific inputs remain contextual where the lifecycle lists only phase inputs.
- **Governing Standards:** [Product activity source](../lifecycle/02-product.md#activities); [Product Vision](product-vision.md); [Execution Protocol Standard](execution-protocol.md); [Work Management Standard](work-management.md)
- **Outputs / Artifacts:** [Product Vision](../lifecycle/02-product.md#outputs-and-artifacts); [Product Vision](product-vision.md). These sources retain applicable selection and optionality.
- **Capability Requirement:** No external capability required by the governing source.
- **Validation / Evidence:** [Product completion evidence](../lifecycle/02-product.md#definition-of-done), [work validation](work-management.md#validation), and [execution evidence linkage](execution-protocol.md#execution-evidence-linkage).
- **Completion Condition:** [Product Definition of Done](../lifecycle/02-product.md#definition-of-done) and [work-item completion](definition-of-done.md).
- **Next-action / Entry-Exit Boundary:** [Product exit criteria](../lifecycle/02-product.md#exit-criteria), [work readiness](definition-of-ready.md), and [Re-entry](work-management.md#re-entry). Entry order alone does not authorize progression.

#### P2 Problem Statement

- **Phase:** [Product](../lifecycle/02-product.md)
- **Lifecycle Activity:** [P2 Problem Statement](../lifecycle/02-product.md#activities)
- **Role / Assignment Source:** [Contextual Assignment](roles-and-actor-assignment.md#assignment-model) and [Accountability and Authority](roles-and-actor-assignment.md#accountability-and-authority); no fixed phase Role is assigned here.
- **Inputs:** [Product inputs](../lifecycle/02-product.md#inputs) and [work readiness](definition-of-ready.md). Activity-specific inputs remain contextual where the lifecycle lists only phase inputs.
- **Governing Standards:** [Product activity source](../lifecycle/02-product.md#activities); [Problem Statement](problem-statement.md); [Execution Protocol Standard](execution-protocol.md); [Work Management Standard](work-management.md)
- **Outputs / Artifacts:** [Problem Statement](../lifecycle/02-product.md#outputs-and-artifacts); [Problem Statement](problem-statement.md). These sources retain applicable selection and optionality.
- **Capability Requirement:** No external capability required by the governing source.
- **Validation / Evidence:** [Product completion evidence](../lifecycle/02-product.md#definition-of-done), [work validation](work-management.md#validation), and [execution evidence linkage](execution-protocol.md#execution-evidence-linkage).
- **Completion Condition:** [Product Definition of Done](../lifecycle/02-product.md#definition-of-done) and [work-item completion](definition-of-done.md).
- **Next-action / Entry-Exit Boundary:** [Product exit criteria](../lifecycle/02-product.md#exit-criteria), [work readiness](definition-of-ready.md), and [Re-entry](work-management.md#re-entry). Entry order alone does not authorize progression.

#### P3 Users

- **Phase:** [Product](../lifecycle/02-product.md)
- **Lifecycle Activity:** [P3 Users](../lifecycle/02-product.md#activities)
- **Role / Assignment Source:** [Contextual Assignment](roles-and-actor-assignment.md#assignment-model) and [Accountability and Authority](roles-and-actor-assignment.md#accountability-and-authority); no fixed phase Role is assigned here.
- **Inputs:** [Product inputs](../lifecycle/02-product.md#inputs) and [work readiness](definition-of-ready.md). Activity-specific inputs remain contextual where the lifecycle lists only phase inputs.
- **Governing Standards:** [Product activity source](../lifecycle/02-product.md#activities); [Users](users.md); [Execution Protocol Standard](execution-protocol.md); [Work Management Standard](work-management.md)
- **Outputs / Artifacts:** [Users and relevant actor roles](../lifecycle/02-product.md#outputs-and-artifacts); [Users](users.md). These sources retain applicable selection and optionality.
- **Capability Requirement:** No external capability required by the governing source.
- **Validation / Evidence:** [Product completion evidence](../lifecycle/02-product.md#definition-of-done), [work validation](work-management.md#validation), and [execution evidence linkage](execution-protocol.md#execution-evidence-linkage).
- **Completion Condition:** [Product Definition of Done](../lifecycle/02-product.md#definition-of-done) and [work-item completion](definition-of-done.md).
- **Next-action / Entry-Exit Boundary:** [Product exit criteria](../lifecycle/02-product.md#exit-criteria), [work readiness](definition-of-ready.md), and [Re-entry](work-management.md#re-entry). Entry order alone does not authorize progression.

#### P4 Outcomes

- **Phase:** [Product](../lifecycle/02-product.md)
- **Lifecycle Activity:** [P4 Outcomes](../lifecycle/02-product.md#activities)
- **Role / Assignment Source:** [Contextual Assignment](roles-and-actor-assignment.md#assignment-model) and [Accountability and Authority](roles-and-actor-assignment.md#accountability-and-authority); no fixed phase Role is assigned here.
- **Inputs:** [Product inputs](../lifecycle/02-product.md#inputs) and [work readiness](definition-of-ready.md). Activity-specific inputs remain contextual where the lifecycle lists only phase inputs.
- **Governing Standards:** [Product activity source](../lifecycle/02-product.md#activities); [Outcomes](outcomes.md); [Execution Protocol Standard](execution-protocol.md); [Work Management Standard](work-management.md)
- **Outputs / Artifacts:** [Outcomes and their evidence](../lifecycle/02-product.md#outputs-and-artifacts); [Outcomes](outcomes.md). These sources retain applicable selection and optionality.
- **Capability Requirement:** No external capability required by the governing source.
- **Validation / Evidence:** [Product completion evidence](../lifecycle/02-product.md#definition-of-done), [work validation](work-management.md#validation), and [execution evidence linkage](execution-protocol.md#execution-evidence-linkage).
- **Completion Condition:** [Product Definition of Done](../lifecycle/02-product.md#definition-of-done) and [work-item completion](definition-of-done.md).
- **Next-action / Entry-Exit Boundary:** [Product exit criteria](../lifecycle/02-product.md#exit-criteria), [work readiness](definition-of-ready.md), and [Re-entry](work-management.md#re-entry). Entry order alone does not authorize progression.

#### P5 Product Scope

- **Phase:** [Product](../lifecycle/02-product.md)
- **Lifecycle Activity:** [P5 Product Scope](../lifecycle/02-product.md#activities)
- **Role / Assignment Source:** [Contextual Assignment](roles-and-actor-assignment.md#assignment-model) and [Accountability and Authority](roles-and-actor-assignment.md#accountability-and-authority); no fixed phase Role is assigned here.
- **Inputs:** [Product inputs](../lifecycle/02-product.md#inputs) and [work readiness](definition-of-ready.md). Activity-specific inputs remain contextual where the lifecycle lists only phase inputs.
- **Governing Standards:** [Product activity source](../lifecycle/02-product.md#activities); [Product Scope](product-scope.md); [Execution Protocol Standard](execution-protocol.md); [Work Management Standard](work-management.md)
- **Outputs / Artifacts:** [Product Scope](../lifecycle/02-product.md#outputs-and-artifacts); [Product Scope](product-scope.md). These sources retain applicable selection and optionality.
- **Capability Requirement:** No external capability required by the governing source.
- **Validation / Evidence:** [Product completion evidence](../lifecycle/02-product.md#definition-of-done), [work validation](work-management.md#validation), and [execution evidence linkage](execution-protocol.md#execution-evidence-linkage).
- **Completion Condition:** [Product Definition of Done](../lifecycle/02-product.md#definition-of-done) and [work-item completion](definition-of-done.md).
- **Next-action / Entry-Exit Boundary:** [Product exit criteria](../lifecycle/02-product.md#exit-criteria), [work readiness](definition-of-ready.md), and [Re-entry](work-management.md#re-entry). Entry order alone does not authorize progression.

#### P6 Product Backlog

- **Phase:** [Product](../lifecycle/02-product.md)
- **Lifecycle Activity:** [P6 Product Backlog](../lifecycle/02-product.md#activities)
- **Role / Assignment Source:** [Contextual Assignment](roles-and-actor-assignment.md#assignment-model) and [Accountability and Authority](roles-and-actor-assignment.md#accountability-and-authority); no fixed phase Role is assigned here.
- **Inputs:** [Product inputs](../lifecycle/02-product.md#inputs) and [work readiness](definition-of-ready.md). Activity-specific inputs remain contextual where the lifecycle lists only phase inputs.
- **Governing Standards:** [Product activity source](../lifecycle/02-product.md#activities); [Product Backlog](product-backlog.md); [Execution Protocol Standard](execution-protocol.md); [Work Management Standard](work-management.md)
- **Outputs / Artifacts:** [Product Backlog](../lifecycle/02-product.md#outputs-and-artifacts); [Product Backlog](product-backlog.md). These sources retain applicable selection and optionality.
- **Capability Requirement:** No external capability required by the governing source.
- **Validation / Evidence:** [Product completion evidence](../lifecycle/02-product.md#definition-of-done), [work validation](work-management.md#validation), and [execution evidence linkage](execution-protocol.md#execution-evidence-linkage).
- **Completion Condition:** [Product Definition of Done](../lifecycle/02-product.md#definition-of-done) and [work-item completion](definition-of-done.md).
- **Next-action / Entry-Exit Boundary:** [Product exit criteria](../lifecycle/02-product.md#exit-criteria), [work readiness](definition-of-ready.md), and [Re-entry](work-management.md#re-entry). Entry order alone does not authorize progression.

### UX

#### U1 UX Vision

- **Phase:** [UX](../lifecycle/03-ux.md)
- **Lifecycle Activity:** [U1 UX Vision](../lifecycle/03-ux.md#activities)
- **Role / Assignment Source:** [Contextual Assignment](roles-and-actor-assignment.md#assignment-model) and [Accountability and Authority](roles-and-actor-assignment.md#accountability-and-authority); no fixed phase Role is assigned here.
- **Inputs:** [UX inputs](../lifecycle/03-ux.md#inputs) and [work readiness](definition-of-ready.md). Activity-specific inputs remain contextual where the lifecycle lists only phase inputs.
- **Governing Standards:** [UX activity source](../lifecycle/03-ux.md#activities); [UX Vision](ux-vision.md); [Execution Protocol Standard](execution-protocol.md); [Work Management Standard](work-management.md)
- **Outputs / Artifacts:** [Documented UX direction](../lifecycle/03-ux.md#outputs-and-artifacts); [UX Vision](ux-vision.md). These sources retain applicable selection and optionality.
- **Capability Requirement:** No external capability required by the governing source.
- **Validation / Evidence:** [UX completion evidence](../lifecycle/03-ux.md#definition-of-done), [work validation](work-management.md#validation), and [execution evidence linkage](execution-protocol.md#execution-evidence-linkage).
- **Completion Condition:** [UX Definition of Done](../lifecycle/03-ux.md#definition-of-done) and [work-item completion](definition-of-done.md).
- **Next-action / Entry-Exit Boundary:** [UX exit criteria](../lifecycle/03-ux.md#exit-criteria), [work readiness](definition-of-ready.md), and [Re-entry](work-management.md#re-entry). Entry order alone does not authorize progression.

#### U2 User Understanding

- **Phase:** [UX](../lifecycle/03-ux.md)
- **Lifecycle Activity:** [U2 User Understanding](../lifecycle/03-ux.md#activities)
- **Role / Assignment Source:** [Contextual Assignment](roles-and-actor-assignment.md#assignment-model) and [Accountability and Authority](roles-and-actor-assignment.md#accountability-and-authority); no fixed phase Role is assigned here.
- **Inputs:** [UX inputs](../lifecycle/03-ux.md#inputs) and [work readiness](definition-of-ready.md). Activity-specific inputs remain contextual where the lifecycle lists only phase inputs.
- **Governing Standards:** [UX activity source](../lifecycle/03-ux.md#activities); [Users](users.md); [User Journey](user-journey.md); [Personas](personas.md); [Execution Protocol Standard](execution-protocol.md); [Work Management Standard](work-management.md)
- **Outputs / Artifacts:** [Evidence-based user and context understanding](../lifecycle/03-ux.md#outputs-and-artifacts); [Users](users.md); [User Journey](user-journey.md); [Personas](personas.md). These sources retain applicable selection and optionality.
- **Capability Requirement:** No external capability required by the governing source.
- **Validation / Evidence:** [UX completion evidence](../lifecycle/03-ux.md#definition-of-done), [work validation](work-management.md#validation), and [execution evidence linkage](execution-protocol.md#execution-evidence-linkage).
- **Completion Condition:** [UX Definition of Done](../lifecycle/03-ux.md#definition-of-done) and [work-item completion](definition-of-done.md).
- **Next-action / Entry-Exit Boundary:** [UX exit criteria](../lifecycle/03-ux.md#exit-criteria), [work readiness](definition-of-ready.md), and [Re-entry](work-management.md#re-entry). Entry order alone does not authorize progression.

#### U3 Experience Structure

- **Phase:** [UX](../lifecycle/03-ux.md)
- **Lifecycle Activity:** [U3 Experience Structure](../lifecycle/03-ux.md#activities)
- **Role / Assignment Source:** [Contextual Assignment](roles-and-actor-assignment.md#assignment-model) and [Accountability and Authority](roles-and-actor-assignment.md#accountability-and-authority); no fixed phase Role is assigned here.
- **Inputs:** [UX inputs](../lifecycle/03-ux.md#inputs) and [work readiness](definition-of-ready.md). Activity-specific inputs remain contextual where the lifecycle lists only phase inputs.
- **Governing Standards:** [UX activity source](../lifecycle/03-ux.md#activities); [User Flows](user-flows.md); [UX Information Architecture](ux-information-architecture.md); [Execution Protocol Standard](execution-protocol.md); [Work Management Standard](work-management.md)
- **Outputs / Artifacts:** [Experience flows and structural decisions](../lifecycle/03-ux.md#outputs-and-artifacts); [User Flows](user-flows.md); [UX Information Architecture](ux-information-architecture.md). These sources retain applicable selection and optionality.
- **Capability Requirement:** No external capability required by the governing source.
- **Validation / Evidence:** [UX completion evidence](../lifecycle/03-ux.md#definition-of-done), [work validation](work-management.md#validation), and [execution evidence linkage](execution-protocol.md#execution-evidence-linkage).
- **Completion Condition:** [UX Definition of Done](../lifecycle/03-ux.md#definition-of-done) and [work-item completion](definition-of-done.md).
- **Next-action / Entry-Exit Boundary:** [UX exit criteria](../lifecycle/03-ux.md#exit-criteria), [work readiness](definition-of-ready.md), and [Re-entry](work-management.md#re-entry). Entry order alone does not authorize progression.

#### U4 Experience Exploration

- **Phase:** [UX](../lifecycle/03-ux.md)
- **Lifecycle Activity:** [U4 Experience Exploration](../lifecycle/03-ux.md#activities)
- **Role / Assignment Source:** [Contextual Assignment](roles-and-actor-assignment.md#assignment-model) and [Accountability and Authority](roles-and-actor-assignment.md#accountability-and-authority); no fixed phase Role is assigned here.
- **Inputs:** [UX inputs](../lifecycle/03-ux.md#inputs) and [work readiness](definition-of-ready.md). Activity-specific inputs remain contextual where the lifecycle lists only phase inputs.
- **Governing Standards:** [UX activity source](../lifecycle/03-ux.md#activities); [Wireframes](wireframes.md); [Prototypes](prototypes.md); [UX Artifacts](ux-artifacts.md); [Execution Protocol Standard](execution-protocol.md); [Work Management Standard](work-management.md)
- **Outputs / Artifacts:** [Proportionate experience representations](../lifecycle/03-ux.md#outputs-and-artifacts); [Wireframes](wireframes.md); [Prototypes](prototypes.md); [UX Artifacts](ux-artifacts.md). These sources retain applicable selection and optionality.
- **Capability Requirement:** No external capability required by the governing source.
- **Validation / Evidence:** [UX completion evidence](../lifecycle/03-ux.md#definition-of-done), [work validation](work-management.md#validation), and [execution evidence linkage](execution-protocol.md#execution-evidence-linkage).
- **Completion Condition:** [UX Definition of Done](../lifecycle/03-ux.md#definition-of-done) and [work-item completion](definition-of-done.md).
- **Next-action / Entry-Exit Boundary:** [UX exit criteria](../lifecycle/03-ux.md#exit-criteria), [work readiness](definition-of-ready.md), and [Re-entry](work-management.md#re-entry). Entry order alone does not authorize progression.

#### U5 UX Validation

- **Phase:** [UX](../lifecycle/03-ux.md)
- **Lifecycle Activity:** [U5 UX Validation](../lifecycle/03-ux.md#activities)
- **Role / Assignment Source:** [Contextual Assignment](roles-and-actor-assignment.md#assignment-model) and [Accountability and Authority](roles-and-actor-assignment.md#accountability-and-authority); no fixed phase Role is assigned here.
- **Inputs:** [UX inputs](../lifecycle/03-ux.md#inputs) and [work readiness](definition-of-ready.md). Activity-specific inputs remain contextual where the lifecycle lists only phase inputs.
- **Governing Standards:** [UX activity source](../lifecycle/03-ux.md#activities); [UX Validation](ux-validation.md); [Product Backlog](product-backlog.md); [Execution Protocol Standard](execution-protocol.md); [Work Management Standard](work-management.md)
- **Outputs / Artifacts:** [Validation findings, decisions, and follow-up work](../lifecycle/03-ux.md#outputs-and-artifacts); [UX Validation](ux-validation.md); [Product Backlog](product-backlog.md). These sources retain applicable selection and optionality.
- **Capability Requirement:** No external capability required by the governing source.
- **Validation / Evidence:** [UX completion evidence](../lifecycle/03-ux.md#definition-of-done), [work validation](work-management.md#validation), and [execution evidence linkage](execution-protocol.md#execution-evidence-linkage).
- **Completion Condition:** [UX Definition of Done](../lifecycle/03-ux.md#definition-of-done) and [work-item completion](definition-of-done.md).
- **Next-action / Entry-Exit Boundary:** [UX exit criteria](../lifecycle/03-ux.md#exit-criteria), [work readiness](definition-of-ready.md), and [Re-entry](work-management.md#re-entry). Entry order alone does not authorize progression.

### Architecture

#### A1 — Define the system boundaries, responsibilities, interfaces, data, and quality attributes relevant to the product

- **Phase:** [Architecture](../lifecycle/04-architecture.md)
- **Lifecycle Activity:** [Define the system boundaries, responsibilities, interfaces, data, and quality attributes relevant to the product](../lifecycle/04-architecture.md#activities)
- **Role / Assignment Source:** [Contextual Assignment](roles-and-actor-assignment.md#assignment-model) and [Accountability and Authority](roles-and-actor-assignment.md#accountability-and-authority); no fixed phase Role is assigned here.
- **Inputs:** [Architecture inputs](../lifecycle/04-architecture.md#inputs) and [work readiness](definition-of-ready.md). Activity-specific inputs remain contextual where the lifecycle lists only phase inputs.
- **Governing Standards:** [Architecture activity source](../lifecycle/04-architecture.md#activities); [Architecture Vision](architecture-vision.md); [System Context](system-context.md); [High-Level Architecture](high-level-architecture.md); [Component Architecture](component-architecture.md); [API Design](api-design.md); [Data Model](data-model.md); [Security, Privacy, and Data Governance Standard](security-privacy-data-governance.md); [Execution Protocol Standard](execution-protocol.md); [Work Management Standard](work-management.md)
- **Outputs / Artifacts:** [System boundaries, interfaces, data, and quality constraints](../lifecycle/04-architecture.md#outputs-and-artifacts); [Architecture Vision](architecture-vision.md); [System Context](system-context.md); [High-Level Architecture](high-level-architecture.md); [Component Architecture](component-architecture.md); [API Design](api-design.md); [Data Model](data-model.md); [Security, Privacy, and Data Governance Standard](security-privacy-data-governance.md). These sources retain applicable selection and optionality.
- **Capability Requirement:** No external capability required by the governing source.
- **Validation / Evidence:** [Architecture completion evidence](../lifecycle/04-architecture.md#definition-of-done), [work validation](work-management.md#validation), and [execution evidence linkage](execution-protocol.md#execution-evidence-linkage).
- **Completion Condition:** [Architecture Definition of Done](../lifecycle/04-architecture.md#definition-of-done) and [work-item completion](definition-of-done.md).
- **Next-action / Entry-Exit Boundary:** [Architecture exit criteria](../lifecycle/04-architecture.md#exit-criteria), [work readiness](definition-of-ready.md), and [Re-entry](work-management.md#re-entry). Entry order alone does not authorize progression.

#### A2 — Evaluate material technical options and record architecture decisions

- **Phase:** [Architecture](../lifecycle/04-architecture.md)
- **Lifecycle Activity:** [Evaluate material technical options and record architecture decisions](../lifecycle/04-architecture.md#activities)
- **Role / Assignment Source:** [Contextual Assignment](roles-and-actor-assignment.md#assignment-model) and [Accountability and Authority](roles-and-actor-assignment.md#accountability-and-authority); no fixed phase Role is assigned here.
- **Inputs:** [Architecture inputs](../lifecycle/04-architecture.md#inputs) and [work readiness](definition-of-ready.md). Activity-specific inputs remain contextual where the lifecycle lists only phase inputs.
- **Governing Standards:** [Architecture activity source](../lifecycle/04-architecture.md#activities); [Architecture Decision Records](architecture-decision-records.md); [Execution Protocol Standard](execution-protocol.md); [Work Management Standard](work-management.md)
- **Outputs / Artifacts:** [Architecture direction and material decision records](../lifecycle/04-architecture.md#outputs-and-artifacts); [Architecture Decision Records](architecture-decision-records.md). These sources retain applicable selection and optionality.
- **Capability Requirement:** No external capability required by the governing source.
- **Validation / Evidence:** [Architecture completion evidence](../lifecycle/04-architecture.md#definition-of-done), [work validation](work-management.md#validation), and [execution evidence linkage](execution-protocol.md#execution-evidence-linkage).
- **Completion Condition:** [Architecture Definition of Done](../lifecycle/04-architecture.md#definition-of-done) and [work-item completion](definition-of-done.md).
- **Next-action / Entry-Exit Boundary:** [Architecture exit criteria](../lifecycle/04-architecture.md#exit-criteria), [work readiness](definition-of-ready.md), and [Re-entry](work-management.md#re-entry). Entry order alone does not authorize progression.

#### A3 — Identify implementation constraints, risks, and validation required before development

- **Phase:** [Architecture](../lifecycle/04-architecture.md)
- **Lifecycle Activity:** [Identify implementation constraints, risks, and validation required before development](../lifecycle/04-architecture.md#activities)
- **Role / Assignment Source:** [Contextual Assignment](roles-and-actor-assignment.md#assignment-model) and [Accountability and Authority](roles-and-actor-assignment.md#accountability-and-authority); no fixed phase Role is assigned here.
- **Inputs:** [Architecture inputs](../lifecycle/04-architecture.md#inputs) and [work readiness](definition-of-ready.md). Activity-specific inputs remain contextual where the lifecycle lists only phase inputs.
- **Governing Standards:** [Architecture activity source](../lifecycle/04-architecture.md#activities); [Architecture Artifacts](architecture-artifacts.md); [Testing Strategy](testing-strategy.md); [Security, Privacy, and Data Governance Standard](security-privacy-data-governance.md); [Execution Protocol Standard](execution-protocol.md); [Work Management Standard](work-management.md)
- **Outputs / Artifacts:** [Technical risks, assumptions, and validation evidence](../lifecycle/04-architecture.md#outputs-and-artifacts); [Architecture Artifacts](architecture-artifacts.md); [Testing Strategy](testing-strategy.md); [Security, Privacy, and Data Governance Standard](security-privacy-data-governance.md). These sources retain applicable selection and optionality.
- **Capability Requirement:** No external capability required by the governing source.
- **Validation / Evidence:** [Architecture completion evidence](../lifecycle/04-architecture.md#definition-of-done), [work validation](work-management.md#validation), and [execution evidence linkage](execution-protocol.md#execution-evidence-linkage).
- **Completion Condition:** [Architecture Definition of Done](../lifecycle/04-architecture.md#definition-of-done) and [work-item completion](definition-of-done.md).
- **Next-action / Entry-Exit Boundary:** [Architecture exit criteria](../lifecycle/04-architecture.md#exit-criteria), [work readiness](definition-of-ready.md), and [Re-entry](work-management.md#re-entry). Entry order alone does not authorize progression.

#### A4 — Refine the Product Backlog with architecture-enabling work where needed

- **Phase:** [Architecture](../lifecycle/04-architecture.md)
- **Lifecycle Activity:** [Refine the Product Backlog with architecture-enabling work where needed](../lifecycle/04-architecture.md#activities)
- **Role / Assignment Source:** [Contextual Assignment](roles-and-actor-assignment.md#assignment-model) and [Accountability and Authority](roles-and-actor-assignment.md#accountability-and-authority); no fixed phase Role is assigned here.
- **Inputs:** [Architecture inputs](../lifecycle/04-architecture.md#inputs) and [work readiness](definition-of-ready.md). Activity-specific inputs remain contextual where the lifecycle lists only phase inputs.
- **Governing Standards:** [Architecture activity source](../lifecycle/04-architecture.md#activities); [Product Backlog](product-backlog.md); [Execution Protocol Standard](execution-protocol.md); [Work Management Standard](work-management.md)
- **Outputs / Artifacts:** [Architecture-enabling backlog work](../lifecycle/04-architecture.md#outputs-and-artifacts); [Product Backlog](product-backlog.md). These sources retain applicable selection and optionality.
- **Capability Requirement:** No external capability required by the governing source.
- **Validation / Evidence:** [Architecture completion evidence](../lifecycle/04-architecture.md#definition-of-done), [work validation](work-management.md#validation), and [execution evidence linkage](execution-protocol.md#execution-evidence-linkage).
- **Completion Condition:** [Architecture Definition of Done](../lifecycle/04-architecture.md#definition-of-done) and [work-item completion](definition-of-done.md).
- **Next-action / Entry-Exit Boundary:** [Architecture exit criteria](../lifecycle/04-architecture.md#exit-criteria), [work readiness](definition-of-ready.md), and [Re-entry](work-management.md#re-entry). Entry order alone does not authorize progression.

### Development

#### D1 Implementation

- **Phase:** [Development](../lifecycle/05-development.md)
- **Lifecycle Activity:** [D1 Implementation](../lifecycle/05-development.md#activities)
- **Role / Assignment Source:** [Contextual Assignment](roles-and-actor-assignment.md#assignment-model) and [Accountability and Authority](roles-and-actor-assignment.md#accountability-and-authority); no fixed phase Role is assigned here.
- **Inputs:** [Development inputs](../lifecycle/05-development.md#inputs) and [work readiness](definition-of-ready.md). Activity-specific inputs remain contextual where the lifecycle lists only phase inputs.
- **Governing Standards:** [Development activity source](../lifecycle/05-development.md#activities); [Coding Standards](coding-standards.md); [Execution Protocol Standard](execution-protocol.md); [Work Management Standard](work-management.md)
- **Outputs / Artifacts:** [Implementation increment and applicable source, configuration, or documentation](../lifecycle/05-development.md#outputs-and-artifacts); [Coding Standards](coding-standards.md). These sources retain applicable selection and optionality.
- **Capability Requirement:** No external capability required by the governing source.
- **Validation / Evidence:** [Development completion evidence](../lifecycle/05-development.md#definition-of-done), [work validation](work-management.md#validation), and [execution evidence linkage](execution-protocol.md#execution-evidence-linkage).
- **Completion Condition:** [Development Definition of Done](../lifecycle/05-development.md#definition-of-done) and [work-item completion](definition-of-done.md).
- **Next-action / Entry-Exit Boundary:** [Development exit criteria](../lifecycle/05-development.md#exit-criteria), [work readiness](definition-of-ready.md), and [Re-entry](work-management.md#re-entry). Entry order alone does not authorize progression.

#### D2 Verification

- **Phase:** [Development](../lifecycle/05-development.md)
- **Lifecycle Activity:** [D2 Verification](../lifecycle/05-development.md#activities)
- **Role / Assignment Source:** [Contextual Assignment](roles-and-actor-assignment.md#assignment-model) and [Accountability and Authority](roles-and-actor-assignment.md#accountability-and-authority); no fixed phase Role is assigned here.
- **Inputs:** [Development inputs](../lifecycle/05-development.md#inputs) and [work readiness](definition-of-ready.md). Activity-specific inputs remain contextual where the lifecycle lists only phase inputs.
- **Governing Standards:** [Development activity source](../lifecycle/05-development.md#activities); [Testing Strategy](testing-strategy.md); [Continuous Integration](continuous-integration.md); [Execution Protocol Standard](execution-protocol.md); [Work Management Standard](work-management.md)
- **Outputs / Artifacts:** [Validation evidence and applicable tests or automation](../lifecycle/05-development.md#outputs-and-artifacts); [Testing Strategy](testing-strategy.md); [Continuous Integration](continuous-integration.md). These sources retain applicable selection and optionality.
- **Capability Requirement:** No external capability required by the governing source.
- **Validation / Evidence:** [Development completion evidence](../lifecycle/05-development.md#definition-of-done), [work validation](work-management.md#validation), and [execution evidence linkage](execution-protocol.md#execution-evidence-linkage).
- **Completion Condition:** [Development Definition of Done](../lifecycle/05-development.md#definition-of-done) and [work-item completion](definition-of-done.md).
- **Next-action / Entry-Exit Boundary:** [Development exit criteria](../lifecycle/05-development.md#exit-criteria), [work readiness](definition-of-ready.md), and [Re-entry](work-management.md#re-entry). Entry order alone does not authorize progression.

#### D3 Review and Integration

- **Phase:** [Development](../lifecycle/05-development.md)
- **Lifecycle Activity:** [D3 Review and Integration](../lifecycle/05-development.md#activities)
- **Role / Assignment Source:** [Contextual Assignment](roles-and-actor-assignment.md#assignment-model) and [Accountability and Authority](roles-and-actor-assignment.md#accountability-and-authority); no fixed phase Role is assigned here.
- **Inputs:** [Development inputs](../lifecycle/05-development.md#inputs) and [work readiness](definition-of-ready.md). Activity-specific inputs remain contextual where the lifecycle lists only phase inputs.
- **Governing Standards:** [Development activity source](../lifecycle/05-development.md#activities); [Code Review Standard](code-review-standard.md); [Branch Workflow](branch-workflow.md); [Execution Protocol Standard](execution-protocol.md); [Work Management Standard](work-management.md)
- **Outputs / Artifacts:** [Integrated increment and review evidence](../lifecycle/05-development.md#outputs-and-artifacts); [Code Review Standard](code-review-standard.md); [Branch Workflow](branch-workflow.md). These sources retain applicable selection and optionality.
- **Capability Requirement:** No external capability required by the governing source.
- **Validation / Evidence:** [Development completion evidence](../lifecycle/05-development.md#definition-of-done), [work validation](work-management.md#validation), and [execution evidence linkage](execution-protocol.md#execution-evidence-linkage).
- **Completion Condition:** [Development Definition of Done](../lifecycle/05-development.md#definition-of-done) and [work-item completion](definition-of-done.md).
- **Next-action / Entry-Exit Boundary:** [Development exit criteria](../lifecycle/05-development.md#exit-criteria), [work readiness](definition-of-ready.md), and [Re-entry](work-management.md#re-entry). Entry order alone does not authorize progression.

#### D4 Learning and Refinement

- **Phase:** [Development](../lifecycle/05-development.md)
- **Lifecycle Activity:** [D4 Learning and Refinement](../lifecycle/05-development.md#activities)
- **Role / Assignment Source:** [Contextual Assignment](roles-and-actor-assignment.md#assignment-model) and [Accountability and Authority](roles-and-actor-assignment.md#accountability-and-authority); no fixed phase Role is assigned here.
- **Inputs:** [Development inputs](../lifecycle/05-development.md#inputs) and [work readiness](definition-of-ready.md). Activity-specific inputs remain contextual where the lifecycle lists only phase inputs.
- **Governing Standards:** [Development activity source](../lifecycle/05-development.md#activities); [Bug Management](bug-management.md); [Technical Debt Management](technical-debt-management.md); [Product Backlog](product-backlog.md); [Execution Protocol Standard](execution-protocol.md); [Work Management Standard](work-management.md)
- **Outputs / Artifacts:** [Traceable findings, defects, debt, and follow-up work](../lifecycle/05-development.md#outputs-and-artifacts); [Bug Management](bug-management.md); [Technical Debt Management](technical-debt-management.md); [Product Backlog](product-backlog.md). These sources retain applicable selection and optionality.
- **Capability Requirement:** No external capability required by the governing source.
- **Validation / Evidence:** [Development completion evidence](../lifecycle/05-development.md#definition-of-done), [work validation](work-management.md#validation), and [execution evidence linkage](execution-protocol.md#execution-evidence-linkage).
- **Completion Condition:** [Development Definition of Done](../lifecycle/05-development.md#definition-of-done) and [work-item completion](definition-of-done.md).
- **Next-action / Entry-Exit Boundary:** [Development exit criteria](../lifecycle/05-development.md#exit-criteria), [work readiness](definition-of-ready.md), and [Re-entry](work-management.md#re-entry). Entry order alone does not authorize progression.

### Release

#### R1 Release planning

- **Phase:** [Release](../lifecycle/06-release.md)
- **Lifecycle Activity:** [R1 Release planning](../lifecycle/06-release.md#activities)
- **Role / Assignment Source:** [Contextual Assignment](roles-and-actor-assignment.md#assignment-model) and [Accountability and Authority](roles-and-actor-assignment.md#accountability-and-authority); no fixed phase Role is assigned here.
- **Inputs:** [Release inputs](../lifecycle/06-release.md#inputs) and [work readiness](definition-of-ready.md). Activity-specific inputs remain contextual where the lifecycle lists only phase inputs.
- **Governing Standards:** [Release activity source](../lifecycle/06-release.md#activities); [Release Strategy](release-strategy.md); [Versioning Standard](versioning-standard.md); [Execution Protocol Standard](execution-protocol.md); [Work Management Standard](work-management.md)
- **Outputs / Artifacts:** [Release scope, audience, versioning decision, and conditions](../lifecycle/06-release.md#outputs-and-artifacts); [Release Strategy](release-strategy.md); [Versioning Standard](versioning-standard.md). These sources retain applicable selection and optionality.
- **Capability Requirement:** No external capability required by the governing source.
- **Validation / Evidence:** [Release completion evidence](../lifecycle/06-release.md#definition-of-done), [work validation](work-management.md#validation), and [execution evidence linkage](execution-protocol.md#execution-evidence-linkage).
- **Completion Condition:** [Release Definition of Done](../lifecycle/06-release.md#definition-of-done) and [work-item completion](definition-of-done.md).
- **Next-action / Entry-Exit Boundary:** [Release exit criteria](../lifecycle/06-release.md#exit-criteria), [work readiness](definition-of-ready.md), and [Re-entry](work-management.md#re-entry). Entry order alone does not authorize progression.

#### R2 Release readiness

- **Phase:** [Release](../lifecycle/06-release.md)
- **Lifecycle Activity:** [R2 Release readiness](../lifecycle/06-release.md#activities)
- **Role / Assignment Source:** [Contextual Assignment](roles-and-actor-assignment.md#assignment-model) and [Accountability and Authority](roles-and-actor-assignment.md#accountability-and-authority); no fixed phase Role is assigned here.
- **Inputs:** [Release inputs](../lifecycle/06-release.md#inputs) and [work readiness](definition-of-ready.md). Activity-specific inputs remain contextual where the lifecycle lists only phase inputs.
- **Governing Standards:** [Release activity source](../lifecycle/06-release.md#activities); [Release Strategy](release-strategy.md); [Release Notes](release-notes.md); [Rollback Strategy](rollback-strategy.md); [Execution Protocol Standard](execution-protocol.md); [Work Management Standard](work-management.md)
- **Outputs / Artifacts:** [Readiness, limitations, communications, and recovery evidence](../lifecycle/06-release.md#outputs-and-artifacts); [Release Strategy](release-strategy.md); [Release Notes](release-notes.md); [Rollback Strategy](rollback-strategy.md). These sources retain applicable selection and optionality.
- **Capability Requirement:** No external capability required by the governing source.
- **Validation / Evidence:** [Release completion evidence](../lifecycle/06-release.md#definition-of-done), [work validation](work-management.md#validation), and [execution evidence linkage](execution-protocol.md#execution-evidence-linkage).
- **Completion Condition:** [Release Definition of Done](../lifecycle/06-release.md#definition-of-done) and [work-item completion](definition-of-done.md).
- **Next-action / Entry-Exit Boundary:** [Release exit criteria](../lifecycle/06-release.md#exit-criteria), [work readiness](definition-of-ready.md), and [Re-entry](work-management.md#re-entry). Entry order alone does not authorize progression.

#### R3 Publication

- **Phase:** [Release](../lifecycle/06-release.md)
- **Lifecycle Activity:** [R3 Publication](../lifecycle/06-release.md#activities)
- **Role / Assignment Source:** [Contextual Assignment](roles-and-actor-assignment.md#assignment-model) and [Accountability and Authority](roles-and-actor-assignment.md#accountability-and-authority); no fixed phase Role is assigned here.
- **Inputs:** [Release inputs](../lifecycle/06-release.md#inputs) and [work readiness](definition-of-ready.md). Activity-specific inputs remain contextual where the lifecycle lists only phase inputs.
- **Governing Standards:** [Release activity source](../lifecycle/06-release.md#activities); [Release Strategy](release-strategy.md); [Deployment Strategy](deployment-strategy.md); [Execution Protocol Standard](execution-protocol.md); [Work Management Standard](work-management.md)
- **Outputs / Artifacts:** [Released increment and release or deployment evidence](../lifecycle/06-release.md#outputs-and-artifacts); [Release Strategy](release-strategy.md); [Deployment Strategy](deployment-strategy.md). These sources retain applicable selection and optionality.
- **Capability Requirement:** No external capability required by the governing source.
- **Validation / Evidence:** [Release completion evidence](../lifecycle/06-release.md#definition-of-done), [work validation](work-management.md#validation), and [execution evidence linkage](execution-protocol.md#execution-evidence-linkage).
- **Completion Condition:** [Release Definition of Done](../lifecycle/06-release.md#definition-of-done) and [work-item completion](definition-of-done.md).
- **Next-action / Entry-Exit Boundary:** [Release exit criteria](../lifecycle/06-release.md#exit-criteria), [work readiness](definition-of-ready.md), and [Re-entry](work-management.md#re-entry). Entry order alone does not authorize progression.

#### R4 Communication and observation

- **Phase:** [Release](../lifecycle/06-release.md)
- **Lifecycle Activity:** [R4 Communication and observation](../lifecycle/06-release.md#activities)
- **Role / Assignment Source:** [Contextual Assignment](roles-and-actor-assignment.md#assignment-model) and [Accountability and Authority](roles-and-actor-assignment.md#accountability-and-authority); no fixed phase Role is assigned here.
- **Inputs:** [Release inputs](../lifecycle/06-release.md#inputs) and [work readiness](definition-of-ready.md). Activity-specific inputs remain contextual where the lifecycle lists only phase inputs.
- **Governing Standards:** [Release activity source](../lifecycle/06-release.md#activities); [Release Notes](release-notes.md); [Product Monitoring](product-monitoring.md); [Execution Protocol Standard](execution-protocol.md); [Work Management Standard](work-management.md)
- **Outputs / Artifacts:** [Release information, observation, and follow-up work](../lifecycle/06-release.md#outputs-and-artifacts); [Release Notes](release-notes.md); [Product Monitoring](product-monitoring.md). These sources retain applicable selection and optionality.
- **Capability Requirement:** No external capability required by the governing source.
- **Validation / Evidence:** [Release completion evidence](../lifecycle/06-release.md#definition-of-done), [work validation](work-management.md#validation), and [execution evidence linkage](execution-protocol.md#execution-evidence-linkage).
- **Completion Condition:** [Release Definition of Done](../lifecycle/06-release.md#definition-of-done) and [work-item completion](definition-of-done.md).
- **Next-action / Entry-Exit Boundary:** [Release exit criteria](../lifecycle/06-release.md#exit-criteria), [work readiness](definition-of-ready.md), and [Re-entry](work-management.md#re-entry). Entry order alone does not authorize progression.

#### R5 Recovery

- **Phase:** [Release](../lifecycle/06-release.md)
- **Lifecycle Activity:** [R5 Recovery](../lifecycle/06-release.md#activities)
- **Role / Assignment Source:** [Contextual Assignment](roles-and-actor-assignment.md#assignment-model) and [Accountability and Authority](roles-and-actor-assignment.md#accountability-and-authority); no fixed phase Role is assigned here.
- **Inputs:** [Release inputs](../lifecycle/06-release.md#inputs) and [work readiness](definition-of-ready.md). Activity-specific inputs remain contextual where the lifecycle lists only phase inputs.
- **Governing Standards:** [Release activity source](../lifecycle/06-release.md#activities); [Rollback Strategy](rollback-strategy.md); [Bug Management](bug-management.md); [Incident Management](incident-management.md); [Execution Protocol Standard](execution-protocol.md); [Work Management Standard](work-management.md)
- **Outputs / Artifacts:** [Recovery decision, action, validation, and follow-up evidence](../lifecycle/06-release.md#outputs-and-artifacts); [Rollback Strategy](rollback-strategy.md); [Bug Management](bug-management.md); [Incident Management](incident-management.md). These sources retain applicable selection and optionality.
- **Capability Requirement:** No external capability required by the governing source.
- **Validation / Evidence:** [Release completion evidence](../lifecycle/06-release.md#definition-of-done), [work validation](work-management.md#validation), and [execution evidence linkage](execution-protocol.md#execution-evidence-linkage).
- **Completion Condition:** [Release Definition of Done](../lifecycle/06-release.md#definition-of-done) and [work-item completion](definition-of-done.md).
- **Next-action / Entry-Exit Boundary:** [Release exit criteria](../lifecycle/06-release.md#exit-criteria), [work readiness](definition-of-ready.md), and [Re-entry](work-management.md#re-entry). Entry order alone does not authorize progression.

### Maintenance

#### M1 Observe and assess

- **Phase:** [Maintenance](../lifecycle/07-maintenance.md)
- **Lifecycle Activity:** [M1 Observe and assess](../lifecycle/07-maintenance.md#activities)
- **Role / Assignment Source:** [Contextual Assignment](roles-and-actor-assignment.md#assignment-model) and [Accountability and Authority](roles-and-actor-assignment.md#accountability-and-authority); no fixed phase Role is assigned here.
- **Inputs:** [Maintenance inputs](../lifecycle/07-maintenance.md#inputs) and [work readiness](definition-of-ready.md). Activity-specific inputs remain contextual where the lifecycle lists only phase inputs.
- **Governing Standards:** [Maintenance activity source](../lifecycle/07-maintenance.md#activities); [Product Monitoring](product-monitoring.md); [Bug Management](bug-management.md); [Incident Management](incident-management.md); [Execution Protocol Standard](execution-protocol.md); [Work Management Standard](work-management.md)
- **Outputs / Artifacts:** [Assessed feedback, incidents, defects, and operational signals](../lifecycle/07-maintenance.md#outputs-and-artifacts); [Product Monitoring](product-monitoring.md); [Bug Management](bug-management.md); [Incident Management](incident-management.md). These sources retain applicable selection and optionality.
- **Capability Requirement:** No external capability required by the governing source.
- **Validation / Evidence:** [Maintenance completion evidence](../lifecycle/07-maintenance.md#definition-of-done), [work validation](work-management.md#validation), and [execution evidence linkage](execution-protocol.md#execution-evidence-linkage).
- **Completion Condition:** [Maintenance Definition of Done](../lifecycle/07-maintenance.md#definition-of-done) and [work-item completion](definition-of-done.md).
- **Next-action / Entry-Exit Boundary:** [Maintenance exit criteria](../lifecycle/07-maintenance.md#exit-criteria), [work readiness](definition-of-ready.md), and [Re-entry](work-management.md#re-entry). Entry order alone does not authorize progression.

#### M2 Respond and recover

- **Phase:** [Maintenance](../lifecycle/07-maintenance.md)
- **Lifecycle Activity:** [M2 Respond and recover](../lifecycle/07-maintenance.md#activities)
- **Role / Assignment Source:** [Contextual Assignment](roles-and-actor-assignment.md#assignment-model) and [Accountability and Authority](roles-and-actor-assignment.md#accountability-and-authority); no fixed phase Role is assigned here.
- **Inputs:** [Maintenance inputs](../lifecycle/07-maintenance.md#inputs) and [work readiness](definition-of-ready.md). Activity-specific inputs remain contextual where the lifecycle lists only phase inputs.
- **Governing Standards:** [Maintenance activity source](../lifecycle/07-maintenance.md#activities); [Incident Management](incident-management.md); [Bug Management](bug-management.md); [Rollback Strategy](rollback-strategy.md); [Execution Protocol Standard](execution-protocol.md); [Work Management Standard](work-management.md)
- **Outputs / Artifacts:** [Corrective work and recovery evidence with accountable ownership](../lifecycle/07-maintenance.md#outputs-and-artifacts); [Incident Management](incident-management.md); [Bug Management](bug-management.md); [Rollback Strategy](rollback-strategy.md). These sources retain applicable selection and optionality.
- **Capability Requirement:** No external capability required by the governing source.
- **Validation / Evidence:** [Maintenance completion evidence](../lifecycle/07-maintenance.md#definition-of-done), [work validation](work-management.md#validation), and [execution evidence linkage](execution-protocol.md#execution-evidence-linkage).
- **Completion Condition:** [Maintenance Definition of Done](../lifecycle/07-maintenance.md#definition-of-done) and [work-item completion](definition-of-done.md).
- **Next-action / Entry-Exit Boundary:** [Maintenance exit criteria](../lifecycle/07-maintenance.md#exit-criteria), [work readiness](definition-of-ready.md), and [Re-entry](work-management.md#re-entry). Entry order alone does not authorize progression.

#### M3 Improve and evolve

- **Phase:** [Maintenance](../lifecycle/07-maintenance.md)
- **Lifecycle Activity:** [M3 Improve and evolve](../lifecycle/07-maintenance.md#activities)
- **Role / Assignment Source:** [Contextual Assignment](roles-and-actor-assignment.md#assignment-model) and [Accountability and Authority](roles-and-actor-assignment.md#accountability-and-authority); no fixed phase Role is assigned here.
- **Inputs:** [Maintenance inputs](../lifecycle/07-maintenance.md#inputs) and [work readiness](definition-of-ready.md). Activity-specific inputs remain contextual where the lifecycle lists only phase inputs.
- **Governing Standards:** [Maintenance activity source](../lifecycle/07-maintenance.md#activities); [Technical Debt Management](technical-debt-management.md); [Product Evolution](product-evolution.md); [Product Backlog](product-backlog.md); [Execution Protocol Standard](execution-protocol.md); [Work Management Standard](work-management.md)
- **Outputs / Artifacts:** [Traceable improvement work and lifecycle re-entry decisions](../lifecycle/07-maintenance.md#outputs-and-artifacts); [Technical Debt Management](technical-debt-management.md); [Product Evolution](product-evolution.md); [Product Backlog](product-backlog.md). These sources retain applicable selection and optionality.
- **Capability Requirement:** No external capability required by the governing source.
- **Validation / Evidence:** [Maintenance completion evidence](../lifecycle/07-maintenance.md#definition-of-done), [work validation](work-management.md#validation), and [execution evidence linkage](execution-protocol.md#execution-evidence-linkage).
- **Completion Condition:** [Maintenance Definition of Done](../lifecycle/07-maintenance.md#definition-of-done) and [work-item completion](definition-of-done.md).
- **Next-action / Entry-Exit Boundary:** [Maintenance exit criteria](../lifecycle/07-maintenance.md#exit-criteria), [work readiness](definition-of-ready.md), and [Re-entry](work-management.md#re-entry). Entry order alone does not authorize progression.

#### M4 Preserve operational knowledge

- **Phase:** [Maintenance](../lifecycle/07-maintenance.md)
- **Lifecycle Activity:** [M4 Preserve operational knowledge](../lifecycle/07-maintenance.md#activities)
- **Role / Assignment Source:** [Contextual Assignment](roles-and-actor-assignment.md#assignment-model) and [Accountability and Authority](roles-and-actor-assignment.md#accountability-and-authority); no fixed phase Role is assigned here.
- **Inputs:** [Maintenance inputs](../lifecycle/07-maintenance.md#inputs) and [work readiness](definition-of-ready.md). Activity-specific inputs remain contextual where the lifecycle lists only phase inputs.
- **Governing Standards:** [Maintenance activity source](../lifecycle/07-maintenance.md#activities); [Artifact Standard](artifact-standard.md); [Documentation Navigation Standard](documentation-navigation.md); [Execution Protocol Standard](execution-protocol.md); [Work Management Standard](work-management.md)
- **Outputs / Artifacts:** [Updated ownership, decisions, evidence, and documentation](../lifecycle/07-maintenance.md#outputs-and-artifacts); [Artifact Standard](artifact-standard.md); [Documentation Navigation Standard](documentation-navigation.md). These sources retain applicable selection and optionality.
- **Capability Requirement:** No external capability required by the governing source.
- **Validation / Evidence:** [Maintenance completion evidence](../lifecycle/07-maintenance.md#definition-of-done), [work validation](work-management.md#validation), and [execution evidence linkage](execution-protocol.md#execution-evidence-linkage).
- **Completion Condition:** [Maintenance Definition of Done](../lifecycle/07-maintenance.md#definition-of-done) and [work-item completion](definition-of-done.md).
- **Next-action / Entry-Exit Boundary:** [Maintenance exit criteria](../lifecycle/07-maintenance.md#exit-criteria), [work readiness](definition-of-ready.md), and [Re-entry](work-management.md#re-entry). Entry order alone does not authorize progression.

## Current coverage and status

The inventory covers all 33 activities currently listed across Foundation (5), Product (6), UX (5), Architecture (4), Development (4), Release (5), and Maintenance (4).

Coverage means that the activity sources and their applicable boundaries are discoverable. It does not declare any adopting product complete, certify an execution mechanism, or publish a machine-readable schema. Future lifecycle changes require corresponding inventory review; each lifecycle document remains authoritative.

## References

- [Foundation Phase](../lifecycle/01-foundation.md)
- [Product Phase](../lifecycle/02-product.md)
- [UX Phase](../lifecycle/03-ux.md)
- [Architecture Phase](../lifecycle/04-architecture.md)
- [Development Phase](../lifecycle/05-development.md)
- [Release Phase](../lifecycle/06-release.md)
- [Maintenance Phase](../lifecycle/07-maintenance.md)
- [Roles and Actor Assignment Standard](roles-and-actor-assignment.md)
- [Work Management Standard](work-management.md)
- [Execution Protocol Standard](execution-protocol.md)
- [Definition of Ready](definition-of-ready.md)
- [Definition of Done](definition-of-done.md)
- [Artifact Standard](artifact-standard.md)
- [Artifact Catalog](artifact-catalog.md)
- [Documentation Information Architecture](documentation-information-architecture.md)
- [Documentation Navigation Standard](documentation-navigation.md)
- [Documentation Style Guide](documentation-style-guide.md)
- [Terminology Standard](terminology-standard.md)
