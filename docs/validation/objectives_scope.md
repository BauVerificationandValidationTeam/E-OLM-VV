## Objective
The objective of the Online Book Lending System is to allow users to search, borrow, return, and renew books through an online interface, while enabling administrators to manage the library catalog, users, and lending policies.
 
## In Scope
- User registration/login (if available in the codebase)
- Browsing/searching the catalog
- Borrowing a book (creating a loan)
- Returning a book (closing a loan)
- Renewing a loan (if supported)
- Admin operations: add/update/remove books, manage users/loans
 
## Out of Scope (for this V&V project)
- Payment processing / fines collection (if not implemented)
- External integrations (email/SMS notifications) unless present
- Performance/load testing beyond basic validation
- Mobile app-specific behaviors (web app only)
 
## Quality Goals (V&V focus)
- Correctness of core lending workflows (borrow/return/renew)
- Input validation and error handling
- Basic security hygiene (no obvious insecure patterns)
- Regression safety through automated tests
,
