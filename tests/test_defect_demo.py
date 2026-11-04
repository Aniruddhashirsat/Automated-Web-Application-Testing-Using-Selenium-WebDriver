"""
STAQA Mini-Project: Defect Reproduction & Screenshot Verification Test
Demonstrates the automated failure hook and defect logging lifecycle.
This test evaluates a strict business rule (Alphabetical Name Validation).
When run, if the application lacks this validation, it fails and triggers
the automatic failure screenshot capture into screenshots/ and attaches to pytest-html.
"""

import uuid
import pytest
from tests.pages.register_page import RegisterPage


class TestDefectReproduction:
    """Test suite demonstrating automated defect detection and screenshot logging."""

    def test_tc_def_01_numeric_name_rejection(self, driver, live_server):
        """
        [DEF_STAQA_01] Verify system rejects names containing numbers or script symbols.
        Expected: Displays inline error 'Name must contain only alphabetical characters'.
        Actual Application State: Accepts alphanumeric string and allows registration.
        Demonstration: This test fails intentionally to verify screenshot capture on failure.
        """
        reg_page = RegisterPage(driver).open(live_server)
        unique_email = f"defect_{uuid.uuid4().hex[:8]}@example.com"

        # Input name with numbers and special characters
        reg_page.register(
            name="Rahul123$#@!",
            email=unique_email,
            password="SecurePassword123",
            confirm_password="SecurePassword123",
        )

        # Strict requirement check: Form should reject numeric/symbolic names
        error_msg = reg_page.get_name_error()
        assert "Name must contain only alphabetical characters" in error_msg, (
            "DEFECT DETECTED: Application accepted numeric/symbolic characters in full name without validation error."
        )
