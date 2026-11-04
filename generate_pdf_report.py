"""
STAQA Mini-Project: PDF Report Generator
Generates a 17-page academic project report matching the exact format, borders,
typography, certificate, acknowledgement, index, chapters, test results,
and screenshots of the reference SPPU STAQA submission.
"""

import os
import base64
import subprocess

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")
DOCS_DIR = os.path.join(BASE_DIR, "docs")
SCREENSHOTS_DIR = os.path.join(STATIC_DIR, "doc_screenshots")


def get_base64_image(image_path):
    """Convert an image to base64 data URI."""
    if not os.path.exists(image_path):
        return ""
    with open(image_path, "rb") as f:
        data = base64.b64encode(f.read()).decode("utf-8")
        ext = os.path.splitext(image_path)[1].lower().replace(".", "")
        if ext == "jpg":
            ext = "jpeg"
        return f"data:image/{ext};base64,{data}"


logo_b64 = get_base64_image(os.path.join(STATIC_DIR, "college_logo.png"))
img1_b64 = get_base64_image(os.path.join(SCREENSHOTS_DIR, "1_dashboard.png"))
img2_b64 = get_base64_image(os.path.join(SCREENSHOTS_DIR, "2_register_validation.png"))
img3_b64 = get_base64_image(os.path.join(SCREENSHOTS_DIR, "3_login_error.png"))
img4_b64 = get_base64_image(os.path.join(SCREENSHOTS_DIR, "4_user_dashboard.png"))
img5_b64 = get_base64_image(os.path.join(SCREENSHOTS_DIR, "5_html_report.png"))
img6_b64 = get_base64_image(os.path.join(SCREENSHOTS_DIR, "6_defect_screenshot.png"))

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>STAQA Mini-Project Report - Athrav Ganorkar</title>
<style>
    @page {{
        size: A4 portrait;
        margin: 0;
    }}
    * {{
        box-sizing: border-box;
    }}
    body {{
        margin: 0;
        padding: 0;
        font-family: 'Times New Roman', Times, Georgia, serif;
        color: #000000;
        background: #ffffff;
        font-size: 11.5pt;
        line-height: 1.45;
    }}
    .page {{
        width: 210mm;
        height: 297mm;
        padding: 10mm 12mm;
        page-break-after: always;
        position: relative;
        background: #fff;
    }}
    .border-box {{
        width: 100%;
        height: 100%;
        border: 1.8px solid #000;
        padding: 16mm 18mm;
        position: relative;
    }}
    .text-center {{
        text-align: center;
    }}
    .text-justify {{
        text-align: justify;
    }}
    .fw-bold {{
        font-weight: bold;
    }}
    .page-title {{
        font-size: 15pt;
        font-weight: bold;
        letter-spacing: 0.5px;
        margin-bottom: 25px;
    }}
    .chapter-title {{
        font-size: 14pt;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
        text-transform: uppercase;
    }}
    .section-title {{
        font-size: 12.5pt;
        font-weight: bold;
        margin-top: 15px;
        margin-bottom: 8px;
    }}
    .bottom-num {{
        position: absolute;
        bottom: 7mm;
        left: 50%;
        transform: translateX(-50%);
        font-size: 11pt;
    }}
    .top-num {{
        position: absolute;
        top: 6mm;
        left: 50%;
        transform: translateX(-50%);
        font-size: 11pt;
    }}
    p {{
        margin-top: 0;
        margin-bottom: 10px;
    }}
    ul {{
        margin-top: 4px;
        margin-bottom: 12px;
        padding-left: 22px;
    }}
    li {{
        margin-bottom: 4px;
    }}
    ol {{
        margin-top: 4px;
        margin-bottom: 12px;
        padding-left: 22px;
    }}
    ol li {{
        margin-bottom: 5px;
    }}
    table {{
        width: 100%;
        border-collapse: collapse;
        margin-top: 10px;
        margin-bottom: 15px;
        font-size: 10.5pt;
    }}
    table, th, td {{
        border: 1px solid #000;
    }}
    th, td {{
        padding: 7px 8px;
        text-align: center;
        vertical-align: middle;
    }}
    .table-left td {{
        text-align: left;
    }}
    .table-green-head th {{
        background-color: #c9dbb2;
        color: #000;
        font-weight: bold;
    }}
    .code-block {{
        font-family: 'Courier New', Courier, monospace;
        font-size: 9pt;
        background-color: #fafafa;
        border: 1px solid #ddd;
        padding: 8px 10px;
        white-space: pre-wrap;
        line-height: 1.35;
        margin-bottom: 12px;
    }}
    .screenshot-img {{
        width: 100%;
        max-height: 96mm;
        object-fit: contain;
        border: 1px solid #333;
        display: block;
        margin-top: 4px;
        margin-bottom: 14px;
    }}
