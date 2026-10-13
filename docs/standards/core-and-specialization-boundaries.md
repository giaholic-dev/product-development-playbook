# Core and Specialization Boundaries

## Purpose

Allocate conceptual ownership between common governance, product-type specialization, and methodology-repository requirements while preserving existing software-product adoption.

## Scope

This standard owns the architectural boundary between Universal Core, Product-type Specialization, and Repository Governance. It does not move files, redefine source concepts, adopt physical/service/hybrid methods, determine every requirement's applicability, or change the existing seven-phase lifecycle. [Standards applicability work #303](https://github.com/giaholic-dev/product-development-playbook/issues/303) and [lifecycle assessment #304](https://github.com/giaholic-dev/product-development-playbook/issues/304) remain distinct decisions.

The [Product Type Model](product-type-model.md) owns Product Type, Product Context, and Product Composition. The [assumption inventory](../practices/product-type-assumption-inventory.md) is the baseline evidence for this allocation; its candidate classifications are research evidence, not automatic adoption of whole documents as universal requirements.

## Architectural concerns

### Universal Core

Universal Core is the shared conceptual governance boundary whose concerns retain their meaning independently of Product Type. It owns cross-type governance distinctions through their existing primary sources; it is not a copied rule catalog or a claim that every current standard applies to every product.

This architecture allocates the following concerns to the common semantic boundary, with their source evidence and rationale:

- Evidence, bounded judgment, proportionality, and explicit uncertainty — [Core Principles](../core/principles.md) states decision principles without selecting product architecture or provider. These are governance concerns rather than a production technique.
- Role, Actor, Assignment, Accountability, Authority, and Delegation distinctions — [Roles and Actor Assignment](roles-and-actor-assignment.md) separates responsibility from execution entities. A change of Product Type does not make participation equivalent to permission or ownership.
- Work-management distinctions — [Work Management](work-management.md) separates work management from Lifecycle Phase and framework. Its conceptual boundaries do not define a type-specific production process.
- Attempt inputs/results, authorization checks, capability checks, and evidence linkage — [Execution Protocol](execution-protocol.md) preserves traceable attempt-level meaning without establishing lifecycle or work Completion. These are distinct from a product-type-specific mechanism.
- Artifact identity, evidence ownership, and terminology ownership — [Artifact](artifact-standard.md) and [Terminology](terminology-standard.md) support different media and primary-source traceability. Evidence medium does not determine Product Type.
- Readiness and completion evidence boundaries — [Definition of Ready](definition-of-ready.md) and [Definition of Done](definition-of-done.md) own work-level conditions. The applicable substantive evidence remains contextual; a common distinction does not create universal product acceptance criteria.
- Product-type/context/composition distinctions — [Product Type Model](product-type-model.md) separates offering scope from technology, provider, Actor, and Artifact dimensions.

The listed primary owners retain their definitions and requirement strength. This allocation identifies common concerns; it does not promote every sentence, example, tool mapping, or inherited lifecycle reference in a source to a universal production requirement. Reuse MUST preserve the primary owner's meaning and identify relevant contextual requirements rather than inventing a parallel definition.

### Product-type Specialization

A Product-type Specialization is the governed boundary for type-specific meanings and application of activities, outcomes, artifacts, quality, production, delivery, and operation. It uses common governance distinctions without silently weakening or redefining their owners.

A proposed specialization MUST identify its type/context scope, owned concerns, relationships to common sources, applicable requirements, explicit gaps, and governing review evidence. It MUST distinguish a source-aligned application from a proposed change to a primary definition. A specialization MUST NOT create an implicit override, waive an applicable requirement, or treat missing evidence as inapplicability.

No physical, service, or hybrid specialization is adopted by this standard. Provider-specific guides and Actor-specific execution modes are separate dimensions; neither is a product-type specialization solely because it uses different tools or participants.

### Repository Governance

