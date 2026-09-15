# 01 — Foundation

## Purpose

Define the minimum reusable foundation that a product repository adopts, configures, and evidences before beginning the Product phase.

Foundation establishes sufficient repository, governance, workflow, and documentation capability for deliberate product work. It does not require every future decision to be made in advance: unresolved decisions MAY remain when their scope, owner, and reassessment condition are recorded.

## Inputs

- A decision to start or substantially reset a product.
- An initial product idea, opportunity, or problem context.
- Access to the version-control and work-tracking capabilities selected by the project.

## Activities

- **F1 Repository Setup:** Establish an accessible repository with the structure, access, and version-control baseline appropriate to the product.
- **F2 Repository Standards Adoption:** Adopt the [Repository Standards](../standards/repository-standards.md); configure applicable choices and record any project-specific extension or exception without redefining the reusable baseline.
- **F3 Governance and Tracking:** Establish a work-tracking and planning model appropriate to the product, including ownership and any applicable milestones. A GitHub Project is one possible platform mapping, not a conceptual requirement.
- **F4 Workflow Adoption:** Adopt the Playbook lifecycle and establish the applicable workflow, readiness, review, and completion gates. Detailed branch workflow and review rules are owned by their dedicated standards.
- **F5 Documentation Foundation:** Establish the documentation architecture, primary language declaration, root entry point, and navigation required by the repository standards.

## Outputs

Outputs are resulting capabilities or states, not documents or tool records.

- An operational repository and version-control baseline.
- An adopted governance and work-tracking model.
- An adopted workflow with identified decision and review gates.
- A navigable documentation foundation.
- A recorded set of any unresolved Foundation decisions and their reassessment conditions.

## Artifacts and Evidence

Artifacts are the inspectable records that evidence Foundation outputs. A project MUST retain the artifacts applicable to its purpose.

- Repository and root entry point.
- [Repository Standards](../standards/repository-standards.md) adoption, including recorded extensions or exceptions where applicable.
- Applicable work item and project-view configuration, evidenced by the [Work Item Taxonomy](../standards/work-item-taxonomy.md), [Work Item Types](../standards/work-item-types.md), and [Project Views](../standards/project-views.md).
- Documentation architecture and navigation, evidenced by the [Documentation Information Architecture](../standards/documentation-information-architecture.md) and [Documentation Navigation Standard](../standards/documentation-navigation.md).
- A documented workflow configuration or explicit links to the adopted workflow, readiness, review, and completion standards.
- A record of unresolved Foundation decisions, when any exist.

The detailed Artifact Standard, Terminology Standard, Definition of Ready, Definition of Done, Branch Workflow, Code Review, and project-management standards are governed by their dedicated follow-up issues; Foundation adopts their outputs rather than restating them.

## Definition of Done

Foundation is complete when observable evidence shows that:

- The repository can store and track the product's applicable work.
- The project has adopted Repository Standards and recorded any applicable extensions or exceptions.
- A work-tracking and planning model has an identified owner and is usable for the project's scope.
- Documentation has a declared language, reachable entry point, and applicable architecture and navigation.
- The workflow and its remaining dedicated standards are either adopted or explicitly recorded as unresolved with owners and reassessment conditions.
- Required Foundation artifacts are present, linked, or assigned to an explicit follow-up owner.

## Exit Criteria

The Product phase may begin when the product team or individual can create, classify, document, and review Product work using the established Foundation. Any remaining Foundation decisions MUST have a known owner, impact, and reassessment condition and MUST NOT prevent the first Product activities.

## References

- [Repository Standards](../standards/repository-standards.md)
- [Work Item Taxonomy](../standards/work-item-taxonomy.md)
- [Work Item Types](../standards/work-item-types.md)
- [Project Views](../standards/project-views.md)
- [Documentation Information Architecture](../standards/documentation-information-architecture.md)
- [Documentation Navigation Standard](../standards/documentation-navigation.md)
- [Artifact Standard issue — planned standard](https://github.com/giaholic-dev/product-development-playbook/issues/111)
- [Terminology Standard issue — planned standard](https://github.com/giaholic-dev/product-development-playbook/issues/86)
- [Definition of Ready issue — planned standard](https://github.com/giaholic-dev/product-development-playbook/issues/69)
- [Definition of Done issue — planned standard](https://github.com/giaholic-dev/product-development-playbook/issues/70)
- [Branch Workflow issue — planned standard](https://github.com/giaholic-dev/product-development-playbook/issues/71)

---

**Next Phase:** [02 — Product](02-product.md)