</style>
</head>
<body>

<!-- ================= PAGE 1: COVER PAGE ================= -->
<div class="page">
    <div class="border-box text-center" style="padding-top: 25mm; padding-bottom: 20mm;">
        <div style="font-size: 13pt; font-weight: bold; margin-bottom: 28px;">
            A MINI-PROJECT ON
        </div>
        
        <div style="font-size: 16pt; font-weight: bold; line-height: 1.35; margin-bottom: 30px;">
            Automated Web Application Testing<br>Using Selenium WebDriver
        </div>
        
        <div style="font-size: 10pt; font-weight: bold; line-height: 1.45; margin-bottom: 35px; padding: 0 10px;">
            SUBMITTED TO THE SAVITRIBAI PHULE PUNE UNIVERSITY, PUNE IN THE<br>
            FULFILLMENT OF THE REQUIREMENTS<br>
            FOR THE AWARD OF THE DEGREE<br>
            OF
        </div>
        
        <div style="font-size: 13pt; font-weight: bold; margin-bottom: 30px;">
            BACHELOR OF ENGINEERING (COMPUTER ENGINEERING)
        </div>
        
        <div style="font-size: 11pt; font-weight: bold; margin-bottom: 10px;">
            SUBMITTED BY
        </div>
        
        <div style="font-size: 12pt; font-weight: bold; margin-bottom: 25px;">
            Athrav Avinash Ganorkar B21038
        </div>
        
        <div style="margin-bottom: 25px;">
            <img src="{logo_b64}" alt="College Logo" style="width: 105px; height: auto;">
        </div>
        
        <div style="font-size: 12pt; font-weight: bold; margin-bottom: 4px;">
            DEPARTMENT OF COMPUTER ENGINEERING
        </div>
        <div style="font-size: 11.5pt; margin-bottom: 4px;">
            Zeal College of Engineering & Research
        </div>
        <div style="font-size: 10pt; margin-bottom: 25px;">
            NARHE, PUNE – 411041
        </div>
        
        <div style="font-size: 11pt; font-weight: bold; margin-bottom: 5px;">
            SAVITRIBAI PHULE PUNE UNIVERSITY
        </div>
        <div style="font-size: 11pt;">
            2026 -2027
        </div>
    </div>
</div>

<!-- ================= PAGE 2: CERTIFICATE ================= -->
<div class="page">
    <div class="border-box text-center" style="padding-top: 15mm;">
        <div style="margin-bottom: 20px;">
            <img src="{logo_b64}" alt="College Logo" style="width: 90px; height: auto;">
        </div>
        
        <div style="font-size: 15pt; font-weight: bold; letter-spacing: 1px; margin-bottom: 35px;">
            CERTIFICATE
        </div>
        
        <div style="font-size: 12pt; margin-bottom: 18px;">
            This is to certify that the project report entitles
        </div>
        
        <div style="font-size: 13pt; font-weight: bold; margin-bottom: 22px;">
            “Automated Web Application Testing Using Selenium WebDriver”
        </div>
        
        <div style="font-size: 11.5pt; margin-bottom: 12px;">
            Submitted by
        </div>
        
        <div style="font-size: 12.5pt; font-weight: bold; margin-bottom: 28px;">
            Athrav Avinash Ganorkar B21038
        </div>
        
        <div class="text-justify" style="font-size: 11.5pt; line-height: 1.6; margin-bottom: 35px;">
            is a bonafide student of this institute and the work has been carried out by him under the supervision of <strong>Prof. Pooja Kachare</strong> and it is approved for the fulfillment of the requirement of Savitribai Phule Pune University, for the award of the degree of Bachelor of Engineering (Computer Engineering).
        </div>
        
        <div style="text-align: left; font-size: 11pt; margin-bottom: 80px;">
            <div>Place: ZCOER, Pune</div>
            <div style="margin-top: 5px;">Date:</div>
        </div>
        
        <table style="border: none; width: 100%; margin-top: 40px;">
            <tr style="border: none;">
                <td style="border: none; width: 50%; text-align: center; vertical-align: bottom;">
                    <strong>Prof. Pooja Kachare</strong><br>
                    Guide<br>
                    Department of Computer Engineering
                </td>
                <td style="border: none; width: 50%; text-align: center; vertical-align: bottom;">
                    <strong>Prof. Shradhdha Dudhani</strong><br>
                    Head<br>
                    Department of Computer Engineering
                </td>
            </tr>
        </table>
    </div>
</div>

