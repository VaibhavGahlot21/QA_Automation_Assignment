import time
from selenium.webdriver.common.by import By
from .base_page import BasePage

class EmailInfraPage(BasePage):
    CREATE_INFRA_BTN = (By.XPATH, "//button[contains(text(), 'Create New Email Infra')]")
    GOOGLE_PROVIDER = (By.XPATH, "//span[text()='Google']")

    def start_new_infra(self):
        print("[STEP] Clicking 'Create New Email Infra' button...")
        self.click(self.CREATE_INFRA_BTN)
        time.sleep(5)

    def select_google_provider(self):
        print("[STEP] Selecting 'Google' as email provider...")
        self.click(self.GOOGLE_PROVIDER)
