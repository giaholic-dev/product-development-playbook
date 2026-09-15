# Continuous Integration

## Purpose

Define how a project automatically evaluates changes against its required validation and integration rules.

## Scope

This standard is independent of CI provider, operating system, language, framework, and workflow syntax.

## Rules

A project SHOULD automate repeatable validation when automation materially improves confidence, speed, or consistency. Its CI configuration MUST state the triggering changes, validation performed, failure behavior, and ownership of maintenance.

CI MUST NOT be treated as the only form of review or completion evidence. A failed required check blocks integration unless an accountable exception records the risk, reason, and follow-up.

A repository without executable content MAY record CI as not applicable or use it for documentation, link, formatting, or other relevant checks.

## Evidence

CI evidence includes the workflow definition, run result, relevant logs or artifacts, and any recorded exception.

## References

- [Development Phase](../lifecycle/05-development.md)
- [Testing Strategy](testing-strategy.md)
- [Definition of Done](definition-of-done.md)
- [Branch Workflow](branch-workflow.md)
