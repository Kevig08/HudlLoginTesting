import time

import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from decouple import config


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()

    yield driver
    driver.quit()


@pytest.mark.usefixtures("driver")
class TestLogin:
    base_url = config("BASE_URL")
    email = config("EMAIL")
    password = config("PASSWORD")

    # assert "Welcome" in driver.title

    def test_invalid_login(self, driver):
        login_page = LoginPage(driver)
        login_page.driver.get(f"{self.base_url}")  # /login

        login_page.enter_email("kevin123@.com")  # replace with invalid email
        login_page.enter_password("invalid_password")  # replace with invalid password
        login_page.click_login_button()

        assert login_page.get_error_message() in "We don't recognize that email and/or password"

    def test_valid_login(self, driver):
        login_page = LoginPage(driver)
        login_page.driver.get(f"{self.base_url}")  # /login

        login_page.enter_email(self.email)
        login_page.enter_password(self.password)
        login_page.click_login_button()
