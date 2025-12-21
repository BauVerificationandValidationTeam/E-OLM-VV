# Report Writing Guide (report/emin-skeleton)

## Where to put content
- Main report outline: `REPORT.md`
- Validation docs: `docs/validation/`
- Verification docs: `docs/verification/`
- Tools review (Part 1): `docs/tools/`
- Test plans/results: `docs/testing/`
- Evidence artifacts (screenshots/logs): `evidence/`

## PR rules
- No direct push to `main`.
- One issue = one branch/PR whenever possible.
- PR description must include:
  - `Closes #<issue>`
  - Evidence links (file paths under docs/evidence)

## Evidence examples
- Test run output screenshot
- Coverage percentage screenshot/report
- Static analysis output (Bandit/Ruff)
- GitHub Actions run screenshot
