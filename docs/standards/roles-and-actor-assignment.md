# Roles and Actor Assignment Standard

## Purpose

Define the minimum actor-independent responsibility and assignment model required to execute Product Development Playbook work.

## Scope

This standard governs Roles, Actors, Assignments, accountability, and authority boundaries. It keeps a Role as a responsibility, an Actor as the entity performing work, and an Assignment as an Actor fulfilling a Role.

The model is independent of actors, providers, tools, organizational structure, and implementation technology. It is usable by an individual, teams, human-only execution, AI-assisted execution, authorized automated execution, and future multi-agent execution; it remains fully usable without AI.

This standard defines responsibility and assignment semantics. It does not redefine lifecycle-specific ownership, approval requirements, work-management flow, execution protocol, Definition of Ready, Definition of Done, AI Collaboration, or security and governance rules owned by other standards.

## Definitions

### Role

A Role represents a responsibility within Playbook execution. A Role MUST NOT represent a specific person, job title, team, AI agent, automation, provider, or tool. Separating responsibility from the entity performing work allows the same responsibility model across execution modes and organizational structures.

### Actor

An Actor is an entity that performs or participates in Playbook work. An Actor MAY be an individual human, team, AI agent, automation, or hybrid execution arrangement; these illustrations are not exhaustive. An Actor MUST NOT, by itself, determine which Role it fulfills, its authority, or its accountability.

### Assignment

An Assignment is the explicit relationship through which an Actor fulfills a Role within a defined scope of Playbook work. It connects a responsibility to an execution entity without changing the identity of either concept. An Assignment MUST identify a scope sufficient to determine where the Role is fulfilled.

## Assignment model

An Actor MAY fulfill multiple Roles within Playbook execution. Each Role remains a distinct responsibility; combining Roles in one Actor MUST NOT collapse or redefine them. Each Assignment MUST remain independently identifiable within its applicable scope.

Multiple Actors MAY contribute to the same Role within a defined scope of Playbook work. The Role remains one distinct responsibility, and each Actor's Assignment MUST remain independently identifiable. Multiple contributing Actors MUST NOT make responsibility attribution ambiguous.

## Accountability and authority

Accountability identifies the Actor answerable for a material responsibility, decision, approval, exception, or completion declaration within a defined scope. Participation does not automatically imply accountability, and multiple Actors contributing to the same Role do not automatically share it. Where accountability is required by the Playbook or another governing rule, the accountable Actor MUST be explicitly identifiable. Assigning work to AI, automation, or another Actor MUST NOT silently transfer accountability; accountability MUST remain traceable when work is delegated, assisted, or automated.

Authority is the explicitly granted permission or decision right that allows an Actor to perform an action, make a decision, approve an outcome, or exercise another governed capability within a defined scope. An Assignment or participation in work MUST NOT, by itself, imply unrestricted Authority. Where authorization is required, Authority MUST be identifiable and remain bounded by its applicable scope; an Actor MUST NOT exercise Authority beyond what has been granted. AI assistance, automation, or delegation MUST NOT silently expand Authority. Authority is distinct from Accountability: accountability does not automatically grant every related Authority, and Authority does not automatically make an Actor accountable for the broader responsibility or outcome.

## Delegation

Delegation is the explicit transfer of performance of some or all assigned work from one Actor to another Actor within a defined scope. Delegation MUST identify its delegated scope and preserve traceability between the original Assignment, receiving Actor, and delegated scope; it MUST NOT redefine the underlying Role. Delegation MUST NOT silently transfer Accountability or transfer or expand Authority. Any Accountability transfer, where permitted by a governing rule, MUST be explicit. Any Authority granted to the receiving Actor MUST be explicit and scope-bounded. A receiving Actor MAY perform delegated work only within its applicable Assignment and Authority boundaries.

## Role model

### Accountable Owner

