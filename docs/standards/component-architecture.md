# Component Architecture

## Purpose

Define how a product describes internal components and their responsibilities when that detail is needed for an architecture or implementation decision.

## Scope

This standard is independent of programming language, framework, module system, and deployment topology.

## Definition

Component Architecture is the decision-oriented description of the internal units that carry major system responsibilities, their interfaces, dependencies, and collaboration boundaries.

## Rules

A Component Architecture MUST identify the decision scope, relevant components, their responsibilities, material interfaces or dependencies, and applicable constraints. It MUST remain consistent with the High-Level Architecture and related Architecture Decision Records.

It MAY use modules, services, packages, bounded contexts, libraries, or another suitable unit. It does not require a fixed decomposition pattern or a complete implementation design.

## Relationships

Component Architecture refines High-Level Architecture. It informs Data Model, implementation work, testing boundaries, and technical-debt decisions.

## References

- [Architecture Phase](../lifecycle/04-architecture.md)
- [High-Level Architecture](high-level-architecture.md)
- [Architecture Decision Records](architecture-decision-records.md)
- [Work Item Types](work-item-types.md)
