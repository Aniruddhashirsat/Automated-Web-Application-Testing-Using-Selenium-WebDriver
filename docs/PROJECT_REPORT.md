# SAVITRIBAI PHULE PUNE UNIVERSITY
## Department of Computer Engineering
### Academic Mini-Project Report on:
# Automated Web Application Testing Using Selenium WebDriver

**Course:** Software Testing and Quality Assurance (STAQA)  
**Curriculum:** SPPU Bachelor of Engineering (B.E. / T.E. Computer Engineering)  
**Academic Year:** 2025–2026  

---

## 1. Abstract
In modern software engineering, web applications undergo frequent updates, continuous integration, and rapid deployment cycles. Manual verification of repetitive flows—such as user onboarding, authentication, session security, and input boundary validation—is prone to human error, time-intensive, and unfeasible for large regression cycles. This project implements a complete, end-to-end automated testing framework for a web application using **Selenium WebDriver** and **PyTest** under the **Page Object Model (POM)** architectural design pattern. A sample web application built with Python Flask, SQLite, and Bootstrap provides realistic authentication workflows. The automated test suite executes 17 comprehensive test cases (spanning positive, negative, boundary, and access-control scenarios), automatically captures failure screenshots, generates interactive HTML execution reports via `pytest-html`, and documents defects adhering to IEEE/ISTQB standards.

---

## 2. Problem Statement
Manual software testing suffers from significant drawbacks including:
1. High turnaround time for regression testing after bug fixes or new feature deployments.
2. Risk of oversight in negative validation paths (e.g., duplicate email checks, boundary password limits, and session hijacking).
3. Lack of consistent, auditable execution logs and automated visual evidence for failed tests.

The goal is to develop an automated testing solution using Selenium WebDriver that programmatically exercises application endpoints, validates UI/server state transitions, logs execution metrics, and provides an end-to-end defect tracking and reporting workflow suitable for academic and industrial QA standards.

---

## 3. Project Objectives
- To develop a secure, local sample web application supporting user registration, authentication, dashboard profile view, and logout with PBKDF2 password hashing.
- To design and implement a robust automated testing framework using Python, Selenium WebDriver 4, and PyTest.
- To implement the **Page Object Model (POM)** pattern to decouple UI locator representations from test assertion scripts.
- To formulate and execute positive and negative test scenarios covering 100% of core application user paths.
- To configure automated **failure screenshot capture hooks** and self-contained **HTML test execution reports**.
- To document formal QA artifacts: Test Scenarios, Detailed Test Case Table, and Defect Reports with root-cause analysis.

---

## 4. Scope

### In-Scope:
- Functional testing of User Registration (valid inputs, empty fields, malformed email, mismatched passwords, duplicate accounts).
- Functional testing of User Authentication (valid login, invalid passwords, non-existent accounts, blank inputs).
- Protected Session Verification (unauthenticated dashboard access redirection, post-logout session invalidation).
- Navigation and UI Testing (document title verification, inter-page hyperlinks, browser back/forward history).
- Defect logging and visual evidence collection.

### Out-of-Scope:
- Performance/Load testing with thousands of concurrent users (e.g. JMeter).
- Third-party OAuth providers (Google/GitHub SSO) requiring live internet connectivity.
- Multi-region cloud database replication.

---

## 5. Existing System vs. Proposed System

| Parameter | Existing System (Manual Testing) | Proposed System (Automated Selenium Framework) |
|---|---|---|
| **Execution Speed** | Slow; manual data entry into form fields takes several minutes per cycle. | Fast; executes the full 17-test regression suite in ~2.5 minutes. |
| **Consistency** | Human fatigue leads to missed edge cases or inconsistent validation. | Deterministic; executes identical test steps and assertions every time. |
| **Regression Feasibility** | Costly; requires dedicated manual testers on every minor release. | Low-cost; run on-demand or automatically in CI/CD pipelines via CLI. |
| **Evidence Collection** | Manual screenshots must be cropped and filed manually by testers. | Automated; PyTest failure hooks capture timestamped PNG screenshots immediately. |
| **Reporting** | Manual spreadsheet tallying prone to typographical errors. | Automated self-contained HTML report with live pass/fail charts and logs. |

---

## 6. Functional & Non-Functional Requirements

### Functional Requirements:
1. **User Registration:**
   - Must validate presence of Name, Email, Password, and Confirm Password.
   - Must validate RFC-compliant email syntax.
   - Must enforce minimum password length of 6 characters.
   - Must enforce matching passwords and reject duplicate emails.
2. **User Authentication:**
   - Must authenticate registered credentials against PBKDF2-SHA256 password hashes.
   - Must present informative error messages without leaking sensitive account details.
3. **Session & Access Control:**
   - Must establish HTTP-only session cookies upon valid login.
   - Must restrict `/dashboard` to active sessions only (HTTP 302 redirect on unauthorized access).
   - Must clear session data on `/logout`.
4. **Automated Test Suite:**
   - Must execute in both Headless (fast) and Headed (visible) browser modes.
   - Must capture screenshots on any assertion or timeout failure.

### Non-Functional Requirements:
- **Portability:** Operates across Windows, Linux, and macOS environments.
- **Reliability:** Zero flakiness achieved via explicit waits (`WebDriverWait`) instead of `time.sleep()`.
- **Test Isolation:** Automatic generation of unique UUID test data preventing cross-test data pollution.

---

## 7. Software and Hardware Requirements

