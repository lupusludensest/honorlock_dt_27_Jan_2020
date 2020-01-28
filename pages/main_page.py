from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import Page

class MainPage(Page):

    LOGIN_STRING = (By.ID, "pseudonym_session_unique_id")
    PASSWORD_STRING = (By.ID, "pseudonym_session_password")
    LOGIN_BTN = (By.CSS_SELECTOR, "button.Button.Button--login")
    LOGIN_REJECTED = (By.CSS_SELECTOR, "li.ic-flash-error")


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
        assert 'Invalid username or password' in self.driver.find_element(*self.LOGIN_REJECTED).text
        print('Sign is here: ', str(self.driver.find_element(*self.LOGIN_REJECTED).text), '.')

