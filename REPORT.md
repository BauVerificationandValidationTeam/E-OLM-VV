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
### 4.3 Structural Testing (Coverage/Mutation)
#### Coverage target & measurement method

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

#### Mutation target & interpretation plan

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
- For each survived mutant:
  - Decide: **add/strengthen a test** (preferred) **or justify** (equivalent mutant / non-impactful change).
- Document:
  - top 5–10 survived mutants + what we did (new test / justification).
  - note limitations (runtime constraints, tool limitations, flaky tests).

#### Entry/Exit criteria (Structural testing)
A structural testing iteration is considered acceptable when:
- Coverage targets are met for critical modules **or** gaps are explained with a clear justification.
- Mutation score meets the target **or** surviving mutants are analyzed with actions/justifications documented.

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
