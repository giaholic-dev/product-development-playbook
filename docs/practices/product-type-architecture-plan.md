# Product-type Architecture Plan

## Purpose and scope

Record the evidence-based plan for issue #292 and the `v0.5.0 — Product-Type Architecture` delivery boundary. This is a research/planning record. The proposed boundaries and delivery records below are not adopted product-type semantics, revised lifecycle rules, or normative specializations.

Baseline: commit `c89ca5a395e5c7b96c12dc0790abe7cd894c231a`, assessed on 2026-10-13. Existing standards and the seven-phase software-product lifecycle remain authoritative until explicitly revised through reviewed governing decisions.

## Current-state assessment

The [README](../../README.md) defines the purpose, vision, mission, and audience around software products while remaining independent of languages, frameworks, and hosting providers. Technology independence does not establish product-type independence.

The following classification is a planning hypothesis grounded in source scope, not a declaration that any requirement already applies to all product types:

- Candidate common governance: [Core Principles](../core/principles.md), [Roles and Actor Assignment](../standards/roles-and-actor-assignment.md), [Work Management](../standards/work-management.md), [Execution Protocol](../standards/execution-protocol.md), [Definition of Ready](../standards/definition-of-ready.md), [Definition of Done](../standards/definition-of-done.md), [Artifact Standard](../standards/artifact-standard.md), and [Terminology](../standards/terminology-standard.md). Their responsibility, evidence, and decision boundaries do not require a product implementation technology. Broader applicability still needs explicit assessment and a governing model.
- Candidate cross-type product concerns with contextual applicability: [Product Vision](../standards/product-vision.md), [Problem Statement](../standards/problem-statement.md), [Users](../standards/users.md), [Outcomes](../standards/outcomes.md), [Product Scope](../standards/product-scope.md), and [Product Backlog](../standards/product-backlog.md). Similar names across types do not prove identical semantics, artifact choices, or ordering requirements.
- Conditional experience and risk concerns: [UX Phase](../lifecycle/03-ux.md) permits proportionate representations; [Accessibility](../standards/accessibility-inclusive-experience.md) and [Security, Privacy, and Data Governance](../standards/security-privacy-data-governance.md) require contextual assessment. Do not make every current UX artifact or software security control mandatory for every future type.
- Explicit software-oriented delivery assumptions: [Architecture](../lifecycle/04-architecture.md) directs technical structure toward implementation; [Development](../lifecycle/05-development.md) adopts coding, testing, and integration standards; [Release](../lifecycle/06-release.md) uses deployment/recovery decisions; [API Design](../standards/api-design.md), [Data Model](../standards/data-model.md), [Coding Standards](../standards/coding-standards.md), and [Continuous Integration](../standards/continuous-integration.md) carry implementation-specific applicability questions. Retain those semantics for existing software adoption; do not universalize them by renaming.
- Repository-specific baseline: [Repository Standards](../standards/repository-standards.md) deliberately requires Git. [Foundation](../lifecycle/01-foundation.md) requires selected version-control and tracking access. Git may govern this methodology repository without becoming a universal physical-product or service-production requirement; the distinction requires an explicit architectural decision.
- Contextual operations: [Maintenance](../lifecycle/07-maintenance.md), [Release Strategy](../standards/release-strategy.md), [Versioning](../standards/versioning-standard.md), and [Integration](../standards/integration-standard.md) expose useful ownership/evidence boundaries, but their applicable product outcomes and operational realizations need type/context assessment.
- Supporting mappings and representations: the [GitHub guide](github-reference-implementation-guide.md) is optional provider guidance. The [Master Execution Checklist](../standards/master-execution-checklist.md) indexes the current lifecycle; its 33 entries are not proof of universal applicability. The [representation decision](machine-readable-execution-decision.md) defers a new machine model.

## Proposed architectural boundary

The proposed universal core owns only concepts whose product-independent applicability is established by reviewed evidence: responsibility, bounded Authority, traceability, governed decisions, and evidence are candidates, not adopted universal definitions in this record.

A specialization would own the product-type-specific meaning and application of activities, outcomes, artifacts, quality, delivery, and operation. A specialization would preserve core obligations where applicable rather than silently weakening them. Conditional requirements would retain explicit triggers, rationale, and traceability; Unknown applicability would remain unresolved instead of being treated as optional or inapplicable.

A provider mapping is a separate concern from product type. Software, physical, service, or hybrid work does not inherently select a hosting provider, AI mode, integration, or organizational model. Hybrid composition needs an explicit account of boundaries and cross-component obligations; it is not assumed to be a union of every possible requirement.

The model must resolve which requirements govern the methodology repository itself versus adopting product work. No hierarchy, override mechanism, exemption catalog, or type taxonomy becomes normative here.

## Dependency-ordered delivery records

Each record below is bounded enough to become an independently tracked issue after this plan is approved. Identifiers are local planning references, not GitHub issue numbers. All belong to the proposed `v0.5.0` architecture scope; implementation of product-specific guides belongs to later, still-provisional work.

### PT1 — Complete the product-type assumption assessment

