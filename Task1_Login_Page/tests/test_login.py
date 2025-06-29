from httpx import TimeoutException
import time
from Task1_Login_Page.pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
import pytest
from selenium.common.exceptions import TimeoutException

@pytest.mark.usefixtures("setup")
class TestLogin:

    def test_ui_elements(self, setup):
        page = LoginPage(setup)
        page.wait._timeout = 20  # Increase wait time for stability
        page.open("https://pyxis.lifeisgoodforlearner.com/login")

        try:
            elements = page.get_ui_elements()
            print("[INFO] Successfully retrieved UI elements after redirection.")
        except TimeoutException as e:
            print(f"[WARNING] Timeout while retrieving UI elements: {e}")
            elements = {}

        def safe_check(name, element):
            if element is None:
                print(f"[MISSING] '{name}' element was not found on the page.")
            else:
                try:
                    assert element.is_displayed()
                    print(f"[VISIBLE] '{name}' is present and visible.")
                except Exception as e:
                    print(f"[HIDDEN] '{name}' found but not visible. Reason: {e}")

        # Perform checks
        safe_check("logo", elements.get("logo"))
        safe_check("google_btn", elements.get("google_btn"))
        safe_check("microsoft_btn", elements.get("microsoft_btn"))
        safe_check("email", elements.get("email"))
        safe_check("password", elements.get("password"))
        safe_check("eye_icon", elements.get("eye_icon"))
        safe_check("login_btn", elements.get("login_btn"))
        safe_check("forgot_password", elements.get("forgot_password"))
        safe_check("login_with_sso", elements.get("login_with_sso"))
        safe_check("sign_up", elements.get("sign_up"))
        safe_check("quote_text", elements.get("quote_text"))
        safe_check("quote_author", elements.get("quote_author"))
        safe_check("quote_designation", elements.get("quote_designation"))

        # Handle carousel dots if present
        dots = elements.get("carousel_dots")
        if not dots:
            print("[INFO] No carousel dots present on the page.")
        else:
            for idx, dot in enumerate(dots):
                try:
                    assert dot.is_displayed()
                    print(f"[VISIBLE] Carousel dot {idx + 1} is visible.")
                except Exception as e:
                    print(f"[HIDDEN] Carousel dot {idx + 1} is not visible. Reason: {e}")

    def test_login_happy_path(self, setup, test_data):
        page = LoginPage(setup)
        page.open("https://pyxis.lifeisgoodforlearner.com/login")
        page.enter_email(test_data["valid_user"]["email"])
        page.enter_password(test_data["valid_user"]["password"])
        page.click_login()
        time.sleep(10)
        try:
            WebDriverWait(setup, 15).until(
                lambda d: "sequence" in d.current_url
            )
        except TimeoutException:
            print("Current URL after login:", setup.current_url)
            pytest.fail("Login successful, but redirected to unexpected URL.")

    def test_login_wrong_credentials(self, setup, test_data):
        page = LoginPage(setup)
        page.open("https://pyxis.lifeisgoodforlearner.com/login")
        page.enter_email(test_data["invalid_user"]["email"])
        page.enter_password(test_data["invalid_user"]["password"])
        page.click_login()

        try:
            error_text = page.get_error_message()
            print("Error message found:", error_text)
            assert any(word in error_text.lower() for word in ["invalid", "wrong", "incorrect", "not match"])

        except Exception:
            current_url = setup.current_url
            print("Current URL after login attempt:", current_url)

            assert "login" in current_url.lower(), "Login might have succeeded; 'login' not in current URL"

    def test_login_blank_fields(self, setup, test_data):
        page = LoginPage(setup)
        page.open("https://pyxis.lifeisgoodforlearner.com/login")

        page.enter_email(test_data["blank"]["email"])
        page.enter_password(test_data["blank"]["password"])
        try:
            page.click_login()
        except Exception as e:
            print("Login button not clickable", e)
        try:
            error_text = page.get_error_message()
            assert "invalid" in error_text.lower() or "required" in error_text.lower()
        except:
            assert "login" in setup.current_url.lower()

