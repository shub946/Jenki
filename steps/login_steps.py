import time
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium import webdriver

@given('user opens login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://wccqa.on24.com/webcast/login")
    context.driver.maximize_window()
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
    time.sleep(5)
    assert "webcasts" in context.driver.current_url.lower()
    print("Login successful")
    context.driver.quit()


@when('user enters invalid username and password')
def step_impl(context):
    context.driver.find_element(By.ID, "username").send_keys("qauser001")
    context.driver.find_element(By.ID, "password").send_keys("Password")
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(10)
    print("User entered invalid credentials")
@then('error messag is displaying')
def step_impl(context):
    time.sleep(5)
    assert "webcasts" in context.driver.current_url.lower()
    print("error messag displayed")
    context.driver.quit()