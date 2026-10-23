# Product Development Playbook

A practical, technology-agnostic framework for turning an idea into a software product and evolving it over time.

## What is it?

> "If I have an idea today, how does it become a product?"

The Product Development Playbook defines the concepts, lifecycle, practices, and standards that guide software product development from inception to long-term maintenance.

## Vision
Enable individuals and teams to build software products through a consistent, technology-agnostic, and continuously improving development process.

## Mission
Establish a standardized and repeatable approach to software product development that can be applied across projects, teams, and technologies.

## Scope
This Playbook defines:
- Product development lifecycle
- Engineering governance
- Engineering standards
- Product management practices
- Documentation standards
- Decision-making processes

The Playbook intentionally remains independent of:
- Programming languages
- Frameworks
- Platform-specific architectures
- Tool-specific implementations

The conceptual method is independent of hosting vendors. This repository deliberately uses Git and includes GitHub mappings and supporting automation as implementation guidance, not as product-technology requirements.

The Playbook supports manual, AI-assisted, and authorized AI-automated execution. No lifecycle phase, standard, or workflow requires an AI provider, model, prompt, integration, or automation platform; every execution mode follows the same accountability, evidence, review, and completion rules.

## Documentation Language

The primary documentation language of this repository is English.

## Repository adoption

The [Repository Conformance Declaration](docs/practices/repository-conformance-declaration.md) records this repository's adopted standards, local mappings, accountable owner, execution practice, validation evidence, and review limits. It is distinct from the reusable conformance template and does not certify execution of an adopting product.

## Start Here

For a first reading of the Playbook, follow the documents that exist today:

1. [Foundation Phase](docs/lifecycle/01-foundation.md)
2. [Repository Standards](docs/standards/repository-standards.md)
3. [Work Item Taxonomy](docs/standards/work-item-taxonomy.md)
4. [Work Item Types](docs/standards/work-item-types.md)
5. [Project Views](docs/standards/project-views.md)
6. [Product Phase](docs/lifecycle/02-product.md)
7. [UX Phase](docs/lifecycle/03-ux.md)
8. [Architecture Phase](docs/lifecycle/04-architecture.md)
9. [Development Phase](docs/lifecycle/05-development.md)
10. [Release Phase](docs/lifecycle/06-release.md)
11. [Maintenance Phase](docs/lifecycle/07-maintenance.md)
12. [Product Vision](docs/standards/product-vision.md)
13. [Problem Statement](docs/standards/problem-statement.md)
14. [Users](docs/standards/users.md)
15. [Outcomes](docs/standards/outcomes.md)
16. [Product Scope](docs/standards/product-scope.md)
17. [Product Backlog](docs/standards/product-backlog.md)

The [Documentation Navigation Standard](docs/standards/documentation-navigation.md) describes how entry points, related links, and link checks should work. For operational navigation, use the [Master Execution Checklist](docs/standards/master-execution-checklist.md), its [reusable record template](templates/master-execution-checklist-record.md), and the [fictional validation walkthrough](examples/master-execution-checklist-walkthrough.md). Checklist coverage does not establish execution or completion of a product. For practical reading selection, documentation sufficiency, and progression questions, use the optional [Lifecycle Execution Guide](docs/practices/lifecycle-execution-guide.md). The audit exporter is optional technical reading, not a prerequisite. The [Stateful Recovery and Migration Decision](docs/practices/stateful-recovery-decision.md) records the selected design input for O02–O04; its integration status is distinct from implementation or release acceptance.

## Lifecycle

The Product Development Playbook defines a complete conceptual lifecycle with seven ordered phases:

1. Foundation
2. Product
3. UX
4. Architecture
5. Development
6. Release
7. Maintenance

Progression is ordered but not irreversible: new evidence or changes may require revisiting an earlier phase. All seven lifecycle phases currently have documents. The current phase and completion status of this repository are reported separately below.

## Audience
This Playbook is intended for:
- Individual developers
- Product managers
- Small teams
- Engineering teams
- Anyone building software products using an iterative process

## Repository Structure

Current directories:

- `docs/core/` — Enduring principles and conceptual boundaries
- `docs/lifecycle/` — Existing lifecycle phase documents
- `docs/standards/` — Reusable repository, documentation, and product standards
- `examples/` — Concrete applications and case studies
- `templates/` — Reusable starting material
- `docs/practices/` — Operational guidance that applies standards
- `.devcontainer/` — Reproducible GitHub Codespaces environment.
- `scripts/` — Supporting implementation utilities. Run `bash scripts/check-export-audit.sh` in a configured Codespace to check shell syntax, formatting, linting, and regression fixtures.

