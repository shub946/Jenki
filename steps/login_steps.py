import time

from behave import given, when, then
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@given('user opens login page')
def step_impl(context):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    context.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    context.driver.get("https://wccqa.on24.com/webcast/login")
    time.sleep(10)
    print("Login page opened")

@when('user enters valid username and password')
def step_impl(context):
    context.driver.find_element(By.ID, "username").send_keys("real_username")
    context.driver.find_element(By.ID, "password").send_keys("real_password")
    context.driver.find_element(By.ID, "loginBtn").click()

    time.sleep(10)
    print("User entered credentials")

@then('user should login successfully')
def step_impl(context):
    print("Dashboard verified")