# Software Environment Record

## Purpose and scope

Optional evidence structure for [Software Environments](../docs/standards/software-environments.md). The standard owns obligations; this template adds none. Replace prompts with actual discoverable records and observed results. Do not include secrets. A template or planned task alone is not conformance evidence.

## Applicability and ownership

- Product/runtime boundary and source baseline:
- Applicability rationale and accountable owner:
- Record location, last verification and reassessment triggers:
- Scoped Contributor, Reviewer and Approver Assignments and Authority references:

## Prepared environments

| Context | Actual location/access and owner | Configuration and credential-scope references | Data and integrations | Deployed source/artifact | Provisioning/access observation | Deployment and recovery method |
| --- | --- | --- | --- | --- | --- | --- |
| Development | | | | | | |
| Test | | | | | | |
| Production | | | | | | |

- Evidence that all three exist and isolation was checked before implementation:
- Access denial, mutable-data isolation and external-effect checks, dates and results:
- Shared infrastructure/public assets and boundary rationale, if applicable:
- Production-derived data authorization and controls, if applicable:
- Application/deployment identity separation, target permissions, authorization, lifetime and audit evidence:
- Test/Production differences, material risk and verification treatment:
- Gaps, responsible owners, remediation and governed exception references:

## Candidate and promotion evidence

For each release, link the candidate source revision and immutable artifact/digest where applicable; Test results; configuration differences and verification; scoped production approval; actual promoted identity; deployment, observation and verification results; recovery readiness and any recovery decision/results. Link release notes and operational handoff.

Before the first release, explicitly record that no promotion has occurred. Preserve failed or inconclusive attempts. Changes to candidate identity require affected Test validation again under the governing standard.

## References

- [Software Environments Standard](../docs/standards/software-environments.md)
- [Deployment Strategy](../docs/standards/deployment-strategy.md)
- [Rollback Strategy](../docs/standards/rollback-strategy.md)
- [Roles and Actor Assignment](../docs/standards/roles-and-actor-assignment.md)
- [Three-environment Example](../examples/end-to-end-playbook-example.md#three-environment-preparation-record)
