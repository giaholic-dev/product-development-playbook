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

## Selection

Selection is the Work Management Activity through which work is chosen from available managed work for progression toward an applicable next action. It is a management decision distinct from Prioritization, Ordering, Readiness, Commitment, and Execution.

Selection MAY consider readiness, relative ordering, Priority, dependencies, capacity, constraints, risk, timing, required capabilities, or current operating conditions. These considerations are non-exhaustive. This standard does not prescribe a universal decision formula. Work being highly prioritized, highly ordered, or Ready MUST NOT by itself mean that it is selected.

Ready work MAY remain unselected, and unselected work MAY remain Ready. Selection MUST consider applicable readiness requirements before choosing work for an action that requires readiness, but Selection MUST NOT itself declare work Ready. Definition of Ready remains authoritative for readiness criteria.

Ordering and Prioritization MAY inform Selection. Selection MUST NOT be reduced to choosing the first item in an ordering or the highest-priority item; applicable constraints or conditions MAY justify another choice.

Selection MAY occur for an individual next action, a bounded set of work, a delivery objective, a planning horizon, or a flow context. These examples are illustrative and do not create a selection-scope taxonomy.

Selection MUST NOT by itself create a commitment, establish a Sprint, establish a delivery promise, authorize execution, establish Work-in-Progress, assign an Actor, or change Workflow State. A system MAY represent Selection through a tool-specific field or state, but this standard does not require that representation.

Selection MAY be reconsidered when readiness, dependencies, risk, Priority, Ordering, capacity, constraints, or operating conditions change. Re-selection MUST NOT require a ceremony, cadence, or workflow transition.

## Commitment

Commitment is the Work Management Activity through which an Actor, group, or governing mechanism explicitly accepts responsibility for progressing selected work or achieving a defined outcome within a specified scope. It is distinct from Selection, Planning, Execution, Workflow State, Priority, and Ordering.

A Commitment MUST identify, where applicable, the work or outcome being committed, its applicable scope, the Actor or governing mechanism responsible for the commitment, and any material conditions or constraints that define it. This does not create a universal commitment record schema. The amount of Commitment information SHOULD remain proportional to its significance, risk, and governance requirements.

Selection chooses work for progression but MUST NOT automatically create Commitment. Work MAY be selected without a formal Commitment, and a Commitment MAY be created only when an applicable operating model, governance rule, or deliberate management decision requires or establishes one. Commitment is not required for all selected work.

Commitment MUST NOT bypass applicable readiness requirements. Where a governing rule requires work to be Ready before Commitment, that rule remains authoritative. Readiness does not automatically create Commitment. Planning MAY establish conditions under which a Commitment is considered, but Commitment is not equivalent to Planning.

Commitment MUST NOT mean that execution has already started; a committed item MAY be awaiting execution. It MUST NOT itself start execution, establish Workflow State, establish Work-in-Progress, assign an Actor to perform work unless that assignment is independently required, or authorize actions beyond the commitment scope.

Commitment MAY apply to a specific work item, a bounded set of work, an outcome, a delivery objective, or another explicitly defined scope. These are illustrative examples, not a commitment taxonomy.

A Commitment MAY be revised, withdrawn, or superseded when material conditions change. Such changes SHOULD remain traceable when the Commitment is governed or material; this does not define a Commitment lifecycle or transition model.

Commitment MUST NOT automatically create Accountability unless an applicable governing rule establishes that relationship. Where explicit Accountability is required, the Roles and Actor Assignment Standard remains authoritative. An Actor may be accountable without making a formal Commitment, and a Commitment may exist without creating a new Accountable Owner when accountability is governed elsewhere.

## Pull

Pull is the Work Management Activity through which an Actor or execution context takes selected work into active progression when applicable capacity, Authority, and other governing conditions permit. It is distinct from Selection, Commitment, Execution, Workflow State, and Work-in-Progress.

Pull represents an explicit progression decision that uses available capacity or execution opportunity to take selected work forward. It MAY be initiated by an individual Actor, a team, an authorized automated mechanism, or another execution context permitted by applicable governance. These examples are non-exhaustive.

Selection determines which work is chosen for progression; Pull determines that selected work is taken into active progression when applicable conditions permit. Selection MUST NOT automatically imply Pull. Pull MUST NOT select arbitrary work outside the applicable selection decision or governing rules.

Pull MUST NOT automatically create Commitment. A work item MAY be pulled without a formal Commitment when the applicable operating model permits, and a committed work item MAY exist before Pull occurs.

