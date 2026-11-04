"""
STAQA Mini-Project: Automated Authentication Test Suite
Automates Scenarios 6 through 9.
Test IDs: TC_LOG_01, TC_LOG_02, TC_LOG_03, TC_LOG_04
"""

import uuid
import pytest
from tests.pages.register_page import RegisterPage
from tests.pages.login_page import LoginPage
from tests.pages.dashboard_page import DashboardPage


class TestLogin:
    """Test Suite verifying User Authentication workflows and error states."""

    @pytest.fixture
    def registered_user(self, driver, live_server):
        """Helper fixture to create a valid user for login testing."""
        unique_email = f"authed_{uuid.uuid4().hex[:8]}@example.com"
        password = "SecurePassword789"
        name = "Kavita Rao"

        reg_page = RegisterPage(driver).open(live_server)
        reg_page.register(name, unique_email, password, password)

        login_page = LoginPage(driver)
        login_page.wait_for_url_contains("/login")

        return {"name": name, "email": unique_email, "password": password}

    def test_tc_log_01_valid_login(self, driver, live_server, registered_user):
        """
        [TC_LOG_01] Verify successful authentication with valid email and password.
        Expected: Redirects to /dashboard and displays personalized welcome banner.
        """
        login_page = LoginPage(driver).open(live_server)
        login_page.login(registered_user["email"], registered_user["password"])

        dashboard_page = DashboardPage(driver)
        dashboard_page.wait_for_url_contains("/dashboard")
        assert "/dashboard" in driver.current_url
        welcome = dashboard_page.get_welcome_message()
        assert registered_user["name"] in welcome

    def test_tc_log_02_incorrect_password(self, driver, live_server, registered_user):
        """
        [TC_LOG_02] Verify authentication fails when given wrong password.
        Expected: Remains on /login and displays invalid password warning.
        """
        login_page = LoginPage(driver).open(live_server)
        login_page.login(registered_user["email"], "WrongIncorrectPassword999")

        assert "/login" in driver.current_url
        assert "Incorrect password" in login_page.get_general_error()

    def test_tc_log_03_unregistered_email(self, driver, live_server):
        """
        [TC_LOG_03] Verify authentication fails when email is not registered in system.
        Expected: Displays account not found error message.
        """
        login_page = LoginPage(driver).open(live_server)
        fake_email = f"nonexistent_{uuid.uuid4().hex[:8]}@example.com"
        login_page.login(fake_email, "SomeRandomPassword123")

        assert "/login" in driver.current_url
        assert "No account found" in login_page.get_general_error()

    def test_tc_log_04_empty_login_fields(self, driver, live_server):
        """
        [TC_LOG_04] Verify validation flags when login submitted with empty inputs.
        Expected: Displays required validation messages for email and password.
        """
        login_page = LoginPage(driver).open(live_server)
        login_page.login("", "")

        assert "/login" in driver.current_url
        assert "Email address is required." in login_page.get_email_error()
        assert "Password is required." in login_page.get_password_error()
