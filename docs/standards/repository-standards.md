# Repository Standards

## Purpose

Define the reusable repository contract that enables consistent, maintainable, and auditable work across repositories adopting the Product Development Playbook.

## Scope

This standard defines the baseline for repository organization, documentation, version control, changes, conformance, and delegation to detailed standards.

The conceptual layer is independent of programming languages, frameworks, product architecture, and repository-hosting vendors. The Playbook deliberately adopts Git as its version-control baseline. A hosting platform is an implementation choice unless a project explicitly adopts a corresponding mapping.

## Normative Language

- **MUST** is mandatory for conformance.
- **SHOULD** is the expected default; a deviation needs a recorded reason.
- **MAY** is permitted and optional.

Statements without these terms are explanatory.

## Exceptions and Extensions

An exception to a MUST requirement MUST record the rule, reason, affected scope, known impact or risk, accountable approver, validation performed or deferred, and a reassessment condition or date.

A project MAY extend this standard when the extension identifies its owner, scope, relationship to the baseline, and evidence of adoption. An extension MUST NOT silently weaken a Playbook MUST requirement; it requires an exception when it does.

Exceptions and extensions change only the adopting repository. They do not modify the Playbook standard.

## Repository Structure

Every repository MUST have a clear structure appropriate to its purpose. Content responsibilities may include documentation, source code, tests, configuration, automation, templates, and examples.

A repository MUST include only the responsibilities it needs. It MUST NOT create empty directories or placeholder content merely to reproduce this list. The root documentation MUST identify the repository purpose, top-level organization, and navigation to its primary content.

Directory names and nesting MAY vary across documentation repositories, applications, services, libraries, and other repository types. The chosen structure SHOULD keep related content together and make each applicable responsibility easy to locate.

## Documentation Contract

Documentation is a first-class artifact. Each project MUST declare a primary documentation language.

Every maintained document MUST make its purpose and responsibility evident, maintain one primary source of truth for each governed concept, distinguish current from planned or historical state, use references instead of duplicate rules, keep internal references resolvable, and be reviewed when its governed concept or decision changes.

Detailed writing, document structure, information architecture, and navigation are owned by the Documentation Style Guide, Documentation Information Architecture, and Documentation Navigation Standard.

## Conceptual Standards

A conceptual standard MUST contain a title, Purpose, Scope, and References when another document owns a related rule. It SHOULD use the conditional sections needed to make its responsibility usable, such as Definitions, Principles, Rules, Process, Evidence, Exceptions, or Examples.

A section may be omitted when it is not applicable, provided the document still communicates its responsibility, requirements, and completion evidence. Lifecycle documents follow their lifecycle template.

## Git Baseline

Git is the version-control system adopted by the Playbook. A repository MUST preserve a traceable history for its changes.

Repositories SHOULD favor small, incremental, reversible changes. Initialization, imported history, emergency recovery, and tool limitations follow the recorded exception process in the [Branch Workflow](branch-workflow.md) rather than silently bypassing history or integration rules.

## Branch and Default-Branch Contract

The [Branch Workflow](branch-workflow.md) owns branch naming, lifecycle, default-branch stability evidence, and traceable exceptions.

The default branch MUST represent the current stable, releasable state. A project uses short-lived branches and reviewed change requests by default, with the narrow exceptions defined in Branch Workflow.

## Commit Convention

The Playbook uses a constrained Conventional-Commits-inspired profile; it does not claim to reproduce the complete external Conventional Commits specification.

A regular commit MUST use `<type>: <description>`. It MAY use `<type>(<scope>): <description>`, a breaking-change indicator, a body, and footers when they improve traceability. The description SHOULD be imperative, concise, and limited to one logical change.

Common types are `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `build`, `ci`, and `perf`.

Merge, revert, release, and automated commits MAY use system-generated syntax. They MUST remain understandable and traceable to their originating change, release, or automation. A repository MAY define additional types as a documented extension.

## Change Readiness, Review, and Integration

A work item or change MUST meet the [Definition of Ready](definition-of-ready.md) before work begins, except under a recorded exception.

A proposed repository change MUST include its purpose, relevant traceability, validation evidence, and review evidence. The [Code Review Standard](code-review-standard.md) owns review depth, solo self-review, independent review, and disposition of blocking findings.

A Pull Request is one possible change-request record. A repository MAY use another mechanism when it preserves equivalent evidence. Before integration, a change MUST satisfy the review gate, have no unresolved blocking finding, and meet the default-branch conditions in Branch Workflow. Merge method, branch-protection rules, and platform configuration are local implementation choices.

The [Definition of Done](definition-of-done.md) owns completion evidence for work items and changes.

## Versioning

A repository MUST use the [Versioning Standard](versioning-standard.md) to distinguish published releases from any explicit development target. Semantic Versioning is appropriate when compatibility promises are needed; another documented approach MAY be adopted when it better fits the product and audience.

## Conformance Declaration

A repository adopting this standard MUST maintain a lightweight conformance declaration in its root documentation or an equivalent governed record. It identifies:

- repository purpose and applicable content responsibilities;
- primary documentation language;
- adopted detailed standards and local mappings;
- active exceptions and project-specific extensions;
- validation and review evidence appropriate to the repository; and
- the accountable owner and next conformance review condition or date.

Conformance is demonstrated by the declaration, resolvable documentation, traceable change history, and evidence that the applicable requirements have been reviewed. It is not demonstrated merely by copying document names or directory structure.

## References

- [Foundation Phase](../lifecycle/01-foundation.md)
- [Branch Workflow](branch-workflow.md)
- [Code Review Standard](code-review-standard.md)
- [Definition of Ready](definition-of-ready.md)
- [Definition of Done](definition-of-done.md)
- [Versioning Standard](versioning-standard.md)
- [Documentation Style Guide](documentation-style-guide.md)
- [Documentation Information Architecture](documentation-information-architecture.md)
- [Documentation Navigation Standard](documentation-navigation.md)
- [Work Item Taxonomy](work-item-taxonomy.md)
- [Work Item Types](work-item-types.md)
- [Project Views](project-views.md)
