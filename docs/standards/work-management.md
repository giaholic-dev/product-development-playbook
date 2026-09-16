# Work Management Standard

## Purpose

Define the minimum framework-independent work-management model used to manage Playbook work from identification through completion and feedback.

## Scope

This standard governs the transversal management of work across the Product Development Playbook. Work management is independent from Lifecycle Phase and applies across lifecycle phases.

The model is framework-independent. It does not require Scrum, Kanban, Sprints, iterations, estimates, ceremonies, work-in-progress limits, or continuous delivery. It does not require AI and does not prescribe a provider, tool, platform, or organizational structure.

Existing authoritative standards remain authoritative for the concepts they already govern.

## Definitions

### Work Management

Work Management is the transversal discipline of governing how Playbook work is identified, prepared, selected, progressed, evaluated, completed, and improved. It operates across Lifecycle Phases, but does not determine the Lifecycle Phase or Work Type of a work item. It is distinct from Workflow State and does not prescribe a delivery framework or operating model.

Lifecycle Phase identifies where work primarily belongs in the product lifecycle, Work Type identifies the work's primary nature, and Workflow State represents its current operational progress. Work Management governs how work is managed through its management lifecycle without replacing those concepts or their authoritative standards.

### Work Management Activity

A Work Management Activity is a responsibility-oriented management action applied to Playbook work for a defined management purpose. It represents something performed to manage work; it is not a Lifecycle Phase, Work Type, or Workflow State.

A Work Management Activity does not by itself imply a mandatory sequence, transition, or persistent status or field. It MAY occur whenever applicable and MAY recur when new information, feedback, risk, or changed conditions require it. Work Management is the transversal discipline; a Work Management Activity is an action performed within that discipline for a management purpose. A project or implementation MAY represent an activity through workflow mechanisms when useful, but this standard does not require that representation.

## Intake

Intake is the Work Management Activity through which potential work is captured from an applicable source and made sufficiently identifiable for subsequent management decisions. Intake does not by itself mean that work is accepted, ready, prioritized, selected, committed, or authorized for execution.

When potential work is retained for management, Intake MUST preserve enough information to distinguish it from other potential work and support a subsequent management decision. Intake SHOULD capture information proportionate to the potential work's nature, risk, and uncertainty. A fully formed Work Item is not required when a signal or other source first appears, and Intake does not require a mandatory form or schema.

Intake MAY originate from user or stakeholder requests, observations, defects, incidents, research findings, operational needs, product opportunities, technical concerns, governance or compliance obligations, feedback, or internally identified work. These examples are non-exhaustive.

Intake does not redefine Work Item. If captured potential work becomes a governed Work Item, the Work Item Taxonomy remains authoritative for its classification. Intake does not determine Lifecycle Phase, Work Type, Priority, Workflow State, readiness, or commitment.

Intake is not restricted to the beginning of a product or Lifecycle Phase. New potential work MAY be captured at any time. Feedback, incidents, validation findings, maintenance observations, or other developments MAY produce additional potential work that enters management through Intake when appropriate.

## Preparation

Preparation is the Work Management Activity through which retained potential work or an existing Work Item is developed to a level of understanding sufficient for an applicable subsequent management decision or action. Preparation MUST be purpose-oriented and proportional; it does not imply that every work item requires the same amount or type of preparation.

Preparation MAY develop or clarify information such as:

- intended outcome or problem;
- scope;
- constraints;
- dependencies;
- assumptions;
- uncertainty;
- relevant evidence;
- acceptance evidence;
- applicable classification;
- ownership or decision responsibility; or
- an actionable next step.

This list is illustrative, not a mandatory preparation schema. Where another authoritative standard requires specific information, that standard remains authoritative. Preparation MUST preserve known material uncertainty rather than manufacture certainty merely to make work appear prepared.

Intake captures and identifies potential work for management; Preparation develops the understanding needed to manage retained work further. Intake MUST NOT imply that Preparation is complete. Preparation MAY begin with information captured during Intake, but the two Activities remain conceptually distinct and do not require a transition between them.

Preparation MAY apply before or after potential work is represented as a governed Work Item; this standard does not prescribe when that representation must occur. If work is classified as a Work Item, the Work Item Taxonomy and Work Item Types remain authoritative.

Preparation MAY produce information used to evaluate readiness, but MUST NOT itself declare work Ready. Definition of Ready remains authoritative for readiness requirements and readiness decisions. Preparation MUST NOT by itself select work, commit work, authorize execution, or declare completion; prepared work may still require other management decisions before execution.

Preparation MAY occur whenever additional understanding is needed. Its depth SHOULD remain proportional to the work's nature, risk, uncertainty, dependencies, and applicable governing requirements. Preparation MAY recur when material information or conditions change.

## Refinement

Refinement is the Work Management Activity through which understanding of retained potential work or a Work Item is iteratively improved when additional clarity is useful for an applicable management decision or action. Refinement MUST be treated as an activity, not as a mandatory ceremony, meeting, phase, state, gate, or scheduled event.

Preparation develops work to sufficient understanding for an applicable subsequent management decision or action. Refinement is an iterative way of improving that understanding when additional clarification is useful. Refinement MAY occur as part of Preparation or later whenever work requires renewed clarification; not every Preparation activity requires a separately identified Refinement activity.

Refinement MAY clarify or update information such as:

- intended outcome or problem;
- scope;
- constraints;
- dependencies;
- assumptions;
- uncertainty;
- evidence;
- acceptance evidence;
- applicable classification;
- ownership or decision responsibility; or
- actionable next steps.

