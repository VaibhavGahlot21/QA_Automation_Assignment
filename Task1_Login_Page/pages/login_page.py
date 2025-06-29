from httpx import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self, url):
        self.driver.get(url)


    def get_ui_elements(self):
        wait = WebDriverWait(self.driver, 30)

        def try_get(locator, multi=False):
            try:
                if multi:
                    elements = wait.until(EC.visibility_of_all_elements_located(locator))
                    for el in elements:
                        self.driver.execute_script("arguments[0].scrollIntoView(true);", el)
                        time.sleep(5)
                    return elements
                else:
                    el = wait.until(EC.visibility_of_element_located(locator))
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", el)
                    time.sleep(5)
                    return el
            except TimeoutException:
                print(f"[SKIP] Timeout for {locator}")
                return None if not multi else []

        return {
            "logo": try_get((By.CSS_SELECTOR, "svg")),
            "google_btn": try_get((By.XPATH, "//button[contains(text(),'Google')]")),
            "microsoft_btn": try_get((By.XPATH, "//button[contains(text(),'Microsoft')]")),
            "email": try_get((By.NAME, "email")),
            "password": try_get((By.NAME, "password")),
            "eye_icon": try_get((By.XPATH, "//button[@aria-label='toggle password visibility']")),
            "login_btn": try_get((By.XPATH, "//button[contains(text(),'Login')]")),
            "forgot_password": try_get((By.LINK_TEXT, "Forgot password?")),
            "login_with_sso": try_get((By.LINK_TEXT, "Login with SSO")),
            "sign_up": try_get((By.LINK_TEXT, "Sign up!")),
            "quote_text": try_get((By.CLASS_NAME, "quote-text")),
            "quote_author": try_get((By.CLASS_NAME, "quote-author")),
            "quote_designation": try_get((By.CLASS_NAME, "quote-designation")),
            "carousel_dots": try_get((By.CLASS_NAME, "dot"), multi=True),
        }

    def enter_email(self, email):
        self.driver.find_element(By.NAME, "email").send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.NAME, "password").send_keys(password)

    def click_login(self):
        print("[INFO] Waiting for login button to become clickable...")
        login_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']"))
        )
        print("[INFO] Clicking login button")
        login_btn.click()

    def get_error_message(self):
        try:
            return self.wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "text-red-500"))
            ).text
        except TimeoutException:
            return ""
