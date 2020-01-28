from behave import given, when, then

@given("Loginpage")
def pn_lgnpag(context):
    context.app.main_page.open_page('login/canvas')

@then('Wrong login "{login}"')
def wrng_lgn(context, login):
    context.app.main_page.wrong_login(login)

@then('Wrong password "{password}"')
def wrng_psswrd(context, password):
    context.app.main_page.wrong_password(password)

@then("Click on login button")
def clck_logn_bttn(context):
    context.app.main_page.click_login_button()

@then('Verify "{sign}" sign is here')
def alrt_is_hr(context, sign):
    context.app.main_page.alert_is_here(sign)