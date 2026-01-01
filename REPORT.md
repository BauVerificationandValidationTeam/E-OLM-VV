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

We model the **Borrow/Return** behavior with a lightweight state machine and a set of invariants.
This helps us reason about correctness and define clear **test oracles**.

#### State machine (per book copy / loan)

`AVAILABLE` --borrow--> `BORROWED` --return--> `AVAILABLE`

#### Transitions (pre/post conditions)

**borrow(user, bookCopy)**
- **Pre:** `availableCopies > 0` AND `bookCopy` has **no ACTIVE loan**
- **Post:** create an **ACTIVE** loan; `availableCopies := availableCopies - 1`

**return(user, bookCopy)**
- **Pre:** there exists an **ACTIVE** loan for `bookCopy`
- **Post:** close the loan (set `returnDate`); `availableCopies := availableCopies + 1`

#### Key invariants (must always hold)

Let:
- `totalCopies` = total number of copies for a book/title
- `availableCopies` = copies available to borrow
- `activeBorrowedCopies` = number of **ACTIVE** loans (currently borrowed)

1. **Non-negativity:** `availableCopies ≥ 0`
2. **Upper bound:** `availableCopies ≤ totalCopies`
3. **Conservation:** `availableCopies + activeBorrowedCopies = totalCopies`
4. **Uniqueness:** a book copy can have **at most one ACTIVE loan** at any time
5. **Valid timeline:** if `returnDate` exists, then `borrowDate ≤ returnDate`

#### How we use this in tests (oracle)

After each borrow/return scenario (integration/E2E), we assert the invariants by querying the DB:
- compute `activeBorrowedCopies = count(Loan where status=ACTIVE)`
- check invariants (1)–(5)
- negative case: when `availableCopies = 0`, a new borrow attempt must be rejected (validation error / user message).

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
