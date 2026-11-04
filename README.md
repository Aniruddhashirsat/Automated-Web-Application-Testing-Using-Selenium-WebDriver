# STAQA Mini-Project: Automated Web Application Testing Using Selenium WebDriver

**Course:** Software Testing and Quality Assurance (STAQA)  
**Affiliation:** Savitribai Phule Pune University (SPPU) &bull; Department of Computer Engineering  
**Academic Year:** 2025–2026  

---

## 1. Abstract
In modern agile software development, continuous regression testing is required to verify that new code changes do not break existing functionality. This project delivers a complete, production-grade automated testing framework for a web application using **Selenium WebDriver** and **PyTest** under the **Page Object Model (POM)** design pattern. It tests user registration, authentication, input validation, session access control, and browser navigation. The framework automatically captures full-resolution screenshots on test failure, compiles an interactive HTML test execution report using `pytest-html`, and documents defects according to IEEE 829 / ISTQB guidelines.

---

## 2. Problem Statement
Manual software testing is repetitive, time-consuming, prone to human fatigue, and insufficient for verifying complex validation combinations and security boundaries. Furthermore, manual test logs frequently lack deterministic reproduction steps and automated visual evidence. This project addresses these challenges by automating end-to-end user workflows, enforcing test data isolation, and generating audit-ready test reports and defect logs.

---

## 3. Project Objectives
- Build a responsive, local sample web application with secure PBKDF2 password hashing and session management.
- Automate 15+ functional, negative, boundary, and access-control test scenarios.
- Apply the **Page Object Model (POM)** design pattern for high code reusability and locator maintainability.
- Eliminate test flakiness by employing **explicit waits** (`WebDriverWait`) instead of hardcoded sleeps.
- Integrate automated **failure screenshot capture** and self-contained **HTML reporting**.
- Provide complete academic submission documentation adhering to the SPPU STAQA syllabus.

---

## 4. Technology Stack
- **Programming Language:** Python 3.10+ (Tested on Python 3.13)
- **Web Framework:** Flask 3.1+, Werkzeug 3.1+
- **Database:** SQLite 3 (isolated test databases via PyTest fixtures)
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5, Bootstrap Icons
- **Test Automation:** Selenium WebDriver 4.51.0 (with automatic driver management via Selenium Manager)
- **Test Runner & Reports:** PyTest 8.4+, pytest-html 4.2+
- **Version Control:** Git

---

## 5. Project Directory Structure
```
STAQA_Selenium_Testing/
├── app/
│   ├── __init__.py           # Flask application factory
│   ├── database.py           # SQLite connection & schema initialization
│   ├── models.py             # User authentication model & password hashing
│   └── routes.py             # Controllers for /register, /login, /dashboard, /
├── templates/
│   ├── base.html             # Bootstrap 5 layout, navbar, flash alerts, footer
│   ├── index.html            # QA Project Dashboard with live test status & guide
│   ├── register.html         # Registration form with explicit validation IDs
│   ├── login.html            # Login form with explicit validation IDs
│   ├── dashboard.html        # Authenticated user dashboard & logout
│   └── report_fallback.html  # Informational fallback when report is pending
├── static/
│   ├── css/custom.css        # Clean UI styling
│   └── js/main.js            # Frontend interactivity
├── tests/
│   ├── __init__.py
│   ├── conftest.py           # PyTest fixtures: live_server, driver, failure screenshot hook
│   ├── pages/                # Page Object Model (POM) classes
│   │   ├── __init__.py
│   │   ├── base_page.py      # Explicit wait wrappers & Selenium actions
│   │   ├── register_page.py  # Registration page locators & methods
│   │   ├── login_page.py     # Login page locators & methods
│   │   └── dashboard_page.py # Dashboard page locators & methods
│   ├── test_registration.py  # Scenarios 1-5, 14 (Valid, invalid, duplicate, lengths)
│   ├── test_login.py         # Scenarios 6-9 (Valid, wrong pass, unreg email, empty)
│   ├── test_dashboard_session.py # Scenarios 10-12, 15 (Access control, logout, sessions)
│   ├── test_navigation.py    # Scenarios 13-14 (Page titles, browser back/forward)
│   └── test_defect_demo.py   # Defect detection test with automatic failure screenshot
├── reports/
│   └── report.html           # Generated self-contained HTML test execution report
├── screenshots/
│   └── FAIL_*.png            # Automatically captured failure screenshots
├── docs/
│   ├── TEST_SCENARIOS.md     # Detailed test scenarios specification
│   ├── TEST_CASES.md         # Detailed test case table with actual results
│   ├── DEFECT_REPORT.md      # Defect template, lifecycle, and DEF_STAQA_01 report
│   ├── PROJECT_REPORT.md     # Comprehensive academic report outline
│   └── VIVA_QUESTIONS.md     # 18 SPPU external viva questions & model answers
├── requirements.txt          # Python dependencies
├── pytest.ini                # PyTest execution configuration
├── run_app.py                # Standalone Flask server launcher
├── run_tests.ps1             # 1-click Windows PowerShell test runner script
├── .gitignore
└── README.md                 # Project documentation & execution guide
```

---

## 6. Step-by-Step Windows PowerShell Execution Guide

Follow these exact commands in **Windows PowerShell**:

