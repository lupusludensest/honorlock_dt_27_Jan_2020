from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

@given("Loginpage")
def pn_lgnpag(context):
    context.app.main_page.open_page( 'login/canvas' )

@then('Wrong login "{login}"')
def wrng_lgn(context, login):
    context.app.main_page.wrong_login(login)

@then('Wrong password "{password}"')
def wrng_psswrd(context, password):
    context.app.main_page.wrong_password(password)

@then("Click on login button")
def clck_logn_bttn(context):
    context.app.main_page.click_login_button()

@then('Verify "Invalid username or password" sign is here')
def alrt_is_hr(context):
    context.app.main_page.alert_is_here()


@then('Clicks "Forgot Password" button')
def click_forgot_password(context):
    context.app.main_page.click_on_forgot_password()


@then('Verify "Enter your Email and we\'ll send you a link to change your password." sign is here')
def forgot_password_inst(context):
    context.app.main_page.forgot_passw_instruct()