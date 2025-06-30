import json
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Task2_DomainSearch_EmailGeneration.pages.login_page import LoginPage
from Task2_DomainSearch_EmailGeneration.pages.dashboard_page import DashboardPage
from Task2_DomainSearch_EmailGeneration.pages.email_infra_page import EmailInfraPage
from Task2_DomainSearch_EmailGeneration.pages.domain_page import DomainPage
import os

def load_test_data():
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_path, "data", "test_data.json")
    with open(file_path) as f:
        return json.load(f)

@pytest.mark.usefixtures("setup")
class TestDomainSearchFlow:
    def test_domain_flow(self, setup):
        data = load_test_data()
        driver = setup
        driver.get("https://pyxis.lifeisgoodforlearner.com/login")

        login = LoginPage(driver)
        login.login(data["username"], data["password"])

        dashboard = DashboardPage(driver)
        dashboard.go_to_email_infra()
        dashboard.create_new_infra()
        dashboard.select_google_provider()

        domain_page = DomainPage(driver)
        domain_page.search_and_add_first_domain(
            domain_name=data["domain_to_search"],
            forwarding_domain=data["forwarding_domain"]
        )

        WebDriverWait(driver, 15).until(
            EC.url_contains("/create-email-accounts")
        )

