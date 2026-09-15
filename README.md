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

## Lifecycle

The Product Development Playbook is organized into seven sequential phases:

1. Foundation
2. Product
3. UX
4. Architecture
5. Development
6. Release
7. Maintenance

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
- [Work Item Taxonomy](docs/standards/work-item-taxonomy.md)
- [Work Item Types](docs/standards/work-item-types.md)
- [Project Views](docs/standards/project-views.md)

### Documentation

- [Documentation Information Architecture](docs/standards/documentation-information-architecture.md)

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
