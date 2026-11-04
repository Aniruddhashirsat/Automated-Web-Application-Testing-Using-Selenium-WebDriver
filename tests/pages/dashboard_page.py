"""
STAQA Test Automation: Dashboard Page Object
"""

from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage


class DashboardPage(BasePage):
    """Page Object modeling the Authenticated User Dashboard."""

    # Locators
    WELCOME_MESSAGE = (By.ID, "welcome-message")
    USER_NAME = (By.ID, "user-name")
    USER_EMAIL = (By.ID, "user-email")
    ACCOUNT_STATUS = (By.ID, "account-status")
    LOGOUT_BTN = (By.ID, "logout-btn")

    def open(self, base_url):
        """Attempt direct navigation to the dashboard URL."""
        self.driver.get(f"{base_url}/dashboard")
        return self

    def get_welcome_message(self):
        return self.get_text(self.WELCOME_MESSAGE)

    def get_user_email(self):
        return self.get_text(self.USER_EMAIL)

    def is_authenticated(self):
        return self.is_displayed(self.WELCOME_MESSAGE)

    def click_logout(self):
        self.click(self.LOGOUT_BTN)
