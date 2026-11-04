# Software Testing & Quality Assurance (STAQA)
## Test Scenario Specification Document
**Project:** Automated Web Application Testing Using Selenium WebDriver  
**Course:** SPPU Computer Engineering (STAQA Mini-Project)  
**Academic Year:** 2025–2026  

---

### 1. Document Overview
This document specifies the high-level test scenarios covering the Registration, Login, Dashboard, Navigation, and Session Management components of the web application.

---

### 2. Test Scenarios Summary Table

| Scenario ID | Module | Scenario Title | Test Type | Objective |
|---|---|---|---|---|
| **TS_REG_01** | Registration | Registration with valid information | Positive | Verify that a new user can successfully register with valid details. |
| **TS_REG_02** | Registration | Registration with missing required fields | Negative | Verify that leaving required fields blank triggers inline validation errors. |
| **TS_REG_03** | Registration | Registration with invalid email format | Negative | Verify that malformed email inputs are rejected with informative error text. |
| **TS_REG_04** | Registration | Registration with mismatched passwords | Negative | Verify that non-matching password confirmation is caught and rejected. |
| **TS_REG_05** | Registration | Registration with duplicate email address | Negative | Verify that duplicate user emails cannot be registered twice in the database. |
| **TS_REG_06** | Registration | Form validation message visibility | Negative | Verify inline error message rendering and focus state. |
| **TS_LOG_01** | Authentication | Login with valid credentials | Positive | Verify registered user can authenticate and access the dashboard. |
| **TS_LOG_02** | Authentication | Login with incorrect password | Negative | Verify system blocks login on wrong password and displays error banner. |
| **TS_LOG_03** | Authentication | Login with unregistered email | Negative | Verify system displays 'No account found' for non-existent users. |
| **TS_LOG_04** | Authentication | Login with empty fields | Negative | Verify system prevents empty submission and flags missing credentials. |
| **TS_DSH_01** | Dashboard | Dashboard access after successful login | Positive | Verify user is greeted by name and profile data is accurately rendered. |
| **TS_DSH_02** | Access Control | Dashboard access without authentication | Security / Negative | Verify unauthenticated requests to `/dashboard` redirect to `/login`. |
| **TS_DSH_03** | Session Mgmt | Successful user logout | Positive | Verify logout terminates session and redirects to login with flash banner. |
| **TS_NAV_01** | Navigation | Browser navigation and page titles | Functional | Verify accurate document `<title>` tags and URLs on each endpoint. |
| **TS_NAV_02** | Navigation | Inter-page links and browser history | Functional | Verify navigation via links and browser back/forward buttons works smoothly. |
| **TS_SES_01** | Session Mgmt | Session state post-logout | Security / Negative | Verify back-button or direct URL access after logout does not re-open dashboard. |
| **TS_DEF_01** | Defect Logging | Name field strict character validation | Boundary / Defect | Verify whether full name field accepts numeric digits or symbols. |

---

### 3. Detailed Scenario Descriptions

#### TS_REG_01: Valid User Registration
- **Preconditions:** Application running, browser opened to `/register`.
- **Action:** User provides valid Full Name, unique email, password (>= 6 chars), matching confirmation.
- **Expected Outcome:** User record persisted into SQLite; browser redirected to `/login` with success banner.

#### TS_REG_02: Missing Required Fields
- **Preconditions:** Browser opened to `/register`.
- **Action:** User clicks "Register Account" without filling any fields.
- **Expected Outcome:** Form remains on `/register`; four distinct inline errors appear for name, email, password, and confirm password.

#### TS_REG_03: Invalid Email Format
- **Preconditions:** Browser opened to `/register`.
- **Action:** User enters an invalid email string (e.g. `invalid-email-format-without-at`).
- **Expected Outcome:** Form validation flags invalid email format; user is not registered.

#### TS_REG_04: Mismatched Passwords
- **Preconditions:** Browser opened to `/register`.
- **Action:** User enters `Password123` in Password and `DifferentPassword456` in Confirm Password.
- **Expected Outcome:** Confirm password field displays "Passwords do not match."

#### TS_REG_05: Duplicate Email Registration
- **Preconditions:** User account with email `duplicate@example.com` already registered.
- **Action:** Second user attempts registration using the same email address.
- **Expected Outcome:** Email field displays "An account with this email already exists."

#### TS_LOG_01: Valid Authentication
- **Preconditions:** User is registered in system; browser at `/login`.
- **Action:** Enter registered email and matching password, click "Sign In".
- **Expected Outcome:** Redirects to `/dashboard`; session cookie established; personalized greeting shown.

#### TS_LOG_02: Incorrect Password
- **Preconditions:** Registered user exists; browser at `/login`.
- **Action:** Enter registered email with invalid password.
- **Expected Outcome:** Stays on `/login`; displays "Incorrect password. Please try again."

#### TS_LOG_03: Unregistered Email
- **Preconditions:** Email does not exist in SQLite database; browser at `/login`.
- **Action:** Enter unregistered email with any password.
- **Expected Outcome:** Displays "No account found with this email address."

#### TS_LOG_04: Empty Login Fields
- **Preconditions:** Browser at `/login`.
- **Action:** Click "Sign In" with empty inputs.
- **Expected Outcome:** Inline errors indicate both email and password are required.

#### TS_DSH_01: Dashboard Presentation
- **Preconditions:** User successfully authenticated.
- **Action:** View `/dashboard`.
- **Expected Outcome:** Welcome banner displays user's full name, email, user ID, and active session badge.

#### TS_DSH_02: Unauthenticated Dashboard Restriction
- **Preconditions:** No active session cookie in browser.
- **Action:** Directly navigate to `/dashboard`.
- **Expected Outcome:** HTTP 302 redirect to `/login`; warning message: "Access restricted. Please log in."

#### TS_DSH_03: User Logout
- **Preconditions:** Authenticated user viewing `/dashboard`.
- **Action:** Click "Log Out" button.
- **Expected Outcome:** Session invalidated; redirected to `/login` with notification: "You have been successfully logged out."

#### TS_SES_01: Session Invalidation Post-Logout
- **Preconditions:** User logged out.
- **Action:** Attempt to re-access `/dashboard` or press browser back button.
- **Expected Outcome:** System restricts access and redirects to `/login`.

#### TS_NAV_01 & TS_NAV_02: Page Titles & Navigation Flow
- **Preconditions:** Application running.
- **Action:** Navigate between home, register, and login; verify `<title>` and history buttons.
- **Expected Outcome:** Titles match specification ("Register - ...", "Login - ...", "Dashboard - ...").
