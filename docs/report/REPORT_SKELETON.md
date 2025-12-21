# SEN4013 Software Verification & Validation Project Report
**Project Title:** Applying Software Verification and Validation Techniques to an Online Book Lending System (E-OLM)  
**Repository:** https://github.com/BauVerificationandValidationTeam/E-OLM-VV
**Course:** SEN4013 Software Verification and Validation  
**Submission Date:** 16 January 2026  
**Team:** (BauVerificationandValidationTeam + E-OLM-VV)

---

## 1. INTRODUCTION
### 1.1 Purpose
Explain why this project was conducted and what V&V aims to achieve for the selected system.

### 1.2 Project Overview (Online Book Lending System)
Short description of E-OLM (Django-based e-library system) and what it does.

### 1.3 Team Responsibilities
| Member | GitHub | Responsibilities |
|---|---|---|
| Emin | @21Emin17 | Intro + Part 1 tools + report structure + coordination |
| Selin | @selinkeskinn | Verification + CI/Security + structural results |
| Feyza | @feyakdeniz |Verification + CI/Security + structural results |
| Samet | @sametbugra| Validation (3.1–3.5) OR other assigned items |
| Aygül | @aygulumur | Incidents + recommendations |

---

## 2. PART 1 — REVIEW OF AUTOMATED V&V TOOLS
### 2.1 Tool Categories and Evaluation Criteria
- Static analysis (quality/security)
- Automated testing
- Structural testing (coverage/mutation)
- CI/CD automation
- Reporting/evidence

### 2.2 Selected Tools and Rationale
List selected tools (e.g., GitHub Actions, Ruff, Bandit, Pytest, pytest-django, coverage/pytest-cov, pip-audit, etc.) and why each tool is used.

### 2.3 Comparison Summary
Provide a comparison table and a short discussion of trade-offs.

---

## 3. VALIDATION
### 3.1 Objectives and Scope of the Software
What the system is expected to do; boundaries of the project.

### 3.2 Assumptions and Constraints
Assumptions about users, environment, dataset, and constraints (time, tooling, repo limitations).

### 3.3 User Stories / Use Cases
Key user stories for Student and Admin modules.

### 3.4 Acceptance Criteria (Given/When/Then)
Write acceptance criteria for the selected user stories.

### 3.5 Traceability Matrix (Requirements → Tests)
Map requirements/user stories to test cases.

---

## 4. VERIFICATION
### 4.1 Static Analysis Results
Summarize static analysis findings (lint, security scan, dependency audit), key issues and fixes (if any).

### 4.2 Test Strategy (Unit / Integration / E2E)
Explain test levels, what is tested at each level, and rationale.

### 4.3 Structural Testing Strategy (Coverage / Mutation)
Coverage targets, what coverage was measured, mutation testing approach (if used).

### 4.4 (Optional) Lightweight Formal Model / Invariants
Any invariants, simple models, or formal-ish checks used (optional section).

---

## 5. TEST RESULTS
### 5.1 Functional Testing Results
Summarize functional techniques used (EP/BVA/Decision Table/State) and key outcomes.

### 5.2 Structural Results (Coverage, Mutation)
Report coverage % and mutation results (if applicable).

### 5.3 Defects Found
| ID | Description | Severity | Status | Evidence |
|---|---|---|---|---|
| D1 | ... | High/Med/Low | Open/Fixed | link/screenshot |

---

## 6. TEST INCIDENTS
### 6.1 Resolved Test Incidents
List resolved incidents with references/evidence.

### 6.2 Unresolved Test Incidents (Known Limitations)
List known issues/limitations not fixed, with impact and justification.

---

## 7. RECOMMENDATIONS
### 7.1 Improvements to Code/Design
### 7.2 Improvements to Test Suite & Automation
### 7.3 Future Work

---

## APPENDIX
- Evidence folder index and naming rules
- CI workflow logs/screenshots
- Raw coverage reports
- Static analysis outputs
- Any additional artifacts
