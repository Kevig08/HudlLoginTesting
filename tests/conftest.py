import pytest
from selenium import webdriver


# Here I defined the scope as function so that each test will run a single browser
# instance per test, performing a setup and teardown per test.
@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
