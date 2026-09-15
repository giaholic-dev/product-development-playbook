# Product Definition Example

## Purpose

Demonstrate how the Product Vision, Problem Statement, Users, Outcomes, Product Scope, and Product Backlog can form one coherent product definition.

This fictional example illustrates the standards; it is not a governing rule, implementation specification, or delivery commitment.

## Context

**Borrow Better** is a hypothetical public-library service that helps members find and reserve available physical books.

The example uses qualitative research notes from a small discovery exercise. The evidence is illustrative and not a claim about a real library.

## Product Vision

Enable library members to confidently find and obtain books that match their interests, while helping library staff spend less time resolving routine availability questions.

## Problem Statement

Members cannot reliably determine whether a book is available at a convenient branch or whether it can be reserved. They call or visit a branch for answers, creating avoidable effort for both members and staff.

The current evidence is a set of member interviews and staff observations. It does not yet establish the size of the problem or select a solution.

## Users and Other Actors

| Actor | Relationship |
| --- | --- |
| Library member | Direct user who searches and reserves books. |
| Library staff member | Direct user who maintains availability information and helps members. |
| Library manager | Stakeholder who sets service expectations and approves operational changes. |

## Outcomes

| Desired change | Affected actor | Evidence |
| --- | --- | --- |
| Members can determine availability without contacting staff for routine questions. | Library members | A usability finding and a reduction in availability-related contacts. |
| Members can reserve an available copy with confidence. | Library members | Successful reservation completion and follow-up feedback. |
| Staff spend less time answering routine availability questions. | Library staff | A qualitative staff check and a comparison of contact categories. |

## Product Scope

### In scope

- Search by title, author, or ISBN.
- Show the availability of physical copies at each branch.
- Reserve an available copy.
- Notify a member when a reserved copy is ready for collection.

### Out of scope

- E-book lending.
- Inter-library loans.
- Payments, fines, or membership administration.
- Personalized recommendations.
- Replacing the library's catalog or inventory system.

## Initial Product Backlog

The order reflects the current hypothesis about what most directly supports the scope. It is not a delivery commitment.

1. Research how availability data can be obtained and how often it changes.
2. Validate that members understand the proposed availability information.
3. Enable title, author, and ISBN search.
4. Show branch-level availability for a selected book.
5. Enable a member to place a reservation.
6. Notify the member when a reservation is ready.
7. Measure whether routine availability contacts change after release.

## Traceability

The initial backlog starts with research and validation because availability information is the main uncertainty. If that evidence invalidates the premise, the Product Scope and backlog should be reconsidered before implementation work expands.

## References

- [Product Vision](../docs/standards/product-vision.md)
- [Problem Statement](../docs/standards/problem-statement.md)
- [Users](../docs/standards/users.md)
- [Outcomes](../docs/standards/outcomes.md)
- [Product Scope](../docs/standards/product-scope.md)
- [Product Backlog](../docs/standards/product-backlog.md)
