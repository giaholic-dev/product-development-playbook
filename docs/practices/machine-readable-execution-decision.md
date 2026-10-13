# Machine-readable Execution Representation Decision

## Purpose and scope

Record the representation-boundary decision for issue #281. This is a Documentation — Decision Record, not an execution schema, application architecture, or new normative methodology. Its proposed decision takes effect through the reviewed repository integration record; it does not authorize external execution.

## Context

Assessment baseline: repository commit `3b8129a1c97dfc8752cd93d8efe61c3a928aebfe`, reviewed on 2026-10-13.

The [Execution Protocol](../standards/execution-protocol.md), [Work Management](../standards/work-management.md), [Roles and Actor Assignment](../standards/roles-and-actor-assignment.md), [Integration Standard](../standards/integration-standard.md), and [Master Execution Checklist](../standards/master-execution-checklist.md) now provide distinct governing boundaries. The checklist exposes ten consistent fields for all 33 current lifecycle activities, with a [human-readable application template](../../templates/master-execution-checklist-record.md) and [fictional walkthrough](../../examples/master-execution-checklist-walkthrough.md).

Publication and structured headings are evidence of documented boundaries, not proof that they are stable enough for a machine model. The broader executable protocol example in [#282](https://github.com/giaholic-dev/product-development-playbook/issues/282) remains pending. [#292](https://github.com/giaholic-dev/product-development-playbook/issues/292) proposes assessing product-type assumptions and universal/specialized boundaries; it does not yet change the existing software-product lifecycle.

The [GitHub guide](github-reference-implementation-guide.md) also shows that exposed provider capabilities can differ materially from native support. A machine representation could conceal that contextual uncertainty if treated as an executable instruction or automatic state transition.

## Decision

Defer a new machine-readable schema or manifest. Retain the existing linked Markdown checklist and records as directly usable human-readable material with consistent structure. Do not establish a parser contract, mandatory data format, generated representation, or machine-execution source through this decision.

A future representation may be non-authoritative and derived from explicitly identified source revisions, but its design requires a separate bounded proposal and review. No additional representation is justified within #281 at this time. Deferral is the research outcome; it does not mean the existing standards are unavailable or unusable.

## Options and evidence

- New schema/manifest now: could assist tooling, but there is no reviewed representation contract, migration model, complete cross-context reference example, or evidence that product-type evolution will preserve the same boundaries. It would risk duplicating source definitions and implying fixed states, Roles, or transitions.
- Formal parser contract for current Markdown: would reuse existing structure, but heading and entry consistency alone does not establish stable identifiers, parser error behavior, contextual applicability, or version compatibility. It is deferred alongside schema work.
- Existing portable Markdown with explicit source links: already supports human-only use and navigation. It preserves primary owners without introducing a second semantic authority. This is the selected current approach.

## Source ownership and drift prevention

The lifecycle documents remain owners of phase activities, inputs/outputs, and entry/exit criteria. Roles and Actor Assignment owns responsibility and Authority. Work Management owns Validation, Completion, and Re-entry. Execution Protocol owns attempt-level semantics. Integration owns capability contracts and contextual support. The checklist remains a navigational index rather than another source of those rules.

While deferred, changes are reviewed at their primary owners and related navigation is updated. A future derived representation would need to identify source revisions, use references instead of parallel definitions, expose missing or changed source links, and make conflicting or stale content unusable as verified current evidence. Machine-to-source edits, silent semantic synchronization, and automatic completion decisions are not established here.

## Validation, migration, and portability implications

No schema is introduced, so no data migration or backward-compatibility promise is created now. Existing human-readable records remain usable under their governing sources.

Before reconsidering a representation, its bounded proposal would need evidence for semantic/source traceability, identifier and revision handling, validation of broken links and incomplete fields, explicit unknown/partial capability handling, compatibility and migration consequences, and readable failure reporting. Validation would compare a derived view to its exact authoritative source revision; it would not treat parser success as Authority, Verification, Approval, or Completion.

Provider-native identifiers and status fields would remain mapping data, separate from Playbook identities and meanings. Portability review would include a provider-independent use and a materially different provider mapping. No queue, transport, storage system, adapter, event model, or runtime is chosen by these implications.

## Scenario review

- Human-only: a person follows the checklist links and retains evidence in the existing record template. The absence of a schema does not remove any source requirement or require AI/tool adoption. Readiness and completion remain separately evidenced.
- Partially capable Integration: a planning-field update may be native-provider Supported but current-connection Unsupported. The Markdown record can preserve this distinction and the unresolved obligation or permitted manual fallback. Deferral prevents a structured record from being mistaken for successful execution; the governing protocol and work decisions still apply.
- Alternative provider: another guide maps different objects to the same governed need and contracts. Existing source links retain their meaning; provider labels do not become normative. No schema locks the core model to a particular provider's object or state catalog.

These are conceptual reviews, not executions of providers or validation of a parser. All three scenarios preserve human-readable ownership and contextual decision boundaries.

## Consequences and follow-up

Machine consumers receive no supported interchange format or execution contract from this decision. They may inspect the existing documents, but cannot claim schema conformance or automatic execution readiness based on this record.

Reassess when the #282 reference example is reviewed, the relevant #292 architectural boundaries have an evidenced outcome, and a concrete consumer need justifies a bounded representation proposal. Reassessment may still choose deferral; completion of an issue alone does not prove semantic stability. Earlier source revisions and decisions retain their provenance.

## Accountability and review

- Decision scope: representation boundary for #281 at the stated baseline.
- Approval and accountable decision owner: the repository maintainer authorizing integration of the linked #281 change; the PR approval/integration record identifies that Actor and decision. This record does not assign permanent runtime or representation ownership.
- Review: recorded conceptual self-review of the three scenarios and the applicable source boundaries, not independent approval or production validation.
- Reassessment: the evidence conditions above, or a material change to the governing model or concrete representation need.
- AI involvement: drafting and evidence synthesis within the user's authorized repository work; integration requires explicit user authorization. The same decision can be reviewed and maintained manually.

## References

- [Decision Record Template](../../templates/decision-record.md)
- [Artifact Standard](../standards/artifact-standard.md)
- [Definition of Done](../standards/definition-of-done.md)
- [Provider Implementation Guide Standard](../standards/provider-implementation-guide-standard.md)
