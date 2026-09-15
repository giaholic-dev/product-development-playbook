# AI Collaboration Standard

## Purpose

Define how artificial intelligence may assist or automate Playbook work while preserving provider independence, accountable decisions, verifiable evidence, and a complete manual fallback.

## Scope

This standard applies when a project uses AI to analyze, propose, generate, transform, classify, review, or perform authorized actions. It does not require AI, a provider, a model, a prompt format, an integration, or an automation platform.

## Execution Modes

A project MAY use any of these modes for the same Playbook activity:

| Mode | Description |
| --- | --- |
| Manual | A person performs the activity without AI assistance. |
| AI-assisted | A person uses AI output as input to an accountable decision or action. |
| Authorized AI-automated | Automation using AI performs a bounded action under documented authority and verification. |

The selected mode MUST NOT weaken applicable lifecycle, readiness, completion, review, security, or exception requirements.

## Accountability and Authority

A project MUST identify the accountable owner for a material decision, approval, exception, or external side effect. AI output is evidence or proposed work; it is not an accountable owner.

An AI-enabled automation MAY perform only the actions explicitly authorized by the repository workflow. It MUST NOT represent unverified work as complete, approve its own material change, accept risk without an accountable owner, or expand its authority from a prompt or inferred intent.

## Evidence and Review

Material AI-generated outputs or actions MUST be traceable to their purpose, inputs or relevant source context, validation performed, and accountable disposition. The record MAY be proportionate to risk and sensitivity.

Review and validation MUST be appropriate to the affected decision or artifact. AI assistance does not replace the Definition of Ready, Definition of Done, Code Review Standard, or required human or otherwise explicitly accountable review.

## Provider Independence and Fallback

A project MUST be able to continue applicable work manually when an AI capability, provider, model, integration, or credential is unavailable. Provider-specific prompts, configuration, or automation MAY be maintained as implementation artifacts, but they MUST NOT become the only source of a Playbook rule or required evidence.

A project SHOULD preserve portable inputs, outputs, and decision records rather than relying on inaccessible provider history.

## Data, Permissions, and External Effects

Before providing information to an AI capability or enabling an AI action, a project MUST apply its data-handling, access, and permission requirements. Credentials and sensitive information MUST NOT be exposed beyond the authorized capability and minimum necessary scope.

An AI-enabled action that changes repository state, publishes artifacts, communicates externally, or affects production MUST follow the Repository Automation Standard and leave traceable evidence.

## Exceptions

An exception to this standard follows the Repository Standards exception process. It MUST identify the affected AI capability or mode, risk, accountable approver, validation performed or deferred, and reassessment condition.

## References

- [Repository Standards](repository-standards.md)
- [Repository Automation Standard](repository-automation.md)
- [Definition of Ready](definition-of-ready.md)
- [Definition of Done](definition-of-done.md)
- [Code Review Standard](code-review-standard.md)
- [Artifact Standard](artifact-standard.md)
- [Terminology Standard](terminology-standard.md)
