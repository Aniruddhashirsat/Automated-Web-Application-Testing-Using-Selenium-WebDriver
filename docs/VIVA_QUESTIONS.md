# Software Testing & Quality Assurance (STAQA)
## College Submission: 18 Comprehensive Viva Questions & Model Answers
**Subject:** Software Testing and Quality Assurance (STAQA)  
**Degree:** Bachelor of Engineering (Computer Engineering) - Savitribai Phule Pune University (SPPU)  
**Project:** Automated Web Application Testing Using Selenium WebDriver  

---

### Q1: What is Selenium WebDriver, and how does it differ from Selenium IDE?
**Answer:**  
Selenium WebDriver is a browser automation tool that provides a programming interface to create and execute test scripts across multiple browsers and platforms. Unlike Selenium IDE (which is a browser plugin limited to record-and-playback with minimal logic), WebDriver directly drives the browser natively using the browser vendor's native HTTP/W3C protocol support. It supports programming languages like Python, Java, and C#, complex assertions, loops, conditionals, dynamic locators, and framework integration (e.g. PyTest).

---

### Q2: What is the Page Object Model (POM), and what are its key advantages?
**Answer:**  
Page Object Model (POM) is an industry-standard test design pattern where each web page in the application is represented by its own class. The class contains:
1. Web element locators (e.g. `By.ID`, `By.XPATH`).
2. Action methods that interact with those elements (e.g. `register()`, `login()`).

**Advantages:**
- **Separation of Concerns:** Test scripts contain only assertions and business logic, while Page classes hold UI locators.
- **Maintainability:** If a locator changes (e.g. button ID changes), it only needs to be updated in one place (the Page class), not across dozens of test cases.
- **Code Reusability:** Methods like `login()` can be reused across multiple test suites.

---

### Q3: Why should hardcoded `time.sleep()` be avoided in automated testing? What should be used instead?
**Answer:**  
`time.sleep()` forces execution to freeze unconditionally for a fixed number of seconds regardless of whether the web element has already loaded. This causes:
- Slow and bloated test suite execution times.
- Flaky tests if network or server delay exceeds the sleep duration.

**Solution:** Use **Explicit Waits** (`WebDriverWait` combined with `expected_conditions`). Explicit waits poll the DOM dynamically (typically every 500ms) until a specific condition is met (such as `element_to_be_clickable` or `visibility_of_element_located`) or a maximum timeout expires, continuing immediately once ready.

---

### Q4: Explain the difference between Implicit Wait and Explicit Wait in Selenium.
**Answer:**  
- **Implicit Wait:** Globally set once for the entire WebDriver instance lifecycle. It tells the driver to poll the DOM for a specified duration whenever searching for any element (`find_element`) before throwing `NoSuchElementException`.
- **Explicit Wait:** Applied conditionally to a specific element and a specific condition (e.g. visibility, clickable, URL change, text presence). It is far more precise, flexible, and robust for dynamic web applications (AJAX, SPAs).

---

### Q5: What is PyTest, and why is it preferred over Python's built-in `unittest`?
**Answer:**  
PyTest is a mature Python testing framework that offers:
1. **Cleaner Syntax:** Plain `assert` statements instead of verbose methods like `self.assertEqual()`.
2. **Powerful Fixture Architecture:** Modular, dependency-injected fixtures with custom scopes (`function`, `session`, `module`) and seamless teardown via `yield`.
3. **Rich Plugin Ecosystem:** Plugins like `pytest-html` (visual execution reports) and `pytest-xdist` (parallel execution).
4. **Detailed Failure Introspection:** Prints exact variables, diffs, and context when an assertion fails.

---

### Q6: What is the difference between Positive Testing and Negative Testing?
**Answer:**  
- **Positive Testing:** Validates that the system works as intended when provided with correct, valid inputs (e.g., registering with a valid email and 8-character password succeeds and redirects to dashboard).
- **Negative Testing:** Validates that the system gracefully handles unexpected, boundary, or invalid inputs without crashing or behaving incorrectly (e.g., submitting an invalid email syntax or mismatched passwords correctly displays validation error messages).

---

### Q7: What is Test Data Isolation, and why is it important in our project?
**Answer:**  
Test Data Isolation ensures that individual test cases do not depend on the execution order or side-effects of other test cases. In our project, each registration test generates a unique user email using `uuid.uuid4().hex[:8]`. If we hardcoded `test@example.com`, the test would pass on the first run but fail on the second run because the email would already exist in the database. Isolation guarantees repeatable, deterministic test runs.

---

### Q8: What are Locators in Selenium? Name the primary locator strategies supported in Selenium 4.
**Answer:**  
Locators are addresses used by Selenium WebDriver to identify HTML elements on a web page. Primary locator strategies include:
1. `By.ID` (Fastest, unique, and preferred).
2. `By.NAME` (Common for form inputs).
3. `By.CLASS_NAME` (CSS classes).
4. `By.CSS_SELECTOR` (Powerful, concise styling queries).
5. `By.XPATH` (Navigates XML/HTML hierarchy; useful when IDs/classes are dynamic).
6. `By.TAG_NAME` (HTML tag such as `h1`, `button`, `input`).
7. `By.LINK_TEXT` and `By.PARTIAL_LINK_TEXT` (Anchor tag text).