- Classification: Foundation / Research; Artifact: Documentation — Record.
- Inputs: this baseline assessment and the existing lifecycle, standards, and repository scopes.
- Outcome: an exhaustive evidence-linked inventory of material assumptions and proposed common, type-specific, conditional, or unresolved concerns, with rationale and affected owners.
- Acceptance evidence: each material assumption cites its source; uncertain applicability is explicit; repository-governance obligations remain separate from product-production obligations; no source requirement is removed or generalized.
- Dependencies: approved #292 planning record. This record deepens the initial assessment rather than pretending the initial category summary is exhaustive.

### PT2 — Define the Product Type Model

- Classification: Architecture / Research; Artifact: Documentation — Standard and supporting decision evidence.
- Inputs: PT1 assessment.
- Outcome: reviewed meanings and relationships for product type, relevant contexts, and hybrid/composite boundaries, with explicit distinction from technology, provider, delivery framework, Actor type, and Artifact Type.
- Acceptance evidence: software, physical, service, and hybrid conceptual scenarios test the distinctions; unresolved classification remains explicit; existing terminology owners are preserved.
- Dependencies: PT1. Naming examples does not establish a closed universal type catalog.

### PT3 — Define universal core and specialization boundaries

- Classification: Architecture / Research; Artifact: Documentation — Decision Record and governing boundary standard where justified.
- Inputs: PT1 assumptions and PT2 model.
- Outcome: an approved allocation of conceptual ownership between common governance, type-specific semantics, and methodology-repository requirements.
- Acceptance evidence: each proposed core concern has applicability rationale; software semantics are preserved in an explicit proposed home; specialization cannot silently override governing obligations; hybrid conflicts and unresolved ownership have accountable treatment.
- Dependencies: PT1 and PT2. No directory restructuring or mass terminology replacement is implied.

### PT4 — Define standards applicability semantics

- Classification: Architecture / Feature; Artifact: Documentation — Standard.
- Inputs: PT2 model and PT3 ownership boundaries.
- Outcome: an evidence-based method to decide applicable requirements and representations by type/context, including conditions, uncertainty, exceptions, and source ownership.
- Acceptance evidence: distinguish inapplicability from optionality, unavailable capability, unmet requirement, and permitted exception; do not allow a mapping or checklist to waive a source rule; validate common and specialized concerns in the four conceptual scenarios.
- Dependencies: PT2 and PT3. No applicability state catalog or override rule is adopted by this planning record.

### PT5 — Assess lifecycle applicability and validate architectural integration

- Classification: Architecture / Research; Artifact: Documentation — Decision Record and assessment evidence.
- Inputs: PT1–PT4 plus all seven current lifecycle sources and checklist entries.
- Outcome: documented assessment of which phase/activity semantics can remain common, require specialization, or remain unresolved; cross-source integration and a migration boundary suitable for later reviewed changes.
- Acceptance evidence: examine software, physical, service, and hybrid scenarios; preserve existing software use; identify affected references and compatibility consequences; record any required later work without claiming it implemented; no phase is renamed, reordered, generalized, or replaced before its governing applicability decision.
- Dependencies: PT1–PT4. Architectural assessment is within `v0.5.0`; broad lifecycle migration and product-type implementation guidance are not implicitly included.

Delivery order: PT1 → PT2 → PT3 → PT4 → PT5. Assessment evidence may be refined as later findings emerge, retaining its history. Each eventual issue needs scoped Assignments, readiness evidence, acceptance review, and traceability under existing governance.

## Validation approach and open questions

Use bounded conceptual scenarios: an existing software increment, a manufactured physical item, a delivered service, and a hybrid software/physical/service offering. These are assessment contexts, not claims that the current seven phases already fit them.

For each scenario, trace responsibility, intended outcomes, required evidence, relevant artifacts, production/delivery/operation constraints, and requirement applicability. Record mismatches instead of filling them with renamed software concepts. Independently review whether a proposed universal concept retains the same meaning and obligations across the scenarios.

Open decisions include: the core's minimum extent; product-type versus contextual specialization; treatment of hybrid dependencies; repository-specific Git obligations; experience applicability; delivery/operation equivalence; exception versus inapplicability; and lifecycle compatibility/migration. This plan identifies their decision order rather than resolving them without evidence.

## Completion and future evolution boundary

#292 is complete when the initial evidence assessment, proposed ownership boundary, and independently traceable dependency-ordered delivery plan are approved and discoverable. This does not complete PT1–PT5 or the `v0.5.0` milestone.

Later software-specialization extraction, physical/service/hybrid guidance, lifecycle revisions, compatibility migrations, examples, and machine representations remain candidate evolution areas. Do not assign later milestone versions or implementation scope until the architecture decisions justify them. The #281 deferral remains unchanged.

## Accountability and reassessment

The reviewed #292 change identifies the repository maintainer approving this planning decision; no permanent specialization owner is invented here. Each delivery record requires its own scoped owner when selected. Reassess the plan when the assumption inventory or governing boundaries change; preserve the rationale and affected delivery records. This assessment is conceptual repository research, not validation of real physical or service product delivery.

## References

- [Issue #292](https://github.com/giaholic-dev/product-development-playbook/issues/292)
- [Roles and Actor Assignment Standard](../standards/roles-and-actor-assignment.md)
- [Definition of Ready](../standards/definition-of-ready.md)
- [Definition of Done](../standards/definition-of-done.md)
- [Artifact Standard](../standards/artifact-standard.md)
