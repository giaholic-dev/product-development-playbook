# Product Development Playbook

A practical, technology-agnostic framework for turning an idea into a software product and evolving it over time.

## What is it?

> "If I have an idea today, how does it become a product?"

The Product Development Playbook defines the concepts, lifecycle, practices, and standards that guide software product development from inception to long-term maintenance.

## Vision
Enable individuals and teams to build software products through a consistent, technology-agnostic, and continuously improving development process.

## Mission
Establish a standardized and repeatable approach to software product development that can be applied across projects, teams, and technologies.

## Scope
This Playbook defines:
- Product development lifecycle
- Engineering governance
- Engineering standards
- Product management practices
- Documentation standards
- Decision-making processes

The Playbook intentionally remains independent of:
- Programming languages
- Frameworks
- Platform-specific architectures
- Tool-specific implementations

The conceptual method is independent of hosting vendors. This repository deliberately uses Git and includes GitHub mappings and supporting automation as implementation guidance, not as product-technology requirements.

## Documentation Language

The primary documentation language of this repository is English.

## Start Here

For a first reading of the Playbook, follow the documents that exist today:

1. [Foundation Phase](docs/lifecycle/01-foundation.md)
2. [Repository Standards](docs/standards/repository-standards.md)
3. [Work Item Taxonomy](docs/standards/work-item-taxonomy.md)
4. [Work Item Types](docs/standards/work-item-types.md)
5. [Project Views](docs/standards/project-views.md)
6. [Product Phase](docs/lifecycle/02-product.md)
7. [UX Phase](docs/lifecycle/03-ux.md)
8. [Architecture Phase](docs/lifecycle/04-architecture.md)
9. [Development Phase](docs/lifecycle/05-development.md)
10. [Release Phase](docs/lifecycle/06-release.md)
11. [Product Vision](docs/standards/product-vision.md)
12. [Problem Statement](docs/standards/problem-statement.md)
13. [Users](docs/standards/users.md)
14. [Outcomes](docs/standards/outcomes.md)
15. [Product Scope](docs/standards/product-scope.md)
16. [Product Backlog](docs/standards/product-backlog.md)

The Maintenance phase document is planned; it is not available yet. The [Documentation Navigation Standard](docs/standards/documentation-navigation.md) describes how entry points, related links, and link checks should work. The audit exporter is optional technical reading, not a prerequisite.

## Lifecycle

The Product Development Playbook defines a complete conceptual lifecycle with seven ordered phases:

1. Foundation
2. Product
3. UX
4. Architecture
5. Development
6. Release
7. Maintenance

Progression is ordered but not irreversible: new evidence or changes may require revisiting an earlier phase. Foundation, Product, UX, Architecture, Development, and Release currently have lifecycle documents; the Maintenance phase document is planned. The current phase and completion status of this repository are reported separately below.

## Audience
This Playbook is intended for:
- Individual developers
- Product managers
- Small teams
- Engineering teams
- Anyone building software products using an iterative process

## Repository Structure

Current directories:

- `docs/lifecycle/` — Existing lifecycle phase documents
- `docs/standards/` — Reusable repository, documentation, and product standards
- `scripts/` — Supporting implementation utilities; [export-audit.sh](scripts/export-audit.sh) is a GitHub CLI-based audit exporter requiring Git, `gh`, and `zip`. Its collection exports may be incomplete until the pagination work is finished.

Planned categories, not present in the current repository:

- `docs/core/` — Enduring philosophy, vision, mission, and principles
- `docs/practices/` — Operational guidance that applies standards without redefining them
- `templates/` — Reusable starting material
- `examples/` — Concrete applications and case studies

The [Documentation Information Architecture](docs/standards/documentation-information-architecture.md) defines these responsibilities without requiring fixed directory names or placeholder content.

## Standards

The Playbook defines reusable standards that can be adopted across software products.

### Repository & Engineering

- [Repository Standards](docs/standards/repository-standards.md)
- [Branch Workflow](docs/standards/branch-workflow.md)
- [Code Review Standard](docs/standards/code-review-standard.md)
- [Definition of Ready](docs/standards/definition-of-ready.md)
- [Definition of Done](docs/standards/definition-of-done.md)
- [Versioning Standard](docs/standards/versioning-standard.md)
- [Coding Standards](docs/standards/coding-standards.md)
- [Testing Strategy](docs/standards/testing-strategy.md)
- [Continuous Integration](docs/standards/continuous-integration.md)
- [Work Item Taxonomy](docs/standards/work-item-taxonomy.md)
- [Work Item Types](docs/standards/work-item-types.md)
- [Project Views](docs/standards/project-views.md)
- [Repository Project Field Standard](docs/standards/repository-project-field-standard.md)
- [Terminology Standard](docs/standards/terminology-standard.md)
- [Artifact Standard](docs/standards/artifact-standard.md)

### Documentation

- [Documentation Information Architecture](docs/standards/documentation-information-architecture.md)
- [Documentation Navigation Standard](docs/standards/documentation-navigation.md)
- [Documentation Style Guide](docs/standards/documentation-style-guide.md)

### Architecture

- [Architecture Vision](docs/standards/architecture-vision.md)
- [System Context](docs/standards/system-context.md)
- [Architecture Decision Records](docs/standards/architecture-decision-records.md)
- [High-Level Architecture](docs/standards/high-level-architecture.md)
- [Component Architecture](docs/standards/component-architecture.md)
- [Data Model](docs/standards/data-model.md)
- [API Design](docs/standards/api-design.md)
- [Architecture Artifacts](docs/standards/architecture-artifacts.md)

### UX

- [UX Vision](docs/standards/ux-vision.md)
- [User Journey](docs/standards/user-journey.md)
- [Personas](docs/standards/personas.md)
- [User Flows](docs/standards/user-flows.md)
- [UX Information Architecture](docs/standards/ux-information-architecture.md)
- [Wireframes](docs/standards/wireframes.md)
- [Prototypes](docs/standards/prototypes.md)
- [UX Validation](docs/standards/ux-validation.md)
- [UX Artifacts](docs/standards/ux-artifacts.md)

### Product

- [Product Vision](docs/standards/product-vision.md)
- [Problem Statement](docs/standards/problem-statement.md)
- [Users](docs/standards/users.md)
- [Outcomes](docs/standards/outcomes.md)
- [Product Scope](docs/standards/product-scope.md)
- [Product Backlog](docs/standards/product-backlog.md)

## Current Status

Latest published release: **[v0.1.0](https://github.com/giaholic-dev/product-development-playbook/releases/tag/v0.1.0)**

Development target: **Not established**

The lifecycle status below measures this repository's documentation coverage, not execution status for an external product:

- **Documented** — the phase document and its current governing artifacts exist and have been reviewed against their documented criteria.
- **Planned** — the phase is part of the lifecycle but its document is not yet available.

Latest documented phase: **Release**

Next planned phase: **Maintenance**

Lifecycle documentation:

- ✅ Foundation — documented
- ✅ Product — documented
- ✅ UX — documented
- ✅ Architecture — documented
- ✅ Development — documented
- ✅ Release — documented
- ⏳ Maintenance — planned

---
*For the latest documented lifecycle phase, see [Release Phase](docs/lifecycle/06-release.md).*
