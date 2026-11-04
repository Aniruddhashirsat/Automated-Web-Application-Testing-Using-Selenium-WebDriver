import os
import time
import threading
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from app import create_app

app = create_app()
server_thread = threading.Thread(
    target=lambda: app.run(host="127.0.0.1", port=5010, debug=False, use_reloader=False),
    daemon=True
)
server_thread.start()
time.sleep(2)

options = Options()
options.add_argument("--headless=new")
options.add_argument("--window-size=1400,900")
driver = webdriver.Chrome(options=options)

def js_click(elem):
    driver.execute_script("arguments[0].click();", elem)

os.makedirs("static/doc_screenshots", exist_ok=True)

# 1. Project Dashboard
driver.get("http://127.0.0.1:5010/")
time.sleep(1)
driver.save_screenshot("static/doc_screenshots/1_dashboard.png")

# 2. Register Page with validation errors
driver.get("http://127.0.0.1:5010/register")
time.sleep(0.5)
driver.find_element("id", "name").send_keys("Rahul123$#@!")
driver.find_element("id", "email").send_keys("invalid-email-format")
driver.find_element("id", "password").send_keys("123")
driver.find_element("id", "confirm_password").send_keys("456")
js_click(driver.find_element("id", "register-btn"))
time.sleep(1)
driver.save_screenshot("static/doc_screenshots/2_register_validation.png")

# 3. Login Page with invalid credentials error
driver.get("http://127.0.0.1:5010/login")
time.sleep(0.5)
driver.find_element("id", "email").send_keys("wrong_user@example.com")
driver.find_element("id", "password").send_keys("wrongpass")
js_click(driver.find_element("id", "login-btn"))
time.sleep(1)
driver.save_screenshot("static/doc_screenshots/3_login_error.png")

# 4. Successful Registration and User Dashboard
driver.get("http://127.0.0.1:5010/register")
time.sleep(0.5)
driver.find_element("id", "name").send_keys("Athrav Ganorkar")
driver.find_element("id", "email").send_keys("athrav.ganorkar@example.com")
driver.find_element("id", "password").send_keys("SecurePass123")
driver.find_element("id", "confirm_password").send_keys("SecurePass123")
js_click(driver.find_element("id", "register-btn"))
time.sleep(1)

driver.find_element("id", "email").send_keys("athrav.ganorkar@example.com")
driver.find_element("id", "password").send_keys("SecurePass123")
js_click(driver.find_element("id", "login-btn"))
time.sleep(1)
driver.save_screenshot("static/doc_screenshots/4_user_dashboard.png")

# 5. HTML Test Execution Report
report_abs = os.path.abspath("reports/report.html").replace("\\", "/")
driver.get(f"file:///{report_abs}")
time.sleep(2)
driver.save_screenshot("static/doc_screenshots/5_html_report.png")

# 6. Failure screenshot / Defect reproduction
defect_img = [f for f in os.listdir("screenshots") if f.startswith("FAIL_")]
if defect_img:
    img_path = os.path.abspath(os.path.join("screenshots", defect_img[0])).replace("\\", "/")
    driver.get(f"file:///{img_path}")
    time.sleep(1)
    driver.save_screenshot("static/doc_screenshots/6_defect_screenshot.png")

driver.quit()
print("All screenshots successfully captured!")
