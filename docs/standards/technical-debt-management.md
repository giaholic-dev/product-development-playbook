# Technical Debt Management

## Purpose

Define how a product makes technical debt visible, assesses its consequences, and deliberately chooses whether to reduce, accept, or revisit it.

## Scope

Technical debt is a condition that creates future cost, risk, reduced adaptability, or constrained quality because of a current technical decision, gap, or deferred improvement. This standard does not treat every non-preferred implementation as debt.

## Debt Record

A technical-debt record MUST identify the observed condition, affected area, consequence or risk, available evidence, accountable owner, and next assessment or action. It SHOULD link to the decision, incident, defect, release, or architecture artifact that provides context.

## Assessment and Decision

Assess debt by its impact on reliability, security, maintainability, delivery capability, cost, and product outcomes. The accountable decision-maker MUST choose to reduce, accept, defer, or investigate it and record the rationale.

Accepted or deferred debt MUST have a reassessment condition when it could materially affect future work.

## Reduction and Closure

Debt reduction work MUST have a stated outcome and validation proportionate to the risk it addresses. Close a debt item only when the condition is resolved, superseded by an explicit decision, or reclassified with traceable evidence.

## References

- [Maintenance Phase](../lifecycle/07-maintenance.md)
- [Bug Management](bug-management.md)
- [Architecture Decision Records](architecture-decision-records.md)
- [Definition of Done](definition-of-done.md)
- [Artifact Standard](artifact-standard.md)