The [Documentation Information Architecture](docs/standards/documentation-information-architecture.md) defines these responsibilities without requiring fixed directory names or placeholder content.

## Documentation checks

Repository maintainers own the standard-library Python checker and its regression cases. With Python 3.12 or later, run `python3 scripts/check-documentation.py` and `python3 -m unittest discover -s scripts -p test_check_documentation.py`. The Documentation checks workflow runs for Markdown, checker, tests and workflow changes in pull requests and on main; it can also be dispatched manually. Failures report a source location and return a nonzero exit status. Fix the target or heading rather than disabling the check.

The checker validates relative inline/image links and explicit reference links, local target existence, and fragments for ATX Markdown headings, including duplicate headings. It ignores fenced/indented code examples and inline code when scanning links, and does not fetch external URLs. It supports the repository's current Markdown conventions; HTML anchors, Setext headings, shortcut reference links and complex nested/escaped Markdown destinations are outside its parser contract. Changes using those forms require explicit review and checker support before relying on automation. Existing directories may be navigation targets; fragments on non-Markdown targets are not interpreted.

Reachability and index coverage remain manual review responsibilities under [Documentation Navigation](docs/standards/documentation-navigation.md). They were considered separately from local-link integrity: automated enforcement would need an agreed navigation-root/index contract. Passing this check does not validate meaning, conformance, completeness or lifecycle progression.

## Audit exporter

The [Audit Package Coverage and Compatibility Contract](docs/practices/audit-package-contract.md) governs the v0.7.0 implementation target. The exporter is tool 2.0.1 / manifest 2.0.0: committed source, repository records, distinct PR conversations/reviews/inline comments, typed Project values and aggregate coverage/integrity checks are implemented. Full-profile completeness is derived only after all required authorized observable collections and relationships pass validation. A06 live comparison and release acceptance remain pending; exporter implementation is not publication of v0.7.0 or governance certification.

[`scripts/export-audit.sh`](scripts/export-audit.sh) creates a timestamped, offline audit package for the current Git repository.

Requirements: Git, GitHub CLI (`gh`), `jq`, and Python 3.12 or later (standard library only). Review the selected repository/Project data, committed-source sensitivity, output destination and retention before exporting. The bounded credential/path checks do not guarantee secret-free content. Authenticate with `gh auth login`, ensure the account has authorized read access, then explicitly confirm the source-scope review:

```bash
GITHUB_AUDIT_SOURCE_REVIEWED=true bash scripts/export-audit.sh
```

The committed-source snapshot is retained at `repository/source/`, with every tracked path's disposition, object/mode, retained-byte SHA-256/size and observation interval in `repository/source-inventory.json`. Bytes come from the once-resolved HEAD object tree; staged, unstaged, ignored and untracked working files are excluded even when the working tree is dirty. Protected/output paths are inventoried without contents. Required-source exclusions or missing required Git LFS/submodule content fail; other pointers/gitlinks remain explicitly incomplete constituent evidence. Symlinks are inert regular files containing only their target bytes. Legacy selected-document copies use these committed bytes, and the convenience tree lists JSON-escaped paths. No external source is fetched. Final source verification rejects changed HEAD, missing/tampered files or inventory.

The helper uses four-space Python style, snake_case names, standard-library dependencies and sanitized exceptions. Run `python3 -m unittest discover -s scripts -p test_audit_source.py` for synthetic isolated Git-repository tests. The exporter checker/CI includes these tests; it does not contact GitHub. Schema/tool 2.0.0 requires complete declared source/record/PR/Project evidence. Legacy 1.x packages remain limited historical evidence; preserve them unchanged and create a new explicitly authorized export to obtain the new coverage. The verifier rejects legacy or unsupported versions for full-profile validation; no automatic conversion manufactures missing records.

