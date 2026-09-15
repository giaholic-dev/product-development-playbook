# Documentation Style Guide

## Purpose

Define the detailed writing and Markdown conventions for documentation adopting the Product Development Playbook.

This guide expresses the repository-level documentation contract. It does not replace requirements for documentation ownership, accuracy, navigation, or conformance.

## Scope

This guide covers writing and Markdown conventions for maintained Playbook documentation. It does not replace rules for documentation ownership, navigation, or repository governance.

## Language and Audience

A repository MUST declare its primary documentation language. This Playbook uses English.

Write for the reader who must make, apply, or verify a decision. Prefer direct language, concrete nouns, short paragraphs, and one meaning per sentence. Define a term before relying on it when its meaning is not evident from the surrounding standard.

## Normative Language

Use the terms defined by [Repository Standards](repository-standards.md) consistently:

- **MUST** expresses a mandatory requirement.
- **SHOULD** expresses a recommendation with a documented reason when not followed.
- **MAY** expresses a permitted option.

Do not use “must,” “should,” “recommended,” or equivalent wording casually when a different normative strength is intended.

## Document Structure

A conceptual standard MUST contain:

1. a title;
2. **Purpose**;
3. **Scope**; and
4. **References** when another repository document owns a related rule.

Use only the sections that are needed to make a document usable, such as Principles, Definitions, Rules, Process, Examples, Inputs, Outputs, Evidence, or Exceptions. When an expected section is intentionally omitted, the remaining content MUST still make the document's responsibility and completion evidence clear.

Lifecycle documents follow their lifecycle template and MAY add the sections needed for the phase. Templates and examples identify their intended use and source standard.

## Headings and Text

- Use sentence case for headings and concise descriptive names.
- Start at one H1 title and use headings in logical order; do not skip levels for visual styling.
- Use present tense for enduring rules and future tense only for planned work.
- Distinguish current, planned, and historical state explicitly.
- Avoid unexplained acronyms; spell them out on first relevant use.
- Use **bold** only for a term or requirement that benefits from emphasis. Use `code` for literal paths, commands, field names, and identifiers.

## Lists, Tables, and Examples

Use a list when order is not important, and a numbered list when the reader must follow a sequence. Keep list items grammatically parallel.

Use a table when readers need to compare the same dimensions across multiple items. Do not use a table solely for layout.

Examples MUST be labeled as examples. They illustrate a rule and MUST NOT silently add requirements or override the governing standard.

## Links and References

Use relative Markdown links for repository documents. Link to the document that owns the rule rather than copying its detailed content.

Links MUST resolve from their containing file. A document that refers to planned material MUST identify it as planned rather than presenting it as available.

## File Names and Markdown

Use lowercase, hyphen-separated file names ending in `.md`. Name a document for its stable responsibility, not its temporary implementation task.

Keep Markdown portable: use standard headings, lists, tables, fenced code blocks, and links. Avoid vendor-specific formatting unless the document explicitly owns a platform mapping.

## Editorial Review Checklist

Before merging a documentation change, verify:

- the primary language and terminology are consistent;
- the document's purpose, scope, and owner are clear;
- normative terms carry intentional strength;
- current, planned, and historical state are not conflated;
- internal links resolve;
- tables and examples clarify rather than redefine rules;
- headings, lists, and file names follow this guide; and
- the change has the evidence required by [Repository Standards](repository-standards.md).

## References

- [Repository Standards](repository-standards.md)
- [Terminology Standard](terminology-standard.md)
- [Documentation Information Architecture](documentation-information-architecture.md)
- [Documentation Navigation Standard](documentation-navigation.md)
