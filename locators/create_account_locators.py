from selenium.webdriver.common.by import By


class CreateAccountLocators:
    FIRST_NAME = (By.ID, "firstname")
    LAST_NAME = (By.ID, "lastname")
    EMAIL = (By.ID, "email_address")
    PASSWORD = (By.ID, "password")
    CONFIRM_PASSWORD = (By.ID, "password-confirmation")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[title='Create an Account']")