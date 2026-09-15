# Work Item Types

## Purpose

Define the standard work item types used by the Product Development Playbook and clarify how they relate to platform-specific issue types.

## Scope

This document defines the semantics of each work item type adopted by the Playbook.

It also explains how these concepts map to issue types provided by different project management platforms, while keeping the Playbook independent of any specific tool.

## Conceptual Model

The Product Development Playbook distinguishes between **Issue Type** and **Work Type**.

A **Work Type** is defined by the Playbook and describes the primary nature of the work being performed, independently of its lifecycle phase.

An **Issue Type** is a category used by a chosen management platform to represent a work item. It may influence platform features or presentation, but it does not define the work's Playbook Work Type, lifecycle phase, or identity.

Different platforms may provide different issue types, while the Playbook Work Types remain consistent across implementations. The distinct responsibilities of all work item dimensions are defined in the [Work Item Taxonomy](work-item-taxonomy.md).

Pull Requests are implementation and review artifacts rather than work items. They MAY be linked to a work item for traceability, but they MUST NOT replace the work item's primary classification.

A platform MAY display Pull Requests beside work items. Treating a Pull Request as a work item requires an explicit, documented platform integration rule that preserves the Work Item Model; platform display alone is not such a rule.

## Classification Rules

Select the Work Type by the work's primary intended outcome:

| If the work primarily… | Use |
| --- | --- |
| Introduces a new user- or stakeholder-relevant capability | Feature |
| Restores expected behavior after an unintended deviation | Bug |
| Improves an existing capability or its user/stakeholder-perceived quality without changing its fundamental purpose | Improvement |
| Reduces internal future cost, risk, or complexity while preserving intended external behavior | Technical Debt |
| Investigates uncertainty before committing to implementation | Research |
| Preserves or restores operational health, stability, supportability, or required routine operation | Operational Maintenance |

When one change has more than one outcome, use its primary outcome and create linked work items for independently planned outcomes. The exception process in [Work Item Taxonomy](work-item-taxonomy.md) applies only when those outcomes are inseparable.

**Maintenance** is a Lifecycle Phase: it answers where the work is primarily addressed. **Operational Maintenance** is a Work Type: it answers what the work primarily does. Any Work Type MAY occur in any Lifecycle Phase when the primary classification remains clear.


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

## Operational Maintenance

Operational Maintenance preserves the operational health, stability, and supportability of the product throughout its lifecycle.

Operational Maintenance work keeps existing functionality operational without introducing new capabilities or significantly changing existing behavior.

Examples include:

- Routine system maintenance
- Configuration updates
- Operational support
- Monitoring improvements
- Preventive maintenance activities

## Classification Examples

The following examples illustrate a primary classification. They do not prescribe a platform issue type, priority, or workflow state.

| Work | Primary Lifecycle Phase | Primary Work Type | Reason |
| --- | --- | --- | --- |
| Improve keyboard navigation and visible focus treatment in an existing checkout flow | UX | Improvement | It improves the user experience of an existing capability without changing its fundamental purpose. |
| Refactor a duplicated authorization module while preserving its external behavior | Development | Technical Debt | Its intended outcome is lower internal complexity and future change cost, not a user-visible change. |
| Rotate an expiring production certificate and verify service health | Maintenance | Operational Maintenance | It preserves operational continuity and supportability. |
| Compare two notification providers and publish a recommendation before implementation is selected | Architecture | Research | Its outcome is evidence that reduces an implementation decision's uncertainty. |
| Address a security concern that needs a new product requirement and a deployment safeguard | Product; Release | Feature; Operational Maintenance | The requirement decision and the operational safeguard have separate outcomes and evidence, so they are planned and traced separately. |

A cross-phase concern is not automatically an exception. Use the exception record in the [Work Item Taxonomy](work-item-taxonomy.md) only when one inseparable objective cannot be split into related work items without losing traceability or creating material coordination cost.

## Platform Mapping

The Product Development Playbook defines Work Types independently of any project management platform.

When implemented in GitHub, Issue Types and Work Types coexist and serve different purposes.

| GitHub Issue Type | Typical Playbook Work Types |
| ----------------- | --------------------------- |
| Feature | Feature, Improvement |
| Bug | Bug |
| Task | Research, Technical Debt, Operational Maintenance, Improvement |

## References

- [Repository Standards](repository-standards.md)
- [Work Item Taxonomy](work-item-taxonomy.md)
- [Product Backlog](product-backlog.md)