PR evidence is collected for every exported PR through three distinct read-only REST collections: `github/pr-conversations.json` (general conversation), `github/pr-reviews.json` (submitted/pending reviews), and `github/review-comments.json` (inline comments and replies). Full observed payloads retain bodies, author references, timestamps, review state and reviewed commit, plus a normalized PR number. `github/pr-evidence-coverage.json` records each PR/collection traversal, HTTP success, page continuation, raw/retained counts and observation interval. The helper follows only validated GitHub next-page links within the selected repository/collection; access errors, malformed responses, conflicting duplicate IDs, foreign parents and missing inline review/reply parents fail instead of becoming empty success. Identical replayed records are deduplicated by provider ID. Offline validation checks retained relations and traversal evidence. This is evidence observable to the authorized account over an interval; it does not reconstruct deleted/inaccessible evidence, an atomic provider snapshot or the PR's current approval decision. Run `python3 -m unittest discover -s scripts -p test_audit_pr_evidence.py` for synthetic HTTP and Bash/CLI integration fixtures. No live GitHub export runs in these tests.

The ZIP contains an `exports/<timestamp>/` root with `repository/`, `git/`, `github/`, and a root `manifest.json`. The schema-2 manifest records the contract, source commit/tree/ref/policy, selected Project/principal, collection status/interval/page/count evidence, relationship checks and a SHA-256/size inventory of every payload except the manifest itself. Repository page responses are retained separately in `github/records-requests.json` with `github/records-coverage.json`; offline replay checks records against the selected target and pagination. Exact replayed records can deduplicate; conflicting provider identities fail. Shared repository/PR conversation observations must agree. Required or selected optional collection errors fail rather than become an empty success. Timeline deduplication scopes provider IDs by issue and event kind. For events without IDs, it compares the complete observed payload and removes only identical records; that comparison is local to the snapshot, not a durable event identity. Different payloads, including cross-references with equal timestamps, are preserved.

Tool 2.0.1 adds Bot and EnterpriseTeam reviewer identities alongside User, Team and Mannequin. Project evidence 1.1.0 records the updated read query; offline verification still supports the original 1.0.0 Project transcript and tool 2.0.0 packages without rewriting them. Unknown reviewer actor types fail rather than silently disappear.

Project evidence is collected by [`scripts/audit-project.py`](scripts/audit-project.py): `github/project-items.json`, `github/project-fields.json`, `github/project-values.json`, and `github/project-views.json`. Each item/field pair has a typed value or an explicit observed-unset, inapplicable or inaccessible-redacted disposition. Zero, empty text and an observed null are distinct from an absent value. Scalar/planning values, organization issue-field wrappers, completed iterations and built-in relationships retain their provider identities; foreign items retain references without fetching their bodies. Unknown types, partial GraphQL errors, missing definitions/options, changed counts/revisions and incomplete nested traversals fail. `github/project-coverage.json` retains selected Project/principal identity, query fingerprints, intervals and per-connection page evidence. `github/project-requests.json` retains only the declared scoped query responses/variables (no credentials or headers) for offline replay against normalized output and coverage. Replay checks internal consistency, not trusted authorship, atomicity or visibility of inaccessible history. Run `python3 -m unittest discover -s scripts -p test_audit_project.py` for synthetic GraphQL fixtures. These Project fixtures do not replace A06 live comparison or release acceptance.

By default, the exporter targets Organization Project #1 owned by the repository owner. Set `GITHUB_PROJECT_NUMBER` to select another project, `GITHUB_PROJECT_OWNER` for its owner login and `GITHUB_PROJECT_OWNER_KIND=user` for a user-owned Project (default `organization`). Set `GITHUB_EXPORT_DISCUSSIONS=true` only for repositories that use GitHub Discussions.

[`scripts/audit-package.py`](scripts/audit-package.py) verifies schema-2 directory packages offline, including reconstructed Git tree/blob identities, payload hashes, source/convenience copies, repository/Project replay, PR relations and local issue/PR/label/milestone joins:

```bash
python3 scripts/audit-package.py verify --package audit/exports/<run>
```

Optional Discussions has an explicit excluded disposition when disabled. When selected, its metadata/body collection is independently paginated and verified, with errors blocking completion; comments/replies/attachments/history stay outside scope. The profile covers authorized observable evidence over intervals, not atomic GitHub state, universal access or deleted history. Hashes and replay establish transport/internal consistency, not authenticity or approval.

ZIP creation and byte verification finish before publication. Final directory/archive/digest creation refuses overwrite; failure rolls back only the current run's outputs and removes staging through the guarded exit trap. A separate `<archive>.manifest.sha256` contains the final manifest digest. No final success summary is emitted on failure. Run `python3 -m unittest discover -s scripts -p test_audit_records.py` and `python3 -m unittest discover -s scripts -p test_audit_package.py` for synthetic coverage/hash/version/ZIP/rollback fixtures; CI includes them without a live export.

