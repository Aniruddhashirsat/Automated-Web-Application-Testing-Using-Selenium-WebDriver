"""
STAQA Test Automation: Base Page Class
Provides robust Selenium explicit wait wrappers and helper methods.
Avoids hardcoded sleeps and ensures resilient synchronization.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BasePage:
    """Base class for all Page Objects in the STAQA test suite."""

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find_element(self, locator):
        """Wait for element to be visible and return it."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator):
        """Wait for elements and return list."""
        try:
            return self.wait.until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            return []

    def click(self, locator):
        """Wait until element is clickable and perform click."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type_text(self, locator, text):
        """Clear existing text and type new text."""
        element = self.find_element(locator)
        element.clear()
        if text:
            element.send_keys(text)

    def get_text(self, locator):
        """Get visible inner text of element."""
        try:
            element = self.find_element(locator)
            return element.text.strip()
        except TimeoutException:
            return ""

    def is_displayed(self, locator):
        """Check if element is currently displayed on the page."""
        try:
            return self.find_element(locator).is_displayed()
        except (TimeoutException, NoSuchElementException):
            return False

    def wait_for_url_contains(self, substring):
        """Wait until current URL contains specific substring."""
        return self.wait.until(EC.url_contains(substring))

    def wait_for_title_contains(self, substring):
        """Wait until page title contains specific substring."""
        return self.wait.until(EC.title_contains(substring))

    def get_title(self):
        """Return the current document title."""
        return self.driver.title

    def get_current_url(self):
        """Return the current browser URL."""
        return self.driver.current_url
