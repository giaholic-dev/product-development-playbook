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
