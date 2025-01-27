from behave import *

@given("I am on the Register page")
def step_impl(context):
    context.register_page.open()

@when("I click Register button")
def step_impl(context):
    context.register_page.click_register_button()

@then("First name mandatory error is displayed")
def step_impl(context):
    context.register_page.verify_first_name_error_displayed()

@then("Last name mandatory error is displayed")
def step_impl(context):
    context.register_page.verify_last_name_error_displayed()

@then("Email mandatory error is displayed")
def step_impl(context):
    context.register_page.verify_email_mandatory_error_displayed()

@then("Password mandatory error is displayed")
def step_impl(context):
    context.register_page.verify_password_mandatory_error_displayed()

@then("Password confirm mandatory error is displayed")
def step_impl(context):
    context.register_page.verify_password_confirm_mandatory_error_displayed()

@then("Password min length error is displayed")
def step_impl(context):
    context.register_page.verify_password_min_length_error_displayed()

@when("I click outside the password field")
def step_impl(context):
    context.register_page.click_your_password_label()