<!-- ================= PAGE 3: ACKNOWLEDGEMENT ================= -->
<div class="page">
    <div class="border-box text-center" style="padding-top: 25mm;">
        <div class="page-title" style="margin-bottom: 40px;">
            ACKNOWLEDGEMENT
        </div>
        
        <div class="text-justify" style="font-size: 12pt; line-height: 1.75; margin-bottom: 80px;">
            We take this opportunity to thank our project guide <strong>Prof. Pooja Kachare</strong> and Head of the department <strong>Prof. Shradhdha Dudhani mam</strong> for their valuable guidance and for providing all the necessary facilities, which were indispensable in the completion of this project report. We are also thankful to all the staff members of Computer Engineering Department for their valuable time, support, comments, suggestions and persuasion. We would also like to thank the institute for providing the required facilities, Internet access and important books.
        </div>
        
        <div style="text-align: right; font-size: 12pt; font-weight: bold; margin-right: 15px; margin-top: 100px;">
            Athrav Ganorkar
        </div>
    </div>
</div>

<!-- ================= PAGE 4: ABSTRACT ================= -->
<div class="page">
    <div class="border-box text-center" style="padding-top: 25mm;">
        <div class="page-title" style="margin-bottom: 35px;">
            ABSTRACT
        </div>
        
        <div class="text-justify" style="font-size: 12pt; line-height: 1.75; margin-bottom: 30px;">
            This mini project focuses on Software Testing and Quality Assurance of an automated web application developed using Python Flask, HTML, CSS, JavaScript, and SQLite. The main purpose of the project is to test the functionality, input validation, user registration, authentication, dashboard profile management, and session access control of the website.
        </div>
        
        <div class="text-justify" style="font-size: 12pt; line-height: 1.75; margin-bottom: 30px;">
            Selenium WebDriver is used for automated browser testing of the web application, while Regular Expressions are used to validate inputs such as email addresses, password length, pattern matching, and input sanitization. PyTest is utilized as the test runner to organize test execution and fixtures.
        </div>
        
        <div class="text-justify" style="font-size: 12pt; line-height: 1.75;">
            Test cases are prepared for both positive and negative scenarios, and executed to identify passed and failed test cases. The framework features automated failure screenshot capture, interactive HTML test execution reporting, and formal defect logging according to IEEE/ISTQB standards.
        </div>
    </div>
</div>

<!-- ================= PAGE 5: INDEX ================= -->
<div class="page">
    <div class="border-box" style="padding-top: 20mm;">
        <div class="chapter-title" style="margin-bottom: 30px;">
            INDEX
        </div>
        
        <table style="width: 100%; border: 1px solid #000;">
            <thead>
                <tr>
                    <th style="width: 15%;">Sr.No</th>
                    <th style="width: 65%; text-align: left; padding-left: 15px;">Title of Chapter</th>
                    <th style="width: 20%;">Page No.</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td class="fw-bold">01</td>
                    <td style="text-align: left; padding-left: 15px;" class="fw-bold">Introduction</td>
                    <td class="fw-bold">1-2</td>
                </tr>
                <tr>
                    <td></td>
                    <td style="text-align: left; padding-left: 35px;">1.1 Steps</td>
                    <td>1</td>
                </tr>
                <tr>
                    <td class="fw-bold">02</td>
                    <td style="text-align: left; padding-left: 15px;" class="fw-bold">Selenium Testing</td>
                    <td class="fw-bold">3-4</td>
                </tr>
                <tr>
                    <td></td>
                    <td style="text-align: left; padding-left: 35px;">2.1 Regular Expression & Form Validation</td>
                    <td>4</td>
                </tr>
                <tr>
                    <td class="fw-bold">03</td>
                    <td style="text-align: left; padding-left: 15px;" class="fw-bold">Results and output</td>
                    <td class="fw-bold">5-11</td>
                </tr>
                <tr>
                    <td></td>
                    <td style="text-align: left; padding-left: 35px;">3.1 Implementation and output</td>
                    <td>5</td>
                </tr>
                <tr>
                    <td></td>
                    <td style="text-align: left; padding-left: 35px;">3.2 Test results</td>
                    <td>7</td>
                </tr>
                <tr>
                    <td></td>
                    <td style="text-align: left; padding-left: 35px;">3.3 Used tools</td>
                    <td>10</td>
                </tr>
                <tr>
                    <td class="fw-bold">04</td>
                    <td style="text-align: left; padding-left: 15px;" class="fw-bold">Conclusion</td>
                    <td class="fw-bold">12</td>
                </tr>
            </tbody>
        </table>
    </div>
</div>

