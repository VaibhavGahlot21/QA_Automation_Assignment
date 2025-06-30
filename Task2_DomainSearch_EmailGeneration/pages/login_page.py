import time

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from Task2_DomainSearch_EmailGeneration.pages.base_page import BasePage

class LoginPage(BasePage):
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BTN = (By.XPATH, "//button[@type='submit']")

    def login(self, email, password):
        print("Entering email")
        self.enter_text(self.EMAIL_INPUT, email)

        print("Entering password")
        self.enter_text(self.PASSWORD_INPUT, password)

        print("Clicking Login")
        try:
            self.click(self.LOGIN_BTN)
        except TimeoutException:
            raise Exception("login button not found.")
        time.sleep(5)
