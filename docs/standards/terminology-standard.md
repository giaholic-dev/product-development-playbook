# Terminology Standard

## Purpose

Define how the Product Development Playbook establishes, uses, and evolves shared terms so that lifecycle documents, standards, practices, and platform mappings remain unambiguous.

## Scope

This standard governs term ownership, naming, capitalization, aliases, and changes to terminology. It does not replace the definition of a governed concept: the document that owns a concept remains its primary source of truth. The [Glossary](glossary.md) is the discoverable catalog of approved terms; it is maintained separately from this governance standard.

## Normative Language

This document uses the normative terms defined in [Repository Standards](repository-standards.md).

## Term Ownership

A term MUST have one primary definition owner. That owner defines its meaning, boundaries, and relationships; other documents MUST link to or use the term consistently rather than redefine it.

The following ownership model applies:

| Term category | Primary owner |
| --- | --- |
| Lifecycle phase | Lifecycle phase document |
| Work item classification | Work Item Taxonomy and Work Item Types |
| View terminology | Project Views |
| Repository, documentation, and version-control concepts | Repository Standards or the dedicated standard |
| Product concepts | Their respective Product standards |
| Cross-cutting approved vocabulary | Glossary |

A planned standard MAY be named in another document only when it is clearly identified as planned and linked to its tracked issue.

## Naming and Presentation

- A defined concept MUST use one preferred name in its primary language.
- Headings, indexes, and links SHOULD use the preferred name.
- A document MAY introduce an alias only when it identifies the preferred name on first use and the alias does not create a second concept.
- Capitalization MUST be consistent within a document and across references to the same named concept.
- Terms that denote a specific lifecycle phase, standard, artifact, or field SHOULD use their approved title case when used as names; generic uses remain sentence case.
- Platform labels or field names MAY preserve the platform's own spelling when explicitly presented as a mapping.

## Ambiguity and Changes

A proposed term change MUST identify the affected primary owner, existing references, and any intended migration or compatibility wording. When an existing word has more than one meaning, the owner MUST either define a qualified name, state the distinguishing context, or remove the ambiguity.

A terminology change MUST be reviewed with the documents that consume the term. It MUST NOT silently change a lifecycle phase, work type, artifact type, or platform mapping's meaning.

## Adoption Evidence

A repository can demonstrate adoption by maintaining a glossary or equivalent index, identifying primary definition owners through navigable references, and reviewing affected documents when preferred terms or aliases change.

## References

- [Repository Standards](repository-standards.md)
- [Work Item Taxonomy](work-item-taxonomy.md)
- [Work Item Types](work-item-types.md)
- [Project Views](project-views.md)
- [Product Vision](product-vision.md)
- [Glossary](glossary.md)