<!-- ================= PAGE 6: CHAPTER 1 - INTRODUCTION (P.1) ================= -->
<div class="page">
    <div class="border-box">
        <div class="top-num">1</div>
        <div class="chapter-title" style="margin-top: 10px;">
            INTRODUCTION
        </div>
        
        <div class="section-title">Problem Definition</div>
        <ul>
            <li>The objective of this mini project is to perform automated functional testing and regular expression validation using Selenium WebDriver on a dynamic web application.</li>
            <li>The website contains user registration, authentication (login/logout), session management, and protected dashboard information.</li>
            <li>The testing process is performed to verify whether the website functions correctly and whether user input follows the required validation rules.</li>
        </ul>
        
        <div class="section-title">Objectives</div>
        <p>The main objectives of the project are:</p>
        <ul>
            <li>To understand the basic concepts of software testing and QA automation.</li>
            <li>To prepare test cases for identified functional and negative test scenarios.</li>
            <li>To prepare test procedures and automation scripts for the test cases.</li>
            <li>To perform automated web testing using Selenium WebDriver and PyTest.</li>
            <li>To perform regular expression-based input validation and boundary testing.</li>
            <li>To verify form field validations, error messaging, and access control.</li>
        </ul>
        
        <div class="section-title">1.1 STEPS</div>
        <div class="fw-bold" style="margin-bottom: 6px;">Steps for Downloading and Installing Selenium WebDriver:</div>
        
        <p><strong>Step 1: Install Python</strong><br>
        Install Python 3.10 or newer (Python 3.13) on the computer.<br>
        Python provides the runtime environment to execute automated Selenium test scripts.</p>
        
        <p><strong>Step 2: Install IDE / Code Editor</strong><br>
        Install Visual Studio Code or PyCharm IDE.<br>
        The editor is used to create, execute, debug, and manage the Selenium testing project.</p>
        
        <p><strong>Step 3: Download Selenium WebDriver & PyTest Libraries</strong><br>
        Install the required Selenium and PyTest client packages via Python pip package manager.<br>
        These libraries provide the classes, locators, explicit waits, and assertion methods required for browser automation.</p>
    </div>
</div>

<!-- ================= PAGE 7: CHAPTER 1 - INTRODUCTION (P.2) ================= -->
<div class="page">
    <div class="border-box">
        <p><strong>Step 4: Configure Virtual Environment and WebDriver</strong><br>
        Create an isolated Python virtual environment and configure Selenium Manager.<br>
        Selenium 4 automatically manages the browser driver binaries (ChromeDriver/EdgeDriver) without manual downloading.</p>
        
        <div class="section-title">Test Plan for Website Testing</div>
        <p class="text-justify">A Test Plan is a document that describes the overall testing process of a software application. It is prepared using information from:</p>
        <ul>
            <li>Product Description</li>
            <li>Software Requirement Specification (SRS)</li>
            <li>Use Case Documents & User Stories</li>
        </ul>
        
        <p>A test plan defines:</p>
        <ul>
            <li>What to test (Scope and Target Modules)</li>
            <li>How to test (Automation Tools, Frameworks, Test Scripts)</li>
            <li>When to test (Execution Schedules, Regression Milestones)</li>
            <li>Who will perform the testing (QA Automation Engineers)</li>
        </ul>
        
        <p>The major components of a website test plan are:</p>
        <ol>
            <li><strong>Define Scope of Testing:</strong> Identify the modules and functions that need to be tested (Registration, Login, Dashboard, Navigation).</li>
            <li><strong>Define Objective of Testing:</strong> Specify what the testing process is expected to verify (Functional correctness, input boundary handling, security).</li>
            <li><strong>Testing Approach:</strong> Define whether testing will be performed manually, automatically, or using both methods (Hybrid with Selenium automation).</li>
            <li><strong>Testing Schedule:</strong> Define when testing activities and regression test runs will be performed.</li>
            <li><strong>Bug Tracking and Reporting:</strong> Record identified defects, capture automated failure screenshots, and prepare test reports showing their status.</li>
        </ol>
        
        <div class="bottom-num">2</div>
    </div>
</div>

