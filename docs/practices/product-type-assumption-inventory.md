# Product-type Assumption Inventory

## Purpose and scope

Assess material product-type assumptions at baseline `9f61f6be40809f21d9569a6368cc54c8831ce4cb` for [#300](https://github.com/giaholic-dev/product-development-playbook/issues/300), PT1 of the [approved architecture plan](product-type-architecture-plan.md). This is a research Record, not a new applicability standard or universal product model.

All 95 Markdown sources at this baseline were fetched and inventoried, including the seven lifecycle documents, standards, practices, examples, templates, and GitHub templates. The inventory distinguishes scope evidence, proposed concern classification, and unresolved applicability. Configuration and scripts are supporting implementation: their Git/GitHub shell-tool requirements belong to the documented optional exporter and repository environment, not evidence that every product requires those tools. No source is edited or superseded by this record.

## Assessment meanings

The categories below describe assessment findings rather than normative applicability states. Candidate common means the stated concern does not inherently require a product implementation technology; transferability still needs the Product Type Model and core-boundary decisions. Conditional means relevance depends on an evidenced context or source trigger; it does not mean optional whenever inconvenient. Repository-governance concerns may govern this Playbook repository without being universal product-production requirements.

Lifecycle-dependent means existing classification or navigation relies on the current phase meanings. Supporting examples, templates, catalogs, and provider mappings retain their existing non-authoritative or navigational status. Unresolved means the evidence does not establish cross-type applicability; it is neither a waiver nor proof of inapplicability.

## Material findings and decision obligations

1. Software scope is explicit in README purpose, vision, mission, and audience. Technology/provider neutrality does not remove that scope. Preserve existing software adoption while #301 and #302 decide type and ownership boundaries.
2. Foundation inputs require selected version-control and work-tracking access; Repository Standards deliberately adopts Git. Separate methodology-repository governance from requirements for producing a physical item or delivering a service. #302 owns the future allocation; no Git exception is granted here.
3. All seven ordered lifecycle phases remain governing sources. Their use of Product/UX/Architecture/Development/Release/Maintenance must be assessed by meaning, inputs, outputs, and gates, not renamed into universality. #304 owns that assessment.
4. Product concepts are often framework-neutral and evidence-oriented. Similar concepts across types are candidates for reuse, not proof that every artifact or phase order transfers unchanged. #301–#303 determine their actual applicability boundaries.
5. UX representations preserve optionality: UX Artifacts and the UX phase do not require every journey, persona, wireframe, or prototype. UX Validation explicitly states product-type independence. Treat validation concern separately from selected representation and lifecycle application; do not silently make software interface artifacts universal.
6. Coding Standards explicitly applies to source code or executable configuration and permits documentation-only non-applicability. It is a conditional implementation concern, not proof that every future physical/service product needs coding conventions. The source's existing trigger remains authoritative pending #303.
7. API Design includes conceptual human-facing and machine-facing interfaces; Data Model separates information requirements from storage technology. The architecture plan's initial software-oriented grouping does not establish that these standards are exclusively software. Their governing contexts and lifecycle relationships still need assessment.
8. Testing Strategy offers proportionate validation and explicitly avoids one universally mandatory test type. Continuous Integration concerns repeatable automated validation. Do not equate all validation with automated software CI or make automation mandatory for other types.
9. Deployment and rollback use change-availability/recovery concerns without prescribing infrastructure. Physical production, service delivery, and hybrid recovery may have materially different irreversibility and evidence; shared naming is insufficient. #304 must assess the mismatch without redefining delivery here.
10. Incident Management describes an affected service; bug and technical-debt concepts have specific meanings. Do not relabel every physical defect, service interruption, or non-preferred choice as an existing software work type or debt condition without semantic evidence.
11. Accountability, Authority, Artifact identity, attempt evidence, work Validation, and Completion are separately owned across standards. They are candidate reusable governance, but Actor neutrality, framework independence, and provider independence are distinct from product-type applicability.
12. Work Item Taxonomy requires a primary Lifecycle Phase and Work Type; the checklist indexes 33 current activities. These representations inherit existing lifecycle meaning. A cross-type model must address that dependence before classification or checklist generalization.
13. GitHub fields, templates, guides, and optional exporter/Codespaces utilities are mappings or implementation support. Provider capability, current connection exposure, and product type remain independent dimensions. Native GitHub support does not decide the universal core.
14. Security/privacy, accessibility, AI, and Integration contain contextual scope conditions. An absent capability, unsupported connection, unmet requirement, permitted exception, optional artifact, and genuinely inapplicable concern remain distinct; #303 must formalize those applicability boundaries.
15. Current examples are fictional software increments. They test documented ownership distinctions, not empirical physical/service applicability. The approved machine-representation decision remains a deferral; a broader product model must not be inferred from Markdown field consistency.

## Source-by-source evidence inventory

Each entry links to its primary source and states its declared scope or purpose as evidence. Quoted excerpts are source text, not new requirements. Classification is an assessment proposal; the destination remains the definition owner. Where Scope is absent, Purpose or introductory text supplies the responsibility evidence.

### ---

- Source: [.github/ISSUE_TEMPLATE/work-item.md](../../.github/ISSUE_TEMPLATE/work-item.md).
- Scope evidence: “name: Work item about: Capture work with traceable scope and evidence title: "" labels: "" assignees: "" ---”
- Assessment: Provider/repository mapping. Platform or repository representation remains a mapping, not a universal production requirement.

### <!-- Use this template to summarize a proposed change and its evidence. Governed by [Pull Request Template Standard](https://github.com/giaholic-dev/product-development-playbook/blob/main/docs/standards/pull-request-template-standard.md). -->

- Source: [.github/pull_request_template.md](../../.github/pull_request_template.md).
- Scope evidence: “## Summary - ## Related work”
- Assessment: Provider/repository mapping. Platform or repository representation remains a mapping, not a universal production requirement.

### Product Development Playbook

- Source: [README.md](../../README.md).
- Scope evidence: “This Playbook defines: - Product development lifecycle - Engineering governance - Engineering standards - Product management practices - Documentation standards - Decision-making processes The Playbook intentionally remains independent of: - Programming languages - Frameworks - Platform-specific architectures - Tool-specific implementations The conceptual method is independent of hosting vendors. This repository deliberately uses Git and includes GitHub mappings and supporting automation as implementation guidance, [excerpt; see full source]”
- Assessment: Declared software scope. Software is the declared adoption context; assess type-independent purpose separately before changing it.

### Playbook Core Principles

- Source: [docs/core/principles.md](../../docs/core/principles.md).
- Scope evidence: “These principles apply to decisions made while adopting or using the Playbook. They do not prescribe a product architecture, delivery method, tool, provider, or implementation.”
- Assessment: Candidate common concern. The stated decision/evidence concern is a reuse candidate; assess cross-type semantics and ownership under #301–#303.

### 01 — Foundation

- Source: [docs/lifecycle/01-foundation.md](../../docs/lifecycle/01-foundation.md).
- Scope evidence: “Define the minimum reusable foundation that a product repository adopts, configures, and evidences before beginning the Product phase. Foundation establishes sufficient repository, governance, workflow, and documentation capability for deliberate product work. It does not require every future decision to be made in advance: unresolved decisions MAY remain when their scope, owner, and reassessment condition are recorded.”
- Assessment: Lifecycle applicability unresolved. Current ordered phase activities and gates remain governing; #304 must assess transferability and mismatches.

### 02 — Product

- Source: [docs/lifecycle/02-product.md](../../docs/lifecycle/02-product.md).
- Scope evidence: “Transform a product idea or opportunity into an evidence-based product definition that can inform later lifecycle work.”
- Assessment: Lifecycle applicability unresolved. Current ordered phase activities and gates remain governing; #304 must assess transferability and mismatches.

### 03 — UX

- Source: [docs/lifecycle/03-ux.md](../../docs/lifecycle/03-ux.md).
- Scope evidence: “Transform the Product definition into a validated experience direction that can inform Architecture and Development without prematurely prescribing implementation.”
- Assessment: Lifecycle applicability unresolved. Current ordered phase activities and gates remain governing; #304 must assess transferability and mismatches.

### 04 — Architecture

- Source: [docs/lifecycle/04-architecture.md](../../docs/lifecycle/04-architecture.md).
- Scope evidence: “Transform validated product and experience decisions into an intentional technical structure that can guide development without selecting unnecessary technology.”
- Assessment: Lifecycle applicability unresolved. Current ordered phase activities and gates remain governing; #304 must assess transferability and mismatches.

### 05 — Development

- Source: [docs/lifecycle/05-development.md](../../docs/lifecycle/05-development.md).
- Scope evidence: “Implement, integrate, and validate product work in small, traceable increments consistent with the current Product, UX, and Architecture decisions.”
- Assessment: Lifecycle applicability unresolved. Current ordered phase activities and gates remain governing; #304 must assess transferability and mismatches.

### 06 — Release

- Source: [docs/lifecycle/06-release.md](../../docs/lifecycle/06-release.md).
- Scope evidence: “Make an integrated product increment available to its intended users with a clear scope, release record, and recovery path.”
- Assessment: Lifecycle applicability unresolved. Current ordered phase activities and gates remain governing; #304 must assess transferability and mismatches.

### 07 — Maintenance

- Source: [docs/lifecycle/07-maintenance.md](../../docs/lifecycle/07-maintenance.md).
- Scope evidence: “Sustain a released product through observation, support, correction, learning, and intentional evolution.”
- Assessment: Lifecycle applicability unresolved. Current ordered phase activities and gates remain governing; #304 must assess transferability and mismatches.

### AI-assisted Execution Practice

- Source: [docs/practices/ai-assisted-execution.md](../../docs/practices/ai-assisted-execution.md).
- Scope evidence: “Offer non-normative guidance for applying the AI Collaboration Standard to a material work item.”
- Assessment: Supporting guidance or decision. Retain the document’s declared responsibility and source status; guidance/planning does not adopt a universal product model.

### GitHub Reference Implementation Guide

- Source: [docs/practices/github-reference-implementation-guide.md](../../docs/practices/github-reference-implementation-guide.md).
- Scope evidence: “Map optional GitHub implementation choices to governed Playbook needs under the Provider Implementation Guide Standard and Provider-independent Integration Standard. GitHub is replaceable implementation guidance, not a required provider or the owner of methodology.”
- Assessment: Supporting guidance or decision. Retain the document’s declared responsibility and source status; guidance/planning does not adopt a universal product model.

### Machine-readable Execution Representation Decision

- Source: [docs/practices/machine-readable-execution-decision.md](../../docs/practices/machine-readable-execution-decision.md).
- Scope evidence: “## Purpose and scope Record the representation-boundary decision for issue #281. This is a Documentation — Decision Record, not an execution schema, application architecture, or new normative methodology. Its proposed decision takes effect through the reviewed repository integration record; it does not authorize external execution. ## Context”
- Assessment: Supporting guidance or decision. Retain the document’s declared responsibility and source status; guidance/planning does not adopt a universal product model.

### Product-type Architecture Plan

- Source: [docs/practices/product-type-architecture-plan.md](../../docs/practices/product-type-architecture-plan.md).
- Scope evidence: “## Purpose and scope Record the evidence-based plan for issue #292 and the `v0.5.0 — Product-Type Architecture` delivery boundary. This is a research/planning record. The proposed boundaries and delivery records below are not adopted product-type semantics, revised lifecycle rules, or normative specializations. Baseline: commit `c89ca5a395e5c7b96c12dc0790abe7cd894c231a`, assessed on 2026-10-13. Existing standards and the seven-phase software-product lifecycle remain authoritative until explicitly revised through re [excerpt; see full source]”
- Assessment: Supporting guidance or decision. Retain the document’s declared responsibility and source status; guidance/planning does not adopt a universal product model.

### Accessibility and Inclusive Experience Standard

- Source: [docs/standards/accessibility-inclusive-experience.md](../../docs/standards/accessibility-inclusive-experience.md).
- Scope evidence: “This standard applies to product decisions, experiences, technical constraints, validation, release, and maintenance where accessibility or inclusion may materially affect an actor. It does not prescribe a standard, tool, test method, or provider.”
- Assessment: Conditional/contextual concern. Assess the declared trigger, decision context, and lifecycle links; neutrality of tooling alone does not prove universal application.

### AI Collaboration Standard

- Source: [docs/standards/ai-collaboration.md](../../docs/standards/ai-collaboration.md).
- Scope evidence: “This standard applies when a project uses AI to analyze, propose, generate, transform, classify, review, or perform authorized actions. It does not require AI, a provider, a model, a prompt format, an integration, or an automation platform.”
- Assessment: Conditional/contextual concern. Assess the declared trigger, decision context, and lifecycle links; neutrality of tooling alone does not prove universal application.

### API Design

- Source: [docs/standards/api-design.md](../../docs/standards/api-design.md).
- Scope evidence: “This standard is independent of protocol, transport, framework, provider, and API style.”
- Assessment: Conditional/contextual concern. Assess the declared trigger, decision context, and lifecycle links; neutrality of tooling alone does not prove universal application.

### Architecture Artifacts

- Source: [docs/standards/architecture-artifacts.md](../../docs/standards/architecture-artifacts.md).
- Scope evidence: “This standard applies to architecture artifacts and delegates categories and subtypes to the Artifact Standard.”
- Assessment: Conditional/contextual concern. Assess the declared trigger, decision context, and lifecycle links; neutrality of tooling alone does not prove universal application.

### Architecture Decision Records

- Source: [docs/standards/architecture-decision-records.md](../../docs/standards/architecture-decision-records.md).
- Scope evidence: “This standard applies to architecture decisions independently of a specific record template or repository platform.”
- Assessment: Candidate common concern. The stated decision/evidence concern is a reuse candidate; assess cross-type semantics and ownership under #301–#303.

### Architecture Vision

- Source: [docs/standards/architecture-vision.md](../../docs/standards/architecture-vision.md).
- Scope evidence: “This standard is independent of programming language, framework, cloud provider, and implementation pattern.”
- Assessment: Conditional/contextual concern. Assess the declared trigger, decision context, and lifecycle links; neutrality of tooling alone does not prove universal application.

### Artifact Catalog

- Source: [docs/standards/artifact-catalog.md](../../docs/standards/artifact-catalog.md).
- Scope evidence: “This catalog covers artifact categories and representative repository locations. It does not govern artifact identity, classification, or work-item fields.”
- Assessment: Navigational catalog. Navigation delegates semantics to primary owners; catalog membership is not an applicability decision.

### Artifact Standard

- Source: [docs/standards/artifact-standard.md](../../docs/standards/artifact-standard.md).
- Scope evidence: “An **artifact** is an inspectable record, deliverable, or durable result created, adopted, or materially changed by product work. It may be a document, source-controlled configuration, decision record, template, example, or another medium appropriate to the product. This standard governs artifact identity, type hierarchy, multiplicity, ownership, and evidence. It does not prescribe a directory layout, tool, file format, or lifecycle phase. The Work Item Taxonomy may reference an Artifact Type when an artifact is re [excerpt; see full source]”
- Assessment: Candidate common concern. The stated decision/evidence concern is a reuse candidate; assess cross-type semantics and ownership under #301–#303.

### Branch Workflow

- Source: [docs/standards/branch-workflow.md](../../docs/standards/branch-workflow.md).
- Scope evidence: “This standard defines version-control workflow expectations. It is Git-oriented because the Playbook deliberately requires version-control capability, but it does not require a hosting vendor.”
- Assessment: Repository-governance concern. Separate maintenance of governed repository records from production obligations of the adopting product.

### Bug Management

- Source: [docs/standards/bug-management.md](../../docs/standards/bug-management.md).
- Scope evidence: “This standard governs defects discovered in development, release, or maintenance. It distinguishes routine defect work from incidents, which require coordinated service restoration.”
- Assessment: Conditional/contextual concern. Assess the declared trigger, decision context, and lifecycle links; neutrality of tooling alone does not prove universal application.

### Code Review Standard

- Source: [docs/standards/code-review-standard.md](../../docs/standards/code-review-standard.md).
- Scope evidence: “This standard applies to code, configuration, automation, documentation, and other repository changes. The review depth MUST be proportionate to the change's risk, impact, and reversibility.”
- Assessment: Repository-governance concern. Separate maintenance of governed repository records from production obligations of the adopting product.

### Coding Standards

- Source: [docs/standards/coding-standards.md](../../docs/standards/coding-standards.md).
- Scope evidence: “This standard applies when a repository contains source code or executable configuration.”
- Assessment: Conditional/contextual concern. Assess the declared trigger, decision context, and lifecycle links; neutrality of tooling alone does not prove universal application.

### Component Architecture

- Source: [docs/standards/component-architecture.md](../../docs/standards/component-architecture.md).
- Scope evidence: “This standard is independent of programming language, framework, module system, and deployment topology.”
- Assessment: Conditional/contextual concern. Assess the declared trigger, decision context, and lifecycle links; neutrality of tooling alone does not prove universal application.

### Continuous Integration

- Source: [docs/standards/continuous-integration.md](../../docs/standards/continuous-integration.md).
- Scope evidence: “This standard is independent of CI provider, operating system, language, framework, and workflow syntax.”
- Assessment: Conditional/contextual concern. Assess the declared trigger, decision context, and lifecycle links; neutrality of tooling alone does not prove universal application.

### Data Model

- Source: [docs/standards/data-model.md](../../docs/standards/data-model.md).
- Scope evidence: “This standard is independent of database technology, storage engine, serialization format, and modeling notation.”
- Assessment: Conditional/contextual concern. Assess the declared trigger, decision context, and lifecycle links; neutrality of tooling alone does not prove universal application.

### Definition of Done

- Source: [docs/standards/definition-of-done.md](../../docs/standards/definition-of-done.md).
- Scope evidence: “This standard applies to the evidence required to complete a work item or outcome. It does not define release criteria, deployment steps, or a platform workflow.”
- Assessment: Candidate common concern. The stated decision/evidence concern is a reuse candidate; assess cross-type semantics and ownership under #301–#303.

### Definition of Ready

- Source: [docs/standards/definition-of-ready.md](../../docs/standards/definition-of-ready.md).
- Scope evidence: “This standard applies to work items before responsible work begins. It does not prescribe delivery methodology, estimation, or workflow states.”
- Assessment: Candidate common concern. The stated decision/evidence concern is a reuse candidate; assess cross-type semantics and ownership under #301–#303.

### Deployment Strategy

- Source: [docs/standards/deployment-strategy.md](../../docs/standards/deployment-strategy.md).
- Scope evidence: “This standard governs deployment decisions and evidence. It does not prescribe infrastructure, environments, automation tooling, or a single delivery method.”
- Assessment: Conditional/contextual concern. Assess the declared trigger, decision context, and lifecycle links; neutrality of tooling alone does not prove universal application.

### Documentation Information Architecture

- Source: [docs/standards/documentation-information-architecture.md](../../docs/standards/documentation-information-architecture.md).
- Scope evidence: “This standard governs documentation categories, placement, relationships, and the representation of current and planned content. Writing conventions belong to the Documentation Style Guide; reading paths and links belong to the Documentation Navigation Standard. Neither GitHub nor a fixed directory tree is required by this conceptual architecture.”
- Assessment: Repository-governance concern. Separate maintenance of governed repository records from production obligations of the adopting product.

### Documentation Navigation Standard

- Source: [docs/standards/documentation-navigation.md](../../docs/standards/documentation-navigation.md).
- Scope evidence: “This standard covers navigation behavior and link verification. Documentation Information Architecture owns categories and placement; Repository Standards owns the repository-level documentation obligation. A repository may implement these rules without GitHub or a prescribed directory layout.”
- Assessment: Repository-governance concern. Separate maintenance of governed repository records from production obligations of the adopting product.

### Documentation Style Guide

- Source: [docs/standards/documentation-style-guide.md](../../docs/standards/documentation-style-guide.md).
- Scope evidence: “This guide covers writing and Markdown conventions for maintained Playbook documentation. It does not replace rules for documentation ownership, navigation, or repository governance.”
- Assessment: Repository-governance concern. Separate maintenance of governed repository records from production obligations of the adopting product.

### Execution Protocol Standard

- Source: [docs/standards/execution-protocol.md](../../docs/standards/execution-protocol.md).
- Scope evidence: “This standard governs execution-protocol semantics without redefining Work Management, Lifecycle Phase, Work Type, Workflow State, Roles or Actor Assignments, Definition of Ready, Definition of Done, provider integrations, or delivery frameworks. The protocol is provider-independent, tool-independent, framework-independent, and AI-optional. Existing authoritative standards retain ownership of the concepts they govern.”
- Assessment: Candidate common concern. The stated decision/evidence concern is a reuse candidate; assess cross-type semantics and ownership under #301–#303.

### Glossary

- Source: [docs/standards/glossary.md](../../docs/standards/glossary.md).
- Scope evidence: “This catalog covers approved cross-cutting vocabulary and links to its primary owners. It does not redefine terms or replace their governing standards.”
- Assessment: Navigational catalog. Navigation delegates semantics to primary owners; catalog membership is not an applicability decision.

### High-Level Architecture

- Source: [docs/standards/high-level-architecture.md](../../docs/standards/high-level-architecture.md).
- Scope evidence: “This standard is independent of implementation language, framework, runtime, provider, and diagram notation.”
- Assessment: Conditional/contextual concern. Assess the declared trigger, decision context, and lifecycle links; neutrality of tooling alone does not prove universal application.

### Incident Management

- Source: [docs/standards/incident-management.md](../../docs/standards/incident-management.md).
- Scope evidence: “This standard governs incident assessment, coordination, recovery, communication, and follow-up. It does not replace routine defect handling or prescribe a particular on-call tool or process.”
- Assessment: Conditional/contextual concern. Assess the declared trigger, decision context, and lifecycle links; neutrality of tooling alone does not prove universal application.

### Standards Index

- Source: [docs/standards/index.md](../../docs/standards/index.md).
- Scope evidence: “This index lists maintained standards and the catalogs that help readers locate them. It does not replace their governing content or enumerate implementation artifacts outside the documentation set.”
- Assessment: Navigational catalog. Navigation delegates semantics to primary owners; catalog membership is not an applicability decision.

### Provider-independent Integration Standard

- Source: [docs/standards/integration-standard.md](../../docs/standards/integration-standard.md).
- Scope evidence: “This standard owns Integration, Capability, Capability Contract, Capability Discovery, contextual support descriptions, integration Verification, Failure handling, Fallback boundaries, and integration Conformance. It does not require an Integration, provider, adapter, execution application, or machine-readable representation. The Execution Protocol Standard retains ownership of attempt-level Capability Requirement, Capability Availability, authorization checks, Protocol Results, evidence linkage, and Execution Disp [excerpt; see full source]”
- Assessment: Conditional/contextual concern. Assess the declared trigger, decision context, and lifecycle links; neutrality of tooling alone does not prove universal application.

### Issue Template Standard

- Source: [docs/standards/issue-template-standard.md](../../docs/standards/issue-template-standard.md).
- Scope evidence: “This standard covers the information requested by an issue template. It does not replace work-item classification, readiness, or completion rules.”
- Assessment: Repository-governance concern. Separate maintenance of governed repository records from production obligations of the adopting product.

### Master Execution Checklist

- Source: [docs/standards/master-execution-checklist.md](../../docs/standards/master-execution-checklist.md).
- Scope evidence: “This standard governs how Master Execution Checklist entries are structured and how they reference their authoritative sources. It does not replace lifecycle documents, Work Management, the Execution Protocol, readiness or completion standards, or artifact governance. The checklist is provider-independent and directly usable by humans. It does not define a workflow, state model, execution mechanism, provider integration, or machine-readable execution format. The operational inventory below covers every activity cur [excerpt; see full source]”
- Assessment: Lifecycle-dependent representation. Current lifecycle or classification sources determine meaning; do not generalize field values or positions before #304.

### Outcomes

- Source: [docs/standards/outcomes.md](../../docs/standards/outcomes.md).
- Scope evidence: “This document defines Outcomes independently of any measurement framework or delivery method.”
- Assessment: Candidate common concern. The stated decision/evidence concern is a reuse candidate; assess cross-type semantics and ownership under #301–#303.

### Personas

- Source: [docs/standards/personas.md](../../docs/standards/personas.md).
- Scope evidence: “This standard is independent of persona template, research method, or design framework.”
- Assessment: Conditional/contextual concern. Assess the declared trigger, decision context, and lifecycle links; neutrality of tooling alone does not prove universal application.

### Problem Statement

- Source: [docs/standards/problem-statement.md](../../docs/standards/problem-statement.md).
- Scope evidence: “This document defines Problem Statement independently of any product management framework or delivery method.”
- Assessment: Candidate common concern. The stated decision/evidence concern is a reuse candidate; assess cross-type semantics and ownership under #301–#303.

### Product Backlog

- Source: [docs/standards/product-backlog.md](../../docs/standards/product-backlog.md).
- Scope evidence: “This document defines Product Backlog independently of a product management platform or delivery framework.”
- Assessment: Candidate common concern. The stated decision/evidence concern is a reuse candidate; assess cross-type semantics and ownership under #301–#303.

### Product Evolution

- Source: [docs/standards/product-evolution.md](../../docs/standards/product-evolution.md).
- Scope evidence: “Product evolution covers material changes to product outcomes, users, scope, experience, architecture, and operating assumptions. It does not replace routine defect correction, incident response, or a delivery workflow.”
- Assessment: Conditional/contextual concern. Assess the declared trigger, decision context, and lifecycle links; neutrality of tooling alone does not prove universal application.

### Product Monitoring

- Source: [docs/standards/product-monitoring.md](../../docs/standards/product-monitoring.md).
- Scope evidence: “Monitoring includes quantitative and qualitative signals. It does not prescribe analytics platforms, dashboards, service-level targets, or data-collection technology.”
- Assessment: Conditional/contextual concern. Assess the declared trigger, decision context, and lifecycle links; neutrality of tooling alone does not prove universal application.

### Product Scope

- Source: [docs/standards/product-scope.md](../../docs/standards/product-scope.md).
- Scope evidence: “This document defines Product Scope independently of implementation architecture, delivery planning, or project management methodology.”
- Assessment: Candidate common concern. The stated decision/evidence concern is a reuse candidate; assess cross-type semantics and ownership under #301–#303.

### Product Vision

- Source: [docs/standards/product-vision.md](../../docs/standards/product-vision.md).
- Scope evidence: “This document defines Product Vision independently of any product management framework or delivery method.”
- Assessment: Candidate common concern. The stated decision/evidence concern is a reuse candidate; assess cross-type semantics and ownership under #301–#303.

### Project Views

- Source: [docs/standards/project-views.md](../../docs/standards/project-views.md).
- Scope evidence: “This standard covers the conceptual purpose, composition, ownership, and evolution of project views. It does not prescribe a specific project-management platform or configuration.”
- Assessment: Conditional/contextual concern. Assess the declared trigger, decision context, and lifecycle links; neutrality of tooling alone does not prove universal application.

### Prototypes

- Source: [docs/standards/prototypes.md](../../docs/standards/prototypes.md).
- Scope evidence: “This standard is independent of prototype fidelity, tooling, and implementation technology.”
- Assessment: Conditional/contextual concern. Assess the declared trigger, decision context, and lifecycle links; neutrality of tooling alone does not prove universal application.

### Provider Implementation Guide Standard

- Source: [docs/standards/provider-implementation-guide-standard.md](../../docs/standards/provider-implementation-guide-standard.md).
- Scope evidence: “This standard governs guide content, source traceability, verification evidence, ownership, and maintenance. A Provider Implementation Guide is non-normative implementation guidance for a named provider and a defined execution context. Its instructions describe an optional mapping; they do not redefine lifecycle policy or Capability Contracts. The Provider-independent Integration Standard owns integration semantics, Capability Contracts, discovery, contextual support descriptions, Verification, Failure, Fallback, a [excerpt; see full source]”
- Assessment: Conditional/contextual concern. Assess the declared trigger, decision context, and lifecycle links; neutrality of tooling alone does not prove universal application.

### Pull Request Template Standard

- Source: [docs/standards/pull-request-template-standard.md](../../docs/standards/pull-request-template-standard.md).
- Scope evidence: “This standard covers the information requested by a pull-request template. It does not replace branch, review, or completion rules.”
- Assessment: Repository-governance concern. Separate maintenance of governed repository records from production obligations of the adopting product.

### Release Notes

- Source: [docs/standards/release-notes.md](../../docs/standards/release-notes.md).
- Scope evidence: “Release notes describe what changed in a specific release. They do not replace implementation history, operational runbooks, or backlog records.”
- Assessment: Conditional/contextual concern. Assess the declared trigger, decision context, and lifecycle links; neutrality of tooling alone does not prove universal application.

### Release Strategy

- Source: [docs/standards/release-strategy.md](../../docs/standards/release-strategy.md).
- Scope evidence: “This standard governs the decision framework for a release. It does not replace detailed deployment, rollback, or release-note procedures.”
- Assessment: Conditional/contextual concern. Assess the declared trigger, decision context, and lifecycle links; neutrality of tooling alone does not prove universal application.

### Repository Automation Standard

- Source: [docs/standards/repository-automation.md](../../docs/standards/repository-automation.md).
- Scope evidence: “This standard applies to repository-local automation, including scripts, checks, workflows, bots, and generated evidence. It does not require a particular automation platform. The AI Collaboration Standard owns AI-specific authority, evidence, provider-independence, and manual-fallback rules.”
- Assessment: Repository-governance concern. Separate maintenance of governed repository records from production obligations of the adopting product.

### Repository Label Standard

- Source: [docs/standards/repository-labels.md](../../docs/standards/repository-labels.md).
- Scope evidence: “This standard applies when a repository uses labels. Labels are optional implementation metadata; the underlying concepts remain technology-neutral.”
- Assessment: Repository-governance concern. Separate maintenance of governed repository records from production obligations of the adopting product.

### Repository Milestone Standard

- Source: [docs/standards/repository-milestones.md](../../docs/standards/repository-milestones.md).
- Scope evidence: “This standard applies when a repository uses milestones. It is technology-neutral; the GitHub mapping is an optional implementation detail.”
- Assessment: Repository-governance concern. Separate maintenance of governed repository records from production obligations of the adopting product.

### Repository Project Field Standard

- Source: [docs/standards/repository-project-field-standard.md](../../docs/standards/repository-project-field-standard.md).
- Scope evidence: “This standard covers a GitHub Projects mapping of the Playbook work-item model. It does not make GitHub configuration a requirement for adopting the conceptual taxonomy.”
- Assessment: Provider/repository mapping. Platform or repository representation remains a mapping, not a universal production requirement.

### Repository Standards

- Source: [docs/standards/repository-standards.md](../../docs/standards/repository-standards.md).
- Scope evidence: “This standard defines the baseline for repository organization, documentation, version control, changes, conformance, and delegation to detailed standards. The conceptual layer is independent of programming languages, frameworks, product architecture, and repository-hosting vendors. The Playbook deliberately adopts Git as its version-control baseline. A hosting platform is an implementation choice unless a project explicitly adopts a corresponding mapping.”
- Assessment: Repository-governance concern. Separate maintenance of governed repository records from production obligations of the adopting product.

### Roles and Actor Assignment Standard

- Source: [docs/standards/roles-and-actor-assignment.md](../../docs/standards/roles-and-actor-assignment.md).
- Scope evidence: “This standard governs Roles, Actors, Assignments, accountability, and authority boundaries. It keeps a Role as a responsibility, an Actor as the entity performing work, and an Assignment as an Actor fulfilling a Role. The model is independent of actors, providers, tools, organizational structure, and implementation technology. It is usable by an individual, teams, human-only execution, AI-assisted execution, authorized automated execution, and future multi-agent execution; it remains fully usable without AI. This s [excerpt; see full source]”
- Assessment: Candidate common concern. The stated decision/evidence concern is a reuse candidate; assess cross-type semantics and ownership under #301–#303.

### Rollback Strategy

- Source: [docs/standards/rollback-strategy.md](../../docs/standards/rollback-strategy.md).
- Scope evidence: “This standard governs rollback decisions, preparation, execution, and evidence. It does not prescribe a specific recovery mechanism or replace incident management.”
- Assessment: Conditional/contextual concern. Assess the declared trigger, decision context, and lifecycle links; neutrality of tooling alone does not prove universal application.

### Security, Privacy, and Data Governance Standard

- Source: [docs/standards/security-privacy-data-governance.md](../../docs/standards/security-privacy-data-governance.md).
- Scope evidence: “This standard applies when a product, repository, automation, or AI capability handles systems, users, data, credentials, or external effects. It does not prescribe a security framework, compliance regime, provider, or tool.”
- Assessment: Conditional/contextual concern. Assess the declared trigger, decision context, and lifecycle links; neutrality of tooling alone does not prove universal application.

### Standards Relationship Map

- Source: [docs/standards/standards-relationship-map.md](../../docs/standards/standards-relationship-map.md).
- Scope evidence: “This map covers principal ownership and dependency relationships among published Playbook standards. It does not define their detailed rules or create additional dependencies.”
- Assessment: Navigational catalog. Navigation delegates semantics to primary owners; catalog membership is not an applicability decision.

### System Context

- Source: [docs/standards/system-context.md](../../docs/standards/system-context.md).
- Scope evidence: “This standard is independent of diagram notation, architecture framework, and implementation technology.”
- Assessment: Conditional/contextual concern. Assess the declared trigger, decision context, and lifecycle links; neutrality of tooling alone does not prove universal application.

### Technical Debt Management

- Source: [docs/standards/technical-debt-management.md](../../docs/standards/technical-debt-management.md).
- Scope evidence: “Technical debt is a condition that creates future cost, risk, reduced adaptability, or constrained quality because of a current technical decision, gap, or deferred improvement. This standard does not treat every non-preferred implementation as debt.”
- Assessment: Conditional/contextual concern. Assess the declared trigger, decision context, and lifecycle links; neutrality of tooling alone does not prove universal application.

### Terminology Standard

- Source: [docs/standards/terminology-standard.md](../../docs/standards/terminology-standard.md).
- Scope evidence: “This standard governs term ownership, naming, capitalization, aliases, and changes to terminology. It does not replace the definition of a governed concept: the document that owns a concept remains its primary source of truth. The Glossary is the discoverable catalog of approved terms; it is maintained separately from this governance standard.”
- Assessment: Candidate common concern. The stated decision/evidence concern is a reuse candidate; assess cross-type semantics and ownership under #301–#303.

### Testing Strategy

- Source: [docs/standards/testing-strategy.md](../../docs/standards/testing-strategy.md).
- Scope evidence: “This standard is independent of test framework, language, platform, and automation provider.”
- Assessment: Candidate common concern. The stated decision/evidence concern is a reuse candidate; assess cross-type semantics and ownership under #301–#303.

### User Flows

- Source: [docs/standards/user-flows.md](../../docs/standards/user-flows.md).
- Scope evidence: “This standard is independent of diagram notation, interface technology, and delivery method.”
- Assessment: Conditional/contextual concern. Assess the declared trigger, decision context, and lifecycle links; neutrality of tooling alone does not prove universal application.

### User Journey

- Source: [docs/standards/user-journey.md](../../docs/standards/user-journey.md).
- Scope evidence: “This standard is independent of journey-map format, research method, or interface technology.”
- Assessment: Conditional/contextual concern. Assess the declared trigger, decision context, and lifecycle links; neutrality of tooling alone does not prove universal application.

### Users

- Source: [docs/standards/users.md](../../docs/standards/users.md).
- Scope evidence: “This document defines Users independently of any persona framework or product management methodology.”
- Assessment: Candidate common concern. The stated decision/evidence concern is a reuse candidate; assess cross-type semantics and ownership under #301–#303.

### UX Artifacts

- Source: [docs/standards/ux-artifacts.md](../../docs/standards/ux-artifacts.md).
- Scope evidence: “This standard applies to UX artifacts and their relationship to the repository-wide Artifact Standard.”
- Assessment: Conditional/contextual concern. Assess the declared trigger, decision context, and lifecycle links; neutrality of tooling alone does not prove universal application.

### UX Information Architecture

- Source: [docs/standards/ux-information-architecture.md](../../docs/standards/ux-information-architecture.md).
- Scope evidence: “This standard concerns product experience information architecture. It is distinct from the repository's Documentation Information Architecture.”
- Assessment: Conditional/contextual concern. Assess the declared trigger, decision context, and lifecycle links; neutrality of tooling alone does not prove universal application.

### UX Validation

- Source: [docs/standards/ux-validation.md](../../docs/standards/ux-validation.md).
- Scope evidence: “This standard is independent of research method, participant count, tooling, and product type.”
- Assessment: Candidate common concern. The stated decision/evidence concern is a reuse candidate; assess cross-type semantics and ownership under #301–#303.

### UX Vision

- Source: [docs/standards/ux-vision.md](../../docs/standards/ux-vision.md).
- Scope evidence: “This document defines UX Vision independently of a design system, interface technology, or specific design method.”
- Assessment: Conditional/contextual concern. Assess the declared trigger, decision context, and lifecycle links; neutrality of tooling alone does not prove universal application.

### Versioning Standard

- Source: [docs/standards/versioning-standard.md](../../docs/standards/versioning-standard.md).
- Scope evidence: “This standard covers version meaning and change communication for a repository or product. It does not prescribe a release cadence or distribution platform.”
- Assessment: Conditional/contextual concern. Assess the declared trigger, decision context, and lifecycle links; neutrality of tooling alone does not prove universal application.

### Wireframes

- Source: [docs/standards/wireframes.md](../../docs/standards/wireframes.md).
- Scope evidence: “This standard is independent of design tooling, visual style, and implementation technology.”
- Assessment: Conditional/contextual concern. Assess the declared trigger, decision context, and lifecycle links; neutrality of tooling alone does not prove universal application.

### Work Item Taxonomy

- Source: [docs/standards/work-item-taxonomy.md](../../docs/standards/work-item-taxonomy.md).
- Scope evidence: “This document defines the classification dimensions used to describe work items throughout the product development lifecycle. The taxonomy is independent of any specific project management platform and may be implemented using labels, custom fields, issue types, or equivalent mechanisms.”
- Assessment: Lifecycle-dependent representation. Current lifecycle or classification sources determine meaning; do not generalize field values or positions before #304.

### Work Item Types

- Source: [docs/standards/work-item-types.md](../../docs/standards/work-item-types.md).
- Scope evidence: “This document defines the semantics of each work item type adopted by the Playbook. It also explains how these concepts map to issue types provided by different project management platforms, while keeping the Playbook independent of any specific tool.”
- Assessment: Lifecycle-dependent representation. Current lifecycle or classification sources determine meaning; do not generalize field values or positions before #304.

### Work Management Standard

- Source: [docs/standards/work-management.md](../../docs/standards/work-management.md).
- Scope evidence: “This standard governs the transversal management of work across the Product Development Playbook. Work management is independent from Lifecycle Phase and applies across lifecycle phases. The model is framework-independent. It does not require Scrum, Kanban, Sprints, iterations, estimates, ceremonies, work-in-progress limits, or continuous delivery. It does not require AI and does not prescribe a provider, tool, platform, or organizational structure. Existing authoritative standards remain authoritative for the conc [excerpt; see full source]”
- Assessment: Candidate common concern. The stated decision/evidence concern is a reuse candidate; assess cross-type semantics and ownership under #301–#303.

### AI Collaboration Example

- Source: [examples/ai-collaboration-example.md](../../examples/ai-collaboration-example.md).
- Scope evidence: “Illustrate how the same Playbook work item can be completed manually, with AI assistance, or through authorized automation while preserving accountable decisions, review, validation, and a manual fallback. This fictional example is provider-agnostic. It does not prescribe a model, prompt, integration, product architecture, or automation platform.”
- Assessment: Supporting representation. Template/example remains supporting material; its selected artifacts and fictional scenarios do not establish universal requirements.

### End-to-end Playbook Example

- Source: [examples/end-to-end-playbook-example.md](../../examples/end-to-end-playbook-example.md).
- Scope evidence: “Illustrate a fictional product increment across the complete lifecycle. It is provider-agnostic and illustrative.”
- Assessment: Supporting representation. Template/example remains supporting material; its selected artifacts and fictional scenarios do not establish universal requirements.

### Executable Protocol Reference Example

- Source: [examples/executable-protocol-reference-example.md](../../examples/executable-protocol-reference-example.md).
- Scope evidence: “## Purpose and scope Illustrate one fictional, bounded software-product increment across Foundation through Maintenance in human-only, AI-assisted, and partially capable Integration contexts. This is an Example, not a prescribed workflow, application, adapter, provider guide, or multi-agent framework. No described research, configuration, implementation, approval, or release actually occurred. Use the Master Execution Checklist for activity navigation and its record template for contextual evidence. The existing ch [excerpt; see full source]”
- Assessment: Supporting representation. Template/example remains supporting material; its selected artifacts and fictional scenarios do not establish universal requirements.

### Master Execution Checklist Walkthrough

- Source: [examples/master-execution-checklist-walkthrough.md](../../examples/master-execution-checklist-walkthrough.md).
- Scope evidence: “Validate the navigational coverage of the Master Execution Checklist through one fictional, bounded product increment. This example illustrates source ownership and evidence selection; it does not report a real implementation, user study, deployment, or release.”
- Assessment: Supporting representation. Template/example remains supporting material; its selected artifacts and fictional scenarios do not establish universal requirements.

### Product Definition Example

- Source: [examples/product-definition-example.md](../../examples/product-definition-example.md).
- Scope evidence: “Demonstrate how the Product Vision, Problem Statement, Users, Outcomes, Product Scope, and Product Backlog can form one coherent product definition. This fictional example illustrates the standards; it is not a governing rule, implementation specification, or delivery commitment.”
- Assessment: Supporting representation. Template/example remains supporting material; its selected artifacts and fictional scenarios do not establish universal requirements.

### AI-assisted Work Evidence Template

- Source: [templates/ai-assisted-work-evidence.md](../../templates/ai-assisted-work-evidence.md).
- Scope evidence: “Use this template for material AI-assisted or authorized AI-automated work. - Work item and purpose: - Accountable owner: - Authorized context and data boundary: - AI task:”
- Assessment: Supporting representation. Template/example remains supporting material; its selected artifacts and fictional scenarios do not establish universal requirements.

### Playbook Conformance Declaration Template

- Source: [templates/conformance-declaration.md](../../templates/conformance-declaration.md).
- Scope evidence: “Use this template to record adoption of Repository Standards. ## Repository and owner - Repository purpose: - Accountable owner:”
- Assessment: Supporting representation. Template/example remains supporting material; its selected artifacts and fictional scenarios do not establish universal requirements.

### Decision Record Template

- Source: [templates/decision-record.md](../../templates/decision-record.md).
- Scope evidence: “Use this template for a material decision. It complements the applicable governing standard. ## Context ## Decision”
- Assessment: Supporting representation. Template/example remains supporting material; its selected artifacts and fictional scenarios do not establish universal requirements.

### Exception Record Template

- Source: [templates/exception-record.md](../../templates/exception-record.md).
- Scope evidence: “Use this template when a Repository Standards requirement cannot be followed. - Rule or standard: - Affected scope: - Reason: - Known impact or risk:”
- Assessment: Supporting representation. Template/example remains supporting material; its selected artifacts and fictional scenarios do not establish universal requirements.

### Foundation Adoption Checklist Template

- Source: [templates/foundation-adoption-checklist.md](../../templates/foundation-adoption-checklist.md).
- Scope evidence: “Use this checklist with the Foundation Phase. - [ ] Repository purpose, owner, and access are recorded. - [ ] Repository Standards and applicable detailed standards are adopted. - [ ] Work classification and planning model are usable. - [ ] Documentation language, entry point, and navigation are established.”
- Assessment: Supporting representation. Template/example remains supporting material; its selected artifacts and fictional scenarios do not establish universal requirements.

### Master Execution Checklist Record

- Source: [templates/master-execution-checklist-record.md](../../templates/master-execution-checklist-record.md).
- Scope evidence: “Provide reusable starting material for recording a bounded application of the Master Execution Checklist. This template is non-normative and does not establish workflow states, a schema, or additional completion requirements.”
- Assessment: Supporting representation. Template/example remains supporting material; its selected artifacts and fictional scenarios do not establish universal requirements.

### Provider Implementation Guide

- Source: [templates/provider-implementation-guide.md](../../templates/provider-implementation-guide.md).
- Scope evidence: “Use this non-normative template to document an optional provider mapping under the Provider Implementation Guide Standard. Replace the instructions with scoped evidence and links. Completing the template does not establish support, Authority, configuration, Verification, or Conformance.”
- Assessment: Supporting representation. Template/example remains supporting material; its selected artifacts and fictional scenarios do not establish universal requirements.

## Coverage, uncertainty, and follow-up

Document coverage is complete for the stated 95-source Markdown baseline. This does not assert exhaustive domain knowledge of every future product type, or prove that every technology-neutral sentence is universally applicable. The material findings identify the semantic decisions needed; the source inventory makes their evidence and owners auditable.

Repository tools remain supporting implementations: [exporter requirements in README](../../README.md#audit-exporter), source-controlled workflow/configuration, and optional native-provider mappings are distinct from production needs. Their implementation dependencies remain unchanged.

No requirement, lifecycle order, Role assignment, applicability state, exception, type taxonomy, or provider model is created or weakened here. Classification uncertainty and cross-type differences proceed to [#301](https://github.com/giaholic-dev/product-development-playbook/issues/301), [#302](https://github.com/giaholic-dev/product-development-playbook/issues/302), [#303](https://github.com/giaholic-dev/product-development-playbook/issues/303), and [#304](https://github.com/giaholic-dev/product-development-playbook/issues/304) in the approved dependency order.

## Review and reassessment

The #300 change review records the assessed baseline, scope, evidence, findings, limitations, and approving maintainer. Reassess affected entries when primary sources, lifecycle applicability, type semantics, or ownership decisions change; retain this baseline as historical evidence rather than silently overwriting its meaning. Approval of this research record does not approve a universal core or specialization.

## References

- [Product-type Architecture Plan](product-type-architecture-plan.md)
- [Roles and Actor Assignment Standard](../standards/roles-and-actor-assignment.md)
- [Artifact Standard](../standards/artifact-standard.md)
- [Terminology Standard](../standards/terminology-standard.md)
