# Testing Strategy

## Purpose

Define how a project selects, executes, and records validation appropriate to its product risks, changes, and quality goals.

## Scope

This standard is independent of test framework, language, platform, and automation provider.

## Rules

A project MUST define validation appropriate to its material behavior, risks, interfaces, data, and operational constraints. The strategy MUST state what evidence is expected, when it is required, how failures are handled, and who owns exceptions.

Validation MAY include automated tests, exploratory testing, integration checks, contract checks, accessibility evaluation, performance evaluation, security evaluation, review, or another appropriate method. No single test type is universally mandatory.

A change MUST have the validation evidence required by its risk and scope before it is declared complete. Missing or deferred validation requires a recorded exception with risk, owner, and reassessment condition.

## Environment validation

For executable software products, validation MUST use the required environments and retain the isolation, Test-fidelity, and candidate evidence governed by the [Software Environments Standard](software-environments.md). Method selection remains proportionate to risk; it does not make the required Test environment optional. CI execution alone does not establish environment conformance or production approval.

## Evidence

Testing evidence MAY be test results, review records, reports, reproducible steps, automated workflow output, or another traceable record.

## References

- [Software Environments Standard](software-environments.md)

- [Development Phase](../lifecycle/05-development.md)
- [Definition of Done](definition-of-done.md)
- [Code Review Standard](code-review-standard.md)
- [Branch Workflow](branch-workflow.md)
- [Continuous Integration](continuous-integration.md)