<!-- ================= PAGE 8: CHAPTER 2 - SELENIUM TESTING (P.3) ================= -->
<div class="page">
    <div class="border-box">
        <div class="chapter-title">
            SELENIUM TESTING
        </div>
        
        <p class="text-justify">Selenium is an open-source project used for automating web browsers. It provides tools and libraries that allow testers to automate web applications and perform functional testing across different browsers.</p>
        
        <p>Selenium WebDriver allows a Python program to:</p>
        <ul>
            <li>Open a web browser (Google Chrome, Microsoft Edge, Firefox)</li>
            <li>Open a website and navigate between endpoints</li>
            <li>Enter information into form fields (Text inputs, passwords)</li>
            <li>Click buttons and submit forms</li>
            <li>Read webpage information and inspect DOM elements</li>
            <li>Verify expected results using assertions</li>
            <li>Perform automated test cases in headed or headless mode</li>
        </ul>
        
        <p class="text-justify">Regular expressions can be used with Selenium WebDriver to perform pattern-based validation. They can be used for:</p>
        <ul>
            <li>Extracting text from a web element</li>
            <li>Validating whether a value matches a specific pattern</li>
            <li>Validating whether a URL matches a specific pattern</li>
            <li>Validating email addresses (RFC compliant pattern)</li>
            <li>Validating password length and character complexity</li>
            <li>Validating other form inputs and error messages</li>
        </ul>
        
        <div class="section-title">Selenium Test Case Example</div>
        <p>The test case can perform the following operations:</p>
        <ul>
            <li>Open the website at local host URL.</li>
            <li>Navigate to the registration page.</li>
            <li>Enter the user's full name.</li>
            <li>Enter the unique email address.</li>
            <li>Enter password and confirm password.</li>
            <li>Submit the form and verify redirected login state.</li>
        </ul>
        
        <div class="bottom-num">3</div>
    </div>
</div>

<!-- ================= PAGE 9: CHAPTER 2 - SELENIUM TESTING (P.4) ================= -->
<div class="page">
    <div class="border-box">
        <div class="section-title" style="margin-top: 0;">Selenium Test Class Structure</div>
        <p>The project uses three important architectural types under the PyTest framework:</p>
        
        <p><strong>1. Before / Setup Fixture</strong><br>
        The fixture method is executed before the test methods of the class. It is used to initialize the WebDriver and launch the application server.<br>
        <em>Example:</em></p>
        <div class="code-block">@pytest.fixture(scope="function")
def driver():
    options = ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()</div>
        
        <p><strong>2. After / Teardown Fixture</strong><br>
        The code following the <code>yield</code> statement is executed after all test methods have completed. It is used to close the browser cleanly and terminate driver processes.</p>
        
        <p><strong>3. Test Method</strong><br>
        The <code>test_*</code> function contains the actual test logic. It performs operations such as opening the webpage, entering data, clicking buttons, and verifying results using assertions.</p>
        
        <div class="section-title">2.1 REGULAR EXPRESSION</div>
        <p class="text-justify">A Regular Expression (Regex) is a sequence of characters used to define a search or validation pattern. Regular expressions can be used to validate:</p>
        <ul>
            <li>Email addresses: <code>^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$</code></li>
            <li>Password length and complexity rules</li>
            <li>Names (Alphabetical characters only)</li>
            <li>URLs and redirect routes</li>
        </ul>
        
        <div class="bottom-num">4</div>
    </div>
</div>

<!-- ================= PAGE 10: CHAPTER 3 - RESULTS AND OUTPUT (P.5) ================= -->
<div class="page">
    <div class="border-box">
        <div class="chapter-title">
            RESULTS AND OUTPUT
        </div>
        
        <div class="section-title">3.1 IMPLEMENTATION</div>
        <p>We are testing it on sign up page and login page using Python Selenium:</p>
        
        <div class="code-block"># tests/test_registration.py - Python Selenium Automation
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest, uuid

class TestRegistration:
    def test_tc_reg_01_valid_registration(self, driver, live_server):
        # Open Website
        driver.get(f"{{live_server}}/register")
        unique_email = f"user_{{uuid.uuid4().hex[:8]}}@example.com"
        
        # Enter user registration information
        driver.find_element(By.ID, "name").send_keys("Athrav Ganorkar")
        driver.find_element(By.ID, "email").send_keys(unique_email)
        driver.find_element(By.ID, "password").send_keys("SecurePass123")
        driver.find_element(By.ID, "confirm_password").send_keys("SecurePass123")
        
        # Click Register button
        driver.find_element(By.ID, "register-btn").click()
        
        # Wait for redirect and verify success banner
        WebDriverWait(driver, 10).until(EC.url_contains("/login"))
        assert "/login" in driver.current_url
        success_msg = driver.find_element(By.ID, "alert-success").text
        assert "Registration successful" in success_msg

    def test_tc_reg_03_invalid_email_format(self, driver, live_server):
        driver.get(f"{{live_server}}/register")
        driver.find_element(By.ID, "name").send_keys("Athrav Ganorkar")
        driver.find_element(By.ID, "email").send_keys("invalid-email-format")
        driver.find_element(By.ID, "password").send_keys("Password123")
        driver.find_element(By.ID, "confirm_password").send_keys("Password123")
        driver.find_element(By.ID, "register-btn").click()
        
        # Verify Regex validation error message
        err = driver.find_element(By.ID, "email-error").text
        assert "valid email address" in err</div>
        
        <div class="bottom-num">5</div>
    </div>
</div>

