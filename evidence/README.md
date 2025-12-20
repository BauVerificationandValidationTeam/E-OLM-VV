# Evidence Folder

This folder contains evidence artifacts used in the V&V report.

## What counts as evidence?
- Test run outputs (screenshots or logs)
- Coverage reports (HTML/text summary, screenshots)
- Static analysis outputs (bandit/ruff/flake8 results)
- CI workflow run screenshots
- Any tool output referenced in the report

## Naming rules
Use this format:

`<issue>-<topic>-<date>.<ext>`

Examples:
- `#23-ci-tests-2025-12-16.png`
- `#24-bandit-scan-2025-12-16.txt`
- `#10-traceability-2025-12-16.png`

## Notes
- Prefer text logs (`.txt`) when possible.
- For screenshots, use `.png`.
- Reference evidence files in PR descriptions and in the final report Appendix.
