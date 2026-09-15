# Security, Privacy, and Data Governance Standard

## Purpose

Define a risk-based approach for identifying and governing security, privacy, access, retention, and data-handling concerns throughout product work.

## Scope

This standard applies when a product, repository, automation, or AI capability handles systems, users, data, credentials, or external effects. It does not prescribe a security framework, compliance regime, provider, or tool.

## Assessment

A project MUST assess applicable concerns before relying on a material design, implementation, release, or automated action. The assessment identifies affected assets or data, relevant actors, access and retention needs, credible risks, accountable owner, evidence, and reassessment trigger.

The depth of assessment MUST be proportionate to impact, exposure, reversibility, and uncertainty.

## Decisions and Exceptions

Material controls, accepted risks, and exceptions MUST record the decision, owner, rationale, evidence, impact, and reassessment condition. A project MAY determine that a concern is inapplicable when it records the rationale.

## Integration

Architecture owns technical structure; Release owns release readiness; Maintenance owns operational response; Repository Automation and AI Collaboration own automated authority. This standard defines the cross-cutting risk and data-governance considerations they apply.

## References

- [Architecture Phase](../lifecycle/04-architecture.md)
- [Release Phase](../lifecycle/06-release.md)
- [Maintenance Phase](../lifecycle/07-maintenance.md)
- [Repository Automation Standard](repository-automation.md)
- [AI Collaboration Standard](ai-collaboration.md)
- [Repository Standards](repository-standards.md)
- [Artifact Standard](artifact-standard.md)
