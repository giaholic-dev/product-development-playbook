# Work Item Types

## Purpose

Define the standard work item types used by the Product Development Playbook and clarify how they relate to platform-specific issue types.

## Scope

This document defines the semantics of each work item type adopted by the Playbook.

It also explains how these concepts map to issue types provided by different project management platforms, while keeping the Playbook independent of any specific tool.

## Conceptual Model

The Product Development Playbook distinguishes between **Issue Type** and **Work Type**.

An **Issue Type** is defined by the project management platform and represents the operational behavior of a work item.

A **Work Type** is defined by the Playbook and represents the nature of the work being performed.

Different platforms may provide different issue types, while the Playbook Work Types remain consistent across all implementations.

## Feature

A Feature introduces new user-visible functionality or capabilities to the product.

Features deliver new value to users or stakeholders and typically originate from product planning activities.

Examples include:

- New user functionality
- New API endpoints
- New integrations
- New business capabilities

## Bug

A Bug corrects unintended behavior that causes the product to deviate from its expected functionality.

Bug work restores intended behavior without introducing new product capabilities.

Examples include:

- Application errors
- Incorrect calculations
- Broken user flows
- Unexpected system behavior

## Improvement

An Improvement enhances an existing capability without fundamentally changing its purpose.

Improvements increase quality, usability, maintainability, or efficiency while preserving the original functionality.

Improvements primarily increase product value perceived by users or stakeholders.

Examples include:

- User experience refinements
- Performance optimizations
- Accessibility improvements
- Existing workflow enhancements

## Research

Research investigates a problem, opportunity, or uncertainty before implementation decisions are made.

Research work reduces uncertainty by collecting evidence, evaluating alternatives, or validating assumptions.

Research may result in recommendations, prototypes, experiments, or documented findings, but does not directly deliver production functionality.

Examples include:

- Technical feasibility studies
- User research
- Proofs of concept
- Architecture evaluation
- Technology assessment

## Technical Debt

Technical Debt represents work that improves the internal quality of the product without directly changing its external behavior.

Technical Debt work reduces future maintenance costs, increases development efficiency, and improves the long-term sustainability of the system.

Technical Debt primarily increases internal engineering quality rather than user-visible value.

Examples include:

- Code refactoring
- Dependency updates
- Architecture improvements
- Test coverage enhancements
- Internal code cleanup

## Maintenance

Maintenance preserves the operational health, stability, and supportability of the product throughout its lifecycle.

Maintenance work keeps existing functionality operational without introducing new capabilities or significantly changing existing behavior.

Examples include:

- Routine system maintenance
- Configuration updates
- Operational support
- Monitoring improvements
- Preventive maintenance activities

## Platform Mapping

The Product Development Playbook defines Work Types independently of any project management platform.

When implemented in GitHub, Issue Types and Work Types coexist and serve different purposes.

| GitHub Issue Type | Typical Playbook Work Types |
| ----------------- | --------------------------- |
| Feature | Feature, Improvement |
| Bug | Bug |
| Task | Research, Technical Debt, Maintenance, Improvement |

## References

- `docs/standards/repository-standards.md`
- `docs/standards/work-item-taxonomy.md`
