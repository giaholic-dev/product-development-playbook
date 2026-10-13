# Executable Protocol Reference Example

## Purpose and scope

Illustrate one fictional, bounded software-product increment across Foundation through Maintenance in human-only, AI-assisted, and partially capable Integration contexts. This is an Example, not a prescribed workflow, application, adapter, provider guide, or multi-agent framework. No described research, configuration, implementation, approval, or release actually occurred.

Use the [Master Execution Checklist](../docs/standards/master-execution-checklist.md) for activity navigation and its [record template](../templates/master-execution-checklist-record.md) for contextual evidence. The existing [checklist walkthrough](master-execution-checklist-walkthrough.md) enumerates the 33 activities; this example adds attempt, assignment, capability, and handoff context without redefining those sources.

## Increment and contextual Assignments

The fictional increment lets a library member view a reservation status. Creating or changing reservations is outside scope. Evidence names below denote fictional records within this narrative, not files or external actions that exist.

Mara, a human Actor, has the Accountable Owner Assignment for material increment decisions and completion declarations, and a separate Contributor Assignment for product and implementation work. Lin, another human Actor, has a scoped Reviewer Assignment for experience, implementation, and evidence review. Mara holds a separately recorded Approver Assignment and Authority for this increment's release decision; neither contribution nor review grants that Authority. The project records any applicable separation-of-duties requirements before combining Roles.

In the AI-assisted context, Assistant A receives a Contributor Assignment for drafting experience alternatives and test ideas. Assistant B receives a distinct Contributor Assignment for identifying documentation gaps. Delegation records link their scope to Mara's originating Assignment. Neither may change external records, approve work, publish, or declare completion. Mara's Accountability remains traceable; two agents contributing do not replace the Accountable Owner. Lin reviews the human-validated outputs. In human-only execution, people perform the same scoped work with the same governing obligations.

These are contextual choices under [Roles and Actor Assignment](../docs/standards/roles-and-actor-assignment.md), not fixed phase Roles. [AI Collaboration](../docs/standards/ai-collaboration.md) governs the assisted context and manual fallback; AI is optional.

## Execution and evidence boundary

For each material attempt, the narrative identifies relevant inputs, preconditions, independent authorization and capability checks, observable result, postcondition examination, and evidence linkage under the [Execution Protocol](../docs/standards/execution-protocol.md). It does not prescribe that every attempt needs the same depth or record format.

A result or verified external change is not automatically work Validation, Approval, Completion, release, or Re-entry. Those decisions remain governed by [Work Management](../docs/standards/work-management.md), [Definition of Ready](../docs/standards/definition-of-ready.md), [Definition of Done](../docs/standards/definition-of-done.md), and the lifecycle sources. Handoffs preserve context and unresolved conditions without transferring Accountability or Authority.

## Foundation

