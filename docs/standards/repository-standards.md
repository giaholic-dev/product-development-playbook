# Repository Standards

## Purpose

Define the repository-level standards that ensure consistency, maintainability, and predictability across all software products adopting the Product Development Playbook.

## Scope

This document defines the mandatory repository standards adopted by projects following the Product Development Playbook.

These standards establish consistent rules for repository organization, documentation, version control, branching, commits, pull requests, and versioning.

Technology-specific implementation details are intentionally out of scope.

## Repository Structure

Every repository adopting the Product Development Playbook should follow a clear and predictable structure.

Unless justified by the project's nature, repositories should organize their content into the following categories:

- Documentation
- Source code
- Tests
- Configuration
- Automation
- Templates
- Examples

Projects may extend this structure when necessary, provided the overall organization remains consistent and easy to navigate.

## Documentation Standards

Documentation is a first-class artifact of the product development process.

All project documentation must:

- Be written in clear and consistent language.
- Have a single, well-defined responsibility.
- Avoid duplicating information available elsewhere.
- Be kept up to date as the project evolves.
- Favor references over repetition when linking related concepts.

## Git Standards

Git is the official version control system adopted by the Product Development Playbook.

All changes must be tracked through Git, preserving a complete, traceable, and auditable project history.

Repositories should favor small, incremental, and reversible changes over large, monolithic updates.

## Branch Strategy

The default branch represents the stable state of the project.

All changes should be developed in short-lived branches and integrated through Pull Requests.

Branch names should clearly communicate the purpose of the work being performed.

Repositories should adopt the following branch prefixes:

- `feature/`
- `fix/`
- `docs/`
- `refactor/`
- `test/`
- `chore/`
- `release/`

## Commit Convention

The Product Development Playbook adopts the Conventional Commits specification as the default commit convention.

Commit messages should:

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

All changes must be integrated through Pull Requests.

Every Pull Request should:

- Focus on a single logical change.
- Include a clear summary of the proposed changes.
- Describe the main modifications introduced.
- Reference related process artifacts when applicable (e.g., phase, issue, ADR, milestone).
- Be reviewed before merging into the default branch.
- Be merged only after successful review.
  
## Versioning Strategy

Projects should adopt Semantic Versioning (SemVer) as the default versioning strategy.

Version numbers follow the format:

`MAJOR.MINOR.PATCH`

Where:

- **MAJOR** — Incompatible or breaking changes.
- **MINOR** — Backward-compatible features and enhancements.
- **PATCH** — Backward-compatible bug fixes and maintenance changes.

Alternative versioning strategies may be adopted when justified by the project's nature.

## References

- `docs/lifecycle/01-foundation.md`
