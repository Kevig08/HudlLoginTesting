from selenium import webdriver


from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service_obj = Service()
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

# Navigate to the Hudl main page
driver.get("https://www.hudl.com/login")
# driver.find_element(By.XPATH, './/a[@data-qa-id="login-select"]').click()
# driver.find_element(By.XPATH, './/a[@data-qa-id="login-hudl"]').click()
driver.find_element(By.ID, "email").send_keys("Kevig18@yahoo.com")
driver.find_element(By.ID, "password").send_keys("Tammylove2020")
driver.find_element(By.ID, "logIn").click()
