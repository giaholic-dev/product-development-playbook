# Lifecycle applicability assessment

## Purpose and context

Record PT5 for [#304](https://github.com/giaholic-dev/product-development-playbook/issues/304): assess the seven lifecycle phases and all 33 indexed activities across software, physical, service, and hybrid conceptual contexts, and establish the architectural integration and migration boundary.

Baseline: `c510375f5c29c0406abe3c2bc2fc3f4ef8912916`, assessed on 2026-10-14. Inputs are the approved [architecture plan](product-type-architecture-plan.md), [assumption inventory](product-type-assumption-inventory.md), [Product Type Model](../standards/product-type-model.md), [Core and Specialization Boundaries](../standards/core-and-specialization-boundaries.md), and [Standards Applicability](../standards/standards-applicability.md). Issues #300–#303 are complete at this baseline.

This is a research and decision record, not a replacement lifecycle or an applicability waiver. Existing lifecycle sources retain phase order, activities, inputs, outputs, and gates. The [Master Execution Checklist](../standards/master-execution-checklist.md) retains navigational ownership; its identifiers below identify existing activities, not new tracking fields. A1–A4 are its navigation identifiers for the Architecture source's four unnumbered bullets.

## Decision and alternatives

Retain the current seven-phase lifecycle and its existing software adoption unchanged. Reuse the approved common governance distinctions through their primary sources; do not promote entire phases, all artifacts, or all source requirements into a universal lifecycle. Cross-type application requires an evidenced contextual assessment, and any changed phase/activity meaning or gate requires a separately reviewed governing source change.

Two alternatives are rejected for this boundary: relabeling the current software-oriented lifecycle as universal without changing its evidence and dependencies; and immediately splitting or reorganizing all source documents into specializations. The first hides material differences; the second would migrate requirements before their replacement and compatibility evidence exist. A universal phase order, dedicated specializations, and broad migration remain unadopted.

The assessment distinguishes reusable concerns from production-specific realization and unresolved decisions. These are research findings, not new applicability states. Actual requirement-level determinations use Standards Applicability, preserving source conditions, uncertainty, normative strength, and exception authority. Shared intent does not establish identical entry or exit criteria.

## Scenario boundaries and evidence limits

- **Software (S):** a bounded reservation-status increment in an existing software product. Retain the current repository, Product/UX/Architecture decisions, implementation validation, review, release, and operational evidence.
- **Physical (P):** a reusable container, with material characteristics, production and delivery concerns, and a separate design/evidence repository if adopted. Digital tools do not make the offering software or hybrid. No manufacturing, safety, certification, or recall method is inferred from software terminology.
- **Service (V):** appointment assistance delivered by people, with recipient outcomes, operating procedures, personal-data concerns where present, and service capacity. A request website may be a tool or a constituent depending on the assessed offering boundary.
- **Hybrid (H):** a monitored device whose intended value depends on a physical device, executable behavior, and an operated monitoring service. Assess constituent obligations and interactions; neither a shared release label nor component availability proves whole-product readiness.

Each activity finding below covers all four scenarios. Phase paragraphs assess the source's inputs, outputs, completion and exit criteria. Representation, capability, and evidence choices remain contextual. These scenarios are conceptual comparisons against repository sources, not real product trials, legal/compliance assessment, independent approval, or complete specialized procedures.

## Phase and activity findings

### Foundation — five activities

Source: [Foundation](../lifecycle/01-foundation.md). Its inputs include version-control/tracking access; outputs and completion require an operational repository, adopted governance/workflow, and navigable documentation before Product entry. S retains these gates. P/V may adopt a repository for evidence, in which case its Git obligations remain; that does not make Git a production or service-delivery prerequisite. H needs constituent and cross-boundary responsibility as well as repository governance. A repository-independent Foundation entry/exit contract is not defined here. Governance/evidence intent is reusable; production preparation needs contextual specialization.

- **F1 Repository Setup:** S retains source/version-control setup; P separates a design repository from material production facilities; V separates an evidence repository from service capacity; H identifies repository scopes without assuming all constituents are versioned executable increments.
- **F2 Repository Standards Adoption:** S retains the adopted Git baseline; P/V retain obligations in any adopting repository without extending them to production/delivery; H keeps each adopting repository's obligations and unresolved cross-repository ownership explicit. No Git exception is granted by type.
- **F3 Governance and Tracking:** S uses existing work ownership and planning; P traces product decisions and relevant production evidence; V traces recipient/service decisions and capacity constraints; H traces constituent dependencies and accountable integration decisions. Common work-management distinctions transfer; platform fields do not determine production meaning.
- **F4 Workflow Adoption:** S retains ordered lifecycle and readiness/review/completion gates; P needs assessed production gates; V needs assessed operating/service gates; H needs constituent and whole-offering coordination gates. Human/AI choice remains independent. P/V/H lifecycle order and gate equivalence remain unresolved, not silently adopted.
- **F5 Documentation Foundation:** S retains repository navigation and language rules; P needs discoverable design/production evidence; V needs discoverable service decisions and operating knowledge; H needs links across constituent evidence. Existing artifact ownership accommodates media differences; exact records and access requirements need context.

### Product — six activities

Source: [Product](../lifecycle/02-product.md). Vision, problem, users, outcomes, scope, and backlog provide reusable decision concerns in S/P/V/H. Its completed-Foundation input, initial ordered work, and later-phase entry dependencies still reference the current lifecycle. S retains them. P/V/H require evidence that their chosen artifacts and preparation satisfy their governing decisions; common names do not prove identical phase gates or permit skipping Foundation.

- **P1 Product Vision:** S states executable-offering direction; P tangible-use direction; V recipient/service direction; H whole-offering direction and constituent contribution. Shared direction-setting does not define a production method.
- **P2 Problem Statement:** S traces the software user problem; P the material/use problem; V the recipient's activity/outcome problem; H the combined problem and interaction assumptions. Contextual evidence is required rather than a type label.
- **P3 Users:** S identifies software users/operators; P users and other material actors; V recipients and service participants; H constituent and cross-boundary actors. Actor roles in a product decision remain distinct from execution Role Assignments.
- **P4 Outcomes:** S identifies observable behavior/value changes; P observable use/material outcomes; V observable service/recipient outcomes; H combined outcomes and evidence dependencies. A source revision, manufactured item, or completed appointment alone does not prove intended value.
- **P5 Product Scope:** S bounds the increment and exclusions; P the item and assessed delivery scope; V the service promise and operating boundary; H constituent interfaces and whole-product exclusions. Composition is not the union of every possible rule.
- **P6 Product Backlog:** S retains traceable ordered work; P distinguishes design, production, and evidence work; V distinguishes service design and operating work; H links dependent objectives and owners. Existing primary phase/work-type classification remains unchanged; proposed non-software classifications require semantic justification, not renamed work types.

### UX — five activities

Source: [UX](../lifecycle/03-ux.md). Product inputs, validated experience direction, traceable representations, findings and risks support all four scenario concerns. The source already permits proportionate representation rather than every journey/persona/wireframe/prototype. [UX Validation](../standards/ux-validation.md) explicitly declares product-type independence. S retains the UX-to-Architecture gate; P/V/H still need contextual interpretation of information structure, architectural dependency, sufficient evidence, and remaining risks. Method independence does not by itself establish universal phase ordering.

- **U1 UX Vision:** S concerns digital interaction; P handling/use; V recipient/participant experience; H interaction across item, executable behavior, and service. Preserve alignment with Product outcomes without imposing a screen interface.
- **U2 User Understanding:** S gathers relevant software-use evidence; P use-setting evidence; V participant/service-context evidence; H evidence across constituent boundaries. Journeys or personas remain selected representations, not mandatory type-independent outputs.
- **U3 Experience Structure:** S addresses user flows/information structure; P examines relevant interaction sequence and information needs; V examines recipient/participant interactions; H examines handoffs and information across constituents. Exact equivalence to current flow/information-architecture artifacts remains contextual, not assumed.
- **U4 Experience Exploration:** S may use wireframes/prototypes; P may use appropriate physical or other representations; V may explore a service interaction; H may explore combined interactions. Representation suitability and evidence need assessment; this record prescribes no prototype or simulation method.
- **U5 UX Validation:** S/P/V/H retain a stated question, relevant actors/evidence, proportionate method, findings, limits, and decision under the primary validation source. Evidence of one constituent's usability does not establish whole-hybrid experience validity.

### Architecture — four activities

Source: [Architecture](../lifecycle/04-architecture.md). Its intent and completion concern intentional technical structure sufficiently evidenced for Development; inputs include current Product/UX decisions and operational/security/quality constraints. S preserves these meanings. P may involve material/structural choices; V may involve operating/service design; H has interacting technical and service structures. Their equivalence to the existing technical-development gate is unresolved. [API Design](../standards/api-design.md) includes conceptual interfaces and [Data Model](../standards/data-model.md) is not a mandatory database: neither is exclusively software merely because of its title.

- **A1 Boundaries, responsibilities, interfaces, data, and quality attributes:** S retains current technical scope; P assesses material boundaries and relevant information/interfaces; V assesses participant, operating, and information boundaries; H assesses constituent interfaces and cross-boundary quality. Similar concerns do not require identical diagrams or data artifacts.
- **A2 Technical options and architecture decisions:** S retains technical alternatives and decision evidence; P needs relevant design/production alternatives; V needs relevant service/operating alternatives; H needs constituent and interaction alternatives. Do not rename every service choice into an existing technical definition; source scope and future specialization decide.
- **A3 Implementation constraints, risks, and validation:** S retains software implementation evidence; P identifies material-production uncertainty; V service-capacity/performance uncertainty; H joint constraints and compatibility uncertainty. Exact quality and validation obligations need contextual sources; none are invented here.
- **A4 Architecture-enabling backlog work:** S retains enabling work; P links design/production questions; V links operating-design questions; H links integration and constituent dependencies. Existing taxonomy and backlog ownership remain; a planning label is not proof of technical readiness.

### Development — four activities

Source: [Development](../lifecycle/05-development.md). Inputs adopt coding/testing/integration and repository standards; outputs include integrated increments and evidence; completion explicitly depends on [Branch Workflow](../standards/branch-workflow.md). S retains this complete contract. P/V may reuse bounded implementation and validation concerns, but production/service completion is not established by a repository merge. H requires both constituent and combined evidence. A production-independent replacement for this gate remains unadopted. [Coding Standards](../standards/coding-standards.md) and [Continuous Integration](../standards/continuous-integration.md) retain their own triggers and options; [Testing Strategy](../standards/testing-strategy.md) does not require one universal test type.

- **D1 Implementation:** S changes executable behavior/configuration as scoped; P realizes a bounded tangible increment; V realizes a bounded service/process increment; H realizes coordinated constituent changes. P/V/H realizations need specialized production meaning rather than automatic equivalence to source-code integration.
- **D2 Verification:** S retains risk-appropriate evidence; P needs evidence appropriate to material behavior; V to performed service outcomes; H to constituent behavior and interactions. Automated CI is neither a universal production method nor the only validation evidence.
- **D3 Review and Integration:** S retains source review and default-branch conditions; P separates design-record integration from item acceptance; V separates operating-document integration from service readiness; H separates repository integration from combined offering acceptance. An approved document cannot certify production completion.
- **D4 Learning and Refinement:** S retains defects/debt/follow-up; P retains findings without automatically classifying every finding as Bug work or technical debt; V retains service findings without relabeling every operational choice; H links constituent findings and cross-boundary impacts. Apply existing work-type definitions where evidenced; unresolved classification stays explicit.

### Release — five activities

Source: [Release](../lifecycle/06-release.md). Inputs require an integrated increment, release/recovery decisions and evidence; outputs include available increment, release identifier/notes, observation and recovery evidence. Completion means availability to intended users, and Maintenance entry needs operational ownership and feedback capability. S retains the full contract. P distribution/acceptance and V service activation may differ materially from software deployment; H requires compatible constituent availability and combined conditions. Those meanings and handoff gates require contextual/specialized decisions before treating them as equivalent. [Deployment](../standards/deployment-strategy.md) and [Rollback](../standards/rollback-strategy.md) are mechanism-neutral but still impose identifiable verification and safe-state obligations; rollback does not require restoration of a prior version in every case.

- **R1 Release planning:** S selects software increment/audience/conditions; P assesses item/delivery scope and relevant identity; V service promise/activation scope; H coordinated constituent scope and dependencies. Identifiers may differ; one version string does not establish synchronized readiness.
- **R2 Release readiness:** S retains validation/review/recovery evidence; P needs assessed material/delivery evidence; V operating/service evidence; H constituent and interface evidence. Unavailable capability or unresolved recovery is not inapplicability or a waiver.
- **R3 Publication:** S makes the approved increment available; P needs an assessed boundary between producing, delivering, and recipient availability; V between procedure approval, capacity, and actual service availability; H between component publication and complete offering availability. These are unresolved equivalences, not adopted specialized release procedures.
- **R4 Communication and observation:** S retains release information and observed behavior; P needs relevant recipient information and use/delivery observations; V service information and recipient/operating observations; H communications and observations across constituent effects. A shipment or announcement alone is not verified intended outcome.
- **R5 Recovery:** S uses its evidenced safe-state/recovery decision; P must assess irreversibility, affected items, and feasible safe-state options; V service interruption/recipient consequences; H mutually compatible recovery across constituents. This record neither invents recall rules nor asserts that rollback can reverse material changes or completed services.

### Maintenance — four activities

Source: [Maintenance](../lifecycle/07-maintenance.md). Released increments, ownership, signals and prior decisions inform assessed outcomes, corrective work, current evidence, and re-entry. S retains the continuous-maintenance model and bounded increment closure. P/V/H share stewardship concerns but need contextual meanings for operational state, support responsibility, corrective acceptance and end-of-service boundaries. Changes affecting scope, experience, or architecture still return to their governing sources; this record establishes no alternate phase route.

- **M1 Observe and assess:** S uses software/product/operational signals; P relevant material/use signals; V recipient/service-performance signals; H constituent and joint signals. Product monitoring needs do not require software telemetry in every context.
- **M2 Respond and recover:** S retains incident/defect/recovery handling; P assesses physical support and safe response without inventing regulatory procedures; V assesses service restoration and recipient effects; H coordinates cross-constituent response. [Incident Management](../standards/incident-management.md) uses affected-service evidence; a material defect is not automatically the same incident in all contexts.
- **M3 Improve and evolve:** S retains traceable changes and applicable debt decisions; P/V distinguish product/service improvements from [Technical Debt](../standards/technical-debt-management.md), which requires an evidenced technical condition; H traces whole-offering consequences and constituent work. [Bug Management](../standards/bug-management.md) governs defects in expected behavior; classification requires its source meaning rather than a type-based exclusion or automatic extension.
- **M4 Preserve operational knowledge:** S retains current decisions/ownership/evidence; P material/product-support knowledge; V operating/service knowledge; H cross-boundary ownership, compatibility and recovery evidence. Storage medium does not establish retention, privacy, authority, or completion; applicable sources govern.

## Integration and compatibility consequences

The architecture is integrated by source ownership, not by copying rules into a new universal lifecycle:

- Product Type Model owns offering/context/composition; Core and Specialization Boundaries owns common/specialized/repository allocation; Standards Applicability owns contextual determinations. Their evidence informs a lifecycle decision without replacing it.
- The seven lifecycle documents own activities, inputs/outputs and gates. Their previous/next links and README order remain unchanged. Existing software adopters retain the same requirements and navigation; this assessment does not retroactively reclassify their evidence or completion.
- Master Execution Checklist owns the 33-entry index. Its Role, capability, input/output, evidence, completion and next-action links inherit current phase meanings; a future changed gate requires review of those fields and its record template/walkthrough, not merely a new phase label.
- [Work Item Taxonomy](../standards/work-item-taxonomy.md), [Work Item Types](../standards/work-item-types.md), [Project Views](../standards/project-views.md), [Repository Project Field Standard](../standards/repository-project-field-standard.md), and GitHub issue/PR templates reference current classification. A future phase/type change requires semantic and historical-record compatibility review; this record adds no phase, field, mapping or automatic reclassification.
- [Artifact Catalog](../standards/artifact-catalog.md), [glossary](../standards/glossary.md), [standards relationship map](../standards/standards-relationship-map.md), [standards index](../standards/index.md), README, and documentation navigation expose primary owners. Future migration must preserve discoverability and link/heading compatibility or explicitly record affected references and transitions.
- [GitHub reference guidance](github-reference-implementation-guide.md), [machine-representation decision](machine-readable-execution-decision.md), [end-to-end example](../../examples/end-to-end-playbook-example.md), [protocol example](../../examples/executable-protocol-reference-example.md), [checklist walkthrough](../../examples/master-execution-checklist-walkthrough.md), and [adoption checklist](../../templates/foundation-adoption-checklist.md) inherit their declared software/current-source context. They do not certify cross-type execution. This assessment neither silently updates their historical meaning nor establishes a supported machine contract.
- Deployment/recovery, testing/CI, incidents/bugs/debt, security/privacy, accessibility, and UX sources retain their own conditional scopes and evidence. A specialization must assess affected clauses and owners; moving a document or changing its category does not preserve semantics by itself.

This change adds only the assessment and a README practice link. No lifecycle, checklist entry, classification, substantive standard, template, example, directory, or historical record is migrated. The added link is navigation, not a universal applicability declaration.

## Unresolved decisions and bounded follow-up

The repository maintainer authorizing this record is the accountable integration decision-maker. The following are explicit future decision boundaries, not newly scheduled work, approved specializations, or missing evidence concealed as completed production support. Each selected follow-up needs its own scoped owner/Assignment, readiness, acceptance evidence and review; no new milestone version is assigned here.

- **Repository versus production preparation:** assess any repository-independent Foundation inputs/outputs and exit gate before claiming P/V production can satisfy the current Foundation unchanged. Reassess when a concrete non-software adoption needs that claim.
- **Phase/gate and classification compatibility:** decide whether current order and phase meanings remain suitable for a bounded P/V/H case, including Architecture/Development entry and completion. Evidence must trace the 33 activities and affected taxonomy/checklist references before revising an owner. Similar phase names are insufficient.
- **Production, delivery, recovery and operation:** establish concrete quality, availability, irreversibility, safe-state and support evidence with relevant domain owners before adopting P/V/H methods. Resolve material whole-offering dependencies rather than assuming software rollback or source integration supplies it.
- **Software specialization extraction:** if selected, identify every retained source obligation and its explicit future home, compatibility consequences, source revisions and reference transition. Do not remove existing software semantics before the governing migration is reviewed.
- **Hybrid conflicts:** obtain accountable source-level decisions for conflicting constituent conditions, authority and evidence. Do not introduce a precedence or inheritance algorithm through a provider mapping or checklist.
- **Representation and examples:** reassess a machine representation only against the existing deferral's evidence conditions and a concrete consumer need. Future physical/service/hybrid examples need explicit source alignment and scenario limits; conceptual examples alone do not prove empirical readiness.

The maintainer owns selection and assignment of these repository evolution decisions; relevant domain ownership is not presumed. Reassess this record when governing sources, concrete adoption evidence, constituent boundaries or phase decisions change. Preserve this baseline, rationale and affected references when adding a later assessment.

## Acceptance review and completion boundary

Coverage: seven phase assessments include their inputs, outputs, completion and exit dependencies; all 33 indexed activities are examined in S/P/V/H contexts. Source ownership, requirement strength, optional representations, unavailable capabilities, unresolved equivalence, and exception boundaries were reviewed against PT1–PT4 and current lifecycle sources. No automatic exemption or adopted non-software gate is inferred.

This is recorded AI-assisted self-review, not independent approval. A separate independent reviewer was not engaged for this bounded documentation research; mitigation is source-linked activity-by-activity coverage, explicit incompatible/unresolved boundaries, unchanged governing sources, link/whitespace validation, and the maintainer's separate integration decision. No blocking finding remains in this assessment's stated scope; domain validation and migration remain explicit future work.

#304 is complete only when this scoped assessment and its acceptance evidence receive the required review/integration decision under [Definition of Done](../standards/definition-of-done.md), [Code Review](../standards/code-review-standard.md), and [Branch Workflow](../standards/branch-workflow.md). That completes the PT5 research outcome, not physical/service/hybrid production guidance, a universal lifecycle, empirical product validation, formal milestone acceptance, or a published release.

## References

- [Roles and Actor Assignment](../standards/roles-and-actor-assignment.md)
- [Artifact Standard](../standards/artifact-standard.md)
- [Documentation Navigation](../standards/documentation-navigation.md)
- [Decision Record Template](../../templates/decision-record.md)
