# 2.3 Comparison Summary Table (Automated V&V Tools for E-OLM)

This table summarizes the selected automated tools and compares them using our evaluation criteria.
E-OLM is a Django/Python web application, so the toolchain prioritizes Python/Django compatibility, CI automation, and clear evidence outputs.

| Tool | Category | What it checks / provides | Why it fits E-OLM (Python/Django) | Effort (Setup) | Evidence Output | CI Friendly |
|---|---|---|---|---|---|---|
| GitHub Actions | CI / Automation | Runs jobs on PRs (tests, lint, scans) | Enforces “no direct main push”, repeatable verification for every PR | Low | Workflow logs, status checks, artifacts | ✅ Yes |
| Ruff | Static analysis (Lint/Quality) | Code quality issues, style, common mistakes | Fast feedback for Python codebase, keeps code clean and consistent | Low | CLI output, PR check status | ✅ Yes |
| Bandit | Static analysis (Security) | Common Python security issues | Useful for web app risks (unsafe patterns, risky calls) | Low–Medium | Scan report / CLI output | ✅ Yes |
| Pytest | Testing (Unit/Integration) | Automated test execution | Standard Python testing; works well with Django via plugins | Medium | Test logs (pass/fail), reports | ✅ Yes |
| pytest-django | Testing (Django support) | Django test client, DB fixtures, settings | Enables realistic tests for auth + CRUD workflows | Medium | Test logs, DB-backed test outputs | ✅ Yes |
| coverage.py / pytest-cov | Structural testing (Coverage) | Measures code coverage | Shows what parts of E-OLM are exercised by tests | Low–Medium | Coverage % + HTML/CLI report | ✅ Yes |
| pip-audit | Dependency security | Known vulnerabilities in Python deps | Quick dependency risk check for web app stack | Low | CLI findings list | ✅ Yes |
| (Optional) mutmut | Mutation testing | Test suite strength (killed/survived mutants) | Demonstrates test effectiveness beyond coverage | Medium–High | Mutation summary report | ✅ Yes (optional) |
| (Optional) Semgrep | Pattern-based static analysis | Custom rules, broader scanning | Useful if we need extra security/code patterns | Medium | Findings report | ✅ Yes (optional) |

## Notes
- Minimum baseline toolchain for the project report: GitHub Actions, Ruff, Bandit, Pytest (+pytest-django), coverage.py/pytest-cov, pip-audit.
- Optional tools (mutmut/Semgrep) can be included if time permits to strengthen structural verification and security analysis.
