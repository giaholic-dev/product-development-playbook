# Incident Management

## Purpose

Define how a product restores acceptable service and captures learning when an unplanned event materially affects users, operations, security, or agreed service conditions.

## Scope

This standard governs incident assessment, coordination, recovery, communication, and follow-up. It does not replace routine defect handling or prescribe a particular on-call tool or process.

## Incident Assessment

An incident MUST have an accountable coordinator or decision-maker and a record of the affected service, observed impact, current status, and time of assessment.

Classify response urgency by the actual or credible impact on users, operations, security, obligations, or recovery options. The classification MUST be reassessed as evidence changes.

## Response

The responsible party MUST prioritize safe restoration and clear communication over root-cause speculation. Record material decisions, mitigations, changes, and handoffs as they occur.

When a rollback or other release recovery is used, follow the [Rollback Strategy](rollback-strategy.md) and preserve the incident record.

## Closure and Learning

Close an incident only when the service state, impact, resolution or accepted residual risk, and accountable follow-up are recorded. A material incident SHOULD produce a proportionate review that identifies contributing conditions and improvement work without assigning blame.

## References

- [Maintenance Phase](../lifecycle/07-maintenance.md)
- [Rollback Strategy](rollback-strategy.md)
- [Deployment Strategy](deployment-strategy.md)
- [Definition of Done](definition-of-done.md)
- [Artifact Standard](artifact-standard.md)