Repository Governance governs the methodology repository and other repository contexts that explicitly adopt its sources. [Repository Standards](repository-standards.md) deliberately adopts Git; [Branch Workflow](branch-workflow.md), [Code Review](code-review-standard.md), and documentation standards govern repository artifacts and changes.

Those obligations remain binding within their existing scope. They MUST NOT be represented as universally necessary physical production or service delivery capabilities solely because the Playbook itself is stored in Git. Conversely, describing a product as non-software MUST NOT silently waive the requirements governing a repository that adopts them.

## Existing software semantics and their home

The existing [seven lifecycle documents](../lifecycle/01-foundation.md), software-oriented adoption purpose in [README](../../README.md), and their currently applicable standards remain the authoritative home for existing software-product semantics. This standard establishes a conceptual boundary, not an extraction, relocation, renamed lifecycle, or completed Software Specialization artifact.

Coding/configuration, technical architecture, implementation, deployment/recovery, and software-example details are retained under their current primary sources. A later software-specialization record may make the type-specific boundary explicit only after applicable assessment and reviewed migration evidence. Requirements cannot disappear during that transition.

Product vision, users, outcomes, experience, architecture, validation, security/privacy, accessibility, release, and maintenance contain concerns that may cross types but require contextual application. Treat them under their current scopes until #303 and #304 establish the relevant decisions. Broad technical neutrality is not proof that all source requirements belong in Universal Core.

## Ownership, conflicts, and exceptions

Every governed concept MUST retain one discoverable primary definition owner. A mapping, checklist, template, or specialization cannot become a competing authority through duplication. Proposed changes to an owner follow normal repository governance and identify affected references and compatibility consequences.

For a hybrid/composite scope, identify constituent and cross-boundary concerns under the Product Type Model. Material conflicting requirements or unresolved ownership MUST have an identifiable accountable decision owner, affected source obligations, evidence, impact, and reassessment condition under existing responsibility and governance rules. Do not silently select the least restrictive rule or merge incompatible meanings.

Unresolved boundaries remain explicit for the next applicable architectural decision; they are not automatic exceptions or permission to proceed. A permitted exception must come from the governing source's existing exception process. This standard creates no universal precedence algorithm, inheritance mechanism, override hierarchy, or new exception authority.

## Non-normative scenario review

- Software: the existing status-view increment retains its current lifecycle, coding, validation, review, release, and repository obligations. Common concern allocation does not remove its substantive acceptance evidence.
- Physical: a reusable container can retain clear responsibility and evidence distinctions without assuming a source-code workflow is its production method. Material quality and delivery obligations need an applicable specialization decision rather than an invented coding equivalent.
- Service: appointment assistance can retain bounded Authority, work decisions, and evidence while performance and service-operation semantics receive contextual treatment. A request website does not make its provider mapping the universal method.
- Hybrid: a monitored device records physical, executable, and operated-service boundaries. A conflict between constituent delivery or evidence obligations is recorded with accountable treatment; no constituent automatically waives another's applicable requirement.

The scenarios validate ownership boundaries conceptually. They do not certify real products, implement specialized methods, resolve all applicability questions, or generalize the existing lifecycle.

## Integration and follow-up

The boundary sources are discoverable through the index, glossary, relationship map, and README. Directory migration and mass terminology replacement are outside this change. #303 defines applicability semantics using these ownership boundaries; #304 assesses phase/activity applicability and compatibility before any lifecycle revision. The existing [machine-representation deferral](../practices/machine-readable-execution-decision.md) remains unchanged.

## References

- [Product Type Model](product-type-model.md)
- [Product-type Architecture Plan](../practices/product-type-architecture-plan.md)
- [Roles and Actor Assignment Standard](roles-and-actor-assignment.md)
- [Repository Standards](repository-standards.md)
- [Artifact Standard](artifact-standard.md)
- [Terminology Standard](terminology-standard.md)
