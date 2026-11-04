"""
STAQA Mini-Project: Database Management Module
Handles SQLite connection, schema initialization, and isolated test resets.
"""

import sqlite3
import os

DB_FILENAME = "staqa_app.db"
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DEFAULT_DB_PATH = os.path.join(BASE_DIR, DB_FILENAME)


def get_db_connection(db_path=None):
    """Establish and return a SQLite database connection with row factory."""
    path = db_path or DEFAULT_DB_PATH
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn


def init_db(db_path=None):
    """Initialize database tables if they do not exist."""
    path = db_path or DEFAULT_DB_PATH
    conn = get_db_connection(path)
    with conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
    conn.close()


def reset_db(db_path=None):
    """Clear all records from database tables for test isolation."""
    path = db_path or DEFAULT_DB_PATH
    if os.path.exists(path):
        conn = get_db_connection(path)
        with conn:
            conn.execute("DELETE FROM users")
        conn.close()
    else:
        init_db(path)
