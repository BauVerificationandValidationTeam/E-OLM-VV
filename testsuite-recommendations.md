### 7.2 Improvements to Test Suite & Automation

Based on the current verification results and the established CI/CD infrastructure, the following improvements are recommended to enhance the reliability and security of E-OLM:

* **CI Security Integration & Static Analysis:** The newly created `ci-security-scan-workflow` should be expanded to include Python-specific security tools like **Bandit**. This will ensure that every "push" is automatically scanned for common security vulnerabilities in the code.
* **Automation of Manual Deployment Steps:** Currently, the system relies on manual execution commands such as `python manage.py runserver` as documented in the `README.md`. A "pipeline gate" should be implemented in GitHub Actions to make **flake8** (static analysis) and **pytest** (unit testing) passes mandatory before any deployment or merge.
* **Bridging the Critical Coverage Gap:** The structural testing results show a significant "test gap," with `library/views.py` covered at only **17%**. Future efforts must prioritize writing unit and integration tests for this module to ensure the 164 currently "missed statements" are verified.
* **Automated Coverage Enforcement (Quality Gate):** To reach the project's **70% coverage goal**, a rule should be added to the CI pipeline that automatically rejects Pull Requests if the total coverage falls below the established threshold.
* **Mutation Testing Baseline:** To go beyond simple line coverage, **mutmut** should be fully integrated to achieve the planned **50% mutation score**. This will provide a concrete metric for the effectiveness of the test oracles in catching logic changes.

* ### Next Steps

- Integrate **pytest**, **flake8**, and **Bandit** into the CI pipeline for every push and pull request.
- Add a **coverage quality gate** to block merges when total coverage falls below the defined threshold.
