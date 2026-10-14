# Standards applicability

## Purpose

Define how to determine and evidence which governing requirements apply to a bounded product or work context without changing their meaning or weakening their obligations.

## Scope

This standard owns requirement-applicability assessment semantics. It uses [Product Type, Product Context, and Product Composition](product-type-model.md) and the [core, specialization, and repository boundaries](core-and-specialization-boundaries.md). It does not assign applicability to every existing standard, adopt a specialization, change the seven lifecycle phases, or create a machine schema, tracking field, or execution framework. [Lifecycle assessment #304](https://github.com/giaholic-dev/product-development-playbook/issues/304) remains separate.

Primary sources retain ownership of definitions, scope, requirement strength, substantive acceptance evidence, and permitted exceptions. An applicability assessment interprets a source within its governing scope; it cannot amend that source. Technology neutrality, a Product Type label, provider support, or a checklist entry alone does not establish applicability.

## Definitions

Requirement applicability is the relationship between an identifiable governing requirement and the assessed scope, established from the source's scope and conditions and relevant contextual evidence. Applicability is separate from whether the requirement is satisfied.

An applicability assessment is the evidence and decision record establishing that relationship, including material uncertainty and reassessment conditions. It may be carried by an existing work, review, or decision record; no separate document or universal format is required.

## Source and context assessment

Before relying on a material applicability determination, the assessment MUST identify:

- The bounded product, constituent, repository, work, or execution context being assessed, using type/context/composition distinctions where relevant.
- The primary source and identifiable revision or assessment date, the requirement or concern being assessed, and its scope, conditions, and normative strength.
- The relevant observed evidence, material assumptions, and missing or conflicting information.
- The determination, rationale, affected obligations, identifiable accountable decision owner, and condition for reassessment under existing [responsibility](roles-and-actor-assignment.md) and [artifact](artifact-standard.md) rules.

Evidence depth MUST be proportionate to risk, uncertainty, and the consequences of an incorrect determination. The assessment MAY group requirements only when they share the evidenced scope and conditions; a whole-standard label MUST NOT conceal different clause-level obligations or unresolved questions. A decision about one constituent does not decide applicability for the whole product or another constituent.

Use these determination meanings:

- **Applicable:** source scope and relevant conditions establish that the requirement governs the assessed context. Preserve its existing strength; applicability does not turn a recommendation or permission into a mandatory action.
- **Inapplicable:** evidence establishes that the assessed context is outside the source's governing scope or that a relevant source condition is not met. The rationale MUST identify that boundary or condition. This finding does not waive an applicable requirement or grant a new exception.
- **Unresolved:** evidence is insufficient, materially conflicting, or too uncertain to establish applicability or inapplicability. Identify the missing evidence or governing decision, its responsible owner, and the next permitted assessment action. Unresolved MUST NOT be represented as inapplicable, optional, satisfied, or permission to proceed.

These meanings are contextual assessment outcomes, not Workflow States, Protocol States, integration support descriptions, or a universal state machine. An applicable concern may contain a mixture of mandatory, recommended, optional, and unresolved details; preserve those distinctions.

## Conditions and requirement strength

A conditional requirement is governed by its source's condition. Establish the condition with evidence rather than inferring it from a type label. If the condition holds, the requirement applies at its original strength; if it does not hold, evidence the scoped inapplicability; if it is materially uncertain, retain an unresolved determination. Other requirements in the same source may still apply.

An optional action or representation is a choice permitted by its source, not proof that the underlying concern is inapplicable. A recommendation retains the source's documented-rationale expectations when not followed. Choosing an option may activate further governing conditions; assess those rather than assuming that optional entry makes all subsequent obligations optional. [Repository Standards](repository-standards.md) remains the owner of normative language.

No assessment, specialization, provider mapping, catalog, template, or checklist MAY change a source requirement's strength or silently waive it. Where a source already permits a contextual non-applicability decision, record its rationale within that permission. A proposed interpretation that contradicts or extends a primary definition requires review of the governing source and affected references; it is not adopted by relabeling the requirement.

## Satisfaction, capability, and exceptions

For an applicable requirement, retain separate evidence of satisfaction, non-satisfaction, or unresolved satisfaction under its governing source. Missing evidence is not evidence that the requirement does not apply. An unmet requirement remains an obligation until fulfilled or given an explicit disposition permitted by its source.

An unavailable Capability, unsupported current Integration, lack of access, missing Authority, cost, or inconvenient evidence does not establish inapplicability. [Execution Protocol](execution-protocol.md) and [Integration](integration-standard.md) own availability and permitted fallback treatment. An authorized alternative may fulfill the same need only while preserving its governing obligations and verification evidence; changing the mechanism does not prove the original attempt succeeded.

A permitted exception is a source-authorized departure from an otherwise applicable obligation. It MUST cite the governing exception permission and retain its required authority, scope, reason, evidence, risk, and reassessment treatment. If that source grants no exception permission, this standard grants none. Approval of an assessment, possession of access, or an Accountable Owner Assignment alone does not create exception Authority. An exception does not make the original requirement inapplicable or erase any remaining obligation.

When unresolved applicability, non-satisfaction, or unavailable capability is material to a next action, use the governing readiness, protocol, work-management, review, or release decision. Do not run dependent actions on an assumed satisfied condition. A bounded research action may gather evidence when separately ready and authorized; uncertainty does not impose a universal halt on unrelated work. [Definition of Ready](definition-of-ready.md), [Work Management](work-management.md), [Definition of Done](definition-of-done.md), and the [lifecycle](../lifecycle/01-foundation.md) retain their decision ownership. An applicability record alone establishes neither authorization, readiness, Validation, Approval, Completion, nor release.

## Composition, conflicting sources, and change

For hybrid or composite scopes, assess constituent obligations and material interactions. Preserve repository-governance obligations separately from product production or service delivery. The absence of source code in a manufactured item does not remove Git obligations from a repository that adopts [Repository Standards](repository-standards.md); use of software tools does not make coding rules its manufacturing method.

Conflicting applicable requirements, disputed scope, or unclear primary ownership MUST remain explicit, with affected sources, impact, evidence, accountable decision owner, and reassessment condition under [Core and Specialization Boundaries](core-and-specialization-boundaries.md#ownership-conflicts-and-exceptions). Do not select the least restrictive rule, invent precedence, or treat the absence of an approved specialization as a waiver. Governing source review resolves interpretation or change; this standard establishes no inheritance or override mechanism.

Reassess when a relevant source, product boundary, composition, material context, condition, or evidence changes or contradicts the recorded determination. Preserve the earlier decision's scope and rationale, identify affected work and references, and retain unresolved consequences. Historical inapplicability MUST NOT be presented as confirmed current applicability evidence without checking its continuing basis.

## Non-normative scenario review

### Software increment

A repository containing implementation code falls within [Coding Standards](coding-standards.md). Coding-convention obligations are applicable; a missing convention record is an unmet obligation, not inapplicability. If an intended planning operation is provider-supported but absent from the current connection, [Integration](integration-standard.md) preserves the unmet need and permitted manual fallback. Neither situation is solved by changing an applicability label. Existing software lifecycle and review obligations remain intact.

### Physical item

For a reusable container, tangible production is not itself a source-code repository. A genuinely documentation-only design repository may record Coding Standards as inapplicable under that source's explicit permission; the finding is about that repository, not every container component or validation obligation. If executable configuration is later introduced, reassess the trigger. Relevant experience questions may still be evaluated under [UX Validation](ux-validation.md), whose declared scope is product-type-independent. Production, quality, delivery, and lifecycle equivalence remain for governing assessment, including #304; this example defines no physical specialization.

### Delivered service

An appointment-assistance service handles personal data, activating assessment under [Security, Privacy, and Data Governance](security-privacy-data-governance.md). Individual controls receive contextual decisions under that source; its explicit permission to determine a concern inapplicable requires rationale. Choosing among permitted UX validation methods does not make experience validation optional. If the operating context or data handling is unknown, affected applicability remains unresolved until evidence or a governing decision is available; this does not certify service lifecycle applicability.

### Hybrid offering

A monitored device has physical, executable, and operated-service constituent boundaries. Assess coding obligations for the software repository and contextual privacy obligations for collected data, rather than applying every rule to every constituent. An irreversible material change and a reversible software deployment do not establish identical recovery semantics. Record the cross-boundary question, affected sources, accountable owner, and decision needed before a dependent release decision. A checklist mark or unavailable recovery mechanism cannot grant a waiver; any exception needs its source's permission and scoped Authority. Do not infer an approved hybrid specialization or universal precedence rule.

These scenarios test semantic distinctions against existing sources. They are conceptual review evidence, not product execution, independent approval, a complete applicability matrix, or empirical validation of physical/service/hybrid methods. Lifecycle/activity coverage and compatibility consequences remain the distinct #304 assessment.

## References

- [Product Type Model](product-type-model.md)
- [Core and Specialization Boundaries](core-and-specialization-boundaries.md)
- [Product-type Assumption Inventory](../practices/product-type-assumption-inventory.md)
- [Product-type Architecture Plan](../practices/product-type-architecture-plan.md)
- [Terminology Standard](terminology-standard.md)
- [Code Review Standard](code-review-standard.md)
