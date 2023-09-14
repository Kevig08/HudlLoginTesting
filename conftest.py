import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def driver():
    # Initialize the WebDriver instance (e.g., Chrome)
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