<!-- ================= PAGE 11: CHAPTER 3 - RESULTS AND OUTPUT (P.6) ================= -->
<div class="page">
    <div class="border-box">
        <div class="code-block" style="margin-top: 0;"># Automatic failure screenshot hook in conftest.py
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = getattr(item, "driver", None)
        if driver:
            driver.save_screenshot(f"screenshots/FAIL_{{item.name}}.png")</div>
        
        <div class="section-title">Implementation Process</div>
        <p>The testing process follows these steps:</p>
        <ol>
            <li>Start the Chrome browser using Selenium WebDriver.</li>
            <li>Open the local test web application.</li>
            <li>Navigate to the sign-up page.</li>
            <li>Enter the required user information.</li>
            <li>Test the validation rules (Regex, required fields, passwords).</li>
            <li>Verify the output and assertion results.</li>
            <li>Record the test result and capture screenshots.</li>
            <li>Close the browser after testing.</li>
        </ol>
        
        <div class="section-title">Test Scenarios for the Sign-up page :</div>
        <ol>
            <li>Verify the messages for each mandatory field.</li>
            <li>Verify if the user cannot proceed without filling all the mandatory fields.</li>
            <li>Verify email format validation using regular expressions.</li>
            <li>Verify if numbers and special characters are restricted in Full Name.</li>
            <li>Verify if a user can sign-up successfully with all the mandatory details.</li>
            <li>Verify if a user can log in with valid credentials.</li>
            <li>Verify if the Password and Confirm Password fields accept matching strings only.</li>
            <li>Verify if the Password field enforces minimum length constraints (>= 6 characters).</li>
            <li>Verify if duplicate email addresses are rejected by the system.</li>
            <li>Verify that inline error messages and flash alerts are displayed clearly for ease of use.</li>
        </ol>
        
        <div class="bottom-num">6</div>
    </div>
</div>

<!-- ================= PAGE 12: CHAPTER 3 - SCREENSHOTS (P.7) ================= -->
<div class="page">
    <div class="border-box">
        <div class="section-title" style="margin-top: 0;">Screenshots:</div>
        
        <p class="fw-bold" style="margin-bottom: 2px;">1. Project Overview Dashboard</p>
        <img src="{img1_b64}" class="screenshot-img" alt="Project Dashboard">
        
        <p class="fw-bold" style="margin-bottom: 2px; margin-top: 8px;">2. Registration Page with Validation Errors</p>
        <img src="{img2_b64}" class="screenshot-img" alt="Registration Validation">
        
        <div class="bottom-num">7</div>
    </div>
</div>

<!-- ================= PAGE 13: CHAPTER 3 - SCREENSHOTS (P.8) ================= -->
<div class="page">
    <div class="border-box">
        <p class="fw-bold" style="margin-bottom: 2px; margin-top: 0;">3. Login Page with Authentication Validation</p>
        <img src="{img3_b64}" class="screenshot-img" alt="Login Error">
        
        <p class="fw-bold" style="margin-bottom: 2px; margin-top: 10px;">4. Authenticated User Dashboard</p>
        <img src="{img4_b64}" class="screenshot-img" alt="User Dashboard">
        
        <div class="bottom-num">8</div>
    </div>
</div>

<!-- ================= PAGE 14: CHAPTER 3 - SCREENSHOTS (P.9) ================= -->
<div class="page">
    <div class="border-box">
        <p class="fw-bold" style="margin-bottom: 2px; margin-top: 0;">5. Automated PyTest HTML Test Execution Report</p>
        <img src="{img5_b64}" class="screenshot-img" alt="PyTest HTML Report">
        
        <p class="fw-bold" style="margin-bottom: 2px; margin-top: 10px;">6. Automated Defect Reproduction & Screenshot Capture</p>
        <img src="{img6_b64}" class="screenshot-img" alt="Defect Screenshot">
        
        <div class="bottom-num">9</div>
    </div>
</div>

