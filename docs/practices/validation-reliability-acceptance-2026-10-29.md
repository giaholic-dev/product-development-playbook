# Validation Reliability — corrective-lot acceptance, 2026-10-29

## Boundary and decision

AP11 / [#381](https://github.com/giaholic-dev/product-development-playbook/issues/381) accepts AP00–AP03 only, with explicit dispositions for AP04–AP10 below. Accountable owner: @giaholic. Execution and review are AI-assisted solo review, not independent approval.

Adopted **unreleased** source: [`9ac4f6027095ceeb54f425bb7333c15bec678d2d`](https://github.com/giaholic-dev/product-development-playbook/commit/9ac4f6027095ceeb54f425bb7333c15bec678d2d). It includes #383, #384 and #385 plus the test-fixture chronology correction identified in this aggregate review. The acceptance-documentation PR records the final candidate, exact-head CI, integration decision and merged-tree verification; its documentation-only follow-up does not change the accepted validator behavior. Previous published/adopted baseline: v0.8.0 / `cb18da31a79eebf192b38bc815aff905a5ef5a56`. Preserve that tag and its assessments.

Distribution decision: **no new tag or release selected for this increment**. Latest published release remains v0.8.0; use the immutable unreleased revision for these fixes. This is a source adoption and bounded correction, not publication or proof of whole-lifecycle efficacy.

## Criteria and evidence

| Action | Combined result and evidence |
| --- | --- |
| AP00 / #370 | Current-source reproductions, original-report provenance gap, ownership and corrective sequence recorded. Fresh evidence does not claim recovery of the unavailable historical review. |
| AP01 / #371, PR #383 | Invalid temporal evidence fails PR verification and aggregate seal/verify; valid controls, UTC-equivalent offsets, generation precision and supported historical-version synthetic fixtures pass. |
| AP02 / #372, PR #384 | Supported labels normalize case/whitespace; first definition wins, including both duplicate orders, fragments, images/collapsed references and undefined-label controls. |
| AP03 / #373, PR #385 | Exporter-root output pruning preserves maintained-tree results with synthetic archived/staged convenience/source copies. Broken maintained links still fail; non-Git --root and explicitly selected archived roots work as documented. Archived bytes remain unchanged. |

All 144 source blobs of the integrated pre-review baseline `643a59a954826a25af2bf602d5548e315f08fbdc` were checked against its Git tree. The full checker passed **118 Markdown files / 2313 local links** before adding this record.

Aggregate execution exposed four intermittent compatibility-test subcase errors: those tests regenerated Project observations after the fixture manifest's generation time. Correct validation rejected that stale synthetic chronology. The acceptance correction generates a new synthetic manifest after collecting each new fixture; it does not relax production validation or alter historical evidence. The same fix keeps the computed-metadata success/foreign-parent tests testing their intended relation rather than an accidental timestamp failure.

After that correction, the complete suite passed **95 tests** (Python 3.13.7, macOS arm64, 12.811s). Python syntax and Bash syntax were checked. Local `check-export-audit.sh` could not run fully: `shfmt` and `shellcheck` are unavailable, and its prerequisite check failed. This is not a local pass. The final PR's ShellCheck job runs that command with installed dependencies on Ubuntu/Python 3.12; its actual result is required and recorded before integration. Documentation CI likewise validates the final maintained tree. No live/provider/private export was run.

## Compatibility, notes and adopter action

- No governing standard changed. Schema 2.0.0, source inventory 1.0.0 and PR evidence 1.1.0 serialization remain unchanged. Existing eligible exporter identifiers 2.0.0–2.0.3 and 2.1.0 are not a guarantee that malformed evidence from those versions passes. Source revision distinguishes this unreleased implementation; any later release/tool-version assignment needs its own distribution decision.
- Temporal validation is intentionally stricter. Preserve old packages, timestamps and prior results. If current verification fails, record that failure and its scope; do not fabricate dates or re-seal an old package as if it were its original. A failed seal leaves the old manifest bytes, potentially including an old true flag, unchanged; only a successful current verifier supports a current completeness claim.
- Whole-second manifest generation describes its containing second; fractional values are exact upper bounds. Collectors remain interval observations, not atomic snapshots. No real historical private archive was inspected; compatibility evidence is synthetic.
- Markdown duplicate definitions now follow the first normalized label. Repair a broken first target rather than relying on a later duplicate.
- Output exclusion is root-relative to `audit/exports/` and `audit/.staging/`. Relocated archives are not automatically excluded. A deliberately selected archived --root remains an explicit standalone inspection.
- Adoption applies to this methodology repository's standards/mappings and support tools. It does not create a served runtime, production database, actual restore evidence, or readiness of an adopting product. Existing runtime/environment/stateful obligations remain governed by their original owners.

## Remaining-work dispositions

The following actions are **deferred beyond this selected corrective lot**, not cancelled, implemented or certified. Their issues remain open in their own milestones. Owner for every row: @giaholic. Reassess on the trigger below or an earlier material change. These dispositions permit bounded corrective acceptance without silently promising optional capability delivery.

| Action | Reason and residual risk | Reassessment trigger |
| --- | --- | --- |
| AP04 / #374 | Current-decision navigation cleanup is outside the defect corrections; stale-summary risk remains. | Next selection of documentation maintenance after this acceptance, or a material F01–F04 decision change. |
| AP05 / #375 | Trust-boundary research/runtime validation is not delivered by validator fixes; no autonomous-safety claim. | Before expanding automation with material effects, or when this research is selected. |
| AP06 / #376 | Short continuity guidance depends on AP04 and the AP05 decision; restart ambiguity remains. | Those prerequisites are recorded and guidance is selected. |
| AP07 / #377 | Requires AP06 and a real authorized bounded task; empirical restart success remains unproved. | A permitted case, data boundaries and method are available after AP06. |
| AP08 / #378 | Enforcement assessment remains separate; no administrative protection is changed or certified. | Next integration-control decision, bypass incident or protection change. |
| AP09 / #379 | Automation awaits a reviewed navigation/index/checklist contract and explicit selection; structural maintenance still needs review. | Contract approved and automation selected; AP02/AP03 are now complete prerequisites. |
| AP10 / #380 | Dependency reproducibility choices remain undecided; external-environment variability remains. | Next CI/devcontainer/dependency update or reproducibility incident. |

Retained-branch reassessment [#382](https://github.com/giaholic-dev/product-development-playbook/issues/382) remains separate ongoing maintenance, due by 2026-11-05 or before reuse. No deletion is claimed. Optional milestones remain open; dispositions are not delivery percentages or automatic Ready states.

## Limits and reassessment

The three reported defects have targeted positive/negative regression evidence and integrated review records. This acceptance is not exhaustive security, Markdown, provider-history or product conformance certification. Original review/fixture recovery remains unavailable; AP00 documented the gap and established fresh observations. No exception waives an applicable standard.

Reassess this adoption on source/contract/provider/schema/operating-context change, a failed validation, optional work selection, or a proposed release. Full implementation of the broader plan remains open work even when this corrective acceptance and its disposition record are complete.

