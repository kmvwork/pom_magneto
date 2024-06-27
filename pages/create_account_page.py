from pages.base_page import BasePage
from locators.create_account_locators import CreateAccountLocators


class CreateAccountPage(BasePage):
    def __init__(self, driver=None):
        super().__init__(driver, "https://magento.softwaretestingboard.com/customer/account/create/")

    def enter_first_name(self, first_name):
        self.find_element(*CreateAccountLocators.FIRST_NAME).send_keys(first_name)
        assert self.find_element(*CreateAccountLocators.FIRST_NAME), "First Name field is not present"

    def enter_last_name(self, last_name):
        self.find_element(*CreateAccountLocators.LAST_NAME).send_keys(last_name)

    def enter_email(self, email):
        self.find_element(*CreateAccountLocators.EMAIL).send_keys(email)

    def enter_password(self, password):
        self.find_element(*CreateAccountLocators.PASSWORD).send_keys(password)

    def enter_confirm_password(self, confirm_password):
        self.find_element(*CreateAccountLocators.CONFIRM_PASSWORD).send_keys(confirm_password)

    def click_submit(self):
        self.find_element(*CreateAccountLocators.SUBMIT_BUTTON).click()