Pull MUST respect applicable readiness requirements. Where work must be Ready before active progression, Pull MUST NOT bypass that requirement. Definition of Ready remains authoritative, and Pull MUST NOT itself declare work Ready.

Pull MAY depend on available capacity or applicable Work-in-Progress constraints. This standard does not prescribe a universal capacity model, Work-in-Progress limit, metric, Kanban policy, or numerical threshold. Where another governing or adopted operating model defines such constraints, those constraints remain authoritative.

Pull does not necessarily mean that substantive Execution has already occurred. It indicates that work has been taken into active progression; Execution remains a distinct concern. Pull MUST NOT itself define execution steps, execution states, handoffs, transitions, or completion.

Pull MUST NOT silently create or change Role Assignments. If active progression requires an Actor to perform a Role, applicable Assignment rules remain authoritative under the Roles and Actor Assignment Standard.

Work MAY cease active progression and later be pulled again when applicable conditions permit. This does not define a workflow transition model or re-entry protocol. Pull is not required for all operating models.

## Work-in-Progress (WIP)

Work-in-Progress (WIP) is work that has entered active progression but has not yet ceased to be actively progressed. WIP describes a condition of managed work, not a Work Management Activity, Workflow State, Lifecycle Phase, Work Type, Commitment, or execution-status taxonomy.

Work may be considered WIP when an applicable management decision has caused it to enter active progression and it remains under active progression. WIP MAY include work that is actively being executed, awaiting an active progression step, or temporarily constrained while still actively owned within the progression context. These examples are illustrative and do not create a WIP-state taxonomy.

Pull MAY cause work to enter WIP, but Pull is not identical to WIP: Pull is the activity through which selected work is taken into active progression, while WIP is the condition describing work that remains in active progression. Work may cease to be WIP without implying that its underlying Work Item is permanently complete.

WIP does not necessarily mean that substantive Execution is occurring at every moment. Work may remain in active progression while temporarily awaiting an applicable next action, input, dependency, or other condition. WIP MUST NOT be used to define execution states.

WIP does not automatically imply Commitment. Committed work MAY become WIP, and work MAY become WIP without a formal Commitment where the applicable operating model permits it.

This standard remains neutral regarding WIP limits. An applicable operating model MAY impose a WIP limit or another constraint on concurrent active work. This standard does not require a WIP limit, numerical threshold, capacity formula, specific WIP policy, Kanban model, metric, or queue policy. Where an applicable governing or adopted operating model defines a WIP constraint, that constraint remains authoritative.

WIP MAY be measured or represented for operational purposes. This standard does not prescribe a metric definition, reporting cadence, tool, field, dashboard, or calculation method.

Work ceases to be WIP when it is no longer considered to be in active progression under the applicable management model. This does not define Completion. A work item may cease to be WIP because it reaches a later management condition, is deliberately removed from active progression, is returned for additional management work, or is otherwise no longer actively progressed. These examples are illustrative and do not define Re-entry or workflow transitions.

WIP limits or equivalent constraints are optional and operating-model dependent; WIP is not universally required.

## Execution

Execution is the realization of selected or otherwise authorized work through actions performed within the applicable scope, responsibilities, constraints, and governing requirements. It is not a Work Management Activity and is distinct from Lifecycle Phase, Work Type, Workflow State, Selection, Pull, Work-in-Progress, and Commitment.

Execution concerns the actual performance of work. It MAY involve creating or modifying artifacts, performing technical or operational actions, investigating, implementing, communicating, testing, configuring, documenting, or other actions appropriate to the work. These examples are illustrative and do not create an execution taxonomy.

Execution remains governed by the applicable Roles and Actor Assignment Standard, security, privacy, and data governance requirements, technical or domain-specific standards, review and validation requirements, and release and maintenance requirements. This standard does not duplicate those rules.

Selection determines work chosen for progression, while Execution realizes work; Selection MUST NOT itself constitute Execution. Execution MAY occur after Selection, but Selection is not its only possible precursor: applicable operating models may authorize or initiate work through other governed mechanisms. Pull may take selected work into active progression, and Execution may occur after Pull, but Pull MUST NOT be treated as synonymous with Execution. WIP describes work that remains in active progression; Execution may occur while work is WIP, but WIP MUST NOT mean that substantive Execution is continuously occurring. Commitment may establish responsibility for progressing work or achieving an outcome, but MUST NOT be treated as proof that Execution has started; Execution MUST NOT automatically create Commitment.