### Step 1: Navigate to the Project Directory
```powershell
Set-Location "C:\Users\aniru\.gemini\antigravity\scratch\STAQA_Selenium_Testing"
```

### Step 2: Create a Virtual Environment (Optional / Recommended)
```powershell
python -m venv venv
```

### Step 3: Activate the Virtual Environment
```powershell
.\venv\Scripts\Activate.ps1
```
*(Note: If execution policies block scripts, run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` first).*

### Step 4: Install Dependencies
```powershell
pip install -r requirements.txt
```

### Step 5: Start the Flask Application (For Manual Exploration)
```powershell
python run_app.py
```
Open your browser and navigate to:
- **Project Dashboard:** `http://127.0.0.1:5000/`
- **Registration Page:** `http://127.0.0.1:5000/register`
- **Login Page:** `http://127.0.0.1:5000/login`
- **Live HTML Report:** `http://127.0.0.1:5000/reports/latest`

*(Press `CTRL+C` in the terminal to stop the application).*

### Step 6: Execute the Automated Selenium Test Suite

#### Option A: One-Click Execution via PowerShell Script
```powershell
.\run_tests.ps1
```

#### Option B: Standard Headless Execution (Fast Execution)
```powershell
pytest tests/ -v --html=reports/report.html --self-contained-html
```

#### Option C: Headed Mode (Visible Browser for Viva Demonstration)
```powershell
pytest tests/ -v --headed --html=reports/report.html --self-contained-html
```

### Step 7: Open the Generated HTML Test Report
```powershell
Start-Process "reports\report.html"
```

---

## 7. Automated Test Scenarios & Execution Results

| Test ID | Module | Scenario Tested | Mode | Result |
|---|---|---|---|---|
| **TC_REG_01** | Registration | Valid registration with unique email and secure password | Positive | **PASS** |
| **TC_REG_02** | Registration | Missing required fields validation (empty submission) | Negative | **PASS** |
| **TC_REG_03** | Registration | Invalid email format syntax rejection | Negative | **PASS** |
| **TC_REG_04** | Registration | Mismatched password and confirm-password rejection | Negative | **PASS** |
| **TC_REG_05** | Registration | Duplicate email registration prevention | Negative | **PASS** |
| **TC_VAL_01** | Registration | Minimum password length validation (< 6 characters) | Boundary | **PASS** |
| **TC_LOG_01** | Authentication | Valid login credentials authorization & redirect | Positive | **PASS** |
| **TC_LOG_02** | Authentication | Incorrect password rejection and error display | Negative | **PASS** |
| **TC_LOG_03** | Authentication | Unregistered email rejection | Negative | **PASS** |
| **TC_LOG_04** | Authentication | Empty login fields validation | Negative | **PASS** |
| **TC_DSH_01** | Dashboard | Dashboard rendering with personalized user name & email | Positive | **PASS** |
| **TC_DSH_02** | Access Control | Unauthenticated dashboard access blocked (302 redirect) | Security | **PASS** |
| **TC_DSH_03** | Session Mgmt | User logout and session destruction | Positive | **PASS** |
| **TC_SES_01** | Session Mgmt | Session state invalidation post-logout | Security | **PASS** |
| **TC_NAV_01** | Navigation | Document `<title>` tag and URL verification across pages | Functional | **PASS** |
| **TC_NAV_02** | Navigation | Inter-page navigation links and browser back/forward buttons | Functional | **PASS** |
| **TC_DEF_01** | Defect Logging | Name field strict character validation (triggers screenshot) | Defect | **FAIL (Defect Caught)** |

---

## 8. Defect Reporting & Failure Screenshots
- When a test fails (e.g. `TC_DEF_01`), PyTest's `pytest_runtest_makereport` hook captures a full browser screenshot and stores it in `screenshots/`.
- The failure screenshot is automatically linked inside `reports/report.html`.
- A formal defect report (`DEF_STAQA_01`) is documented in [`docs/DEFECT_REPORT.md`](file:///C:/Users/aniru/.gemini/antigravity/scratch/STAQA_Selenium_Testing/docs/DEFECT_REPORT.md).

---

## 9. Academic Documentation Files
- **Test Scenarios:** [`docs/TEST_SCENARIOS.md`](file:///C:/Users/aniru/.gemini/antigravity/scratch/STAQA_Selenium_Testing/docs/TEST_SCENARIOS.md)
- **Detailed Test Cases Table:** [`docs/TEST_CASES.md`](file:///C:/Users/aniru/.gemini/antigravity/scratch/STAQA_Selenium_Testing/docs/TEST_CASES.md)
- **Defect Report & Life Cycle:** [`docs/DEFECT_REPORT.md`](file:///C:/Users/aniru/.gemini/antigravity/scratch/STAQA_Selenium_Testing/docs/DEFECT_REPORT.md)
- **Project Report Outline:** [`docs/PROJECT_REPORT.md`](file:///C:/Users/aniru/.gemini/antigravity/scratch/STAQA_Selenium_Testing/docs/PROJECT_REPORT.md)
- **Viva Questions & Model Answers:** [`docs/VIVA_QUESTIONS.md`](file:///C:/Users/aniru/.gemini/antigravity/scratch/STAQA_Selenium_Testing/docs/VIVA_QUESTIONS.md)
