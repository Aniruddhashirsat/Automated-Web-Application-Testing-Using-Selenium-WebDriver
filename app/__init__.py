"""
STAQA Mini-Project: Application Factory
Initializes Flask app instance, registers blueprints, and ensures database schema.
"""

import os
from flask import Flask
from app.database import init_db


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    template_dir = os.path.join(base_dir, "templates")
    static_dir = os.path.join(base_dir, "static")

    app = Flask(
        __name__,
        template_folder=template_dir,
        static_folder=static_dir,
    )

    app.config.from_mapping(
        SECRET_KEY=os.environ.get("SECRET_KEY", "staqa-sppu-selenium-secret-key-2026"),
        DB_PATH=os.path.join(base_dir, "staqa_app.db"),
    )

    if test_config:
        app.config.update(test_config)

    # Initialize SQLite database
    init_db(app.config["DB_PATH"])

    # Register routes
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app
