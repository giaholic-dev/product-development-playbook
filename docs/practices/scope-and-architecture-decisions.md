# Scope Evolution and Proportionate Architecture Decisions

## Purpose and boundaries

Use this optional practice when new capabilities suggest a larger product or a different technical structure. [Product Scope](../standards/product-scope.md), [Product Evolution](../standards/product-evolution.md), the [Architecture Phase](../lifecycle/04-architecture.md), and [Architecture Decision Records](../standards/architecture-decision-records.md) remain authoritative. The examples concern software specialization and do not prescribe an architecture for every product type.

## Possibility or scope change?

First separate a recorded opportunity from a decision to include it.

| Situation | Suggested handling under the governing sources |
| --- | --- |
| A future idea has no effect on the selected increment | Capture it as a possibility with its evidence and explicit exclusion from current scope. Use an existing intake or decision record where appropriate. |
| A proposal changes users, outcomes, inclusions, exclusions, or operating obligations | Assess it through Product; record the accountable decision and update affected product evidence before implementation depends on the change. |
| A proposal changes experience or technical assumptions within current intent | Revisit UX or Architecture as applicable; reassess Product if that examination reveals a changed product boundary. |

For example, a portfolio landing page may record tasks, calendar, habits, training, and personal knowledge as future possibilities. Shared domain ownership does not establish that they are one product, nor does the list commit their delivery. Examine the user needs, outcomes, access model, data relationships, ownership, and operational obligations before choosing one product, multiple products, or a shared platform.

Record accepted changes and their consequences for backlog, milestones, dependencies, and prior decisions. Preserve valid earlier evidence and trace superseding decisions instead of silently rewriting the historical scope.

## Architecture decision prompts

Begin with the next bounded capability and the current constraints. Compare meaningful alternatives using evidence:

| Dimension | Questions |
| --- | --- |
| Boundaries and ownership | Which responsibilities and data belong together? Who changes and operates each part? |
| Deployment | Is independent deployment needed now? What observed requirement justifies it? |
| Integration | What synchronous calls, events, failure cases, latency, and consistency are acceptable? |
| Identity and privacy | How are authentication, authorization, sessions, sensitive data, and cross-app access handled? |
| Operation | Who handles deployment, monitoring, backups, restore, failures, and upgrades? |
| Cost and maintenance | What hosting, tooling, coordination, and ongoing effort can the owner sustain? |
| Change and reversibility | What evidence would justify splitting or consolidating later? What migration would that require? |

For a small software product, compare a modular monolith, separate applications with explicitly selected shared capabilities, and independently deployed services only where they are meaningful alternatives. A modular monolith can retain internal boundaries in one deployable unit. Separate user-facing apps need not imply microservices; a microservice boundary carries independent deployment and operating responsibilities.

URLs are a separate exposure decision: paths and subdomains do not determine service boundaries. Evaluate routing, cookies, origin restrictions, and security obligations in the selected context before choosing them.

Record the selected option, alternatives, rationale, consequences, owner, and status under the ADR standard; link supporting evidence and work. State unresolved assumptions and reassessment triggers, such as a measured scaling constraint or a demonstrated need for independent deployment. Confirm that the decision supplies enough direction for the next development increment, rather than fixing every future architectural choice.
