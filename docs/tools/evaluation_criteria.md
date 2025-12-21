# 2.1 Tool Categories & Evaluation Criteria

This section reviews automated verification, validation, and testing tools that can be applied to the E-OLM (Online Book Lending System) codebase and similar web applications.

---

## A) Tool Categories (V&V Tool Landscape)

### 1) Static Code Analysis (SAST / linting)
**Goal:** Find defects without executing the program (code smells, insecure patterns, bad practices).  
**Examples:** Ruff/Flake8, Pylint, Bandit, Semgrep.

### 2) Dynamic Testing Frameworks (Automated tests)
**Goal:** Validate behavior by executing test cases.  
**Examples:** Pytest, unittest, Django test framework.

### 3) Coverage Measurement (Structural testing support)
**Goal:** Measure which parts of code are exercised (statement/branch coverage).  
**Examples:** coverage.py, pytest-cov.

### 4) Mutation Testing
**Goal:** Evaluate test suite strength by injecting small code changes (mutants) and checking if tests catch them.  
**Examples:** mutmut, cosmic-ray.

### 5) Dependency / Vulnerability Scanning (SCA)
**Goal:** Detect known vulnerabilities in third-party packages.  
**Examples:** pip-audit, Safety, Dependabot (GitHub).

### 6) CI/CD Automation (Continuous Verification)
**Goal:** Run tests/analysis automatically on every pull request to prevent regressions.  
**Examples:** GitHub Actions, GitLab CI.

### 7) API / End-to-End (E2E) Testing (optional)
**Goal:** Validate the system from user perspective (web UI flows).  
**Examples:** Selenium, Playwright.

---

## B) Evaluation Criteria (How We Choose Tools)

### 1) Project Fit / Technology Compatibility
- Works with **Python + Django** and the existing project structure.
- Minimal changes to integrate.

### 2) Effectiveness (Fault-Finding Power)
- Ability to detect common real-world issues (bugs, security issues, regressions).
- Supports rules/checks relevant to web applications.

### 3) Ease of Setup & Usability
- Simple installation and configuration.
- Clear documentation; easy for first-time GitHub users in the team.

### 4) Automation & CI Integration
- Can run reliably in GitHub Actions.
- Produces machine-readable outputs (text/JSON) and clear logs.

### 5) Output Quality & Actionability
- Findings are understandable and include file/line references.
- Low noise (manageable false positives) and supports tuning.

### 6) Performance & Runtime Cost
- Reasonable runtime on a standard laptop and on CI.
- Suitable for frequent PR checks.

### 7) Reporting & Evidence Support
- Outputs can be attached as evidence (screenshots/logs) and referenced in the final report.
- Supports summary metrics (coverage %, number of issues).

### 8) Cost / Licensing
- Prefer free/open-source tools and free-tier friendly CI usage.

---

## C) Mapping Criteria to Our Project Needs (Short Summary)

For E-OLM, the main priorities are:
1) **Reliable automated tests (Pytest/Django tests)**
2) **Static analysis for code quality and security (Ruff + Bandit/Semgrep)**
3) **Structural confidence via coverage + mutation (coverage.py + mutmut)**
4) **Repeatable CI pipeline (GitHub Actions)**
