"""
STAQA Test Automation: Register Page Object
"""

from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage


class RegisterPage(BasePage):
    """Page Object modeling the Registration page interface and actions."""

    # Locators
    NAME_INPUT = (By.ID, "name")
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    CONFIRM_PASSWORD_INPUT = (By.ID, "confirm_password")
    REGISTER_BTN = (By.ID, "register-btn")
    LOGIN_LINK = (By.ID, "login-link")

    NAME_ERROR = (By.ID, "name-error")
    EMAIL_ERROR = (By.ID, "email-error")
    PASSWORD_ERROR = (By.ID, "password-error")
    CONFIRM_PASSWORD_ERROR = (By.ID, "confirm-password-error")
    GENERAL_ERROR = (By.ID, "general-error")

    def open(self, base_url):
        """Navigate to the registration page."""
        self.driver.get(f"{base_url}/register")
        self.wait_for_title_contains("Register")
        return self

    def fill_form(self, name=None, email=None, password=None, confirm_password=None):
        """Fill registration input fields."""
        if name is not None:
            self.type_text(self.NAME_INPUT, name)
        if email is not None:
            self.type_text(self.EMAIL_INPUT, email)
        if password is not None:
            self.type_text(self.PASSWORD_INPUT, password)
        if confirm_password is not None:
            self.type_text(self.CONFIRM_PASSWORD_INPUT, confirm_password)
        return self

    def submit(self):
        """Click the registration submit button."""
        self.click(self.REGISTER_BTN)
        return self

    def register(self, name, email, password, confirm_password):
        """Execute full registration sequence."""
        self.fill_form(name, email, password, confirm_password)
        self.submit()
        return self

    def get_name_error(self):
        return self.get_text(self.NAME_ERROR)

    def get_email_error(self):
        return self.get_text(self.EMAIL_ERROR)

    def get_password_error(self):
        return self.get_text(self.PASSWORD_ERROR)

    def get_confirm_password_error(self):
        return self.get_text(self.CONFIRM_PASSWORD_ERROR)

    def get_general_error(self):
        return self.get_text(self.GENERAL_ERROR)

    def click_login_link(self):
        self.click(self.LOGIN_LINK)
