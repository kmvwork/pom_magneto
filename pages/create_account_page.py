from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CreateAccountPage(BasePage):
    FIRST_NAME = (By.ID, "firstname")
    LAST_NAME = (By.ID, "lastname")
    EMAIL = (By.ID, "email_address")
    PASSWORD = (By.ID, "password")
    CONFIRM_PASSWORD = (By.ID, "password-confirmation")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[title='Create an Account']")

    def enter_first_name(self, first_name):
        self.find_element(*self.FIRST_NAME).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.find_element(*self.LAST_NAME).send_keys(last_name)

    def enter_email(self, email):
        self.find_element(*self.EMAIL).send_keys(email)

    def enter_password(self, password):
        self.find_element(*self.PASSWORD).send_keys(password)

    def enter_confirm_password(self, confirm_password):
        self.find_element(*self.CONFIRM_PASSWORD).send_keys(confirm_password)

    def click_submit(self):
        self.find_element(*self.SUBMIT_BUTTON).click()
