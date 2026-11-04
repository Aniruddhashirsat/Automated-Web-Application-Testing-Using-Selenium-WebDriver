# Software Testing & Quality Assurance (STAQA)
## Detailed Test Case Specification & Execution Table
**Project:** Automated Web Application Testing Using Selenium WebDriver  
**Course:** SPPU Computer Engineering (STAQA Mini-Project)  
**Academic Year:** 2025–2026  
**Automation Tool:** Selenium WebDriver (v4.51.0) with PyTest (v8.4.2)  
**Execution Environment:** Windows 11, Google Chrome (Headless/Headed), Python 3.13  

---

### Test Case Execution Summary
- **Total Test Cases Executed:** 17
- **Passed Test Cases:** 16
- **Failed Test Cases (Genuine Defect Detected):** 1 (`TC_DEF_01`)
- **Execution Mode:** Automated via PyTest & Selenium WebDriver
- **HTML Report Generated:** `reports/report.html`
- **Failure Screenshot Generated:** `screenshots/FAIL_test_tc_def_01_numeric_name_rejection_*.png`

---

### Detailed Test Case Specification Table

| Test ID | Module | Preconditions | Steps | Test Data | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|---|---|
| **TC_REG_01** | Registration | Server live; navigate to `/register`. | 1. Enter valid Full Name.<br>2. Enter unique email.<br>3. Enter valid password (>=6 chars).<br>4. Re-enter password.<br>5. Click 'Register Account'. | Name: "Aarav Deshmukh"<br>Email: `user_{uuid}@example.com`<br>Pass: "SecurePassword123"<br>Confirm: "SecurePassword123" | Redirect to `/login`; display success banner: "Registration successful! Please log in with your credentials." | Redirected to `/login`; alert-success rendered with expected confirmation. | **PASS** |
| **TC_REG_02** | Registration | Server live; navigate to `/register`. | 1. Leave all fields empty.<br>2. Click 'Register Account'. | Name: ""<br>Email: ""<br>Pass: ""<br>Confirm: "" | Stay on `/register`; show inline validation errors for all 4 required fields. | Form remained on `/register`; four inline validation errors displayed. | **PASS** |
| **TC_REG_03** | Registration | Server live; navigate to `/register`. | 1. Enter name.<br>2. Enter malformed email.<br>3. Enter valid passwords.<br>4. Click 'Register Account'. | Name: "Pooja Kadam"<br>Email: "invalid-email-format-without-at"<br>Pass: "Password123"<br>Confirm: "Password123" | Form flags invalid email format: "Please enter a valid email address". | Registration rejected; invalid email error displayed inline. | **PASS** |
| **TC_REG_04** | Registration | Server live; navigate to `/register`. | 1. Enter name & unique email.<br>2. Enter password in first field.<br>3. Enter different password in confirm field.<br>4. Click 'Register Account'. | Name: "Siddharth Patil"<br>Email: `user_{uuid}@example.com`<br>Pass: "Password123"<br>Confirm: "DifferentPassword456" | Confirm password field flags error: "Passwords do not match." | Error displayed; registration rejected; form retained on `/register`. | **PASS** |
| **TC_REG_05** | Registration | User account with specified email already registered. | 1. Enter existing email.<br>2. Fill other fields with valid data.<br>3. Click 'Register Account'. | Email: `duplicate_{uuid}@example.com`<br>Name: "Second User"<br>Pass: "Password123"<br>Confirm: "Password123" | Reject registration; display error: "An account with this email already exists." | Registration rejected; duplicate email error message rendered. | **PASS** |
| **TC_VAL_01** | Registration | Server live; navigate to `/register`. | 1. Enter valid name & email.<br>2. Enter password shorter than 6 chars.<br>3. Confirm password.<br>4. Click 'Register Account'. | Name: "Neha Joshi"<br>Email: `short_{uuid}@example.com`<br>Pass: "123"<br>Confirm: "123" | Password field flags error: "Password must be at least 6 characters long." | System blocked submission; minimum length warning displayed. | **PASS** |
| **TC_LOG_01** | Authentication | User registered in database; navigate to `/login`. | 1. Enter registered email.<br>2. Enter correct password.<br>3. Click 'Sign In'. | Email: `authed_{uuid}@example.com`<br>Pass: "SecurePassword789" | Redirect to `/dashboard`; display user greeting and active session badge. | Redirected to `/dashboard`; welcome banner rendered with user name. | **PASS** |
| **TC_LOG_02** | Authentication | User registered in database; navigate to `/login`. | 1. Enter registered email.<br>2. Enter incorrect password.<br>3. Click 'Sign In'. | Email: `authed_{uuid}@example.com`<br>Pass: "WrongIncorrectPassword999" | Stay on `/login`; display error banner: "Incorrect password. Please try again." | Stays on `/login`; alert banner displayed with expected message. | **PASS** |
| **TC_LOG_03** | Authentication | Server live; navigate to `/login`. | 1. Enter unregistered email.<br>2. Enter password.<br>3. Click 'Sign In'. | Email: `nonexistent_{uuid}@example.com`<br>Pass: "SomeRandomPassword123" | Stay on `/login`; display error banner: "No account found with this email address." | Stays on `/login`; unregistered account error banner rendered. | **PASS** |
| **TC_LOG_04** | Authentication | Server live; navigate to `/login`. | 1. Leave email & password empty.<br>2. Click 'Sign In'. | Email: ""<br>Pass: "" | Display inline validation errors for email and password required fields. | Form remained on `/login`; both required validation errors shown. | **PASS** |
| **TC_DSH_01** | Dashboard | User logged in. | 1. Inspect dashboard elements. | Logged in user: "Tanvi Kulkarni" | Verify personalized welcome banner, email ID, and active session status badge. | All user details displayed accurately in dashboard tables. | **PASS** |
| **TC_DSH_02** | Access Control | No active user session in browser. | 1. Attempt direct GET navigation to `http://127.0.0.1:5000/dashboard`. | No session cookie | HTTP 302 Redirect to `/login`; flash warning: "Access restricted. Please log in..." | Browser redirected to `/login`; access restriction warning displayed. | **PASS** |
| **TC_DSH_03** | Session Mgmt | User authenticated on `/dashboard`. | 1. Click 'Log Out' button. | Active session | Session destroyed; redirect to `/login` with notification: "You have been successfully logged out." | Session invalidated; redirected to `/login` with logout confirmation alert. | **PASS** |
| **TC_SES_01** | Session Mgmt | User just logged out. | 1. Attempt direct GET request to `/dashboard` immediately after logout. | Invalidated session | Deny access; redirect back to `/login`. | System denied access and maintained protected state. | **PASS** |
| **TC_NAV_01** | Navigation | Server live. | 1. Visit `/`.<br>2. Visit `/register`.<br>3. Visit `/login`. | Public URLs | Document `<title>` tags match expected page identity strings. | All document titles verified with correct SPPU STAQA branding. | **PASS** |
| **TC_NAV_02** | Navigation | Server live. | 1. On `/login`, click 'Create One Here'.<br>2. On `/register`, click 'Sign In Here'.<br>3. Click browser back and forward. | Navigation links & browser history | URLs change appropriately; browser history stack preserved without errors. | Inter-page links and browser history navigation executed smoothly. | **PASS** |
| **TC_DEF_01** | Defect Logging | Server live; navigate to `/register`. | 1. Input name with numeric digits & symbols (`Rahul123$#@!`).<br>2. Fill other fields.<br>3. Submit. | Name: "Rahul123$#@!"<br>Email: `defect_{uuid}@example.com`<br>Pass: "SecurePassword123" | Expected: Inline error "Name must contain only alphabetical characters." | Actual: Application accepted input and completed registration (Defect DEF_STAQA_01). | **FAIL (Defect Captured)** |
