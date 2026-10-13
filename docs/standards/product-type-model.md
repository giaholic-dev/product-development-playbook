# Product Type Model

## Purpose

Define product-type meanings and relationships needed to assess core and specialization boundaries without turning technology, provider, Actor, or artifact classifications into product types.

## Scope

This standard owns Product Type, Product Context, and Product Composition as conceptual distinctions. It does not define a universal lifecycle, applicability states, normative specializations, a closed type catalog, implementation architecture, or machine schema. Existing software-product lifecycle and standards retain their governing scope until explicitly revised.

The [assumption inventory](../practices/product-type-assumption-inventory.md) supplies current-state evidence. Core/specialization ownership, requirement applicability, and lifecycle assessment remain separate work under [#302](https://github.com/giaholic-dev/product-development-playbook/issues/302), [#303](https://github.com/giaholic-dev/product-development-playbook/issues/303), and [#304](https://github.com/giaholic-dev/product-development-playbook/issues/304).

## Definitions

### Product Type

Product Type describes the nature of the intended product offering in the decision scope being assessed, including what is provided and how its value is realized. It is distinct from the technology used to produce it or the medium used to document it.

A product-type description MUST identify its product boundary, intended offering or outcome, classification rationale, and material uncertainty. It MUST NOT infer governing requirements solely from a type label. Existing requirements remain authoritative; future applicability decisions must cite their governing source.

### Product Context

Product Context is the set of circumstances relevant to a product decision, such as intended users, operating setting, delivery conditions, constraints, risk, and obligations. Context may affect a decision without changing Product Type.

Material context assumptions MUST be identifiable and distinguishable from observed evidence. A type label MUST NOT conceal context-specific uncertainty or imply that all products sharing that label have identical requirements.

### Product Composition

Product Composition describes how materially distinct offerings or components relate within an assessed product boundary. It identifies constituent scopes and their relationships; it does not require a particular architecture or decomposition method.

When composition materially affects a decision, its record MUST identify relevant constituent boundaries, interactions or dependencies, and unresolved concerns. Classification of a constituent MUST NOT automatically classify the whole product or determine obligations for every other constituent.

## Open descriptive categories

The following descriptions are non-exhaustive reference categories. They support assessment, not a mandatory enumeration or adopted specialization:

- Software: an offering whose intended scope centers on executable digital behavior or functionality.
- Physical: an offering whose intended scope centers on a tangible item and its material characteristics or use.
- Service: an offering whose intended scope centers on performance of activities or provision of an ongoing capability for a recipient.
- Hybrid: an offering whose material value in the assessed scope depends on a combination of distinguishable software, physical, or service concerns.

These descriptions can overlap by scope. Hosted software may provide executable functionality and an operated service; that does not force an exclusive choice or make every software tool a service product. A physical item produced with software tooling does not become Hybrid solely because the production tool is digital. Record the offering boundary and rationale rather than resolving ambiguity through a tool label.

Additional descriptions are permitted when their meaning, scope, relationships, and rationale remain explicit. Unknown or disputed classification MUST remain explicit when material; it is not proof of inapplicability or permission to omit a requirement.

## Independent dimensions

- Technology describes implementation or production means. A language, material, cloud platform, or manufacturing technique is not itself Product Type.
- Provider identifies an external system or service offering capabilities under the [Integration Standard](integration-standard.md). Selecting it does not classify the resulting product.
- Delivery framework or work approach organizes how work is managed under [Work Management](work-management.md); it does not define the offering.
- Actor identifies an entity performing work under [Roles and Actor Assignment](roles-and-actor-assignment.md). Human, AI, team, or automated execution does not determine Product Type.
- Artifact Type classifies inspectable evidence under the [Artifact Standard](artifact-standard.md). Documentation, source, or a prototype may evidence different product types; a source file alone does not classify the complete offering.
- Lifecycle Phase and Work Type retain their existing meanings under [Work Item Taxonomy](work-item-taxonomy.md) and [Work Item Types](work-item-types.md). Product Type does not rename or replace either dimension.

Records MUST preserve these distinctions when the dimensions materially affect a decision. No new mandatory tracking field or storage format is established here.

## Composition and hybrid boundaries

For a hybrid or composite scope, examine the relationships that matter to intended value, quality, delivery, operation, and evidence. Separate material product constituents from incidental tools and providers. A combination of components MUST NOT be interpreted as automatic adoption of every possible requirement or as permission to select the least restrictive constituent rule.

Unresolved cross-constituent requirements and ownership MUST remain traceable for the governing boundary and applicability decisions. This model does not determine precedence, inheritance, waiver, conflict-resolution policy, or specialization conformance; those belong to their approved primary owners.

## Evidence and changes

A material product-type assessment MUST retain its scope, rationale, relevant context and composition, source evidence, unresolved questions, and responsible decision record under existing [Artifact](artifact-standard.md) and [Roles](roles-and-actor-assignment.md) rules. Revise the assessment when the offering boundary or material evidence changes, preserving the reason and affected records.

Reclassification does not automatically change lifecycle progression, Authority, readiness, Completion, or governing requirement strength. Any affected applicability or migration decision requires its own authoritative treatment. The current repository's Git baseline remains unchanged.

## Non-normative scenario review

- Software increment: a library reservation-status offering centers on executable digital behavior. Its hosted provider, programming language, human/AI Contributors, and documentation Artifacts remain separate dimensions. Existing software lifecycle requirements are preserved.
- Physical item: a reusable container centers on tangible characteristics and use. Digital design tools do not by themselves make the offering Hybrid. Material production, quality, and delivery concerns remain open for applicable governing assessment; the model does not map them into coding requirements.
- Service: an appointment assistance offering centers on performed activities for recipients. A website used to request it may be a tool or a product constituent depending on the assessed boundary and intended value. Context and evidence decide the distinction; no universal phase order is inferred.
- Hybrid: a monitored device offering depends materially on a physical device, executable behavior, and an operated monitoring service. The assessment records constituent scopes and dependencies. One constituent's classification does not establish all obligations or resolve cross-boundary responsibility.

These conceptual scenarios test distinctions, not real product delivery or normative specialized methods. Ambiguous cases retain explicit rationale or uncertainty rather than forcing a closed label.

## References

- [Product-type Architecture Plan](../practices/product-type-architecture-plan.md)
- [Product Scope](product-scope.md)
- [Terminology Standard](terminology-standard.md)
- [Artifact Standard](artifact-standard.md)
- [Roles and Actor Assignment Standard](roles-and-actor-assignment.md)
- [Work Management Standard](work-management.md)
- [Provider-independent Integration Standard](integration-standard.md)
