# Project Views

## Purpose

Define how projects select, configure, and evolve views that make work visible for a stated management purpose.

A project view is a conceptual presentation of work items. It is not synonymous with a GitHub Project view or any other vendor feature.

## Scope

This standard covers the conceptual purpose, composition, ownership, and evolution of project views. It does not prescribe a specific project-management platform or configuration.

## Principles

- A view MUST have a named purpose and an owner.
- A view MAY serve more than one purpose when its audience, decisions, and required information remain clear.
- A view MUST expose enough work-item and workflow information for its purpose without duplicating the [Work Item Taxonomy](work-item-taxonomy.md).
- A project SHOULD start with the default view set and add or retire views based on a recurring decision need.
- A view MUST be reviewed when its intended decisions, workflow, or supporting fields materially change.

## View Types

A **View Type** is the presentation mechanism. A platform may implement the same type differently.

| Type | Use |
| --- | --- |
| Board | Compare and move work through a workflow state. |
| Table | Inspect, filter, sort, and compare structured work-item information. |
| Timeline | Show scheduled work over a defined time range using dates or iterations. |
| Roadmap | Communicate a higher-level sequence of outcomes, themes, or delivery horizons without asserting a day-by-day schedule. |
| Calendar | Inspect work against specific dates, deadlines, or events. |

A Timeline is date- or iteration-based and supports scheduling decisions. A Roadmap is outcome- and horizon-based and supports strategic communication. A roadmap MAY link to a timeline, but it MUST NOT imply that its horizons are committed dates unless the project states so.

## View Purposes

A **View Purpose** is the management decision a view supports.

| Purpose | Primary decision |
| --- | --- |
| Operational | What needs attention now, who owns it, and what is blocked or in progress? |
| Planning | What work should be selected, sequenced, or prepared next? |
| Reporting | What has changed, what is the current distribution of work, and what needs escalation? |
| Strategic | Which outcomes, themes, and lifecycle investments best support the intended direction? |

## Composition and Selection

Select a View Type and View Purpose independently. One view MAY combine purposes only when the same audience can make both decisions from the same information. Otherwise, create focused views.

A project MAY choose another set when it documents the decision need, audience, owner, and minimum information. A useful default set is:

| View | Type | Purpose | Minimum information |
| --- | --- | --- | --- |
| Current Work | Board | Operational | Title, Status, Assignees, Work Type, blockers or equivalent. |
| Backlog Planning | Table | Planning | Title, Phase, Work Type, Priority when used, readiness or equivalent. |
| Delivery Outlook | Timeline or Calendar | Planning | Title, Status, Iteration and/or Target Date when used. |
| Outcome Roadmap | Roadmap | Strategic | Outcome or theme, Phase, owner, horizon, and dependency when relevant. |

A Reporting view is created when a recurring reporting decision needs a stable filter, grouping, or aggregation beyond these views.

## Taxonomy and Workflow Information

Views consume — but do not redefine — the taxonomy:

| Information | Typical view use |
| --- | --- |
| Lifecycle Phase | Planning and strategic grouping or filtering. |
| Work Type | Planning, reporting, and workload distribution. |
| Artifact Category | Traceability or reporting when artifacts are relevant. |
| Priority | Planning comparison when the project has chosen to use priority. |
| Workflow State | Operational flow and reporting. |
| Assignees | Operational ownership and workload awareness. |
| Iteration / Target Date | Planning and delivery outlook when the project has configured them. |

A layout, filter, grouping, or sort order MUST NOT create or infer a taxonomy classification. The record remains the source of the classification.

## Pull Request Visibility

Pull Requests are implementation and review artifacts, not default work items. A view MAY include linked pull-request or reviewer information when it supports an integration, review, release, or operational decision.

For example, a Current Work view may display linked pull requests for items under review, while a strategic roadmap normally omits them. A project MUST state the purpose before including pull-request data; it is neither universally required nor universally excluded.

## GitHub Projects Mapping

GitHub Projects is one possible implementation. A GitHub table, board, roadmap, or equivalent layout implements a conceptual Project View only when it declares the intended purpose, owner, and information configuration.

Use the [Repository Project Field Standard](repository-project-field-standard.md) for GitHub-provided metadata and configurable field definitions. GitHub-specific choices such as filters, grouping, sorting, layout, automation, and visibility are local implementation details and MUST NOT redefine the conceptual view or work-item taxonomy.

## Ownership and Evolution

The project owner appoints a view owner for each maintained view. The owner MUST:

- keep the purpose, audience, and essential information current;
- review field use and filters when workflow or taxonomy changes;
- remove, merge, or replace views that no longer support a recurring decision; and
- record material exceptions or local extensions according to [Repository Standards](repository-standards.md).

## References

- [Repository Standards](repository-standards.md)
- [Work Item Taxonomy](work-item-taxonomy.md)
- [Work Item Types](work-item-types.md)
- [Repository Project Field Standard](repository-project-field-standard.md)
- [Product Backlog](product-backlog.md)
