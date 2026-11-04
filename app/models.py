"""
STAQA Mini-Project: User Model & Authentication Service
Provides secure password hashing (PBKDF2-SHA256) and user persistence.
"""

from werkzeug.security import generate_password_hash, check_password_hash
from app.database import get_db_connection


class UserModel:
    """Encapsulates user authentication and database queries."""

    @staticmethod
    def get_by_email(email, db_path=None):
        """Retrieve user record by email."""
        conn = get_db_connection(db_path)
        user = conn.execute(
            "SELECT * FROM users WHERE LOWER(email) = LOWER(?)", (email.strip(),)
        ).fetchone()
        conn.close()
        return dict(user) if user else None

    @staticmethod
    def get_by_id(user_id, db_path=None):
        """Retrieve user record by ID."""
        conn = get_db_connection(db_path)
        user = conn.execute(
            "SELECT * FROM users WHERE id = ?", (user_id,)
        ).fetchone()
        conn.close()
        return dict(user) if user else None

    @staticmethod
    def create_user(name, email, password, db_path=None):
        """
        Create a new user with securely hashed password.
        Returns the new user ID on success, or raises an Exception.
        """
        password_hash = generate_password_hash(password, method="pbkdf2:sha256")
        conn = get_db_connection(db_path)
        try:
            with conn:
                cursor = conn.execute(
                    """
                    INSERT INTO users (name, email, password_hash)
                    VALUES (?, ?, ?)
                    """,
                    (name.strip(), email.strip().lower(), password_hash),
                )
                user_id = cursor.lastrowid
            return user_id
        finally:
            conn.close()

    @staticmethod
    def verify_credentials(email, password, db_path=None):
        """
        Verify user credentials.
        Returns (success: bool, user_or_error_message: dict | str).
        """
        user = UserModel.get_by_email(email, db_path)
        if not user:
            return False, "No account found with this email address."

        if not check_password_hash(user["password_hash"], password):
            return False, "Incorrect password. Please try again."

        return True, user
