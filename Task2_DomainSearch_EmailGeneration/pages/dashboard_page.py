import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from .base_page import BasePage

class DashboardPage(BasePage):
    EMAIL_INFRA_MENU = (By.XPATH, "//a[contains(@href, '/email-account') and contains(., 'Email')]")
    CREATE_INFRA_BTN = (By.XPATH, "//button[contains(., 'Create New Email Infra')]")
    GOOGLE_PROVIDER = (By.XPATH, "//button[contains(., 'Google')]")

    def go_to_email_infra(self):
        print("Clicking Email Infra menu")
        self.click(self.EMAIL_INFRA_MENU)

    def create_new_infra(self):
        print("Clicking 'Create New Email Infra button")
        try:
            self.click(self.CREATE_INFRA_BTN)
        except TimeoutException:
            raise Exception("Failed to click 'Create New Email Infra' button.")
        time.sleep(5)

    def select_google_provider(self):
        print("Selecting 'Google' as email provider")
        try:
            self.click(self.GOOGLE_PROVIDER)
        except TimeoutException:
            raise Exception("Failed to select Google provider")
        time.sleep(2)