<!-- ================= PAGE 15: CHAPTER 3 - TEST RESULTS (P.10) ================= -->
<div class="page">
    <div class="border-box">
        <div class="chapter-title" style="margin-top: 0; margin-bottom: 12px;">
            Test Result Report
        </div>
        
        <p style="margin-bottom: 6px;">&bull; <strong>Selenium Testing Report</strong></p>
        
        <table style="margin-bottom: 15px;">
            <tr>
                <th style="width: 45%; text-align: left; padding-left: 12px; background: #f2f2f2;">EXECUTION STATUS</th>
                <td style="width: 55%; font-weight: bold; color: green;">COMPLETED</td>
            </tr>
            <tr>
                <th style="text-align: left; padding-left: 12px; background: #f2f2f2;">PASSED TESTCASES</th>
                <td style="font-weight: bold;">16</td>
            </tr>
            <tr>
                <th style="text-align: left; padding-left: 12px; background: #f2f2f2;">FAILED TESTCASES</th>
                <td style="font-weight: bold; color: red;">1</td>
            </tr>
            <tr>
                <th style="text-align: left; padding-left: 12px; background: #f2f2f2;">PENDING TESTCASES</th>
                <td>0</td>
            </tr>
            <tr>
                <th style="text-align: left; padding-left: 12px; background: #f2f2f2;">TEST CASES PLANNED</th>
                <td style="font-weight: bold;">17</td>
            </tr>
        </table>
        
        <table class="table-green-head" style="margin-bottom: 15px;">
            <thead>
                <tr>
                    <th style="width: 18%;">MODULES / SCENARIOS</th>
                    <th style="width: 30%;">DESCRIPTION</th>
                    <th style="width: 13%;">% TCs EXECUTED</th>
                    <th style="width: 13%;">% TCs PASSED</th>
                    <th style="width: 10%;">TCs PENDING</th>
                    <th style="width: 16%;">PRIORITY</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td class="fw-bold">REGISTRATION</td>
                    <td style="text-align: left; padding-left: 8px;">User signup & input validation</td>
                    <td>100</td>
                    <td>86</td>
                    <td>00</td>
                    <td>HIGH</td>
                </tr>
                <tr>
                    <td class="fw-bold">LOGIN</td>
                    <td style="text-align: left; padding-left: 8px;">Credential verification & state</td>
                    <td>100</td>
                    <td>100</td>
                    <td>00</td>
                    <td>HIGH</td>
                </tr>
                <tr>
                    <td class="fw-bold">DASHBOARD</td>
                    <td style="text-align: left; padding-left: 8px;">Protected session & access control</td>
                    <td>100</td>
                    <td>100</td>
                    <td>00</td>
                    <td>HIGH</td>
                </tr>
                <tr>
                    <td class="fw-bold">NAVIGATION</td>
                    <td style="text-align: left; padding-left: 8px;">Page titles & browser history</td>
                    <td>100</td>
                    <td>100</td>
                    <td>00</td>
                    <td>MODERATE</td>
                </tr>
            </tbody>
        </table>
        
        <p style="margin-bottom: 6px; margin-top: 15px;">&bull; <strong>Regular Expression & Validation Testing</strong></p>
        
        <table>
            <tr>
                <th style="width: 45%; text-align: left; padding-left: 12px; background: #f2f2f2;">EXECUTION STATUS</th>
                <td style="width: 55%; font-weight: bold; color: green;">COMPLETED</td>
            </tr>
            <tr>
                <th style="text-align: left; padding-left: 12px; background: #f2f2f2;">PASSED TESTCASES</th>
                <td style="font-weight: bold;">5</td>
            </tr>
            <tr>
                <th style="text-align: left; padding-left: 12px; background: #f2f2f2;">FAILED TESTCASES</th>
                <td style="font-weight: bold; color: red;">1</td>
            </tr>
            <tr>
                <th style="text-align: left; padding-left: 12px; background: #f2f2f2;">PENDING TESTCASES</th>
                <td>0</td>
            </tr>
        </table>
        
        <div class="bottom-num">10</div>
    </div>
</div>