### Software Requirements:
- **Operating System:** Windows 10/11, Ubuntu 20.04+, or macOS.
- **Programming Language:** Python 3.10 or newer (Tested on Python 3.13).
- **Web Framework:** Flask 3.1+, Werkzeug 3.1+.
- **Database:** SQLite 3 (serverless, zero external setup).
- **Browser Automation:** Selenium WebDriver 4.51.0 (with automatic driver management via Selenium Manager).
- **Test Runner:** PyTest 8.4+, pytest-html 4.2+.
- **Browser:** Google Chrome (v120+) or Microsoft Edge.

### Hardware Requirements:
- **Processor:** Intel Core i3 / AMD Ryzen 3 or higher.
- **RAM:** Minimum 4 GB (8 GB recommended for browser automation).
- **Hard Disk:** Minimum 500 MB free disk space for project files, virtualenv, and test reports.

---

## 8. System Architecture

```
                               ┌────────────────────────────────────────┐
                               │             TEST RUNNER                │
                               │        (PyTest CLI / Runner)           │
                               └──────────────────┬─────────────────────┘
                                                  │
                                                  ▼
                               ┌────────────────────────────────────────┐
                               │           TEST SUITE LAYER             │
                               │  test_registration.py, test_login.py,  │
                               │  test_dashboard_session.py, test_nav.py │
                               └──────────────────┬─────────────────────┘
                                                  │
                                                  ▼
                               ┌────────────────────────────────────────┐
                               │       PAGE OBJECT MODEL (POM)          │
                               │  RegisterPage, LoginPage, DashboardPage │
                               │  BasePage (WebDriverWait explicit waits)│
                               └──────────────────┬─────────────────────┘
                                                  │
                                                  ▼ (W3C WebDriver Protocol)
                               ┌────────────────────────────────────────┐
                               │          SELENIUM WEBDRIVER            │
                               │          (ChromeDriver Engine)         │
                               └──────────────────┬─────────────────────┘
                                                  │
                                                  ▼
                               ┌────────────────────────────────────────┐
                               │         TARGET WEB APPLICATION         │
                               │         (Local Flask App :5000)        │
                               │          - Jinja2 HTML Templates       │
                               │          - SQLite User Database        │
                               │          - PBKDF2 Password Hashing     │
                               └────────────────────────────────────────┘
```

---

## 9. Test Strategy
The test strategy utilizes a **Black-Box Testing** approach augmented by **Page Object Model** encapsulation:
1. **Explicit Synchronization:** Dynamic element polling using `WebDriverWait` and `expected_conditions` (`visibility_of_element_located`, `element_to_be_clickable`, `url_contains`).
2. **Data-Driven Dynamic Fixtures:** Unique test identities created per test iteration using `uuid.uuid4().hex[:8]`.
3. **Failure Hook:** `pytest_runtest_makereport` automatically intercepts failed assertions and writes full-resolution PNG screenshots to `screenshots/`.
4. **Execution Reporting:** `pytest-html` aggregates metadata, test hierarchy, execution durations, and failure screenshots into a single self-contained HTML deliverable (`reports/report.html`).

---

## 10. Test Execution & Results Summary
- **Total Tests:** 17
- **Passed:** 16 (All functional requirements verified)
- **Failed / Defect Captured:** 1 (`TC_DEF_01` validating strict alphabetical name validation)
- **Execution Time:** ~2 minutes 35 seconds
- **HTML Report Path:** `reports/report.html`
- **Screenshots Generated:** Saved in `screenshots/` directory.

---

## 11. Defect Reporting Process
Defects are tracked using the IEEE 829 / ISTQB compliant standard:
- Defect ID, Title, Severity, Priority, Environment, Reproduction Steps, Expected vs Actual Behavior, and Screenshot Evidence.
- Formally documented in `docs/DEFECT_REPORT.md` (Defect `DEF_STAQA_01` logged).

---

## 12. Screenshots to Capture for College File
When compiling the academic report submission file, the following visual evidence should be included:
1. **Application UI Screenshots:**
   - Registration Page with form fields (`/register`).
   - Registration Page displaying inline validation errors.
   - Login Page (`/login`).
   - Protected Dashboard showing authenticated user profile (`/dashboard`).
   - Project Overview Dashboard (`/`).
2. **Automation Execution Screenshots:**
   - Windows PowerShell console showing `pytest tests/ -v` execution progress.
   - Failure screenshot generated in `screenshots/` (`FAIL_test_tc_def_01_numeric_name_rejection_*.png`).
   - Self-contained HTML report (`reports/report.html`) showing Passed & Failed test breakdown and execution summary graph.

---

## 13. Limitations
1. Testing is conducted in local single-server environments; high latency network delays are not simulated.
2. Captcha verification is not included to avoid blocking automated regression scripts.
3. Database tests currently use SQLite; production multi-node databases (PostgreSQL/MySQL) may have different concurrency locks.

---

## 14. Future Scope
1. **CI/CD Integration:** Integrate the PyTest suite into GitHub Actions or Jenkins pipelines to trigger automatically on pull requests.
2. **Cross-Browser Grid:** Run tests concurrently across Chrome, Firefox, Safari, and Edge using Selenium Grid or Docker containers.
3. **API & Contract Testing:** Integrate REST API tests using `requests` to test backend endpoints without spinning up the browser.
4. **BDD (Behavior Driven Development):** Implement Gherkin syntax (Given/When/Then) using `behave` or `pytest-bdd` for non-technical stakeholder communication.

---

## 15. Conclusion
The "Automated Web Application Testing Using Selenium WebDriver" mini-project successfully demonstrates how QA automation principles can be applied to ensure software reliability, data integrity, and access security. By utilizing Selenium WebDriver, PyTest, and the Page Object Model, the framework delivers high maintainability, zero test flakiness, automated failure documentation, and comprehensive HTML reporting. The project satisfies all requirements for the SPPU Computer Engineering Software Testing and Quality Assurance (STAQA) curriculum.
