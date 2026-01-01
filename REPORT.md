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
### 4.4 Lightweight Formal Model / Invariants (Optional)
#### 4.4 Lightweight Formal Model / Invariants (Optional)

We model the **Borrow/Return** behavior with a lightweight state machine and a set of invariants.
This helps us reason about correctness and define test oracles.

**State machine (per book copy / loan):**
- **Available** → (borrow) → **Borrowed**
- **Borrowed** → (return) → **Available**

**Transitions (pre/post conditions):**
- **borrow(user, bookCopy)**
  - Pre: bookCopy is Available, `availableCopies > 0`
  - Post: create an active Loan record, `availableCopies := availableCopies - 1`, state becomes Borrowed
- **return(user, bookCopy)**
  - Pre: bookCopy is Borrowed, there exists an active Loan for that copy
  - Post: close the Loan (set return date), `availableCopies := availableCopies + 1`, state becomes Available

**Key invariants (must always hold):**
1. **Non-negativity:** `availableCopies >= 0`
2. **Upper bound:** `availableCopies <= totalCopies`
3. **Conservation of copies:** `totalCopies = availableCopies + activeBorrowedCopies`
4. **Uniqueness:** a book copy can have **at most one active loan** at any time
5. **Valid timeline:** `borrowDate <= returnDate` (if returnDate exists)

**How we verify in tests:**
- After borrow/return operations, assert invariants #1–#3.
- En


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
