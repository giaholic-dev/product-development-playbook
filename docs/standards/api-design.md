# API Design

## Purpose

Define how a product documents interfaces through which systems, components, or actors exchange capabilities and information.

## Scope

This standard is independent of protocol, transport, framework, provider, and API style.

## Definition

API Design is the decision-oriented definition of an interface's purpose, consumers, capabilities, contracts, information exchange, constraints, and lifecycle expectations.

## Rules

An API decision MUST identify the interface purpose, consumers or dependents, boundary, contract, relevant data, failure or compatibility considerations, and ownership. It MUST distinguish a conceptual interface decision from a specific implementation or endpoint format.

An API MAY be synchronous, asynchronous, internal, external, human-facing, machine-facing, or another suitable interface. Material choices MUST link to Architecture Decision Records.

## Relationships

API Design refines System Context, High-Level Architecture, Component Architecture, and Data Model. It informs implementation, testing, integration, release, and operational support.

## References

- [Architecture Phase](../lifecycle/04-architecture.md)
- [System Context](system-context.md)
- [High-Level Architecture](high-level-architecture.md)
- [Component Architecture](component-architecture.md)
- [Data Model](data-model.md)
- [Architecture Decision Records](architecture-decision-records.md)
