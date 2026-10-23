# End-to-end Playbook Example

## Purpose

Illustrate a fictional product increment across the complete lifecycle. It is provider-agnostic and illustrative. All provisioning, identities, observations and approvals below are fictional; they are not evidence of an actual deployment.

## Foundation

A solo owner adopts the standards, records a manual-first execution mode with optional AI assistance, and creates a conformance declaration.

## Product

The owner defines a problem, users, outcome, scope, and an initial backlog for a library reservation service.

## UX

The owner validates a reservation flow with representative users and records findings and risks.

## Architecture

The owner records context, data, interface, quality, security, and accessibility decisions proportionate to the increment.

### Three-environment preparation record

Before implementation, the owner provisions all three contexts under the [Software Environments Standard](../docs/standards/software-environments.md). The optional [environment record](../templates/software-environment-record.md) can hold the real evidence in an adopting product.

| Context | Fictional observed preparation | Configuration, identity and resources |
| --- | --- | --- |
| Development | Local runtime starts and responds to a health check. | Local configuration, development-only identity, synthetic reservation database and notification sink. |
| Test | Isolated test runtime responds; deployment and teardown permissions are checked. | Test configuration and identity, separate synthetic database and sandbox notifications. |
| Production | Restricted empty runtime and routing target are provisioned and respond to an operator health check; no product is exposed. | Production configuration, production-only runtime identity, empty production database and disabled outbound notifications until approval. |

Mara owns the record and access review. Its configuration and credential references identify controlled records without secret values. The preparation observations include denied Development/Test attempts to access Production data and credentials; test notifications reach only the sink; production writes are unavailable to both non-production runtimes. Shared infrastructure does not bypass these boundaries. A separate deployment-task identity has only the authorized target permissions, a bounded session lifetime and an operation log; it is unavailable to product runtimes and untrusted changes.

The Architecture exit decision verifies these observations before Development begins. Provisioning Production is not release approval. At this point each runtime has only its provisioning baseline; no product candidate or promotion has yet occurred.

Mara's fictional state-recovery record treats reservation IDs, borrower references and accepted changes as material state, separately from the application artifact. It identifies a consistent copy plus change journal, compatible application/state versions, a loss/time boundary and isolated synthetic restoration/application checks. Those fictional checks verify linked records and recovery of later accepted changes; backup existence alone is not readiness. The [stateful recovery walkthrough](stateful-recovery-and-migration-example.md) illustrates a later schema-changing increment, including a failed restore and a held promotion. No real restoration evidence is claimed by either example.

## Development

A small reservation-status increment is implemented, reviewed, tested, and linked to its evidence. AI may propose test cases; the owner validates them. Development uses its isolated data and notification sink. The integrated revision produces immutable artifact `reservation-status-r1`; its recorded digest is used as the candidate identity in Test and Production.

## Release

The fictional release record identifies `reservation-status-r1` and its digest. Test receives that immutable artifact and records successful status rendering, missing/stale-data behavior, accessibility checks, isolation checks and sandbox notifications. Test and Production differ in endpoint references, credentials and data; those differences are documented, with production-specific routing and configuration verified before user exposure. A simulation does not establish that an untested production integration works.

Mara's separate Approver Assignment authorizes promotion of this candidate to this Production target after examining the Test results, configuration differences and recovery readiness. The approval has recorded scope and time; CI or contribution alone is not approval. The authorized deployment task promotes the same digest, verifies the actual served revision and status behavior, and records observation results before expanding exposure. A failed check holds exposure and invokes the approved recovery path. Recovery readiness includes the state-specific record above and the previous known-good artifact/configuration or, for this first release, disabling product exposure. Disablement alone does not restore lost reservation data, and an old artifact is not sufficient without compatible state; any replacement candidate must receive affected Test validation again. Release notes and operational ownership complete the handoff.

## Maintenance

Feedback and monitoring identify a confusing status label. A follow-up item returns to UX and Product for refinement.

## Evidence and Fallback

Each phase records accountable decisions, artifacts, validation, and exceptions. If AI is unavailable, the owner performs the same research, review, and documentation manually.

## References

- [Playbook Core Principles](../docs/core/principles.md)
- [AI Collaboration Standard](../docs/standards/ai-collaboration.md)
- [Foundation Phase](../docs/lifecycle/01-foundation.md)
- [Maintenance Phase](../docs/lifecycle/07-maintenance.md)
