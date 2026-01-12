## 7.1 Code & Design Improvements

Based on the static analysis results and architectural review, the following improvements are recommended to enhance the system's scalability, maintainability, and data integrity.

| ID | Recommendation | Priority | Justification (Why?) |
| :--- | :--- | :--- | :--- |
| **REC-01** | **Replace Silent Failures with Logging** | **High** | The usage of `try-except-pass` blocks (identified by Bandit) hides critical runtime errors. Python’s `logging` module should be implemented to track system crashes instead of silencing them. |
| **REC-02** | **Enforce Referential Integrity** | **High** | Currently, `IssuedBook` relies on loose IDs (`student_id`). Refactoring to use `ForeignKey` ensures ACID compliance and prevents orphaned records when a student is deleted. |
| **REC-03** | **Sanitize UI/UX with a CSS Framework** | **Medium** | The interface currently lacks responsiveness and visual consistency. Integrating **Bootstrap 5** would solve alignment issues and ensure a professional design language across the dashboard. |
| **REC-04** | **Optimize Database Models for Search** | **Medium** | To solve the "Difficult to search record" issue, database indexing (`db_index=True`) should be added to `ISBN` and `Student.roll_no` fields to significantly speed up query performance. |
| **REC-05** | **Externalize Hardcoded Configurations** | **Medium** | Configuration values (e.g., loan period: 14 days) are hardcoded. These should be moved to `settings.py` or `.env` files to adhere to the **12-Factor App** methodology and allow easier policy updates. |
| **REC-06** | **Standardize ISBN Data Type** | **Low** | `PositiveIntegerField` strips leading zeros from ISBNs. Converting this to `CharField` with validation ensures data accuracy and compliance with international ISBN standards. |
