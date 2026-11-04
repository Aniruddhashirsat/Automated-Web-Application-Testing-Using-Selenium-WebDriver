"""
STAQA Mini-Project: Application Routes & Controllers
Handles HTTP endpoints for user registration, authentication, protected dashboard,
and project overview documentation.
"""

import os
import re
from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash,
    send_from_directory,
    jsonify,
    current_app,
)
from app.models import UserModel

main_bp = Blueprint("main", __name__)
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")


@main_bp.route("/")
def project_home():
    """Project Overview Dashboard showing submission metadata, workflow, and report links."""
    reports_dir = os.path.abspath(
        os.path.join(current_app.root_path, "..", "reports")
    )
    report_file = os.path.join(reports_dir, "report.html")
    has_report = os.path.exists(report_file)

    return render_template(
        "index.html",
        has_report=has_report,
        page_title="STAQA Project Dashboard - Automated Web Testing",
    )


@main_bp.route("/register", methods=["GET", "POST"])
def register():
    """User Registration Controller with comprehensive input validation."""
    if "user_id" in session:
        return redirect(url_for("main.dashboard"))

    errors = {}
    form_data = {
        "name": "",
        "email": "",
        "password": "",
        "confirm_password": "",
    }

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")

        form_data["name"] = name
        form_data["email"] = email

        # Validation rules
        if not name:
            errors["name"] = "Full name is required."
        elif len(name) < 2:
            errors["name"] = "Name must be at least 2 characters long."

        if not email:
            errors["email"] = "Email address is required."
        elif not EMAIL_REGEX.match(email):
            errors["email"] = "Please enter a valid email address (e.g., student@example.com)."
        else:
            db_path = current_app.config.get("DB_PATH")
            existing_user = UserModel.get_by_email(email, db_path)
            if existing_user:
                errors["email"] = "An account with this email already exists."

        if not password:
            errors["password"] = "Password is required."
        elif len(password) < 6:
            errors["password"] = "Password must be at least 6 characters long."

        if not confirm_password:
            errors["confirm_password"] = "Please confirm your password."
        elif password and password != confirm_password:
            errors["confirm_password"] = "Passwords do not match."

        if not errors:
            try:
                db_path = current_app.config.get("DB_PATH")
                UserModel.create_user(name, email, password, db_path)
                flash("Registration successful! Please log in with your credentials.", "success")
                return redirect(url_for("main.login"))
            except Exception as e:
                errors["general"] = f"Registration failed due to a system error: {str(e)}"

    return render_template(
        "register.html",
        errors=errors,
        form=form_data,
        page_title="Register - STAQA Web Application",
    )


@main_bp.route("/login", methods=["GET", "POST"])
def login():
    """User Login Controller with authentication and error handling."""
    if "user_id" in session:
        return redirect(url_for("main.dashboard"))

    errors = {}
    form_data = {"email": "", "password": ""}

    if request.method == "POST":
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")

        form_data["email"] = email

        if not email:
            errors["email"] = "Email address is required."

        if not password:
            errors["password"] = "Password is required."

        if not errors:
            db_path = current_app.config.get("DB_PATH")
            success, result = UserModel.verify_credentials(email, password, db_path)
            if success:
                session.clear()
                session["user_id"] = result["id"]
                session["user_name"] = result["name"]
                session["user_email"] = result["email"]
                session.permanent = False
                flash(f"Welcome back, {result['name']}! Login successful.", "success")
                return redirect(url_for("main.dashboard"))
            else:
                errors["general"] = result

    return render_template(
        "login.html",
        errors=errors,
        form=form_data,
        page_title="Login - STAQA Web Application",
    )


@main_bp.route("/dashboard")
def dashboard():
    """Protected User Dashboard requiring active session."""
    if "user_id" not in session:
        flash("Access restricted. Please log in to view the dashboard.", "warning")
        return redirect(url_for("main.login"))

    db_path = current_app.config.get("DB_PATH")
    user = UserModel.get_by_id(session["user_id"], db_path)
    if not user:
        session.clear()
        flash("Session expired or user not found. Please log in again.", "danger")
        return redirect(url_for("main.login"))

    return render_template(
        "dashboard.html",
        user=user,
        page_title="Dashboard - STAQA Web Application",
    )


@main_bp.route("/logout", methods=["GET", "POST"])
def logout():
    """Log out user and invalidate session."""
    session.clear()
    flash("You have been successfully logged out.", "info")
    return redirect(url_for("main.login"))


@main_bp.route("/reports/latest")
def view_latest_report():
    """Serve the generated pytest HTML test execution report."""
    reports_dir = os.path.abspath(
        os.path.join(current_app.root_path, "..", "reports")
    )
    report_file = os.path.join(reports_dir, "report.html")
    if os.path.exists(report_file):
        return send_from_directory(reports_dir, "report.html")
    return render_template(
        "report_fallback.html",
        page_title="Test Report Status - STAQA Web Application",
    )


@main_bp.route("/api/test-status")
def test_status():
    """API endpoint returning live execution report availability status."""
    reports_dir = os.path.abspath(
        os.path.join(current_app.root_path, "..", "reports")
    )
    report_file = os.path.join(reports_dir, "report.html")
    if os.path.exists(report_file):
        size = os.path.getsize(report_file)
        mtime = os.path.getmtime(report_file)
        return jsonify({
            "report_generated": True,
            "report_url": url_for("main.view_latest_report"),
            "file_size_bytes": size,
            "last_modified": mtime,
        })
    return jsonify({
        "report_generated": False,
        "message": "No test report generated yet. Run pytest to produce results.",
    })
