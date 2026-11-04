"""
STAQA Mini-Project: Automated Dashboard & Session Security Test Suite
Automates Scenarios 10, 11, 12, and 15.
Test IDs: TC_DSH_01, TC_DSH_02, TC_DSH_03, TC_SES_01
"""

import uuid
import pytest
from tests.pages.register_page import RegisterPage
from tests.pages.login_page import LoginPage
from tests.pages.dashboard_page import DashboardPage


class TestDashboardSession:
    """Test Suite verifying Session Lifecycle, Access Control, and Logout."""

    @pytest.fixture
    def auth_user(self, driver, live_server):
        """Register and log in a fresh user, yielding credentials."""
        unique_email = f"session_{uuid.uuid4().hex[:8]}@example.com"
        password = "UserSession123"
        name = "Tanvi Kulkarni"

        reg_page = RegisterPage(driver).open(live_server)
        reg_page.register(name, unique_email, password, password)

        login_page = LoginPage(driver)
        login_page.wait_for_url_contains("/login")
        login_page.login(unique_email, password)

        dashboard_page = DashboardPage(driver)
        dashboard_page.wait_for_url_contains("/dashboard")

        return {"name": name, "email": unique_email, "password": password}

    def test_tc_dsh_01_dashboard_access_after_login(self, driver, live_server, auth_user):
        """
        [TC_DSH_01] Verify dashboard displays user details after successful login.
        Expected: Displays personalized greeting, email, and active session badge.
        """
        dashboard_page = DashboardPage(driver)
        assert "/dashboard" in driver.current_url
        assert auth_user["name"] in dashboard_page.get_welcome_message()
        assert auth_user["email"] in dashboard_page.get_user_email()

    def test_tc_dsh_02_dashboard_access_unauthenticated(self, driver, live_server):
        """
        [TC_DSH_02] Verify direct navigation to /dashboard without session is blocked.
        Expected: 302 Redirect to /login with access restriction warning.
        """
        dashboard_page = DashboardPage(driver)
        dashboard_page.open(live_server)

        login_page = LoginPage(driver)
        login_page.wait_for_url_contains("/login")
        assert "/login" in driver.current_url
        alert_text = login_page.get_alert_warning()
        assert "Access restricted" in alert_text or "Please log in" in alert_text

    def test_tc_dsh_03_successful_logout(self, driver, live_server, auth_user):
        """
        [TC_DSH_03] Verify clicking logout terminates user session.
        Expected: Redirects to /login and displays logged out confirmation banner.
        """
        dashboard_page = DashboardPage(driver)
        dashboard_page.click_logout()

        login_page = LoginPage(driver)
        login_page.wait_for_url_contains("/login")
        assert "/login" in driver.current_url
        assert "successfully logged out" in login_page.get_alert_info()

    def test_tc_ses_01_session_behavior_post_logout(self, driver, live_server, auth_user):
        """
        [TC_SES_01] Verify after logout, user cannot navigate back to dashboard.
        Expected: Attempting to reload /dashboard redirects back to /login.
        """
        dashboard_page = DashboardPage(driver)
        dashboard_page.click_logout()

        login_page = LoginPage(driver)
        login_page.wait_for_url_contains("/login")

        # Attempt to access protected dashboard again
        dashboard_page.open(live_server)
        login_page.wait_for_url_contains("/login")
        assert "/login" in driver.current_url
