# 5. TEST INSTANCES

## 5.1 Resolved Test Incidents

| ID | Condition | Impact | Status | Evidence |
|----|----------|--------|--------|----------|
| **INC-01** | `Bandit` security scan detected a `try-except-pass` issue in `library/views.py`.| **High:** Silent failure swallows errors, posing a security risk.| **RESOLVED** | Fixed in `fix/4.1-bandit-report` branch (PR #41). |
| **INC-02** | Initial setup of GitHub Actions CI workflow failed to execute properly.| **High:** Build automation was broken. Team performed a "Revert".| **RESOLVED** | Visible in `revert-39-ci` branch history (PR #39). |
| **INC-03** | `SystemCheckError`: `Cannot use ImageField because Pillow is not installed`.| **Medium:** System crashed due to missing dependency.| **RESOLVED** | Fixed by adding Pillow to `requirements.txt` (PR #40). |
| **INC-04** | `pytest` framework failed to locate Django settings configuration. | **Medium:** Test automation could not be initialized locally. | **RESOLVED** | Fixed by adding `pytest.ini` configuration file (PR #50). |
| **INC-05** | CI Workflow could not be triggered manually for debugging. | **Low:** Hampered DevOps troubleshooting efficiency. | **RESOLVED** | Fixed by adding `workflow_dispatch` event (PR #52). |
| **INC-06** | Coverage artifacts (`.coverage`, `htmlcov`) were polluting the repository. | **Low:** Version control hygiene issue; junk files committed. | **RESOLVED** | Fixed by updating `.gitignore` rules (PR #51). |
| **INC-07** | Automated security scanning was missing from the CI pipeline. | **Medium:** Potential vulnerabilities could merge without checks. | **RESOLVED** | Fixed by adding Security Scan Workflow (PR #54). |

## 5.2 Unresolved Test Incidents

| ID | Condition | Impact | Status | Evidence |
|----|----------|--------|--------|----------|
| **INC-08** | Code coverage metrics did not reach the targeted 100% level. | **Low:** Potential hidden bugs in untested code blocks. | **UNRESOLVED** | Detailed in "5.2 Coverage Results" of `REPORT.md`. |
| **INC-09** | Visual alignment issues observed on the setup pages. | **Low:** Visual inconsistency affecting UX. | **UNRESOLVED** | Screenshot available at `evidence/setup/ui-pages.png`. |
| **INC-10** | "Forgot Password" functionality is missing from Login screens. | **Medium:** Users cannot reset credentials without Admin support. | **UNRESOLVED** | Visible in `evidence/setup/ui-pages.png` (Login Screens). |
| **INC-11** | Homepage images use non-transparent placeholder assets. | **Low:** Unprofessional UI appearance. | **UNRESOLVED** | Visible in `evidence/homepage.png`. |
