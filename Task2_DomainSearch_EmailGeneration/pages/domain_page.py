from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import os

from Task2_DomainSearch_EmailGeneration.pages.base_page import BasePage


class DomainPage(BasePage):
    DOMAIN_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Primary Domain')]")
    SEARCH_BTN = (By.XPATH, '//button[.//span[text()="Search"]]')
    DOMAIN_ROW = (By.XPATH, "//table//tbody//tr")
    ADD_BTN = (By.XPATH, "//table//tbody//tr[1]//td[3]//*[contains(@class,'add-to-cart-icon')]")
    NEXT_BUTTON = (By.XPATH, "//button[.//span[text()='Next']]")
    FORWARD_INPUT = (By.XPATH, "//form//input[contains(@placeholder, 'Forwarding Domain')]")    # updated based on your provided XPath
    SAVE_BTN = (By.XPATH, "//button[.//span[text()='Save']]")
    GENERATED_EMAIL = (By.XPATH, "//div[contains(@class,'email-account')]")

    def search_and_add_first_domain(self, domain_name, forwarding_domain="sales.com"):
        try:
            print(f"Entering domain: {domain_name}")

            for _ in range(3):
                try:
                    input_box = WebDriverWait(self.driver, 15).until(
                        EC.visibility_of_element_located(self.DOMAIN_INPUT)
                    )
                    input_box.clear()
                    input_box.send_keys(domain_name)
                    break
                except TimeoutException:
                    self.driver.refresh()
            else:
                raise TimeoutException("Domain input field not found after 3 retries.")

            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.SEARCH_BTN)).click()
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.DOMAIN_ROW))
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.ADD_BTN)).click()
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.NEXT_BUTTON)).click()
            time.sleep(2)
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.FORWARD_INPUT)).send_keys(
                forwarding_domain)
            time.sleep(2)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.SAVE_BTN)).click()
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.GENERATED_EMAIL))
            print("Staying on page 20s to allow all UI elements to load")
            time.sleep(20)

            print("Done: All elements are visible as expected.")

        except TimeoutException as e:
            print(f"Timeout while waiting for element: {e}")
            raise e


        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_path = f"screenshots/domain_flow_success_{timestamp}.png"
        self.driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved: {screenshot_path}")



