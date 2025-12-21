# 2.2 Selected Tools and Rationale (E-OLM)

This section lists the automated verification, validation, and testing tools selected for the E-OLM (Online Library Management System) project and explains the rationale behind the selection.

The E-OLM codebase is a Django/Python web application with role-based workflows (Student/Admin), authentication flows, CRUD operations (books/authors/categories), and book issuing/return-date tracking. Therefore, we selected tools that are:
- Compatible with Python/Django
- Easy to run locally and in CI
- Able to produce clear evidence (logs, reports, screenshots) for the project report

Note: The repository documentation mentions mixed technologies (e.g., PHP/MySQL) together with Django. Our V&V activities and tool selection are based on the actual repository implementation (Python/Django).

---

## A) Continuous Integration / Automation

### 1) GitHub Actions (CI)
**Why chosen**
- Runs checks automatically on every Pull Request (consistent verification).
- Produces auditable evidence (workflow logs, artifacts).
**How it supports E-OLM**
- Ensures every PR is validated before merging (tests + static checks).
**Evidence**
- CI workflow run logs and screenshots.

---

## B) Static Analysis (Verification)

### 2) Ruff (Linting / code quality)
**Why chosen**
- Fast and easy to configure for Python projects.
- Catches common issues early (unused imports, risky patterns, style violations).
**How it supports E-OLM**
- Improves maintainability and reduces defects in Django/Python code.
**Evidence**
- Ruff output in CI logs and PR status checks.

### 3) Bandit (Python security static analysis)
**Why chosen**
- Focused on common Python security issues and insecure coding patterns.
- Useful for identifying risks related to authentication, input handling, and file operations.
**How it supports E-OLM**
- Helps review security risks in web-app logic (e.g., unsafe functions, weak patterns).
**Evidence**
- Bandit scan output (CI logs or terminal output) summarized in the report.

---

## C) Automated Testing (Validation + Verification)

### 4) Pytest + pytest-django
**Why chosen**
- Widely used, readable testing framework.
- Strong support for Django (database access, test client, fixtures).
**How it supports E-OLM**
- Validates key workflows:
  - Student registration/login/password flows
  - Viewing available/issued books and return date details
  - Admin CRUD (books/authors/categories)
  - Issuing a book to a student
**Evidence**
- Test results (passed/failed), logs, and screenshots.

---

## D) Structural Testing

### 5) coverage.py / pytest-cov (Coverage measurement)
**Why chosen**
- Standard tool for measuring statement/branch coverage in Python.
- Produces clear structural testing metrics for the report.
**How it supports E-OLM**
- Shows which parts of critical workflows are exercised by tests.
**Evidence**
- Coverage report (CLI/HTML) and coverage percentage in CI output.

---

## E) Dependency / Vulnerability Scanning

### 6) pip-audit (Dependency vulnerability scanning)
**Why chosen**
- Scans Python dependencies for known vulnerabilities.
- Simple to run locally and in CI.
**How it supports E-OLM**
- Helps ensure project dependencies used in a web app are not known-vulnerable.
**Evidence**
- pip-audit output (CI logs or terminal output) and summary in security section.

---

## Optional Tools (time permitting)

### 7) mutmut (Mutation testing)
**Why chosen**
- Evaluates test suite strength beyond coverage.
**Evidence**
- Mutmut summary (killed/survived mutants) as report evidence.

### 8) Semgrep (Additional static analysis rules)
**Why chosen**
- Powerful pattern-based scanning; useful if we need extra rules.
**Evidence**
- Semgrep findings report (if enabled).

---

## Selected Toolchain Summary

Minimum baseline (must-have):
- GitHub Actions
- Ruff
- Bandit
- Pytest + pytest-django
- coverage.py / pytest-cov
- pip-audit

Nice-to-have (optional):
- mutmut
- Semgrep
