# Repository Automation Standard

## Purpose

Define how repositories adopt automation that improves consistency, verification, or traceability without obscuring ownership or creating unsafe, vendor-dependent assumptions.

## Scope

This standard applies to repository-local automation, including scripts, checks, workflows, bots, and generated evidence. It does not require a particular automation platform. The [AI Collaboration Standard](ai-collaboration.md) owns AI-specific authority, evidence, provider-independence, and manual-fallback rules.

## Automation Requirements

An automation MUST have a documented purpose, accountable owner, trigger or invocation method, inputs, outputs, failure behavior, and required permissions.

Automation that changes repository state, publishes artifacts, or communicates externally MUST be explicitly authorized by the repository workflow and leave traceable evidence. It MUST use the minimum permissions needed.

Automation MUST fail clearly when required preconditions are not met. A repository MUST NOT represent skipped, partial, or failed automation as successful validation.

## Change and Review

Changes to automation MUST be reviewed according to their risk and include validation appropriate to their behavior. Generated output MUST identify its source automation or be linked to the relevant run or command when traceability matters.

## References

- [Repository Standards](repository-standards.md)
- [Continuous Integration](continuous-integration.md)
- [Code Review Standard](code-review-standard.md)
- [Artifact Standard](artifact-standard.md)
- [AI Collaboration Standard](ai-collaboration.md)
