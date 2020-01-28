from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import Page

class MainPage(Page):
    LOGIN_STRING = (By.ID, "pseudonym_session_unique_id")
    PASSWORD_STRING = (By.ID, "pseudonym_session_password")
    LOGIN_BTN = (By.CSS_SELECTOR, "button.Button.Button--login")
    LOGIN_REJECTED = (By.CSS_SELECTOR, "li.ic-flash-error")



