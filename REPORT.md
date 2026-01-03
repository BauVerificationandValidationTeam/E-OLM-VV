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

##### Coverage target & measurement method

**Coverage goal (minimum):**
- Aim for **≥ 70% statement/line coverage** for the main application modules.
- Aim for **≥ 60% branch coverage** where applicable (critical decision points).
- Focus on **risk-based coverage**: authentication, book/search, borrow/return, and any core business logic.

**How we measure coverage:**
- Tooling: `pytest` + `pytest-cov` (or Django test runner with coverage).
- Command (example):
  - `pytest --cov=LibraryManagementSystem --cov-report=term-missing --cov-report=html`
- Reporting:
  - Save the console summary in the report and keep an HTML report under `evidence/coverage/` (or similar).
  - Track “missed lines” to identify untested logic and prioritize tests for those areas.

##### Mutation testing target & interpretation plan

**Mutation goal:**
- Aim for **≥ 50% mutation score** as an initial target (mutation testing is stricter than coverage).
- Prioritize mutation testing on modules with business rules (e.g., borrow/return logic, search filters, auth checks).

**Tool & approach:**
- Tooling option: `mutmut` (Python) or an equivalent mutation testing tool.
- Run mutations on selected modules first (small scope), then expand if runtime allows.

**How we interpret results (plan):**
- **Surviving mutants** indicate either:
  1) missing/weak assertions in tests, or
  2) code that is not meaningfully checked by tests (no behavioral verification).
- For equivalent/non-impactful mutants, document a clear justification.

##### Entry/Exit criteria

**Entry criteria:**
- CI pipeline is available and runs tests/lint/coverage on PRs.
- Baseline unit tests exist and pass (`pytest` green).
- Test environment requirements documented (deps, DB if needed, env vars).

**Exit criteria:**
- Coverage report generated and saved (console + HTML under `evidence/coverage/`).
- Mutation results recorded (command used, scope, score, key survivors/killed mutants).
- If targets are not met, provide a short rationale and follow-up actions.

### 4.4 Lightweight Formal Model / Invariants (Optional)

We model the **Borrow/Return** behavior with a lightweight state machine and a set of invariants.  
This helps us reason about correctness and defines clear **test oracles**.

##### State machine (per book copy)
States:
- **Available**
- **Borrowed**

Transitions:
- **borrow(copy)**: Available → Borrowed
- **return(copy)**: Borrowed → Available

##### Transition rules (pre/post conditions)
- **borrow(user, copy)**
  - Pre: copy is **Available**
  - Post: an active loan is created for (user, copy), and copy becomes **Borrowed**

- **return(user, copy)**
  - Pre: copy is **Borrowed** and there exists an active loan for (user, copy)
  - Post: the loan is closed (return date set), and copy becomes **Available**

##### Key invariants (must always hold)
1. **Non-negativity:** `availableCopies >= 0`
2. **Upper bound:** `availableCopies <= totalCopies`
3. **Conservation of copies:** `totalCopies = availableCopies + activeBorrowedCopies`
4. **Uniqueness:** a book copy can have **at most one active loan** at any time
5. **Valid timeline:** `borrowDate <= returnDate` (if returnDate exists)

##### How we verify in tests (oracle)
- After each borrow/return operation, assert invariants **(1)-(4)** on the updated state.
- For returned loans, also assert invariant **(5)**.


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
