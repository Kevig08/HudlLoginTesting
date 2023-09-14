from selenium.webdriver.common.by import By


# This initializes a login page object
class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # These are the locators that are defined and utilized in the tests.
    email = (By.ID, "email")
    password = (By.ID, "password")
    login_button = (By.ID, "logIn")
    error_message = (By.CSS_SELECTOR, ".error-message")

    # These are reusable page objects for the tests.
    def enter_email(self, email):
        self.driver.find_element(*self.email).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text
