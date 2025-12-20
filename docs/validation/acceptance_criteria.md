## 3.4 Acceptance Criteria (Given / When / Then)

### AC-01 Student Login
**Given** the student has a registered account  
**When** the student enters valid username and password  
**Then** the system logs the student in and shows the dashboard  

**Negative Scenario**  
**Given** the student enters invalid credentials  
**When** login is attempted  
**Then** the system displays an error message  

---

### AC-02 View Available Books
**Given** the student is logged in  
**When** the student navigates to the books page  
**Then** the system displays a list of available books  

---

### AC-03 Borrow Book (Success)
**Given** the student is logged in and has not reached the borrow limit  
**And** the selected book is in stock  
**When** the student clicks “Borrow”  
**Then** the book is issued to the student  
**And** the available stock is reduced by 1  

---

### AC-04 Borrow Book – Stock Not Available
**Given** the student is logged in  
**And** the selected book stock is 0  
**When** the student attempts to borrow the book  
**Then** the system prevents borrowing  
**And** shows an “Out of stock” message  

---

### AC-05 Borrow Limit Exceeded
**Given** the student has already reached the borrow limit  
**When** the student attempts to borrow another book  
**Then** the system blocks the action  
**And** displays a limit warning  

---

### AC-06 Return Book
**Given** the student has borrowed a book  
**When** the student returns the book  
**Then** the system marks the book as returned  
**And** updates availability  

---

### AC-07 Overdue Book Restriction
**Given** the student has an overdue book  
**When** the student tries to borrow another book  
**Then** the system blocks borrowing  
**And** shows an overdue warning  

---

### AC-08 Admin Add Book
**Given** the admin is logged in  
**When** the admin adds a new book with valid details  
**Then** the book is saved and appears in the book list  

---

### AC-09 Admin Issue Book
**Given** the admin is logged in  
**When** the admin issues a book to a student  
**Then** the system records the transaction successfully