---

### Q9: How does the automated failure screenshot hook work in our testing framework?
**Answer:**  
Our framework implements the PyTest hook `pytest_runtest_makereport` inside `conftest.py`. Whenever a test execution completes (`report.when == "call"`), the hook checks if `report.failed` is true. If so, it extracts the active `driver` instance from the test node, calls `driver.save_screenshot()`, saves a timestamped PNG into the `screenshots/` directory, and attaches the image directly into the generated HTML report via `pytest_html.extras.image()`.

---

### Q10: What is the difference between Defect Severity and Defect Priority? Provide examples.
**Answer:**  
- **Severity:** The technical impact of the defect on system operation (Critical, High, Medium, Low).
- **Priority:** The business urgency of resolving the defect (P1, P2, P3, P4).
- *Example 1 (High Severity, High Priority):* The Login button crashes the server with a 500 Internal Server Error, preventing all users from accessing the app.
- *Example 2 (Low Severity, High Priority):* The university logo on the homepage is misspelled or displays a broken image icon. Technically harmless, but immediately visible and urgent for reputation.

---

### Q11: How does Selenium WebDriver communicate with the web browser?
**Answer:**  
Selenium 4 communicates via the **W3C WebDriver Standard Protocol**. When a test command is issued (e.g. `driver.find_element()`):
1. The language binding (Python Selenium client) converts the command into an HTTP REST request with JSON payload.
2. The request is sent to the browser driver executable (e.g. `chromedriver.exe`).
3. The browser driver translates the command into internal browser native automation calls and executes it in the browser.
4. The browser returns the result back over HTTP to the Python test client.

---

### Q12: How do you handle session and authentication testing in Selenium?
**Answer:**  
Web applications maintain state using HTTP cookies (e.g. `session` cookie). We test session authentication by:
1. Logging in via the UI and verifying that subsequent requests to protected endpoints (like `/dashboard`) are permitted.
2. Logging out and verifying that the session cookie is invalidated or cleared.
3. Attempting to directly navigate to `/dashboard` without an active session and verifying that the server issues a 302 redirect back to `/login` with an unauthorized warning banner.

---

### Q13: What is the role of `conftest.py` in PyTest?
**Answer:**  
`conftest.py` is PyTest's configuration file for sharing fixtures, hooks, and CLI options across multiple test files in a directory without needing explicit imports. In our project, `conftest.py` provides:
- Custom CLI options `--headed` and `--browser`.
- The `live_server` fixture that spins up the background Flask server.
- The `driver` fixture that initializes and tears down Chrome/Edge WebDriver.
- The `pytest_runtest_makereport` hook for failure screenshot capturing.

---

### Q14: How are passwords secured in the Flask web application? Why shouldn't tests print passwords?
**Answer:**  
Passwords must never be stored in plain text. Our application hashes passwords using **PBKDF2 with SHA-256** and a cryptographic salt via Werkzeug's `generate_password_hash()`. When authenticating, `check_password_hash()` compares the hashed input against the stored hash. Automated test scripts and logs must never log raw passwords to console or reports to prevent credential leakage in CI/CD build artifacts.

---

### Q15: What is the Defect Life Cycle (Bug Life Cycle)?
**Answer:**  
The Defect Life Cycle is the sequence of states a defect traverses from identification to closure:
1. **New:** Defect is discovered and logged.
2. **Open / Assigned:** Lead assigns the defect to a developer.
3. **In Progress:** Developer investigates and codes a fix.
4. **Fixed:** Developer deploys the updated code.
5. **Retest / Verification:** QA re-executes the automated test script.
6. **Closed:** If the defect is resolved, status becomes Closed.
7. **Reopened:** If the test fails again, it is returned to the developer.

---

### Q16: What is Headless Browser Testing? When is it used versus Headed mode?
**Answer:**  
Headless browser testing runs the browser without a graphical user interface (GUI window).
- **Headless Mode (`--headless`):** Used in CI/CD pipelines, automated build servers, and large regression suites because it consumes significantly less memory and CPU, and executes faster.
- **Headed Mode (`--headed`):** Renders the visible browser window on screen. It is used during test development, interactive debugging, and college viva presentations to visually demonstrate browser interactions to examiners.

---

### Q17: What is the difference between Verification and Validation in Software Testing?
**Answer:**  
- **Verification:** "Are we building the product right?" Evaluates artifacts, code reviews, and specifications without executing code (Static Testing).
- **Validation:** "Are we building the right product?" Evaluates the actual working software by executing tests against user and business requirements (Dynamic Testing, such as our Selenium test suite).

---

### Q18: What are Flaky Tests and how does this framework prevent them?
**Answer:**  
A flaky test is a test that exhibits both a passing and a failing status across multiple runs without any changes to the underlying code. The primary causes are race conditions, network latency, and hardcoded sleeps. Our framework prevents flakiness by:
1. Replacing fixed delays with **explicit waits** (`WebDriverWait` with conditions like `element_to_be_clickable`).
2. Ensuring complete **test data isolation** with dynamically generated UUID test emails.
3. Employing the **Page Object Model** to isolate locator changes from test assertions.