Source: [Foundation activities F1–F5 and gates](../docs/lifecycle/01-foundation.md), [checklist Foundation entries](../docs/standards/master-execution-checklist.md#foundation).

The inputs are the bounded idea and selected version-control/tracking access. Mara adopts the repository baseline, scoped Assignments, planning model, review/readiness/completion gates, English documentation, and reachable entry point. The fictional conformance record, repository observation, and workflow record evidence the outputs. Lin examines them against Foundation's completion and exit criteria before Product begins.

Human-only: Mara prepares and verifies these records manually. AI-assisted: the two Assistants may propose missing documentation references within their Assignments; Mara examines the proposals and Lin reviews the adopted evidence. A draft is an observable result, not adopted configuration.

Partially capable Integration: the fictional provider natively supports planning-field mutation, but the current connection exposes reads and documentation updates only. The two support descriptions are recorded separately under the [Integration Standard](../docs/standards/integration-standard.md). Attempt-level capability checking finds the planning update unavailable; the attempt receives an explicit Fallback disposition, without claiming an update or automatically changing work state.

The bootstrap record identifies the intended planning field, value, target, scoped Authority, unavailable operation, and evidence needed. Mara has separately established native access and Authority, performs the permitted manual update, and observes the actual target value. Lin reviews that observation. If Mara lacked access, Authority, or verification, the obligation would remain unresolved for governed Defer or Block treatment; the example would not declare Foundation complete.

The Foundation-to-Product handoff links the adopted records, observations, remaining decisions, and gate assessment. No capability category, permanent Role assignment, or provider requirement is created by this example.

## Product

Source: [Product activities P1–P6 and gates](../docs/lifecycle/02-product.md), [checklist Product entries](../docs/standards/master-execution-checklist.md#product).

The Product attempt uses accepted Foundation evidence and relevant opportunity context. Mara identifies vision, problem, users, outcome evidence, scope, and initial ordered backlog in six linked fictional records. Relevant preconditions and Authority are checked; the result is a documented product definition. Lin examines each record against Product's completion evidence. UX entry is assessed separately; Product completion does not start later phases in parallel.

Human-only: Mara drafts from the available context. AI-assisted: Assistant A suggests wording and Assistant B checks gaps; Mara separates assumptions from supported observations and adopts only examined content. Partial Integration: document reads/updates can support recording, but planning-field updates use the scoped manual path or remain explicit obligations. Successful document mutation does not prove that the backlog order changed externally.

The Product-to-UX handoff identifies the six record revisions, exclusions, material assumptions, and applicable completion/entry decisions. It preserves Mara's Accountability and Lin's review scope.

## UX

Source: [UX activities U1–U5 and gates](../docs/lifecycle/03-ux.md), [checklist UX entries](../docs/standards/master-execution-checklist.md#ux).

Mara uses Product inputs to document experience direction, user understanding, flow/structure, a proportionate paper representation, and fictional validation findings. A persona is not selected; the source's optionality is preserved. Lin reviews whether the evidence supports the architectural decision at hand and records an unresolved accessibility question with owner, impact, and reassessment condition.

Human-only: people prepare and assess the fictional representations. AI-assisted: Assistant A proposes status-label alternatives and Assistant B notes evidence gaps; neither proposal counts as user research or validation. Mara evaluates the suggestions against the fictional findings. Partial Integration: reading a truncated research record cannot satisfy a contract requiring complete evidence; an authorized complete observation or manual source inspection is needed before relying on it.

The UX-to-Architecture handoff carries findings, selected representation, applicable constraints, residual question, and the entry assessment. A handoff does not imply that the recipient approved the work or received new Authority.

## Architecture

Source: [Architecture's four activity bullets and gates](../docs/lifecycle/04-architecture.md), [checklist Architecture entries A1–A4](../docs/standards/master-execution-checklist.md#architecture).

The fictional records define boundaries, data/interfaces and quality constraints, compare material options, identify technical risks and required checks, and link architecture-enabling backlog work. Mara records a decision adequate for the bounded increment; Lin evaluates its evidence. Any uncertainty retains an owner, impact, and reassessment condition. Ready development work and the phase exit condition are examined separately.

Human-only: the same records are prepared without AI or Integration. AI-assisted: bounded suggestions remain contributions, with human examination before adoption. Partial Integration: permission to read an architecture record is not permission to overwrite it; the attempt independently checks the authorized revision and content scope. Unavailable or unverified writes are not represented as updated constraints.

The Architecture-to-Development handoff preserves the selected source revisions, decision rationale, risk checks, work scope, and applicable readiness evidence. It does not freeze all future design choices.

## Development

Source: [Development activities D1–D4 and gates](../docs/lifecycle/05-development.md), [checklist Development entries](../docs/standards/master-execution-checklist.md#development).

The fictional implementation attempt starts with ready bounded work, applicable constraints, and scoped Authority. It produces a changed increment and linked test observations. Lin's review record identifies examined revisions, behavior, validation, and findings under [Code Review](../docs/standards/code-review-standard.md). Mara records the integration decision after governing conditions are satisfied. Follow-up records preserve limitations or debt.

Human-only: people implement, verify, and review. AI-assisted: Assistant A proposes test cases; Assistant B reviews documentation gaps as a Contributor, not an independent Reviewer. Mara checks and incorporates applicable suggestions. Multiple proposals do not collectively establish approval, completion, or accountability transfer.

Partial Integration: an update acknowledgment does not prove that content changed. A permitted observation compares target and revision to the intended postcondition. A timeout leaves the effect ambiguous; Mara reconciles the existing revision before any repeat. The originating attempt retains its actual result and evidence. Only subsequently verified and reviewed work can meet the applicable completion/integration criteria.

The Development-to-Release handoff links integrated revision, tests, Lin's review, integration decision, accepted risks, and required release evidence. A PR or automation success is evidence only for its examined scope.

## Release

Source: [Release activities R1–R5 and gates](../docs/lifecycle/06-release.md), [checklist Release entries](../docs/standards/master-execution-checklist.md#release).

Mara identifies audience, scope, release identifier, conditions, communications, and recovery path. Lin reviews readiness evidence. Mara's explicit release approval is a separate scoped decision under the recorded Approver Assignment; implementation or review alone does not supply it.

Human-only: authorized publication and observation are performed manually. AI-assisted: the Assistants may draft notes within scope; Mara validates their content and retains publication/approval responsibility. Partial Integration: native provider publication support is distinct from a connection that exposes only release reads. The unavailable publish attempt receives permitted Fallback treatment. Mara uses independently authorized native publication and verifies source identifier and audience availability. Read support is not publication support.

In this fictional narrative, initial observation finds an older status label served to users. The recovery attempt has its own inputs, Authority and capability checks, observed correction, postcondition evaluation, and evidence. It does not rewrite the first attempt as successful. Release completion and Maintenance entry are assessed only after availability, information, operational ownership, feedback intake, and remaining obligations are evidenced.

The Release-to-Maintenance handoff preserves publication and recovery observations, release notes, operating responsibility, known risks, and follow-up ownership. No approval right silently transfers with the handoff.

## Maintenance

Source: [Maintenance activities M1–M4 and gates](../docs/lifecycle/07-maintenance.md), [checklist Maintenance entries](../docs/standards/master-execution-checklist.md#maintenance).

Fictional feedback records continuing status-label confusion. Mara assesses signals, coordinates a proportionate response, creates traceable improvement work, and updates operational knowledge. Lin examines the response and evidence. The maintenance increment records its outcome and obligations; the active product still requires ongoing maintenance.

Human-only: people receive and assess the feedback. AI-assisted: proposed grouping or wording from the Assistants is examined by people and never treated as an authoritative user signal on its own. Partial Integration: unavailable work-tracking mutation receives governed treatment; an authorized manual record retains the same evidence and ownership obligations where permitted.

Work Management independently determines Re-entry to Product and UX for the improvement. The originating release attempts and their evidence remain historical; feedback does not automatically reopen work, transition protocol state, or authorize a retry. The re-entry handoff links the assessed need, prior results, next bounded work, and accountable decision. Any later attempt independently satisfies its governing conditions.

## Validation and ownership review

This narrative was checked against all seven phase sources, the 33 checklist entries, and the linked standards. Every phase identifies the applicable inputs/results, evidence/gates, three execution contexts, and accountable handoff boundaries. Optional representations remain optional.

The Roles standard owns contextual Assignments and Authority; the Execution Protocol owns attempt checks, results, dispositions, evidence linkage, and handoff semantics; Integration owns provider/current-connection support separation and Verification; Work Management and completion sources own work decisions. No example label creates a parallel protocol, universal transition, or fixed lifecycle owner.

Unavailable planning and publication capabilities demonstrate permitted manual bootstrap and verified results without claiming that the connector performed them. Partial reads and ambiguous writes retain uncertainty. Multi-agent contributions preserve one identifiable Accountable Owner and distinct contribution/review/approval responsibilities.

Validation is conceptual and fictional. It does not prove production execution, native configuration, provider conformance, parser readiness, or real review/approval. The human-readable source boundaries remain authoritative under the [representation decision](../docs/practices/machine-readable-execution-decision.md).

## References

- [Master Execution Checklist](../docs/standards/master-execution-checklist.md)
- [Roles and Actor Assignment Standard](../docs/standards/roles-and-actor-assignment.md)
- [Execution Protocol Standard](../docs/standards/execution-protocol.md)
- [Provider-independent Integration Standard](../docs/standards/integration-standard.md)
- [Provider Implementation Guide Standard](../docs/standards/provider-implementation-guide-standard.md)
- [Artifact Standard](../docs/standards/artifact-standard.md)
- [AI Collaboration Standard](../docs/standards/ai-collaboration.md)
