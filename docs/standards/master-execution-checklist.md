# Master Execution Checklist

## Purpose

Define the governing contract and stable entry structure for the cross-lifecycle operational index spanning Foundation through Maintenance.

The Master Execution Checklist makes applicable sources and execution boundaries discoverable for each lifecycle activity. It links to authoritative Playbook content rather than duplicating that content.

## Scope

This standard governs how Master Execution Checklist entries are structured and how they reference their authoritative sources. It does not replace lifecycle documents, Work Management, the Execution Protocol, readiness or completion standards, or artifact governance.

The checklist is provider-independent and directly usable by humans. It does not define a workflow, state model, execution mechanism, provider integration, or machine-readable execution format.

This initial publication defines only the governing contract and entry structure. The Foundation-through-Maintenance operational inventory is not yet populated and remains pending.

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

## Current coverage and status

This publication establishes only the governing contract, source-of-truth boundaries, and stable entry structure.

No lifecycle activity entries are populated. Foundation, Product, UX, Architecture, Development, Release, and Maintenance coverage remains pending a later increment. The Master Execution Checklist MUST NOT be treated as complete until that operational inventory and its required validation are published.

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