Audit packages can contain issue bodies, comments, and sensitive repository/Project data. The exporter uses owner-only permissions; approve the selected data/destination/retention and any disclosure separately. Retry after correcting a failure creates a new run; earlier exports remain unchanged.

## Standards

The Playbook defines reusable standards that can be adopted across software products.

### Core

- [Playbook Core Principles](docs/core/principles.md)

### Templates

- [Conformance Declaration](templates/conformance-declaration.md)
- [Software Environment Record](templates/software-environment-record.md)
- [Foundation Adoption Checklist](templates/foundation-adoption-checklist.md)
- [Master Execution Checklist Record](templates/master-execution-checklist-record.md)
- [Provider Implementation Guide](templates/provider-implementation-guide.md)
- [Exception Record](templates/exception-record.md)
- [Decision Record](templates/decision-record.md)
- [Stateful Recovery and Migration Record (optional)](templates/stateful-recovery-record.md)
- [AI-assisted Work Evidence](templates/ai-assisted-work-evidence.md)

### Releases

- [v0.6.0 release notes and M6 review](docs/releases/v0.6.0.md) — published baseline and release evidence.

### Practices

- [Playbook Upgrade Guide](docs/practices/playbook-upgrade-guide.md)
- [Data Recovery and Migrations](docs/practices/data-recovery-and-migrations.md)
- [Stateful Recovery and Migration Decision](docs/practices/stateful-recovery-decision.md)

- [Playbook Remediation Plan](docs/practices/playbook-remediation-plan.md)
- [Lifecycle Execution Guide](docs/practices/lifecycle-execution-guide.md)
- [Milestone and Phase Boundary Review](docs/practices/milestone-boundary-review.md)
- [Scope Evolution and Proportionate Architecture Decisions](docs/practices/scope-and-architecture-decisions.md)
- [AI-assisted Execution Practice](docs/practices/ai-assisted-execution.md)
- [GitHub Reference Implementation Guide](docs/practices/github-reference-implementation-guide.md)
- [Machine-readable Execution Representation Decision](docs/practices/machine-readable-execution-decision.md)
- [Product-type Architecture Plan](docs/practices/product-type-architecture-plan.md)
- [Product-type Assumption Inventory](docs/practices/product-type-assumption-inventory.md)
- [Lifecycle Applicability Assessment](docs/practices/lifecycle-applicability-assessment.md)

### Examples

- [Foundation Completion Example](examples/foundation-completion-example.md)
- [Product Definition Example](examples/product-definition-example.md)
- [AI Collaboration Example](examples/ai-collaboration-example.md)
- [End-to-end Playbook Example](examples/end-to-end-playbook-example.md)
- [Stateful Recovery and Migration Example](examples/stateful-recovery-and-migration-example.md)
- [Master Execution Checklist Walkthrough](examples/master-execution-checklist-walkthrough.md)
- [Executable Protocol Reference Example](examples/executable-protocol-reference-example.md)

### Standards Index

- [Standards Index](docs/standards/index.md)
- [Standards Relationship Map](docs/standards/standards-relationship-map.md)

### Repository & Engineering

- [Repository Standards](docs/standards/repository-standards.md)
- [Branch Workflow](docs/standards/branch-workflow.md)
- [Code Review Standard](docs/standards/code-review-standard.md)
- [Pull Request Template Standard](docs/standards/pull-request-template-standard.md)
- [Issue Template Standard](docs/standards/issue-template-standard.md)
- [Definition of Ready](docs/standards/definition-of-ready.md)
- [Definition of Done](docs/standards/definition-of-done.md)
- [Master Execution Checklist](docs/standards/master-execution-checklist.md)
- [Provider-independent Integration Standard](docs/standards/integration-standard.md)
- [Provider Implementation Guide Standard](docs/standards/provider-implementation-guide-standard.md)
- [Product Type Model](docs/standards/product-type-model.md)
- [Core and Specialization Boundaries](docs/standards/core-and-specialization-boundaries.md)
- [Standards Applicability](docs/standards/standards-applicability.md)
- [Versioning Standard](docs/standards/versioning-standard.md)
- [Coding Standards](docs/standards/coding-standards.md)
- [Testing Strategy](docs/standards/testing-strategy.md)
- [Software Environments Standard](docs/standards/software-environments.md)
- [Continuous Integration](docs/standards/continuous-integration.md)
- [Repository Automation Standard](docs/standards/repository-automation.md)
- [AI Collaboration Standard](docs/standards/ai-collaboration.md)
- [Security, Privacy, and Data Governance Standard](docs/standards/security-privacy-data-governance.md)
- [Work Item Taxonomy](docs/standards/work-item-taxonomy.md)
- [Work Item Types](docs/standards/work-item-types.md)
- [Project Views](docs/standards/project-views.md)
- [Repository Project Field Standard](docs/standards/repository-project-field-standard.md)
- [Repository Milestone Standard](docs/standards/repository-milestones.md)
- [Repository Label Standard](docs/standards/repository-labels.md)
- [Terminology Standard](docs/standards/terminology-standard.md)
- [Glossary](docs/standards/glossary.md)
- [Artifact Standard](docs/standards/artifact-standard.md)
- [Artifact Catalog](docs/standards/artifact-catalog.md)

