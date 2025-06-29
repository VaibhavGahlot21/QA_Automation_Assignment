import pytest
import json
import os
from selenium import webdriver

@pytest.fixture(scope="session")
def test_data():
    path = os.path.join(os.path.dirname(__file__), "test_data", "credentials.json")
    with open(path) as f:
        return json.load(f)

@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()
    driver.set_window_size(1366, 768)
    yield driver
    driver.quit()
