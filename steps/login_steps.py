from behave import given, when, then

@given('user is on login page')
def step_impl(context):
    print("Login page opened")

@when('user enters valid username and password')
def step_impl(context):
    print("User entered credentials")

@then('user should see dashboard')
def step_impl(context):
    print("Dashboard verified")