# Software Testing & Quality Assurance (STAQA)
## Defect Reporting & Bug Life Cycle Document
**Project:** Automated Web Application Testing Using Selenium WebDriver  
**Course:** SPPU Computer Engineering (STAQA Mini-Project)  
**Academic Year:** 2025–2026  

---

### 1. Conceptual Distinction: Defects vs. Intentionally Invalid Inputs

In Software Quality Assurance, a critical distinction must be drawn between **negative testing inputs** and **genuine software defects**:

| Aspect | Intentionally Invalid Test Inputs (Negative Testing) | Genuine Application Defects (Bugs) |
|---|---|---|
| **Definition** | Deliberately supplying malformed, empty, or boundary-breaking data to test system resilience. | A deviation between actual application behavior and specified requirements or expected software contracts. |
| **Purpose** | To verify that error-handling pathways, input sanitization, and validation logic function as intended. | To identify flaws that need developer intervention and software fixes. |
| **Expected Behavior** | System catches the invalid condition, prevents transaction, and displays a user-friendly error message. | System should conform to requirements without unhandled crashes, state leaks, or bypasses. |
| **Example in Project** | Submitting an invalid email `user@` -> The system flags "Please enter a valid email address." (Test **PASSES**). | Submitting a name containing numeric digits or script symbols `Rahul123$#@!` -> The system silently accepts it without validation warning (Test **FAILS**, defect logged). |

---

### 2. Defect Severity vs. Priority Matrix

- **Severity (Technical Impact):** Measures the degree of impact that a defect has on the development or operation of a system (Critical, High, Medium, Low).
- **Priority (Business Urgency):** Indicates the urgency or importance of fixing the defect (P1 - Immediate, P2 - High, P3 - Medium, P4 - Low).

```
   ┌────────────────────────────────────────────────────────┐
   │             SEVERITY vs PRIORITY EXAMPLES              │
   ├────────────────────────┬───────────────────────────────┤
   │ High Severity / High P │ App crashes on login button   │
   ├────────────────────────┼───────────────────────────────┤
   │ High Severity / Low P  │ Edge crash on rare legacy OS  │
   ├────────────────────────┼───────────────────────────────┤
   │ Low Severity / High P  │ Misspelled university logo    │
   ├────────────────────────┼───────────────────────────────┤
   │ Low Severity / Low P   │ Minor pixel alignment issue   │
   └────────────────────────┴───────────────────────────────┘
```

---

### 3. Defect Report Template

```markdown
Defect ID:          [Unique Identifier, e.g., DEF_STAQA_01]
Defect Title:       [Concise summary of deviation]
Module:             [Component name, e.g., Registration, Login, Dashboard]
Severity:           [Critical / High / Medium / Low]
Priority:           [P1 / P2 / P3 / P4]
Reported By:        [QA Automation Engineer Name]
Date Logged:        [YYYY-MM-DD]
Test Environment:   [OS, Browser version, Python version, Selenium version]
Prerequisites:      [Initial state required to trigger the defect]
Steps to Reproduce: [Numbered, deterministic reproduction steps]
Expected Behavior:  [Behavior defined by requirements]
Actual Behavior:    [Observed deviation in the application]
Status:             [New / Open / In Progress / Fixed / Retest / Closed]
Associated Evidence:[Path to screenshot or test execution log]
```

---

### 4. Logged Defect: DEF_STAQA_01

#### Defect Details

- **Defect ID:** `DEF_STAQA_01`
- **Defect Title:** Full Name field accepts numeric digits and special characters without validation warning
- **Module:** User Registration (`/register`)
- **Severity:** Medium (Data Integrity / Input Sanitization)
- **Priority:** P3 (Should be fixed before production release)
- **Reported By:** Senior QA Automation Engineer
- **Date Logged:** 2026-10-21
- **Test Environment:** Windows 11, Google Chrome 130+, Python 3.13, Selenium 4.51.0

#### Prerequisites
- Application running on local host.
- User navigated to registration page (`/register`).

#### Steps to Reproduce
1. Open Google Chrome and navigate to `http://127.0.0.1:5000/register`.
2. In the **Full Name** field, input: `Rahul123$#@!`.
3. In the **Email Address** field, input a valid unique email: `user_test@example.com`.
4. In the **Password** field, input: `SecurePassword123`.
5. In the **Confirm Password** field, input: `SecurePassword123`.
6. Click the **Register Account** button.

#### Expected Behavior
The form validation should reject the submission and display an inline validation warning beneath the Full Name field:  
`"Name must contain only alphabetical characters and spaces."`

#### Actual Behavior
The registration form successfully submits, stores the alphanumeric string `Rahul123$#@!` in the database, and redirects the user to `/login` with `"Registration successful!"`. No input format error is surfaced to the user.

#### Automated Test Execution & Evidence
- **Automated Test Script:** `tests/test_defect_demo.py::TestDefectReproduction::test_tc_def_01_numeric_name_rejection`
- **Result:** `FAILED` (AssertionError: DEFECT DETECTED: Application accepted numeric/symbolic characters in full name)
- **Automated Screenshot Captured:** `screenshots/FAIL_test_tc_def_01_numeric_name_rejection_*.png`
- **pytest-html Report Link:** Embedded in `reports/report.html` under Failed Tests table.

#### Current Status
**Status:** `OPEN` / Under Review by Development Team.

---

### 5. Defect Life Cycle in STAQA

```
      [ NEW ] ──────> [ OPEN ] ──────> [ IN PROGRESS ]
                                              │
                                              ▼
      [ CLOSED ] <─── [ VERIFIED ] <─── [ FIXED ]
           │                 │
           │                 ▼ (If bug still exists)
           └───────────> [ REOPENED ]
```

1. **New:** QA automation script catches assertion failure and auto-saves screenshot.
2. **Open:** QA reviews test failure, isolates bug from test input errors, and logs defect report.
3. **In Progress:** Developer receives defect ID, reproduces using the test script, and prepares fix.
4. **Fixed:** Developer deploys code update (e.g. adding regex `^[A-Za-z\s]+$` validation).
5. **Verified:** Automated regression test suite re-executes.
6. **Closed:** If assertion passes, defect is moved to Closed status.
