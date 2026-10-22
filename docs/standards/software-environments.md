# Software Environments Standard

## Purpose

Require distinct Development, Test, and Production environments for executable software products, with verifiable isolation and controlled promotion.

## Scope and applicability

This standard applies to software products with an executable or served runtime, including static sites, applications, services, and software constituents of hybrid products. Small size, low traffic, manual deployment, or use of a free hosting tier does not remove the requirement.

A repository used only for documentation, governance, or supporting development utilities does not require three product environments solely because it contains scripts or CI. Its applicability assessment MUST identify whether it delivers a runtime product and record the rationale under [Standards Applicability](standards-applicability.md). A documentation site delivered as a software product is within scope. Non-software production methods are outside this standard's scope.

The three environments MUST exist and have verified isolation before product implementation work begins under the Development phase. Provisioning and verifying them is architecture-enabling preparation; Production can be provisioned without exposing a product to real users. Existing adopting products MUST assess their current environments, record gaps and accountable remediation, and satisfy this standard before further production promotion unless a governed exception applies. Planned names or future provisioning tasks are not evidence that environments exist.

## Environment definitions

| Environment | Required purpose |
| --- | --- |
| Development | Implement and experiment with changes without affecting real users or production resources. Local runtimes are permitted. |
| Test | Validate an identified release candidate, including applicable integrations and configuration, before production promotion. This is the required test/homologation environment; staging or acceptance environments may supplement it. |
| Production | Operate the approved release for its intended real users or consumers. Provisioning it does not by itself authorize release exposure. |

An environment is an identifiable execution or serving context with its own effective configuration, access boundary, and applicable data resources. An environment name, Git branch, source directory, or dashboard label alone MUST NOT be treated as an environment.

The three environments MUST be distinct. They MAY share physical infrastructure when the required logical isolation is demonstrated. Separate servers, providers, branches, or subdomains are not mandatory. Additional preview, acceptance, performance, or recovery environments MAY be used without replacing the three required environments.

## Isolation and identification

A project MUST:

- Separate environment configuration and secret scopes. Development and Test application runtimes MUST NOT use production credentials or identities that grant production access. Authorized deployment-task identities are governed separately below.
- Isolate mutable application data and state. Development and Test MUST NOT write to production databases, storage, queues, or equivalent resources. Stateless products MUST record which data-isolation concerns do not apply.
- Route non-production integrations to isolated test resources, sandboxes, or controlled substitutes. Test messages, payments, notifications, and jobs MUST NOT cause real production effects.
- Apply environment-specific access permissions and control production changes through authorized deployment paths.
- Make the active environment unambiguous to operators in configuration, deployment records, logs, and management interfaces where present. Production user interfaces need not display an environment banner.
- Govern any production-derived test data under [Security, Privacy, and Data Governance](security-privacy-data-governance.md), with authorization, minimization or sanitization, access, and retention controls.

Shared infrastructure MUST preserve these boundaries during normal operation and representative failure or misconfiguration checks. Public or immutable assets MAY be shared when the project records why this cannot expose protected data or permit cross-environment mutation.

## Application and deployment identities

An application identity is used by the running or served product and its jobs. A deployment-task identity performs an authorized provisioning, deployment, verification, or recovery operation. The distinction depends on the operation and effective access, not the machine or environment name where a task runs.

A deployment task MAY use scoped production access from a controlled automation or operator execution context when that access is required for an authorized production operation. The project MUST record the task's purpose, target, accountable owner, authorization, permission scope, credential reference, and duration or expiry policy. Permissions MUST be limited to the authorized operation, with the actual operation and result retained as evidence. Deployment authority does not itself supply production-promotion approval.

Production deployment credentials MUST NOT be exposed to Development or Test application runtimes, untrusted code or pull-request execution, test data, logs, or artifacts. A shared runner or host MUST enforce the same separation and restrict when the deployment identity can be obtained and used. Performing ordinary development or testing with a production-capable identity is not a deployment-task exception. Secret handling remains governed by [Security, Privacy, and Data Governance](security-privacy-data-governance.md).

## Configuration and test fidelity

The maintained environment record MUST identify each environment's location or access method, owner, deployed source/artifact identifier, configuration reference, credential scope reference, data resources, integrations, and deployment/recovery method. References MUST NOT expose secret values.

Test MUST reproduce the production behavior and configuration relevant to the release's material risks. Differences in scale, providers, integrations, build configuration, or data MUST be recorded with their impact and validation treatment. A simulated integration does not prove that an untested production integration works.

## Promotion and production approval

Changes MUST progress through Development and Test validation before Production exposure. Production MUST receive the same identified release candidate validated in Test. Where build artifacts exist, promote the same immutable artifact; environment-specific configuration MAY differ through the recorded configuration mechanism. Where no build is needed, preserve the exact validated source revision.

A source or artifact change after validation MUST receive the affected Test validation again before promotion. Material production-specific configuration or integration differences MUST have explicit verification evidence before exposure; an unexplained rebuild or untested configuration change does not preserve candidate identity.

Before production promotion, the project MUST retain:

- the candidate identity and required Test validation results;
- the environment/configuration differences and their disposition;
- a recorded approval by an identified Approver with scoped production-promotion Authority; and
- production deployment, observation, verification, and recovery readiness under [Deployment Strategy](deployment-strategy.md) and [Rollback Strategy](rollback-strategy.md).

Assignments and Authority follow [Roles and Actor Assignment](roles-and-actor-assignment.md). An individual MAY perform contribution, review, and approval through separately identifiable Assignments where governing rules permit; review or a passing CI run alone is not production approval. Scoped automation MAY enforce an approved promotion policy when its decision, Authority, candidate, and evidence remain traceable.

After deployment, verify and record the actual Production result. Failed or inconclusive verification follows Deployment Strategy before exposure expands. Rollback or emergency recovery follows the governed recovery procedure and preserves authorization and evidence; any bypass of this standard requires the exception treatment below.

## Evidence, maintenance, and exceptions

Conformance evidence MUST include actual access or provisioning observations for all three environments, the maintained environment record, isolation checks covering applicable data/access/external-effect boundaries, and promotion evidence for releases that have occurred. Before the first release, record that promotion has not yet occurred rather than inventing deployment evidence.

Reassess affected evidence when infrastructure, permissions, data, integrations, configuration, or delivery paths materially change. Existing architecture, deployment, or conformance records MAY hold this evidence; a new file is not mandatory.

An unmet requirement is a gap, not inapplicability. Exceptions MUST follow [Repository Standards](repository-standards.md#exceptions-and-extensions), identifying the affected requirement and scope, reason, risk, accountable approver, validation performed or deferred, and reassessment condition or date. An exception does not establish three-environment conformance or silently waive production approval.

## References

- [Architecture Phase](../lifecycle/04-architecture.md)
- [Development Phase](../lifecycle/05-development.md)
- [Release Phase](../lifecycle/06-release.md)
- [Standards Applicability](standards-applicability.md)
- [Testing Strategy](testing-strategy.md)
- [Deployment Strategy](deployment-strategy.md)
- [Rollback Strategy](rollback-strategy.md)
- [Roles and Actor Assignment Standard](roles-and-actor-assignment.md)
- [Security, Privacy, and Data Governance Standard](security-privacy-data-governance.md)
- [Repository Standards](repository-standards.md)
