# Repository Standards

## Purpose

Define the repository-level standards that ensure consistency, maintainability, and predictability across all software products adopting the Product Development Playbook.

## Scope

This document defines the baseline repository standards adopted by projects following the Product Development Playbook.

These standards establish consistent rules for repository organization, documentation, version control, branching, commits, pull requests, and versioning.

The Playbook remains independent of programming languages, frameworks, product architectures, and repository-hosting vendors. It explicitly adopts Git as its version control baseline. Platform-specific behavior is implementation guidance unless a project selects that platform and the relevant mapping identifies a requirement.

## Normative Language

The keywords `MUST`, `SHOULD`, and `MAY` define the strength of a rule in this document:

- **MUST** indicates a requirement for conformance with the Playbook.
- **SHOULD** indicates the expected default. A project may deviate when the exception is explicitly recorded.
- **MAY** indicates an optional practice.

Statements that do not use a normative keyword are explanatory and do not create an independent conformance requirement.

A recorded exception MUST identify:

- The rule being excepted
- The reason for the exception
- The affected scope
- The known impact or risk
- The person or role responsible for reviewing it
- The condition or date that triggers reassessment

An exception changes only the identified project implementation. It does not modify the Playbook standard.

## Standards Layers

Repository standards are organized into three layers:

1. **Conceptual rules** define portable repository responsibilities and expected outcomes independently of programming language, framework, architecture, or hosting vendor.
2. **Git baseline rules** define version control conventions explicitly adopted by the Playbook.
3. **Platform mappings** explain how conceptual and Git rules are implemented in a specific service, such as GitHub.

Platform mappings MUST preserve the meaning of the rules they implement. A platform-specific mechanism becomes a project requirement only when the project adopts that platform and the mapping marks the mechanism as required.

## Repository Structure

Every repository adopting the Product Development Playbook MUST provide a clear and predictable structure appropriate to its purpose.

Repository structure is defined through content responsibilities rather than mandatory directory names. Applicable responsibilities include:

- Documentation
- Source code
- Tests
- Configuration
- Automation
- Templates
- Examples

A repository MUST include only the responsibilities needed for its purpose. It MUST NOT create empty directories or placeholder content solely to reproduce this list.

The root documentation MUST identify the repository's purpose, describe its top-level organization, and provide navigation to its primary content.

Directory names and nesting MAY vary across documentation repositories, applications, services, libraries, and other repository types. The chosen structure SHOULD keep related content together and make each applicable responsibility easy to locate.

Projects MAY add responsibilities or extend the structure when necessary. Any deviation from a `MUST` rule requires a recorded exception as defined in this document.

## Documentation Standards

Documentation is a first-class artifact of the product development process.

All project documentation MUST:

- Be written in clear and consistent language.
- Have a single, well-defined responsibility.
- Avoid duplicating information available elsewhere.
- Be kept up to date as the project evolves.
- Favor references over repetition when linking related concepts.

## Conceptual Standards

Conceptual standards SHOULD generally follow a consistent document structure whenever applicable.

The recommended structure is:

- Purpose
- Scope
- Definition
- Conceptual Model
- Characteristics
- Relationships
- References

Documents MAY omit sections that are not applicable to the concept being defined.

## Git Standards

Git is the official version control system adopted by the Product Development Playbook.

All changes MUST be tracked through Git, preserving a complete, traceable, and auditable project history.

Repositories SHOULD favor small, incremental, and reversible changes over large, monolithic updates.

## Branch Strategy

The default branch represents the stable state of the project.

All changes SHOULD be developed in short-lived branches and integrated through Pull Requests.

Branch names SHOULD clearly communicate the purpose of the work being performed.

Repositories SHOULD adopt the following branch prefixes:

- `feature/`
- `fix/`
- `docs/`
- `refactor/`
- `test/`
- `chore/`
- `release/`

## Commit Convention

The Product Development Playbook adopts the Conventional Commits specification as the default commit convention.

Commit messages SHOULD:

- Be written in the imperative mood.
- Describe a single logical change.
- Be concise and meaningful.
- Follow the `<type>: <description>` format.

Common commit types include:

- `feat`
- `fix`
- `docs`
- `refactor`
- `test`
- `chore`
- `build`
- `ci`
- `perf`

## Pull Request Standard

All changes MUST be integrated through Pull Requests.

Every Pull Request SHOULD:

- Focus on a single logical change.
- Include a clear summary of the proposed changes.
- Describe the main modifications introduced.
- Reference related process artifacts when applicable (e.g., phase, issue, ADR, milestone).
- Be reviewed before merging into the default branch.
- Be merged only after successful review.

## Versioning Strategy

Projects SHOULD adopt Semantic Versioning (SemVer) as the default versioning strategy.

Version numbers follow the format:

`MAJOR.MINOR.PATCH`

Where:

- **MAJOR** — Incompatible or breaking changes.
- **MINOR** — Backward-compatible features and enhancements.
- **PATCH** — Backward-compatible bug fixes and maintenance changes.

Alternative versioning strategies MAY be adopted when justified by the project's nature.

## References

- `docs/lifecycle/01-foundation.md`
- `docs/standards/work-item-taxonomy.md`
- `docs/standards/work-item-types.md`
- `docs/standards/project-views.md`