This list is illustrative and MUST NOT become a mandatory refinement schema. Refinement MUST preserve unresolved material uncertainty and MUST NOT manufacture certainty merely to satisfy a process expectation.

Refinement MAY occur before readiness evaluation, after new information becomes available, after feedback, after a dependency changes, after risk or uncertainty changes, or after work has begun when renewed clarification is necessary. These examples are non-exhaustive; Refinement is not restricted to a single point in work management.

Refinement MAY produce information useful for readiness evaluation, but MUST NOT itself declare work Ready. Definition of Ready remains authoritative. Refinement MUST NOT by itself prioritize work, select work, commit work, authorize execution, approve an outcome, or declare completion. It improves understanding; other applicable management or governance decisions remain distinct.

## Prioritization

Prioritization is the Work Management Activity through which relative importance is evaluated to support management decisions among retained potential work or Work Items. It is distinct from Priority: Priority is a recorded relative planning classification when applicable, while Prioritization is the activity through which relative importance is evaluated or reconsidered.

Prioritization MAY consider intended outcomes, user or stakeholder value, risk, urgency, dependencies, obligations, uncertainty, cost of delay, available evidence, strategic relevance, or operational impact. These considerations are non-exhaustive. It MUST NOT prescribe a scoring model, formula, fixed factor weights, ranking framework, or mandatory prioritization method. Prioritization SHOULD use relevant available evidence and make material decision rationale traceable when durable justification is required; it does not require universal documentation for every decision.

The existing authoritative standards remain responsible for the meaning and representation of Priority. Prioritization MAY establish, change, or retain a Priority, or make a relative management decision without persisting a Priority value. Those outcomes MUST NOT make Priority mandatory where existing standards treat it as optional.

Prioritization is not equivalent to backlog order or execution sequence. Relative importance MAY inform ordering, but Priority and Prioritization do not by themselves determine exact work order.

Prioritization MUST NOT by itself select work for execution, pull work, commit work, or authorize execution. Higher relative importance MUST NOT automatically mean immediate execution; selection, commitment, and execution remain distinct concepts.

Prioritization MAY recur when relevant evidence, risk, urgency, dependencies, obligations, objectives, or operating conditions change. Reconsidering relative importance MUST NOT require a specific ceremony or cadence.

## Ordering

Ordering is the Work Management Activity through which a relative precedence relationship is established or reconsidered among retained potential work or Work Items for an applicable management purpose. It is distinct from Prioritization, Priority, Selection, commitment, and execution sequence.

Ordering MAY establish that one item should be considered before, after, or in relation to another item for an applicable management purpose. It MAY consider relative importance, dependencies, sequencing constraints, risk, urgency, obligations, availability of required inputs, coordination needs, or applicable timing constraints. These considerations are non-exhaustive. This standard does not prescribe a universal ordering method.

Prioritization evaluates relative importance, while Ordering establishes a relative precedence relationship. Prioritization MAY inform Ordering, but relative importance MUST NOT be treated as the only possible basis for Ordering. A lower-priority item MAY legitimately precede a higher-priority item when another applicable constraint or management reason requires it.

Ordering MUST NOT require every retained item to receive a unique position in one fully ranked list. Items MAY remain unordered relative to each other when no management decision requires a precedence relationship.

Where work is represented in a Product Backlog, Ordering MAY inform its ordering or another applicable management representation. Product Backlog remains governed by its existing authoritative standard; Ordering does not require all Playbook work to exist in one Product Backlog.

Ordering MUST NOT by itself select work, pull work, commit work, authorize execution, or establish that work has started. An item appearing earlier in an ordering MUST NOT automatically mean that it is selected, committed, or executable. Ordering is not an immutable execution sequence; applicable conditions MAY cause work to be selected or executed differently from an existing ordering.

Ordering MAY be reconsidered when relevant priorities, dependencies, constraints, risks, obligations, inputs, or operating conditions change. Reordering MUST NOT require a specific ceremony, cadence, or workflow transition.

## Readiness

Readiness is the Work Management Activity through which the current condition of work is evaluated against the applicable criteria for a responsible next action. It is distinct from Preparation, Refinement, Selection, Commitment, Execution, and Workflow State.

Definition of Ready is the authoritative source for specific readiness criteria. Readiness evaluates whether applicable readiness conditions are satisfied; it does not duplicate or replace those requirements. Work that does not satisfy applicable readiness requirements MUST NOT be treated as Ready merely because it has been prepared or refined.

Readiness MUST be contextual and purpose-specific. Work may be sufficiently ready for one responsible action while not ready for another action requiring additional information, Authority, evidence, or coordination. This standard does not require a universal binary readiness model. Where an applicable governing standard defines a specific readiness requirement, that requirement remains authoritative.

Preparation develops sufficient understanding for a subsequent management decision or action, and Refinement improves that understanding when additional clarification is useful. Readiness evaluates the resulting condition against applicable readiness requirements. Preparation or Refinement MUST NOT, by themselves, establish that work is Ready. A Readiness evaluation MAY reveal that additional Preparation or Refinement is required.

Readiness MUST NOT by itself select work, commit work, authorize execution, start execution, establish Work-in-Progress, or declare completion. Work MAY be Ready without being selected and MUST NOT be treated as selected merely because it is Ready. Readiness is a condition relevant to responsible progression, not a commitment or execution event.

Readiness MAY be reassessed when new information, assumptions, dependencies, risk, scope, required evidence, or governing requirements change. These examples are non-exhaustive. Reassessment MUST NOT require a ceremony, cadence, or workflow transition.