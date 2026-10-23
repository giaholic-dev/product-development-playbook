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

## Recovery Copies and Restore Data

When backup, recovery, replay, export or migration copies contain governed information, the assessment MUST include their scope, sensitivity, accountable owner, authorized access, protection, retention/deletion treatment and relevant provider or key-access dependencies. Recovery copies are data assets, not an automatic exemption from the original data-handling obligations. Record conflicts or limits between recovery retention and deletion needs with their applicable authority and reassessment; do not silently claim that every historical copy was erased.

Restore/migration verification using production-derived data MUST have authorized, minimized or sanitized handling, isolation and disposal consistent with the affected risk and [Software Environments](software-environments.md). Records MUST reference credentials and recovery-key access without embedding secret values. A backup or restore mechanism does not itself grant broader access, authorize disclosure or prove a completed restoration. [Rollback Strategy](rollback-strategy.md) owns recovery verification; [Data Model](data-model.md) owns migration compatibility.

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
- [Rollback Strategy](rollback-strategy.md)
- [Data Model](data-model.md)
- [Software Environments Standard](software-environments.md)
