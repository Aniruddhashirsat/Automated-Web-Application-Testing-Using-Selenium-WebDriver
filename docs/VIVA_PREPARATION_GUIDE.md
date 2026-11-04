# STAQA MINI-PROJECT: VIVA VOCE & EXTERNAL EXAM PREPARATION GUIDE

**Project Title:** Automated Web Application Testing Using Selenium WebDriver  
**Course:** Software Testing and Quality Assurance (STAQA)  
**Curriculum:** Savitribai Phule Pune University (SPPU) &bull; BE Computer Engineering  
**Student Name:** Athrav Avinash Ganorkar (B21038)  
**College:** Zeal College of Engineering & Research, Pune  
**Academic Year:** 2026–2027  

---

## 1. PROJECT EXECUTIVE SUMMARY (HOW TO EXPLAIN IN 1 MINUTE)

> *"Good morning/afternoon, Sir/Madam. My STAQA mini-project is **Automated Web Application Testing Using Selenium WebDriver**.*  
>  
> *The objective is to eliminate repetitive, error-prone manual web testing by building an end-to-end test automation framework. I developed a responsive web application using **Flask, SQLite, and Bootstrap** that features user registration with strict regex input validation, secure authentication with PBKDF2 password hashing, and session-guarded dashboard access.*  
>  
> *For automated testing, I used **Selenium WebDriver 4** and **PyTest** implementing the **Page Object Model (POM)** design pattern. The suite automates **17 test cases** covering positive, negative, boundary, and access-control scenarios.*  
>  
> *Key highlights include:*  
> *1. **Zero Flakiness:** Dynamic explicit waits (`WebDriverWait`) instead of hardcoded sleeps.*  
> *2. **Test Data Isolation:** Dynamically generated unique UUID test credentials for every run.*  
> *3. **Failure Screenshot Capture:** PyTest hook automatically takes a screenshot upon assertion failure.*  
> *4. **Audit Reporting:** Generates self-contained HTML test execution reports via `pytest-html` and logs formal defect reports according to IEEE/ISTQB standards."*

---

## 2. KEY TECHNICAL SPECIFICATIONS

| Component | Technology / Library | Purpose in this Project |
|---|---|---|
| **Programming Language** | Python 3.10+ (Tested on 3.13) | Core programming language for app and test scripts |
| **Browser Automation** | Selenium WebDriver 4.51.0 | Drives Chrome/Edge browsers natively via W3C protocol |
| **Test Runner** | PyTest 8.4.2 | Discovers tests, executes assertions, manages fixtures |
| **Reporting Tool** | pytest-html 4.2.0 | Compiles standalone HTML reports with embedded screenshots |
| **Web Application** | Flask 3.1.2 & Jinja2 | Local target web application with real HTTP routes |
| **Database** | SQLite 3 | Embedded database for user persistence and test isolation |
| **Password Security** | Werkzeug PBKDF2-SHA256 | Cryptographic password hashing (no plain-text passwords) |
| **Design Pattern** | Page Object Model (POM) | Decouples HTML locators from test logic for maintainability |

---

## 3. HOW TO RUN THE PROJECT (EXACT COMMANDS)

All commands are run in **Windows PowerShell**.

### Step 1: Open Terminal & Navigate to Project Directory
```powershell
Set-Location "C:\Users\aniru\.gemini\antigravity\scratch\STAQA_Selenium_Testing"
```

