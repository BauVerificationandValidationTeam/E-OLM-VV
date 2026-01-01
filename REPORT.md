# SEN4013 – Software Verification & Validation Project Report
## Applying V&V Techniques to an Online Book Lending System (E-OLM)


## 1. Introduction - Emin
### 1.1 Purpose
### 1.2 Project Overview (Online Book Lending System)
### 1.3 Team Responsibilities

## 2. Part 1 – Review of Automated V&V Tools - Emin
### 2.1 Tool Categories & Evaluation Criteria
### 2.2 Selected Tools & Rationale
### 2.3 Comparison Summary

## 3. Validation - Samet
### 3.1 Objectives & Scope
### 3.2 Assumptions & Constraints
### 3.3 User Stories / Use Cases
### 3.4 Acceptance Criteria (Given/When/Then)
### 3.5 Traceability Matrix (Req → Test)

## 4. Verification - Selin and Feyzanur
### 4.1 Static Analysis Results
### 4.2 Test Strategy (Unit/Integration/E2E)
#### Test pyramid & goals
We follow a **test pyramid** approach to balance confidence and cost:
- **Unit tests (majority):** fast feedback, isolate business logic and small components.
- **Integration tests (some):** verify multiple components working together (views + DB + forms/models).
- **E2E / system tests (few):** validate critical user journeys from a user perspective.

**Goals**
- Catch defects early with fast unit tests.
- Protect core user flows (auth, search, borrow/return) with higher-level tests.
- Keep tests deterministic and repeatable (stable test data, isolated environment).
- Run automatically in CI on each PR (tests + coverage).

#### What is tested at each level (module → level mapping)

| Area / Module (E-OLM) | Unit Tests | Integration Tests | E2E / System Tests |
|---|---|---|---|
| Authentication (login/logout/register) | input validation, helper funcs, permission checks | auth views with DB, session behavior | register → login → logout (smoke) |
| Book catalogue & search | query/filters logic, model methods | list/detail/search views with DB | search a book → open details |
| Borrow/Return workflow | business rules (availability, status changes) | views/endpoints + DB updates | login → borrow/issue → return |
| User/Profile management | form validation, utility functions | profile update view + DB | update profile (optional smoke) |
| Admin/Librarian operations | role/permission checks | create/update book & user via views | librarian creates a book (optional) |

#### Test data & environment
- Use an isolated **test database** (Django test DB / SQLite) so tests do not affect real data.
- Use **fixtures / factories** where needed to create users, books, and transactions consistently.

#### Execution & CI
- Tests are executed locally and in **GitHub Actions** on each pull request.
- CI runs: **tests + coverage** (and optionally lint/static checks) to prevent regressions.

#### Entry/Exit criteria
A change is acceptable when:
- All unit/integration tests pass in CI.
- Critical user journeys (auth + search + borrow/return) are covered by at least smoke-level scenarios.
- No new failures are introduced and coverage does not drop significantly for cr

### 4.3 Structural Testing (Coverage/Mutation)
### 4.4 Lightweight Formal Model / Invariants (Optional)

## 5. Test Results - Aygül
### 5.1 Functional Test Cases (EP/BVA/Decision Table/State)
### 5.2 Structural Results (Coverage, Mutation)
### 5.3 Defects Found (List + severity + status)

## 6. Test Incidents - Aygül
### 6.1 Resolved Test Incidents
### 6.2 Unresolved Test Incidents (Known limitations)

## 7. Recommendations - All
### 7.1 Improvements to code/design
### 7.2 Improvements to test suite & automation
### 7.3 Future work

## Appendix
- Tool configs, pipeline YAML, raw coverage report, screenshots, logs, etc.
