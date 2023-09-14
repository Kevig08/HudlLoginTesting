import time
import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from decouple import config


# The TestLogin test class contains test cases for the login functionality.
# It uses fixtures defined in the conftest.py file to set up and tear down
# a webdriver instance for each test case.
@pytest.mark.usefixtures("driver")
class TestLogin:
    base_url = config("BASE_URL")
    email = config("EMAIL")
    password = config("PASSWORD")

    # This the valid login test case.
    def test_valid_login(self, driver):
        login_page = LoginPage(driver)
        login_page.driver.get(f"{self.base_url}")
        login_page.enter_email(self.email)
        login_page.enter_password(self.password)
        login_page.click_login_button()
        time.sleep(2)
        display_name_element = driver.find_element(By.LINK_TEXT, "Home")
        # This is a simple assertion that after a successful login the test will find
        # the "Home" text in the upper right corner of the next page and if it doesn't, it
        # will display the error message assigned to the assert.
        assert display_name_element.is_displayed(), "Display name element is not displayed"

    # This is the first invalid test case using an incorrect email address.
    def test_invalid_email(self, driver):
        login_page = LoginPage(driver)
        login_page.driver.get(f"{self.base_url}")  # /login
        login_page.enter_email("kevin123@gmal.com")  # replace with invalid email
        login_page.enter_password(self.password)  # replace with invalid password
        login_page.click_login_button()
        # This assert returns the error message defined in the UI for an invalid login attempt.
        assert login_page.get_error_message() in "We don't recognize that email and/or password"

    # This is the second invalid test case using an incorrect password
    def test_invalid_password(self, driver):
        login_page = LoginPage(driver)
        login_page.driver.get(f"{self.base_url}")
        login_page.enter_email(self.email)
        login_page.enter_password("Thisisnotthemypassword")
        login_page.click_login_button()

        # This assert returns the error message defined in the UI for an invalid login attempt.
        assert login_page.get_error_message() in "We don't recognize that email and/or password"

    def test_email_empty_string(self, driver):
        login_page = LoginPage(driver)
        login_page.driver.get(f"{self.base_url}")
        login_page.enter_email("")
        login_page.enter_password(self.password)
        login_page.click_login_button()

        # This assert returns the error message defined in the UI for required fields.
        assert login_page.get_error_message() in "Please fill in all of the required fields"

    def test_password_empty_string(self, driver):
        login_page = LoginPage(driver)
        login_page.driver.get(f"{self.base_url}")
        login_page.enter_email(self.email)
        login_page.enter_password("")
        login_page.click_login_button()

        # This assert returns the error message defined in the UI for required fields.
        assert login_page.get_error_message() in "Please fill in all of the required fields"
