# Bug Management

## Purpose

Define how a product records, assesses, corrects, validates, and learns from defects in expected behavior.

## Scope

This standard governs defects discovered in development, release, or maintenance. It distinguishes routine defect work from incidents, which require coordinated service restoration.

## Bug Record

A bug record MUST describe the observed behavior, expected behavior, affected context, available evidence, impact, and accountable next action. It MUST link to the affected release, work item, or artifact when known.

## Assessment and Prioritization

Assess severity, user or operational impact, reproducibility, scope, and risk. Prioritize corrective work using the repository’s adopted work-item method. A defect with material active impact MUST be assessed for incident handling.

## Correction and Validation

A correction MUST preserve traceability to the defect record and include validation appropriate to the affected behavior and risk. Close a bug only when the resolution, validation evidence, and any remaining limitation or follow-up are recorded.

## References

- [Maintenance Phase](../lifecycle/07-maintenance.md)
- [Incident Management](incident-management.md)
- [Testing Strategy](testing-strategy.md)
- [Definition of Done](definition-of-done.md)
- [Artifact Standard](artifact-standard.md)
