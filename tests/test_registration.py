"""
STAQA Mini-Project: Automated Registration Test Suite
Automates Scenarios 1 through 5, and partial Scenario 14 (Form Validation).
Test IDs: TC_REG_01, TC_REG_02, TC_REG_03, TC_REG_04, TC_REG_05, TC_VAL_01
"""

import uuid
import pytest
from tests.pages.register_page import RegisterPage
from tests.pages.login_page import LoginPage


class TestRegistration:
    """Test Suite verifying User Registration workflows and validations."""

    def test_tc_reg_01_valid_registration(self, driver, live_server):
        """
        [TC_REG_01] Verify successful registration with valid inputs.
        Expected: Redirects to /login with success alert banner.
        """
        reg_page = RegisterPage(driver).open(live_server)
        unique_email = f"user_{uuid.uuid4().hex[:8]}@example.com"

        reg_page.register(
            name="Aarav Deshmukh",
            email=unique_email,
            password="SecurePassword123",
            confirm_password="SecurePassword123",
        )

        login_page = LoginPage(driver)
        login_page.wait_for_url_contains("/login")
        assert "/login" in driver.current_url
        alert_text = login_page.get_alert_success()
        assert "Registration successful" in alert_text

    def test_tc_reg_02_missing_required_fields(self, driver, live_server):
        """
        [TC_REG_02] Verify registration fails when required fields are submitted empty.
        Expected: Inline validation errors for name, email, password, and confirm password.
        """
        reg_page = RegisterPage(driver).open(live_server)
        reg_page.register(name="", email="", password="", confirm_password="")

        assert "/register" in driver.current_url
        assert "Full name is required." in reg_page.get_name_error()
        assert "Email address is required." in reg_page.get_email_error()
        assert "Password is required." in reg_page.get_password_error()
        assert "Please confirm your password." in reg_page.get_confirm_password_error()

    def test_tc_reg_03_invalid_email_format(self, driver, live_server):
        """
        [TC_REG_03] Verify registration rejection with invalid email formats.
        Expected: Inline error indicating invalid email syntax.
        """
        reg_page = RegisterPage(driver).open(live_server)
        reg_page.register(
            name="Pooja Kadam",
            email="invalid-email-format-without-at",
            password="Password123",
            confirm_password="Password123",
        )

        assert "/register" in driver.current_url
        assert "valid email address" in reg_page.get_email_error()

    def test_tc_reg_04_mismatched_passwords(self, driver, live_server):
        """
        [TC_REG_04] Verify registration rejection when passwords do not match.
        Expected: Inline error on confirm password field indicating mismatch.
        """
        reg_page = RegisterPage(driver).open(live_server)
        unique_email = f"user_{uuid.uuid4().hex[:8]}@example.com"

        reg_page.register(
            name="Siddharth Patil",
            email=unique_email,
            password="Password123",
            confirm_password="DifferentPassword456",
        )

        assert "/register" in driver.current_url
        assert "Passwords do not match." in reg_page.get_confirm_password_error()

    def test_tc_reg_05_duplicate_email_registration(self, driver, live_server):
        """
        [TC_REG_05] Verify system prevents registering an already existing email.
        Expected: Inline error on email field stating account already exists.
        """
        reg_page = RegisterPage(driver).open(live_server)
        duplicate_email = f"duplicate_{uuid.uuid4().hex[:8]}@example.com"

        # 1. First registration (Success)
        reg_page.register(
            name="First User",
            email=duplicate_email,
            password="Password123",
            confirm_password="Password123",
        )
        login_page = LoginPage(driver)
        login_page.wait_for_url_contains("/login")

        # 2. Second registration with the same email (Should be blocked)
        reg_page.open(live_server)
        reg_page.register(
            name="Second User",
            email=duplicate_email,
            password="Password123",
            confirm_password="Password123",
        )

        assert "/register" in driver.current_url
        assert "already exists" in reg_page.get_email_error()

    def test_tc_val_01_password_length_validation(self, driver, live_server):
        """
        [TC_VAL_01] Verify password minimum length validation (< 6 characters).
        Expected: Inline error requiring at least 6 characters.
        """
        reg_page = RegisterPage(driver).open(live_server)
        unique_email = f"short_{uuid.uuid4().hex[:8]}@example.com"

        reg_page.register(
            name="Neha Joshi",
            email=unique_email,
            password="123",
            confirm_password="123",
        )

        assert "/register" in driver.current_url
        assert "at least 6 characters" in reg_page.get_password_error()
