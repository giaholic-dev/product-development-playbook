# Repository Milestone Standard

## Purpose

Define how a repository uses milestones to group related work against a shared delivery, learning, or decision boundary without turning a milestone into a workflow state.

## Scope

This standard applies when a repository uses milestones. It is technology-neutral; the GitHub mapping is an optional implementation detail.

## Milestone Content

A milestone MUST state:

- the intended outcome or decision;
- its scope boundary;
- the accountable owner;
- the included work items or selection rule; and
- completion criteria.

A milestone SHOULD state a target date when the work has a meaningful date-based commitment. A target date is not a priority, workflow state, or promise that unplanned work will be included.

Milestones MAY group a release, lifecycle increment, remediation effort, learning objective, or cross-cutting improvement.

## Relationship to Work Items

A milestone groups work items; it does not replace their required classification or operational state.

- Each included item retains its Lifecycle Phase and Work Type.
- Milestone membership is optional unless a repository explicitly requires it for a planning purpose.
- A milestone MUST NOT be used as a substitute for backlog order, priority, or workflow status.
- Work outside a milestone remains valid when it meets the repository's Definition of Ready.

## Completion and Change

A milestone is complete only when its stated completion criteria are met and the outcome, decision, or remaining exception is recorded.

A repository MAY change a milestone's scope or target date when evidence changes. The change SHOULD preserve the reason and affected work items so planning remains traceable.

## Platform Mapping

In GitHub, use a repository or organization milestone to group the relevant issues and pull requests. GitHub Project fields and views may expose milestone-related planning information, but they MUST preserve the distinctions in this standard.

## References

- [Work Item Taxonomy](work-item-taxonomy.md)
- [Definition of Ready](definition-of-ready.md)
- [Definition of Done](definition-of-done.md)
- [Project Views](project-views.md)
- [Repository Project Field Standard](repository-project-field-standard.md)
- [Release Strategy](release-strategy.md)
