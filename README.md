# Product Development Playbook

A practical, technology-agnostic playbook for planning, building, releasing, and evolving software products.

## What is it?
This repository answers one fundamental question:

> "If I have an idea today, how does it become a product?"

The Product Development Playbook is a structured framework for defining, building, releasing, and evolving software products.

It defines the concepts, lifecycle, practices, and standards used to guide software product development from inception to long-term maintenance.

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
7. [Product Vision](docs/standards/product-vision.md)
8. [Problem Statement](docs/standards/problem-statement.md)
9. [Users](docs/standards/users.md)
10. [Outcomes](docs/standards/outcomes.md)
11. [Product Scope](docs/standards/product-scope.md)
12. [Product Backlog](docs/standards/product-backlog.md)

The UX, Architecture, Development, Release, and Maintenance phase documents are planned; they are not available yet. The [Documentation Navigation Standard](docs/standards/documentation-navigation.md) describes how entry points, related links, and link checks should work. The audit exporter is optional technical reading, not a prerequisite.

## Lifecycle

The Product Development Playbook defines a complete conceptual lifecycle with seven ordered phases:

1. Foundation
2. Product
3. UX
4. Architecture
5. Development
6. Release
7. Maintenance

Progression is ordered but not irreversible: new evidence or changes may require revisiting an earlier phase. Only Foundation and Product have lifecycle documents today; the remaining phase documents are planned. The current phase and completion status of this repository are reported separately below.

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

### Product

- [Product Vision](docs/standards/product-vision.md)
- [Problem Statement](docs/standards/problem-statement.md)
- [Users](docs/standards/users.md)
- [Outcomes](docs/standards/outcomes.md)
- [Product Scope](docs/standards/product-scope.md)
- [Product Backlog](docs/standards/product-backlog.md)

## Current Status

Current version: **v0.2.0**

Current phase: **Product**

Lifecycle progress:

- ✅ Foundation
- ✅ Product
- ⏳ UX
- ⏳ Architecture
- ⏳ Development
- ⏳ Release
- ⏳ Maintenance

---
*For more details on the process lifecycle, check the [Product Phase](docs/lifecycle/02-product.md).*