### Step 2: Start the Web Application (For Manual Demonstration)
```powershell
python run_app.py
```
Open your browser and navigate to:
- **Project QA Dashboard:** [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
- **Registration Page:** [http://127.0.0.1:5000/register](http://127.0.0.1:5000/register)
- **Login Page:** [http://127.0.0.1:5000/login](http://127.0.0.1:5000/login)
- **Latest HTML Test Report:** [http://127.0.0.1:5000/reports/latest](http://127.0.0.1:5000/reports/latest)

*(Press `CTRL+C` in the terminal to stop the application).*

---

### Step 3: Run the Automated Test Suite

Open a **new** PowerShell terminal:

#### Option A: Quick 1-Click Runner Script
```powershell
Set-Location "C:\Users\aniru\.gemini\antigravity\scratch\STAQA_Selenium_Testing"
.\run_tests.ps1
```

#### Option B: Visible (Headed) Browser Mode — **BEST FOR VIVA DEMO**
Shows the actual browser opening, typing, clicking, and validating in real time:
```powershell
pytest tests/ -v --headed --html=reports/report.html --self-contained-html
```

#### Option C: Headless Mode (Fast Execution)
```powershell
pytest tests/ -v --html=reports/report.html --self-contained-html
```

---

### Step 4: Open Test Results & Documentation

```powershell
# 1. Open the Interactive HTML Test Execution Report
Start-Process "reports\report.html"

# 2. Open the Automatically Captured Failure Screenshots
Get-ChildItem "screenshots\"

# 3. Open the 17-Page Academic Project Report PDF
Start-Process "C:\Users\aniru\Downloads\STAQA_Project_Report_Athrav_Ganorkar.pdf"
```

---

## 4. TOP 20 VIVA QUESTIONS & HIGH-SCORING MODEL ANSWERS

### Q1: What is Software Testing and what is the difference between Verification and Validation?
**Answer:**  
Software testing is the process of executing a program with the intent of finding defects and evaluating whether it meets specified requirements.  
- **Verification ("Are we building the product right?"):** Static testing without executing code. Includes code inspections, walkthroughs, and specification reviews.  
- **Validation ("Are we building the right product?"):** Dynamic testing by executing software against requirements (e.g. running our Selenium automated test suite).

---

### Q2: What is Selenium WebDriver and how does it work internally?
**Answer:**  
Selenium WebDriver is an open-source browser automation framework. In Selenium 4, it communicates using the official **W3C WebDriver Protocol**:
1. The Python test script sends actions (e.g., `driver.find_element()`) as HTTP REST requests with JSON payloads.
2. The browser driver executable (`chromedriver.exe`) receives the request.
3. The driver translates the request into native browser API calls to control Chrome.
4. The browser executes the action and returns an HTTP response back to the Python client.

---

### Q3: What is the Page Object Model (POM) and why did you use it?
**Answer:**  
The Page Object Model (POM) is an architectural design pattern in test automation where each web page has a corresponding class:
- **Page Classes (`RegisterPage`, `LoginPage`, `DashboardPage`):** Hold the UI locators (`By.ID`, `By.XPATH`) and user action methods (`register()`, `login()`).
- **Test Scripts (`test_registration.py`, `test_login.py`):** Contain only test workflows and `assert` statements.  
**Key Advantage:** If a developer changes a button ID or field locator, we only update it once in the Page class—none of our test cases break. It eliminates code duplication and simplifies maintenance.

---

### Q4: Why should we avoid `time.sleep()` in automated testing? What is the alternative?
**Answer:**  
`time.sleep()` freezes execution unconditionally for a fixed duration. This slows down test execution and causes "flaky tests" if the server or network takes slightly longer than the hardcoded sleep.  
**Alternative:** We use **Explicit Waits** (`WebDriverWait` combined with `expected_conditions`). It dynamically polls the DOM every 500ms until the expected condition (e.g., `element_to_be_clickable` or `url_contains`) is satisfied, proceeding immediately once ready.

---

### Q5: What is the difference between Implicit Wait and Explicit Wait?
**Answer:**  
- **Implicit Wait:** Configured globally once on the `driver` instance. It tells the driver to poll the DOM for a default time whenever searching for any element (`find_element`) before raising `NoSuchElementException`.
- **Explicit Wait:** Configured for a specific web element and condition (e.g., waiting for an alert, element visibility, or URL change). It offers finer control and handles dynamic asynchronous web content.

---

### Q6: What are the primary Locator strategies in Selenium? Which is best?
**Answer:**  
1. `By.ID` &mdash; **Best and fastest** because IDs are unique in well-structured DOMs.
2. `By.NAME` &mdash; Common for form inputs.
3. `By.CSS_SELECTOR` &mdash; Fast, flexible, and powerful for complex styling paths.
4. `By.XPATH` &mdash; Navigates up/down the XML/HTML DOM hierarchy; useful for dynamic elements.
5. `By.CLASS_NAME`, `By.TAG_NAME`, `By.LINK_TEXT`, `By.PARTIAL_LINK_TEXT`.

---

### Q7: What is Test Data Isolation and how did you implement it?
**Answer:**  
Test Data Isolation ensures tests do not depend on previous runs or execution order.  
In our project, registration tests dynamically generate unique email addresses using Python's `uuid.uuid4().hex[:8]` (e.g., `user_a1b2c3d4@example.com`). If we used hardcoded emails like `test@example.com`, the test would pass on the first run but fail on the second run because the email would already exist in the database.

---

### Q8: What is the difference between Positive and Negative Testing? Give examples from your project.
**Answer:**  
- **Positive Testing:** Verifies the system behaves as expected with valid inputs.  
  *Example:* Submitting valid name, email, and password redirects to `/login` with `"Registration successful!"` (`TC_REG_01`).
- **Negative Testing:** Verifies the system gracefully handles invalid or boundary inputs without crashing.  
  *Example:* Submitting mismatched passwords flags `"Passwords do not match."` (`TC_REG_04`), or submitting an invalid email flags `"Please enter a valid email address"` (`TC_REG_03`).

---

### Q9: What is the difference between an Intentionally Invalid Input and a Genuine Defect?
**Answer:**  
- **Invalid Test Input (Negative Test):** We supply invalid data expecting the application to catch it and display a validation error. The test **PASSES** when the error message is correctly displayed.
- **Genuine Defect (Bug):** A deviation where the software fails to enforce a requirement. In our project, test `TC_DEF_01` inputs numeric/symbolic characters in the Full Name (`Rahul123$#@!`). Because the application accepted it without validation, the test **FAILED** and logged defect `DEF_STAQA_01`.

---

### Q10: What is Defect Severity vs. Defect Priority?
**Answer:**  
- **Severity (Technical Impact):** The extent of damage the defect causes to system functionality (Critical, High, Medium, Low).
- **Priority (Business Urgency):** How quickly the defect must be fixed based on business needs (P1 - Immediate to P4 - Low).  
*Example:* A broken Login button is **High Severity & High Priority**. A misspelled college name on the homepage is **Low Severity & High Priority** (harmless technically, but critical for institution reputation).

---

### Q11: Explain the Defect Life Cycle (Bug Life Cycle).
**Answer:**  
1. **New:** Defect is identified and logged.
2. **Assigned / Open:** Test lead reviews and assigns it to a developer.
3. **In Progress:** Developer investigates the root cause and writes a code fix.
4. **Fixed:** Developer deploys the updated build.
5. **Retest / Verification:** QA re-executes the automated test script.
6. **Closed:** If verified passing, the bug is closed. (If still failing, it is **Reopened**).

---

### Q12: How does your framework capture screenshots automatically on test failure?
**Answer:**  
Inside `tests/conftest.py`, we implement PyTest's hook `pytest_runtest_makereport`. When a test finishes execution (`report.when == "call"`), the hook checks if `report.failed` is true. If so, it takes the test node's `driver` instance, calls `driver.save_screenshot()`, saves a timestamped PNG into `screenshots/`, and embeds it into the HTML report via `pytest_html.extras.image()`.

---

### Q13: Why did you choose PyTest instead of Python's built-in `unittest`?
**Answer:**  
1. PyTest uses standard Python `assert` statements rather than cumbersome methods like `self.assertEqual()`.
2. Powerful **Fixture Architecture** (`@pytest.fixture`) with modular dependency injection and setup/teardown via `yield`.
3. Rich plugin ecosystem, including `pytest-html` for visual reporting.
4. Clear terminal failure introspection showing exact variable values at the point of failure.

---

### Q14: How does session security and authentication work in your application?
**Answer:**  
When a user logs in, Flask sets an encrypted, HTTP-only session cookie (`session['user_id']`). The protected route `/dashboard` checks for this session key. If an unauthenticated user attempts direct navigation to `/dashboard`, the server issues an HTTP 302 redirect back to `/login` with an `"Access restricted"` flash message (`TC_DSH_02`). Logging out clears the session, preventing re-access (`TC_DSH_03` & `TC_SES_01`).

---

### Q15: How are passwords stored and secured in your application?
**Answer:**  
Passwords are never stored in plain text. We use **PBKDF2 with SHA-256** and random cryptographic salts via Werkzeug's `generate_password_hash()`. When authenticating, `check_password_hash()` hashes the entered password with the stored salt and compares the resulting hashes.

---

### Q16: What is Headless Browser Testing and when is it used?
**Answer:**  
Headless browser testing runs the browser without displaying a graphical window.  
- **Headless Mode (`--headless=new`):** Consumes less memory/CPU, runs faster, and is used in CI/CD build pipelines (e.g. GitHub Actions, Jenkins).  
- **Headed Mode (`--headed`):** Opens the visual browser window; ideal for local debugging and live viva presentations.

---

### Q17: What Regular Expressions did you use in your testing framework?
**Answer:**  
We used regular expressions for email and input pattern matching:  
- **Email Regex:** `^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$`  
It verifies presence of a valid recipient name, `@` delimiter, domain name, and top-level domain.

---

### Q18: What is a Flaky Test and how did you prevent it?
**Answer:**  
A flaky test is a test that intermittently passes and fails across runs without any underlying code changes. The main causes are race conditions, fixed sleeps, and shared state. We eliminated flakiness by:
1. Using **Explicit Waits** (`WebDriverWait`) instead of `time.sleep()`.
2. Ensuring complete **Test Data Isolation** with unique UUIDs.
3. Encapsulating all UI interactions inside the **Page Object Model**.

---

### Q19: What is Regression Testing? How does this project support it?
**Answer:**  
Regression testing verifies that recent code modifications or bug fixes have not broken existing functionality. Our automated suite runs all 17 test cases across registration, login, dashboard, and navigation in under 3 minutes with a single command, making regression testing fast, continuous, and repeatable.

---

### Q20: What are the future enhancements for this QA framework?
**Answer:**  
1. **CI/CD Integration:** Automatically trigger the test suite on every Git push using GitHub Actions.  
2. **Selenium Grid / Docker:** Run tests concurrently across Chrome, Firefox, and Edge.  
3. **BDD (Behavior-Driven Development):** Add Gherkin scenarios (`Given`, `When`, `Then`) using `behave` or `pytest-bdd` for non-technical stakeholders.

---

## 5. PROJECT FILES & DELIVERABLES LOCATION

- 📘 **Viva Guide (This Document):** [`docs/VIVA_PREPARATION_GUIDE.md`](file:///C:/Users/aniru/.gemini/antigravity/scratch/STAQA_Selenium_Testing/docs/VIVA_PREPARATION_GUIDE.md)
- 🎓 **18 Viva Questions & Answers:** [`docs/VIVA_QUESTIONS.md`](file:///C:/Users/aniru/.gemini/antigravity/scratch/STAQA_Selenium_Testing/docs/VIVA_QUESTIONS.md)
- 📑 **17-Page College Project Report PDF:** [`docs/STAQA_Project_Report_Athrav_Ganorkar.pdf`](file:///C:/Users/aniru/.gemini/antigravity/scratch/STAQA_Selenium_Testing/docs/STAQA_Project_Report_Athrav_Ganorkar.pdf)  
  *(Also saved in your Downloads folder: `C:\Users\aniru\Downloads\STAQA_Project_Report_Athrav_Ganorkar.pdf`)*
- 📊 **Interactive HTML Test Execution Report:** [`reports/report.html`](file:///C:/Users/aniru/.gemini/antigravity/scratch/STAQA_Selenium_Testing/reports/report.html)
- 📝 **Detailed Test Case Table (17 TCs):** [`docs/TEST_CASES.md`](file:///C:/Users/aniru/.gemini/antigravity/scratch/STAQA_Selenium_Testing/docs/TEST_CASES.md)
- 🐞 **Formal Defect Report (DEF_STAQA_01):** [`docs/DEFECT_REPORT.md`](file:///C:/Users/aniru/.gemini/antigravity/scratch/STAQA_Selenium_Testing/docs/DEFECT_REPORT.md)
- 📋 **Test Scenarios Document:** [`docs/TEST_SCENARIOS.md`](file:///C:/Users/aniru/.gemini/antigravity/scratch/STAQA_Selenium_Testing/docs/TEST_SCENARIOS.md)
