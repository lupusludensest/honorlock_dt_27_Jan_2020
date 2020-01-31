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
    FORGOT_EMAIL_FIELD = (By.CSS_SELECTOR, "input#pseudonym_session_unique_id_forgot.ic-Input.email_address.text")
    RQST_PSWRD_BTN = (By.CSS_SELECTOR, "button.Button.Button--login")
    PSSWRD_CNFRMTN_SNT = (By.XPATH, "//li[@class='ic-flash-success']")


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

    def enter_email_for_restoring(self, text):
        """
        Input email "RestoreAccess@gmail.com" for restoring access
        """
        self.input_text(text, *self.FORGOT_EMAIL_FIELD)

    def click_on_restore_psswrd_btn(self):
        """
        Click on Request Password button
        """
        self.driver.find_elements(*self.RQST_PSWRD_BTN)[-1].click()

    def password_cnfrmtn_snt(self):
        """
        Verify "Password confirmation sent to RestoreAccess@gmail.com.Make sure you check your spam box." sign is here
        """
        assert "Password confirmation sent to RestoreAccess@gmail.com. Make sure you check your spam box." in self.driver.find_element(
            *self.PSSWRD_CNFRMTN_SNT).text
        print('\nSign is here: ', '"', str(self.driver.find_element(*self.PSSWRD_CNFRMTN_SNT).text), '"', '.')
