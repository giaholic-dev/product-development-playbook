# AI Collaboration Example

## Purpose

Illustrate how the same Playbook work item can be completed manually, with AI assistance, or through authorized automation while preserving accountable decisions, review, validation, and a manual fallback.

This fictional example is provider-agnostic. It does not prescribe a model, prompt, integration, product architecture, or automation platform.

## Scenario

A product team needs to decide whether its product-definition example has complete links to the governing Product standards.

The accountable owner creates a research work item with the question, acceptance evidence, and a next action. The completion evidence is a reviewed link check and a recorded decision.

## Manual Execution

1. The owner reads the example and the related Product standards.
2. The owner checks each referenced path against the repository tree.
3. The owner records the resulting decision and any follow-up work.
4. A reviewer verifies the evidence before the work item is completed.

## AI-assisted Execution

1. The owner provides the AI only the authorized repository context and asks it to identify candidate missing or inconsistent links.
2. The AI returns a proposed list of findings and source paths.
3. The owner verifies each proposal against the repository and records the decision.
4. A reviewer evaluates the change and evidence using the same completion rules as the manual path.

The AI output accelerates analysis but is not completion evidence by itself.

## Authorized AI-automated Execution

An authorized repository automation may run a link check and produce an artifact containing the command, inputs, results, and timestamp. The automation cannot approve its own finding, merge a change, or declare the work complete. The accountable owner and reviewer still make those decisions.

## Manual Fallback

If the AI provider, integration, or credential is unavailable, the owner follows the Manual Execution path. The work item, acceptance evidence, review requirement, and completion criteria do not change.

## Evidence and Accountability

| Concern | Record |
| --- | --- |
| Accountable decision | The work item's owner and recorded decision. |
| AI use, when applicable | Authorized context, purpose, proposed output, and validation performed. |
| Validation | Link-check result and reviewer disposition. |
| Follow-up | A linked work item for any unresolved issue. |

## References

- [AI Collaboration Standard](../docs/standards/ai-collaboration.md)
- [Definition of Ready](../docs/standards/definition-of-ready.md)
- [Definition of Done](../docs/standards/definition-of-done.md)
- [Code Review Standard](../docs/standards/code-review-standard.md)
- [Repository Automation Standard](../docs/standards/repository-automation.md)
