# Branch Workflow

## Purpose

Define a lightweight, traceable branch workflow for repositories adopting the Product Development Playbook.

## Scope

This standard defines version-control workflow expectations. It is Git-oriented because the Playbook deliberately requires version-control capability, but it does not require a hosting vendor.

## Default Workflow

The default branch represents the current stable, releasable repository state.

A change SHOULD be made on a short-lived branch and integrated through a Pull Request or equivalent reviewed change request. The branch name MUST identify the change category and use a concise hyphen-separated description.

Recommended prefixes are:

- `feature/`
- `fix/`
- `docs/`
- `refactor/`
- `test/`
- `chore/`
- `release/`

## Stability Evidence

Before a change enters the default branch, the change MUST have:

- a stated purpose and traceability to the governing work item when one exists;
- the validation appropriate to its risk and affected artifacts;
- the review evidence required by the Code Review Standard;
- no unresolved blocking discussion; and
- a merge decision that preserves an understandable repository history.

A default branch is stable when these conditions are met for its integrated changes and no known blocking defect or failed required validation prevents normal use or release of the repository.

## Exceptions

Repository initialization, imported history, emergency recovery, and a tool limitation MAY bypass the default branch workflow only when the change records:

- why the normal workflow was not practical;
- the scope and risk of the exception;
- the person accountable for the decision;
- the validation performed or deferred; and
- the follow-up condition or date.

An exception does not remove the obligation to restore traceability and validation as soon as practical.

## Traceability

When a work item exists, the branch, commits, Pull Request or equivalent change request, and release evidence SHOULD link to it. A repository MUST NOT create artificial work items solely to satisfy this rule.

Commits remain meaningful records of a change. Pull Requests are review and integration artifacts, not work items.

## Branch Lifecycle

Keep branches current with their target branch when required to validate or merge safely. After integration or abandonment, delete the short-lived branch unless retention is needed for a documented operational or audit purpose.

## References

- [Repository Standards](repository-standards.md)
- [Code Review Standard](code-review-standard.md)
- [Definition of Ready](definition-of-ready.md)
- [Definition of Done](definition-of-done.md)
- [Work Item Taxonomy](work-item-taxonomy.md)
