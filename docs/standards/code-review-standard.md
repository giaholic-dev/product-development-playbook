# Code Review Standard

## Purpose

Define the review gate that verifies a proposed change is understandable, sufficiently validated, and safe to integrate.

## Scope

This standard applies to code, configuration, automation, documentation, and other repository changes. The review depth MUST be proportionate to the change's risk, impact, and reversibility.

## Review Evidence

Before integration, a change MUST have review evidence that records:

- the change purpose and affected scope;
- the validation performed and its result;
- the review outcome, including any unresolved risk; and
- the integration decision or an approved exception.

A review checks the change against its governing work item, applicable standards, correctness, safety, maintainability, documentation, and validation evidence. It does not guarantee that a change is defect-free.

## Team Review

When an independent qualified reviewer is available, a change with material risk or impact SHOULD receive an independent review before integration. The reviewer MUST be able to request changes and MUST not approve work they have not examined.

The project MAY define risk thresholds, protected-branch rules, or required reviewer roles as a local extension.

## Solo Review

An individual developer MAY satisfy the review gate through recorded self-review. Self-review MUST NOT be described as independent approval.

Self-review evidence MUST include:

- a comparison of the intended change with the implemented change;
- the applicable checklist or standards reviewed;
- validation results;
- known limitations, deferred risks, or follow-up work; and
- a clear merge decision.

For higher-risk changes, the developer SHOULD seek external review or record why that is not practical and which additional validation mitigates the risk.

## Discussion and Blocking Findings

A blocking finding MUST be resolved, explicitly accepted by the accountable owner, or converted into a traceable follow-up before integration. Non-blocking suggestions MAY be deferred when their disposition is recorded.

## Platform Mapping

A Pull Request is one possible review record. A platform's approval state is not the only valid form of evidence, and a self-authored approval MUST NOT be represented as independent review.

A project MAY use checklists, automated checks, review comments, change-request records, or equivalent mechanisms to capture the required evidence.

## References

- [Repository Standards](repository-standards.md)
- [Branch Workflow](branch-workflow.md)
- [Documentation Style Guide](documentation-style-guide.md)
- [Work Item Taxonomy](work-item-taxonomy.md)
