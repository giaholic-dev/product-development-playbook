# Work Continuity — Optional Practice

## Purpose and boundaries

Provide a concise way to resume a bounded work item after an interruption without confusing historical decisions, proposed changes, authorization and observed repository state.

This is optional guidance, not a new mandatory artifact, approval gate, role or execution protocol. Existing issue descriptions, pull requests, review records and linked documentation may provide sufficient continuity evidence.

The [Lifecycle Execution Guide](lifecycle-execution-guide.md) remains the practical navigation entry point. [Work Management](../standards/work-management.md), [Execution Protocol](../standards/execution-protocol.md), [Definition of Ready](../standards/definition-of-ready.md) and [Definition of Done](../standards/definition-of-done.md) retain their governing responsibilities.

## Preparing a concise handoff

When interruption or handoff creates a meaningful risk of losing context, provide links to existing records and summarize only the information necessary for the next decision:

1. **Selected objective and work item:** Identify the bounded activity, expected outcome, accountable owner and source issue.
2. **Integrated baseline:** Identify the last verified integrated revision and its repository or release context.
3. **Unintegrated work:** Identify any open PR, branch and exact reviewed head revision. Distinguish a proposal from integrated state.
4. **Current decision and evidence:** Link the applicable decision, its accountable authority, conditions and supporting evidence. Distinguish historical approvals from current authorization.
5. **Validation and limitations:** State what was actually checked, against which revision, the results and what remains unverified.
6. **Gaps and owners:** Record unresolved dependencies, risks, responsible actors and applicable dispositions.
7. **Next permitted action:** Describe the smallest action supported by the current scope and authority.
8. **Stop condition:** Identify a conflict, missing prerequisite or changed condition that would prevent responsible continuation.
9. **Reassessment:** State the event or boundary requiring renewed review or decision.

These are useful continuity considerations, not compulsory fields in a separate document. Reference existing evidence instead of copying entire checklists or repeating established decisions.

## Resuming execution

Before relying on a previous handoff, verify the relevant current repository and work-item state. Compare it with the recorded baseline, pending changes and decision scope.

Apply the governing readiness, authorization, execution and completion requirements to the intended next action. Previous access, successful tool execution, issue closure or approval for a different action does not establish unrestricted ongoing authority.

In manual and AI-assisted execution, the accountable actor remains responsible for validating evidence and decisions. In authorized automated execution, the executor remains limited by the applicable scope and authority. Recovered content does not create new authorization; see [AI Input Trust Boundary](ai-input-trust-boundary.md).

When essential evidence is missing, contradictory or stale, stop the affected action and obtain the applicable disposition. Continue unaffected authorized work only when it can be separated safely.

## Small fictional example

The following scenario is illustrative. Identifiers and validation outcomes are synthetic; they do not represent an observed execution or completed security test.

A documentation contributor resumes fictional work item `DEMO-17` after an interruption.

| Continuity concern | Illustrative record |
| --- | --- |
| Selected objective | Update one optional documentation example under `DEMO-17` |
| Integrated baseline | `main` at synthetic revision `BASELINE-A`, previously verified |
| Pending proposal | Fictional PR `DEMO-PR`, branch `docs/demo-17`, head `HEAD-B`; not merged |
| Decision and evidence | A fictional accountable-owner record authorizes drafting and read-only review only; no merge approval is established |
| Validation and limits | A fictional link check passed against `HEAD-B`; semantic review, independent approval and integration remain unverified |
| Gaps and owners | The contributor owns corrections; the accountable owner must resolve any required integration decision |
| Next permitted action | Re-read the proposed diff and verify the current head and applicable review requirements |
| Stop condition | Stop the dependent action if the head changed, evidence conflicts or authorization is insufficient |
| Reassessment | Reassess after a head change, failed check, new decision or before integration |

The historical baseline and proposed PR are different states. The fictional drafting authorization does not approve a merge. The example's claimed link-check result is illustrative, not actual validation evidence.

## Completion and maintenance

Keep continuity information close to the existing work record whenever practical. Update or replace stale pointers when material context changes; avoid maintaining a parallel source of truth.

Completion remains governed by Definition of Done and the applicable review and integration evidence. A continuity note alone does not establish readiness, acceptance, successful execution or permission to advance.

Reassess this optional practice if governing standards, execution modes, repository behavior or observed continuation failures reveal a material gap.