Execution MUST NOT define Workflow States. A tool or operating model MAY represent execution progress using Workflow State, but this standard does not prescribe state names, transitions, status fields, state machines, or progress percentages.

Execution MUST occur within applicable Role Assignments, Authority boundaries, and governance requirements. An Actor MUST NOT gain Authority or become an Accountable Owner merely because the Actor performs Execution. Where delegation is used, the Roles and Actor Assignment Standard remains authoritative.

Execution MUST NOT itself mean that work is complete. Completion requires applicable completion requirements and evidence governed by Definition of Done or other authoritative standards. Execution MUST NOT itself constitute review or validation; where either is required, the applicable governing standards remain authoritative.

This standard does not define execution states, activity taxonomies, transitions, handoffs, blocking, escalation, metrics, service levels, tools, provider-specific mechanisms, or a universal execution procedure. The future Execution Protocol Standard remains the owner of execution-protocol concerns where applicable.

## Validation

Validation is the evaluation of work, evidence, or an outcome against applicable requirements to determine whether those requirements have been satisfied for the applicable purpose. It is not a Work Management Activity and is distinct from Execution, Review, Readiness, Completion, and Workflow State.

Validation MAY evaluate required outcomes, acceptance criteria, evidence, functional requirements, quality requirements, governance requirements, security, privacy, or data requirements, or applicable technical or operational requirements. These examples are illustrative and do not create a validation taxonomy. Validation MUST use the requirements applicable to the work and its governing context.

Execution produces or changes work; Validation evaluates resulting work, evidence, or outcomes. Execution MUST NOT itself constitute Validation. Validation MAY occur during or after Execution when applicable and MAY identify that additional Execution, Preparation, Refinement, or other management action is required. This does not define rework semantics or execution transitions.

Review and Validation may overlap in practice but MUST remain conceptually distinct. Review concerns examination or evaluation by a Reviewer when a Reviewer responsibility is applicable; Validation concerns whether applicable requirements have been satisfied. The Roles and Actor Assignment Standard remains authoritative for Reviewer responsibility, and this standard does not create a universal reviewer requirement.

Validation MAY provide evidence used in a Readiness evaluation but MUST NOT itself declare work Ready. Definition of Ready remains authoritative for readiness requirements. Validation MAY also provide evidence relevant to Completion but MUST NOT itself mean that work is complete. Definition of Done and other applicable completion requirements remain authoritative.

Validation MUST NOT automatically constitute Approval. Where an approval decision is required, the Approver role and applicable Authority remain governed by the Roles and Actor Assignment Standard and other applicable standards.

Validation SHOULD rely on appropriate evidence when the applicable requirement requires evidence. The form, sufficiency, and retention of evidence remain governed by the applicable standard. This standard does not prescribe a universal evidence format, test framework, tool, or storage mechanism.

Validation MAY determine that applicable requirements are not satisfied. An unmet requirement MUST NOT automatically define a workflow transition. The result may inform additional Execution, Preparation, Refinement, or another applicable management action; this does not define Blocking, Re-entry, or workflow transitions.

Validation MAY be repeated when work, requirements, or evidence change, a previous validation result becomes outdated, or additional work is performed. These examples are non-exhaustive and do not define a validation cadence.

## Completion

Completion is the determination that applicable completion requirements for work have been satisfied and that the work may be considered complete for its applicable scope and purpose. It is not a Work Management Activity and is distinct from Execution, Validation, Review, Readiness, Commitment, and Workflow State.

Definition of Done remains the authoritative source for applicable completion requirements where it governs the work. Completion determines whether those requirements have been satisfied; this standard does not duplicate their criteria. Work MUST NOT be treated as complete merely because Execution or Validation occurred, or because it was selected, committed, or pulled.

Validation MAY provide evidence relevant to Completion, but MUST NOT automatically mean Completion. Completion MAY depend on validation evidence when applicable requirements require it. Review MAY also provide relevant evidence or evaluation, but MUST NOT automatically mean Completion.

Completion MAY apply to a Work Item, defined outcome, bounded piece of work, or another explicitly governed scope. These examples are illustrative and do not create a completion taxonomy. Work remains incomplete when only some applicable requirements have been satisfied.

When work is considered complete under applicable requirements, it MAY cease to be Work-in-Progress. Completion is not merely leaving Work-in-Progress, and work may cease to be Work-in-Progress for other reasons without being complete. Completion MAY satisfy the outcome of a Commitment when the applicable Commitment concerns that outcome, but MUST NOT automatically create or modify Commitment.

