from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import Page

class MainPage(Page):

    LOGIN_STRING = (By.ID, "pseudonym_session_unique_id")
    PASSWORD_STRING = (By.ID, "pseudonym_session_password")
    LOGIN_BTN = (By.CSS_SELECTOR, "button.Button.Button--login")
    LOGIN_REJECTED = (By.CSS_SELECTOR, "li.ic-flash-error")
    FORGOT_PASSWORD_BTN = (By.ID, "login_forgot_password")
    FORGOT_PASSWORD_INSTR = (By.ID, "forgot_password_instructions")


    def wrong_login(self, text):
        """
        Input wrong email into login
        """
        self.input_text(text, *self.LOGIN_STRING)

    def wrong_password(self, text):
        """
        Input wrong password
        """
        self.input_text(text, *self.PASSWORD_STRING)

    def click_login_button(self):
        """
        Click on login button
        """
        self.click(*self.LOGIN_BTN)

    def alert_is_here(self):
        """
        Alert is here
        """
        assert "Invalid username or password" in self.driver.find_element(*self.LOGIN_REJECTED).text
        print('\nSign is here: ','"' ,str(self.driver.find_element(*self.LOGIN_REJECTED).text),'"' ,'.')

    def click_on_forgot_password(self):
        """
        Clicks "Forgot Password?" button
        """
        self.click(*self.FORGOT_PASSWORD_BTN)

    def forgot_passw_instruct(self):
        """
        Verify "Enter your Email and we'll send you a link to change your password." sign is here
        """
        assert "Enter your Email and we'll send you a link to change your password" in self.driver.find_element(*self.FORGOT_PASSWORD_INSTR).text
        print('\nSign is here: ','"' ,str(self.driver.find_element(*self.FORGOT_PASSWORD_INSTR).text),'"' ,'.')


