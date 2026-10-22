# Lifecycle Execution Guide

## Purpose and boundaries

Use this optional practice to answer four questions for a bounded increment: what to read, what to produce, how to evidence completion, and whether the next activity can begin. It applies existing rules; it creates no new gate, mandatory artifact, Role, or execution format.

The [Master Execution Checklist](../standards/master-execution-checklist.md) remains the activity-level navigation source. Lifecycle documents own inputs, outputs, and exit criteria; [Definition of Ready](../standards/definition-of-ready.md), [Definition of Done](../standards/definition-of-done.md), [Work Management](../standards/work-management.md), and [Execution Protocol](../standards/execution-protocol.md) retain their responsibilities.

## Before starting an item

1. Identify the intended outcome, current phase, bounded activity, and next decision.
2. Open that activity's Master Execution Checklist entry and the linked lifecycle document.
3. Read the sources governing this item's acceptance evidence, constraints, and affected artifacts. Read the applicable readiness and execution conditions before acting.
4. Follow complementary examples or provider guides only when they help implement a selected approach. Their existence does not make every document, tool, or example a prerequisite.
5. Identify actual inputs, scoped Assignments, relevant Authority, and unresolved dependencies. Apply the governing readiness and authorization checks; reading alone does not satisfy them.

For a local reading path, distinguish **governing reading** (sources applicable to this item), **contextual prerequisites** (decisions or evidence it consumes), and **complementary reading** (examples and optional implementations). These labels help navigation; they do not introduce a new normative classification.

## Phase orientation

This table points to authoritative sources rather than reproducing their inventories. Select the activity within the linked inventory for its governing standards, outputs, validation, and completion conditions.

| Phase | Begin with | Activity-level sources | Before advancing |
| --- | --- | --- | --- |
| Foundation | [Purpose and inputs](../lifecycle/01-foundation.md#inputs) | [F1–F5](../standards/master-execution-checklist.md#foundation) | [Foundation exit criteria](../lifecycle/01-foundation.md#exit-criteria) and [Product inputs](../lifecycle/02-product.md#inputs) |
| Product | [Inputs](../lifecycle/02-product.md#inputs) | [P1–P6](../standards/master-execution-checklist.md#product) | [Product exit criteria](../lifecycle/02-product.md#exit-criteria) and [UX inputs](../lifecycle/03-ux.md#inputs) |
| UX | [Inputs](../lifecycle/03-ux.md#inputs) | [U1–U5](../standards/master-execution-checklist.md#ux) | [UX exit criteria](../lifecycle/03-ux.md#exit-criteria) and [Architecture inputs](../lifecycle/04-architecture.md#inputs) |
| Architecture | [Inputs](../lifecycle/04-architecture.md#inputs) | [Architecture activities](../standards/master-execution-checklist.md#architecture) | [Architecture exit criteria](../lifecycle/04-architecture.md#exit-criteria) and [Development inputs](../lifecycle/05-development.md#inputs) |
| Development | [Inputs](../lifecycle/05-development.md#inputs) | [D1–D4](../standards/master-execution-checklist.md#development) | [Development exit criteria](../lifecycle/05-development.md#exit-criteria) and [Release inputs](../lifecycle/06-release.md#inputs) |
| Release | [Inputs](../lifecycle/06-release.md#inputs) | [R1–R5](../standards/master-execution-checklist.md#release) | [Release exit criteria](../lifecycle/06-release.md#exit-criteria) and [Maintenance inputs](../lifecycle/07-maintenance.md#inputs) |
| Maintenance | [Inputs](../lifecycle/07-maintenance.md#inputs) | [M1–M4](../standards/master-execution-checklist.md#maintenance) | [Maintenance exit criteria](../lifecycle/07-maintenance.md#exit-criteria); identify the applicable phase for resulting work |

## Documentation sufficient for the next decision

Assess sufficiency against the bounded work and governing criteria, rather than the number of files or populated headings:

- Can the next activity find and use its necessary inputs?
- Are material decisions, constraints, and acceptance evidence explicit and consistent?
- Does the evidence show the required outcome, rather than only that a document was written?
- For unresolved questions, does the governing source permit deferral, and are owner, impact, and reassessment condition recorded as required?
- Would a deferred question prevent the specific next decision? If so, resolve it before depending on it.

For example, Foundation can establish a usable documentation entry point without specifying future deployment infrastructure. That infrastructure question may wait if it does not prevent Product work and its disposition meets Foundation's rules. A missing tracking owner cannot be dismissed as future detail when assessing Foundation completion.

Use existing records where they suffice. A separate document per activity is not assumed.

## Closing work and checking progression

Compare the actual result with acceptance evidence, record validation and applicable review, and identify any required integration evidence. Preserve limitations and their governed disposition. Record the completion decision under Definition of Done before updating the selected tracking representation.

Then assess the phase outcome and the next activity's entry conditions separately. Closed items do not by themselves establish phase completion; phase completion does not automatically authorize the next execution attempt. Use the [boundary review](milestone-boundary-review.md) when checking the combined result and the [Foundation example](../../examples/foundation-completion-example.md) for a bounded illustration.

## Repository reading map

Under [Documentation Navigation](../standards/documentation-navigation.md), a reading map can be a short ordered list in the root entry point or a linked guide. Start with purpose and current state, continue through governing sources and decisions, then point to implementation and validation details.

Record who maintains the map under the repository's adopted ownership model. Review it when documents are added, moved, removed, or superseded. Check paths and heading targets, distinguish optional implementation reading, and keep planned content separate from existing destinations.

A tool-specific file such as `.repo-reader.json` is an optional implementation. Before adopting it, check the selected reader's current schema and behavior, validate its paths against the repository, and keep it aligned with the human-readable map. This practice defines no JSON schema and makes no claim that every Repo Reader supports the same format. File order is navigation, never execution authorization or completion evidence.
