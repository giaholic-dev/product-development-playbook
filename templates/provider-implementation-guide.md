# Provider Implementation Guide

## Purpose

Use this non-normative template to document an optional provider mapping under the [Provider Implementation Guide Standard](../docs/standards/provider-implementation-guide-standard.md). Replace the instructions with scoped evidence and links. Completing the template does not establish support, Authority, configuration, Verification, or Conformance.

## Identity and scope

Identify the provider, audience, current Integration or execution environment, included capabilities, exclusions, and versions or observation date. State that the guide is replaceable implementation guidance and does not redefine the Playbook.

## Governing sources and concepts

Link each governed need and Capability Contract to its primary owner. Identify relevant provider concepts, mappings, limits, and losses of meaning. Preserve lifecycle and artifact semantics.

## Capability mapping record

Repeat this record for each material Capability:

- Governed need and contract: identify scope and source.
- Provider mapping: identify relevant objects or operations and constraints.
- Provider support: state the evidenced contextual support description, source, date or revision, and limits.
- Current Integration support: separately state its evidenced description, exposed scope, permissions, context, and limits.
- Unknowns and reassessment: identify missing evidence and conditions that require a fresh assessment.
- Authority and approval: link applicable permission or decision sources; distinguish those from access settings.
- Configuration: identify prerequisites, options, target identity, and verification evidence without recording secrets.
- Instructions and expected result: describe the bounded action, preconditions, postconditions, and relevant contract references.
- Verification and evidence: identify the external observation, completeness checks, evidence location, and limits.
- Failure and repetition: link applicable rejection, partial/ambiguous outcome, reconciliation, and repeat/idempotency treatment.
- Manual or alternative fallback: identify the permitted approach, preserved obligations, or explicit unresolved requirement.
- Conformance review: identify what was validated, the outcome, limits, and separate work Validation or completion sources.

Use only the support meanings governed by the [Integration Standard](../docs/standards/integration-standard.md#discovery-and-support-descriptions). Mark hypothetical content as hypothetical and unperformed operations as unverified.

## Ownership and maintenance

Identify the maintained source, responsible owner, evidence provenance, review outcome, known gaps, and reassessment trigger. Changes in the provider, connection, permissions, configuration, or governing sources may invalidate earlier observations; retain their provenance without presenting them as current evidence.

## References

- [Provider Implementation Guide Standard](../docs/standards/provider-implementation-guide-standard.md)
- [Provider-independent Integration Standard](../docs/standards/integration-standard.md)
- [Security, Privacy, and Data Governance Standard](../docs/standards/security-privacy-data-governance.md)