Accountable Owner is the Role assigned to the single Actor who holds Accountability for a material responsibility, decision, approval, exception, or completion declaration when a governing Playbook rule requires explicit accountability. In that case, exactly one Actor MUST be identifiable as the Accountable Owner within the applicable scope. Multiple Actors MAY contribute to the same work without becoming Accountable Owner automatically. Assigning Accountable Owner MUST NOT imply unrestricted Authority; the Accountable Owner MUST have only the Authority explicitly granted or required for the applicable responsibility. Delegation of performance, AI assistance, or automation MUST NOT silently transfer, replace, or change the Accountable Owner assignment. The Accountable Owner assignment MUST remain traceable within its applicable scope.

### Contributor

Contributor is the Role assigned to an Actor that performs or contributes work within a defined scope without, by that contribution alone, becoming accountable for the material responsibility or gaining Authority over governed decisions. One or more Actors MAY hold a Contributor Assignment within the same applicable scope, and each Contributor Assignment MUST identify that scope. A Contributor MAY separately hold another Role through another identifiable Assignment, including Accountable Owner when independently assigned. Assigning Contributor MUST NOT obscure the Actor who is Accountable Owner when explicit accountability is required. An Actor need not hold a formal Contributor Assignment unless an applicable governing rule requires it to be represented.

### Reviewer

Reviewer is the Role assigned to an Actor responsible for evaluating governed work or evidence against applicable requirements within a defined scope. A Reviewer Assignment MUST identify that review scope. Performing review MUST NOT, by itself, make the Reviewer the Accountable Owner or grant approval Authority. A Reviewer MAY hold another Role through a separately identifiable Assignment when permitted by the applicable governing rules. Where another standard requires reviewer independence or separation of duties, that requirement remains authoritative.

### Approver

Approver is the Role assigned to an Actor responsible for making an approval decision within a defined scope when a governing Playbook rule requires or explicitly establishes approval. An Approver Assignment MUST identify that approval scope, and the Approver MUST have the Authority required to make that decision. Being assigned as Approver MUST NOT imply Authority beyond the applicable approval scope or make the Approver the Accountable Owner for the broader responsibility or outcome. Review and approval remain distinct responsibilities: performing review MUST NOT automatically make an Actor the Approver. An Actor MAY hold Reviewer and Approver through distinct Assignments when the applicable governing rules permit. Where another standard requires reviewer/approver independence or separation of duties, that requirement remains authoritative.

### Role relationships

Accountable Owner, Contributor, Reviewer, and Approver are distinct responsibilities; assigning one MUST NOT automatically assign another. The same Actor MAY fulfill multiple Roles through separately identifiable Assignments when applicable governing rules permit, but combining Roles MUST NOT collapse or redefine their responsibilities. Where required, the Accountable Owner, Reviewer, Approver, and applicable approval Authority MUST remain identifiable; multiple Contributors MAY participate without changing that model. A single Actor MAY fulfill multiple applicable Roles in lightweight or individual execution when governing rules permit, without eliminating required Accountability, Authority, review, approval, or separation of duties. The four Roles need not all be represented unless required by a governing rule or deliberately assigned for the applicable scope. Governing requirements for independence, separation of duties, or incompatible responsibilities take precedence over otherwise permitted Role combination.

## Examples

The following non-normative examples validate the portability of the responsibility model.

### Human-only individual execution

A human Actor holds distinct Accountable Owner and Contributor Assignments for a documentation change. The responsibilities remain distinct even though one Actor fulfills both. The same Actor may also hold Reviewer or Approver only when the applicable governing rules permit; a required separation of duties still takes precedence.

### AI-assisted execution

For the same documentation change, a human Actor retains the Accountable Owner Assignment. An AI Actor has an identifiable Contributor Assignment for drafting support. That participation does not itself grant the AI Actor Accountability or Authority, and it does not replace the Accountable Owner. Review or approval remains separately assigned when required. The AI Actor could hold another Role only through an explicit Assignment when governing rules permit.

Role, Actor, Assignment, Accountability, Authority, and applicable separation-of-duties requirements retain the same semantics regardless of whether execution is human-only or AI-assisted.

## References

- [Definition of Ready](definition-of-ready.md)
- [Definition of Done](definition-of-done.md)
- [AI Collaboration Standard](ai-collaboration.md)
- [Security, Privacy, and Data Governance Standard](security-privacy-data-governance.md)