<!-- ================= PAGE 16: CHAPTER 3 - TOOLS (P.11) ================= -->
<div class="page">
    <div class="border-box">
        <table style="margin-top: 0; margin-bottom: 12px;">
            <tr>
                <th style="width: 45%; text-align: left; padding-left: 12px; background: #f2f2f2;">TEST CASES PLANNED</th>
                <td style="width: 55%; font-weight: bold;">6</td>
            </tr>
        </table>
        
        <table class="table-green-head" style="margin-bottom: 25px;">
            <thead>
                <tr>
                    <th style="width: 18%;">MODULES / SCENARIOS</th>
                    <th style="width: 32%;">DESCRIPTION</th>
                    <th style="width: 13%;">% TCs EXECUTED</th>
                    <th style="width: 13%;">% TCs PASSED</th>
                    <th style="width: 10%;">TCs PENDING</th>
                    <th style="width: 14%;">PRIORITY</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td class="fw-bold">Email Validation</td>
                    <td style="text-align: left; padding-left: 8px;">Email must have valid @ and domain format</td>
                    <td>100</td>
                    <td>100</td>
                    <td>00</td>
                    <td>HIGH</td>
                </tr>
                <tr>
                    <td class="fw-bold">Password Length</td>
                    <td style="text-align: left; padding-left: 8px;">Password must have at least 6 characters</td>
                    <td>100</td>
                    <td>100</td>
                    <td>00</td>
                    <td>HIGH</td>
                </tr>
                <tr>
                    <td class="fw-bold">Password Match</td>
                    <td style="text-align: left; padding-left: 8px;">Confirm password must match password</td>
                    <td>100</td>
                    <td>100</td>
                    <td>00</td>
                    <td>HIGH</td>
                </tr>
                <tr>
                    <td class="fw-bold">Duplicate Email</td>
                    <td style="text-align: left; padding-left: 8px;">Duplicate email address will not get assigned</td>
                    <td>100</td>
                    <td>100</td>
                    <td>00</td>
                    <td>HIGH</td>
                </tr>
                <tr>
                    <td class="fw-bold">Strict Name Check</td>
                    <td style="text-align: left; padding-left: 8px;">Restrict numbers & symbols in Full Name</td>
                    <td>100</td>
                    <td>0</td>
                    <td>00</td>
                    <td>MEDIUM</td>
                </tr>
            </tbody>
        </table>
        
        <div class="chapter-title" style="text-align: left; font-size: 13pt; margin-bottom: 10px;">
            TOOLS
        </div>
        <ul>
            <li><strong>Python 3.13:</strong> Core programming language for application and test automation.</li>
            <li><strong>Selenium WebDriver 4.51:</strong> Browser automation framework with Selenium Manager.</li>
            <li><strong>PyTest 8.4:</strong> Test runner, modular fixtures, and test lifecycle orchestration.</li>
            <li><strong>PyTest-HTML 4.2:</strong> Generates self-contained HTML execution reports.</li>
            <li><strong>Flask 3.1 & Werkzeug 3.1:</strong> Web application framework and PBKDF2 password security.</li>
            <li><strong>SQLite 3:</strong> Embedded database engine for isolated local user persistence.</li>
            <li><strong>Google Chrome Browser:</strong> Modern web browser for automated execution.</li>
            <li><strong>Windows PowerShell:</strong> CLI scripting environment for execution.</li>
        </ul>
        
        <div class="bottom-num">11</div>
    </div>
</div>

<!-- ================= PAGE 17: CHAPTER 4 - CONCLUSION (P.12) ================= -->
<div class="page">
    <div class="border-box">
        <div class="chapter-title" style="margin-top: 15px; margin-bottom: 25px;">
            Conclusion
        </div>
        
        <div class="text-justify" style="line-height: 1.65; margin-bottom: 18px;">
            Selenium is a cost-effective and flexible tool for automating the testing of web applications. The project demonstrated how Selenium WebDriver can be used to automate a dynamic web application developed with Python Flask and SQLite.
        </div>
        
        <p style="margin-bottom: 6px;">The testing process covered important website functions such as:</p>
        <ul>
            <li>User registration</li>
            <li>Login and authentication</li>
            <li>Form validation and error messages</li>
            <li>Button testing and navigation flows</li>
            <li>Email address validation using regular expressions</li>
            <li>Password length and matching validation</li>
            <li>Session security and access control</li>
            <li>Database-related operations and duplicate prevention</li>
        </ul>
        
        <div class="text-justify" style="line-height: 1.65; margin-bottom: 18px;">
            Regular expressions were used to validate whether input values followed the required patterns. The use of Selenium helps reduce manual testing effort and provides repeatable test execution. One of the major advantages of Selenium is its ability to automate web applications across different modern browsers.
        </div>
        
        <div class="text-justify" style="line-height: 1.65; margin-bottom: 18px;">
            Regular expressions are particularly useful when testing structured text values such as email addresses, phone numbers, URLs, and passwords. Furthermore, integrating PyTest fixtures and automated failure screenshot hooks guarantees immediate visual evidence for defect logging.
        </div>
        
        <div class="text-justify" style="line-height: 1.65;">
            Overall, the project provides practical knowledge of Software Testing, Selenium WebDriver, PyTest, Regular Expressions, Functional Testing, Defect Tracking, and HTML Test Reporting.
        </div>
        
        <div class="bottom-num">12</div>
    </div>
</div>

</body>
</html>
"""

html_path = os.path.join(DOCS_DIR, "report_document.html")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"[OK] Generated report HTML document at: {{html_path}}")

# Convert HTML to PDF using Chrome Headless
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
pdf_path = os.path.join(DOCS_DIR, "STAQA_Project_Report_Athrav_Ganorkar.pdf")

cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={{pdf_path}}",
    html_path,
]

print(f"[*] Compiling PDF using Google Chrome...")
res = subprocess.run(cmd, capture_output=True, text=True)
if os.path.exists(pdf_path):
    size_kb = os.path.getsize(pdf_path) / 1024
    print(f"[SUCCESS] PDF Generated successfully: {{pdf_path}} ({{size_kb:.2f}} KB)")
else:
    print(f"[ERROR] Failed to generate PDF: {{res.stderr}}")
