"""
STAQA Mini-Project: Automated UI & Browser Navigation Test Suite
Automates Scenarios 13 and partial 14.
Test IDs: TC_NAV_01, TC_NAV_02
"""

from tests.pages.register_page import RegisterPage
from tests.pages.login_page import LoginPage


class TestNavigation:
    """Test Suite verifying Page Titles, Browser History Navigation, and Inter-page Links."""

    def test_tc_nav_01_page_titles_and_urls(self, driver, live_server):
        """
        [TC_NAV_01] Verify correct HTML title tags and URL paths across public endpoints.
        Expected: Title contains descriptive page identity and STAQA branding.
        """
        # Home / Project Dashboard
        driver.get(live_server)
        assert "STAQA Project Dashboard" in driver.title

        # Register Page
        driver.get(f"{live_server}/register")
        assert "Register - STAQA Web Application" in driver.title

        # Login Page
        driver.get(f"{live_server}/login")
        assert "Login - STAQA Web Application" in driver.title

    def test_tc_nav_02_inter_page_links_and_history(self, driver, live_server):
        """
        [TC_NAV_02] Verify seamless navigation between Login and Register via hyperlinks and browser back/forward.
        Expected: Links navigate between forms correctly without breaking history stack.
        """
        login_page = LoginPage(driver).open(live_server)
        assert "/login" in driver.current_url

        # Click Register link from Login page
        login_page.click_register_link()
        register_page = RegisterPage(driver)
        register_page.wait_for_url_contains("/register")
        assert "/register" in driver.current_url

        # Click Sign In link from Register page
        register_page.click_login_link()
        login_page.wait_for_url_contains("/login")
        assert "/login" in driver.current_url

        # Test browser back button
        driver.back()
        register_page.wait_for_url_contains("/register")
        assert "/register" in driver.current_url

        # Test browser forward button
        driver.forward()
        login_page.wait_for_url_contains("/login")
        assert "/login" in driver.current_url