### Release

- [Release Strategy](docs/standards/release-strategy.md)
- [Release Notes](docs/standards/release-notes.md)
- [Deployment Strategy](docs/standards/deployment-strategy.md)
- [Rollback Strategy](docs/standards/rollback-strategy.md)

### Maintenance

- [Incident Management](docs/standards/incident-management.md)
- [Bug Management](docs/standards/bug-management.md)
- [Technical Debt Management](docs/standards/technical-debt-management.md)
- [Product Monitoring](docs/standards/product-monitoring.md)
- [Product Evolution](docs/standards/product-evolution.md)

### Documentation

- [Documentation Information Architecture](docs/standards/documentation-information-architecture.md)
- [Documentation Navigation Standard](docs/standards/documentation-navigation.md)
- [Documentation Style Guide](docs/standards/documentation-style-guide.md)

### Architecture

- [Architecture Vision](docs/standards/architecture-vision.md)
- [System Context](docs/standards/system-context.md)
- [Architecture Decision Records](docs/standards/architecture-decision-records.md)
- [High-Level Architecture](docs/standards/high-level-architecture.md)
- [Component Architecture](docs/standards/component-architecture.md)
- [Data Model](docs/standards/data-model.md)
- [API Design](docs/standards/api-design.md)
- [Architecture Artifacts](docs/standards/architecture-artifacts.md)

### UX

- [UX Vision](docs/standards/ux-vision.md)
- [User Journey](docs/standards/user-journey.md)
- [Personas](docs/standards/personas.md)
- [User Flows](docs/standards/user-flows.md)
- [UX Information Architecture](docs/standards/ux-information-architecture.md)
- [Wireframes](docs/standards/wireframes.md)
- [Prototypes](docs/standards/prototypes.md)
- [UX Validation](docs/standards/ux-validation.md)
- [UX Artifacts](docs/standards/ux-artifacts.md)
- [Accessibility and Inclusive Experience Standard](docs/standards/accessibility-inclusive-experience.md)

### Product

- [Product Vision](docs/standards/product-vision.md)
- [Problem Statement](docs/standards/problem-statement.md)
- [Users](docs/standards/users.md)
- [Outcomes](docs/standards/outcomes.md)
- [Product Scope](docs/standards/product-scope.md)
- [Product Backlog](docs/standards/product-backlog.md)
- [Product Evolution](docs/standards/product-evolution.md)

## Current Status

Latest published release: **[v0.6.0](https://github.com/giaholic-dev/product-development-playbook/releases/tag/v0.6.0)**

Development target: **v0.7.0 — Audit Evidence Coverage (in development)**

Scope and work records: [Playbook Remediation Plan](docs/practices/playbook-remediation-plan.md).

The lifecycle status below measures this repository's documentation coverage, not execution status for an external product:

- **Documented** — the phase document and its current governing artifacts exist and have been reviewed against their documented criteria.
- **Planned** — the phase is part of the lifecycle but its document is not yet available.

Latest documented phase: **Maintenance**

Next planned phase: **None**

Lifecycle documentation:

- ✅ Foundation — documented
- ✅ Product — documented
- ✅ UX — documented
- ✅ Architecture — documented
- ✅ Development — documented
- ✅ Release — documented
- ✅ Maintenance — documented

---
*For the latest documented lifecycle phase, see [Maintenance Phase](docs/lifecycle/07-maintenance.md).*
