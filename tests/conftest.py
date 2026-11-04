"""
STAQA Test Automation: PyTest Configuration and Fixtures
Provides WebDriver setup, automatic Flask background server, isolated test data,
and automated screenshot capture upon test failure for pytest-html reports.
"""

import os
import time
import socket
import threading
import pytest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from app import create_app
from app.database import init_db, reset_db


# CLI Options
def pytest_addoption(parser):
    """Register custom CLI options."""
    parser.addoption(
        "--headed",
        action="store_true",
        default=False,
        help="Run browser in visible (headed) mode for demonstration.",
    )
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Target browser: chrome (default) or edge.",
    )


def find_free_port():
    """Find and return an available localhost TCP port."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        return s.getsockname()[1]


@pytest.fixture(scope="session")
def test_db_path(tmp_path_factory):
    """Provide a dedicated temporary SQLite database path for the test session."""
    db_file = tmp_path_factory.mktemp("staqa_data") / "test_staqa.db"
    db_path = str(db_file)
    init_db(db_path)
    return db_path


@pytest.fixture(scope="session")
def live_server(test_db_path):
    """
    Launch Flask test application on an isolated localhost port in a background thread.
    Yields the base URL: http://127.0.0.1:<port>
    """
    port = find_free_port()
    app = create_app({
        "TESTING": True,
        "DB_PATH": test_db_path,
        "SECRET_KEY": "staqa-automated-testing-secret-key",
    })

    server_thread = threading.Thread(
        target=lambda: app.run(host="127.0.0.1", port=port, debug=False, use_reloader=False),
        daemon=True,
    )
    server_thread.start()

    base_url = f"http://127.0.0.1:{port}"

    # Poll until server is responding
    max_wait = 10
    start_time = time.time()
    server_ready = False

    while time.time() - start_time < max_wait:
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=1):
                server_ready = True
                break
        except (OSError, ConnectionRefusedError):
            time.sleep(0.1)

    if not server_ready:
        raise RuntimeError(f"Live Flask test server failed to start within {max_wait}s on port {port}")

    yield base_url


@pytest.fixture(scope="function")
def driver(request):
    """
    Instantiate and configure Selenium WebDriver.
    Defaults to headless mode for CI/CD speed, with --headed flag support for viva demonstration.
    """
    is_headed = request.config.getoption("--headed")
    browser_type = request.config.getoption("--browser").lower()

    if browser_type == "chrome":
        chrome_options = ChromeOptions()
        if not is_headed:
            chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--log-level=3")

        # Selenium 4 Manager handles driver binary automatically
        driver_instance = webdriver.Chrome(options=chrome_options)
    elif browser_type == "edge":
        from selenium.webdriver.edge.options import Options as EdgeOptions
        edge_options = EdgeOptions()
        if not is_headed:
            edge_options.add_argument("--headless=new")
        edge_options.add_argument("--window-size=1920,1080")
        driver_instance = webdriver.Edge(options=edge_options)
    else:
        raise ValueError(f"Unsupported browser option: {browser_type}")

    driver_instance.implicitly_wait(1)  # Minimal fallback implicit wait; explicit waits preferred
    request.node.driver = driver_instance

    yield driver_instance

    try:
        driver_instance.quit()
    except Exception:
        pass


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    PyTest hook to automatically capture screenshots on test failure
    and attach them to pytest-html execution reports.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver_instance = getattr(item, "driver", None)
        if driver_instance:
            base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
            screenshots_dir = os.path.join(base_dir, "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            safe_name = item.name.replace("[", "_").replace("]", "_").replace("/", "_")
            filename = f"FAIL_{safe_name}_{timestamp}.png"
            filepath = os.path.join(screenshots_dir, filename)

            try:
                driver_instance.save_screenshot(filepath)
                # Attach to pytest-html report if plugin is active
                try:
                    import pytest_html
                    import base64
                    with open(filepath, "rb") as image_file:
                        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
                    
                    extra_item = pytest_html.extras.image(
                        f"data:image/png;base64,{encoded_string}", ""
                    )
                    
                    if hasattr(report, "extras"):
                        report.extras.append(extra_item)
                    else:
                        extra = getattr(report, "extra", [])
                        extra.append(extra_item)
                        report.extra = extra
                except Exception as ex:
                    print(f"[HTML Attach Error] {ex}")
            except Exception as e:
                print(f"[Screenshot Error] Could not capture screenshot: {e}")
