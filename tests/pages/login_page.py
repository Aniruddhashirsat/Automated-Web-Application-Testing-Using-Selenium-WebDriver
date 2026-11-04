"""
STAQA Test Automation: Login Page Object
"""

from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage


class LoginPage(BasePage):
    """Page Object modeling the Login page interface and actions."""

    # Locators
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-btn")
    REGISTER_LINK = (By.ID, "register-link")

    EMAIL_ERROR = (By.ID, "email-error")
    PASSWORD_ERROR = (By.ID, "password-error")
    GENERAL_ERROR = (By.ID, "general-error")

    ALERT_SUCCESS = (By.ID, "alert-success")
    ALERT_WARNING = (By.ID, "alert-warning")
    ALERT_INFO = (By.ID, "alert-info")
    ALERT_DANGER = (By.ID, "alert-danger")

    def open(self, base_url):
        """Navigate to the login page."""
        self.driver.get(f"{base_url}/login")
        self.wait_for_title_contains("Login")
        return self

    def fill_form(self, email=None, password=None):
        """Fill login input fields."""
        if email is not None:
            self.type_text(self.EMAIL_INPUT, email)
        if password is not None:
            self.type_text(self.PASSWORD_INPUT, password)
        return self

    def submit(self):
        """Click login submit button."""
        self.click(self.LOGIN_BTN)
        return self

    def login(self, email, password):
        """Execute full login sequence."""
        self.fill_form(email, password)
        self.submit()
        return self

    def get_email_error(self):
        return self.get_text(self.EMAIL_ERROR)

    def get_password_error(self):
        return self.get_text(self.PASSWORD_ERROR)

    def get_general_error(self):
        return self.get_text(self.GENERAL_ERROR)

    def get_alert_success(self):
        return self.get_text(self.ALERT_SUCCESS)

    def get_alert_warning(self):
        return self.get_text(self.ALERT_WARNING)

    def get_alert_info(self):
        return self.get_text(self.ALERT_INFO)

    def click_register_link(self):
        self.click(self.REGISTER_LINK)
