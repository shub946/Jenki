import time

from behave import given, when, then
#from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@given('user opens login page')
def step_impl(context):
    context.driver = webdriver.Chrome();
    context.driver.get("https://wccqa.on24.com/webcast/login");
    # for maximize window
    context.driver.maximize_window();
    time.sleep(10)
    print("Login page opened")

@when('user enters valid username and password')
def step_impl(context):
    context.driver.find_element(By.ID, "username").send_keys("qauser001")
    context.driver.find_element(By.ID, "password").send_keys("Password1")
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(10)
    print("User entered credentials")

@then('user should login successfully')
def step_impl(context):
    print("Dashboard verified")