Completion MUST NOT define Workflow State. An operating model MAY represent completed work using Workflow State, but this standard does not prescribe state names, status fields, transitions, state machines, or completion statuses.

Completion SHOULD be supported by appropriate evidence when applicable governing requirements require evidence. Evidence format, sufficiency, and retention remain governed by the applicable standards; this standard does not prescribe a universal completion-evidence schema.

Completion does not imply that the underlying product, system, or domain can never require future work. Future defects, changes, feedback, maintenance, or requirements may result in new or additional work. This does not define Re-entry, reopening, Feedback, or Maintenance semantics.

## Feedback

Feedback is information arising from work, its outcomes, its context, or subsequent observations that may provide evidence for reconsidering how work is managed. It is not a Work Management Activity, workflow state, or process stage.

Feedback MAY concern outcomes, user or stakeholder responses, validation findings, operational observations, incidents, defects, risks, changed dependencies, new requirements, lessons, performance or quality observations, or other relevant evidence. These examples are illustrative and do not create a feedback taxonomy.

Feedback MAY inform Preparation, Refinement, Prioritization, Ordering, Readiness, Selection, Validation, Completion, or future Improvement. These are possible uses, not a mandatory sequence; Feedback MUST NOT imply that any particular Activity must occur.

Completion does not terminate the possibility of future Feedback. Feedback MAY arise before Completion, during Validation, after Completion, during operation or maintenance, or from subsequent use or observation. Feedback after Completion MUST NOT automatically reopen completed work; this does not define Re-entry or reopening mechanics.

Feedback MAY result in identification of new potential work. When appropriate, that potential work MAY enter management through Intake. Feedback MUST NOT automatically create a Work Item.

Validation findings MAY constitute Feedback when they provide information relevant to subsequent management. Feedback is not equivalent to Validation: Validation evaluates requirements, while Feedback is information that may influence subsequent management.

Feedback MAY provide evidence for Improvement, but MUST NOT itself constitute Improvement. Improvement is a separate management concern to be defined later.

Material Feedback SHOULD remain traceable when its consequences materially affect management decisions or governed work. This does not impose universal documentation requirements. Representation and retention MAY depend on significance, risk, governance requirements, applicable evidence requirements, or operational context; these considerations are non-exhaustive.

Feedback may indicate satisfactory outcomes, deficiencies, new opportunities, changed conditions, uncertainty, or new information. It is not limited to negative outcomes. Feedback MAY occur repeatedly and whenever relevant information becomes available; this standard does not prescribe a feedback cadence, ceremony, meeting, or review cycle.

## Improvement

Improvement is the deliberate consideration and application of relevant evidence, Feedback, observations, or identified opportunities to improve the effectiveness, clarity, reliability, or appropriateness of Work Management. It is not a Work Management Activity.

Improvement MAY concern management practices, decision-making, work representation, Preparation, Refinement, Prioritization, Ordering, Readiness evaluation, Selection, Commitment practices, Execution support, Validation practices, Completion practices, information flow, governance, or traceability. These examples are illustrative and do not create an improvement taxonomy.

Feedback MAY provide evidence for Improvement, but Improvement is not equivalent to Feedback. Feedback is information that may inform management; Improvement is the deliberate consideration or application of that information to improve Work Management.

Improvement MAY result in changes to how Work Management Activities are performed or represented. It MUST NOT imply that every Activity requires improvement or require a specific Activity, ceremony, retrospective, cadence, or process framework. This standard does not create a mandatory improvement cycle.

Improvement MAY identify clarifications to standards, changes to practices or representations, changes to decision criteria, or opportunities to reduce ambiguity, improve traceability, or improve effectiveness. Improvement MUST NOT automatically modify authoritative standards. Changes to authoritative standards remain subject to the applicable governance and documentation process, which this standard does not define.

Improvement of Work Management remains distinct from Lifecycle Phase. It may concern how work is managed across any Lifecycle Phase and does not create a new Lifecycle Phase. This standard defines Improvement only and does not define process-improvement methodology, retrospectives, continuous-improvement frameworks, Kaizen, Lean, organizational transformation, or change-management procedures.

Improvement MAY occur whenever relevant evidence, Feedback, observations, or opportunities justify reconsideration. It does not require a fixed cadence, retrospective schedule, review cycle, or improvement meeting.

Material Improvement decisions SHOULD remain traceable when they change governed Work Management practices or materially affect work. This does not impose a universal improvement-record schema. The applicable governance standard remains authoritative for changes to the Playbook itself.