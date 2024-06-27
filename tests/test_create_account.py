import pytest
from pages.create_account_page import CreateAccountPage
from locators.create_account_locators import CreateAccountLocators
import random


class TestCreateAccount:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.page = CreateAccountPage()

    def test_first_name_field_present(self):
        assert self.page.find_element(*CreateAccountLocators.FIRST_NAME), "First Name field is not present"

    def test_create_account_with_valid_data(self):
        self.page.enter_first_name("John")
        self.page.enter_last_name("Doe")
        self.page.enter_email(f"john.doe@example{random.randint(1, 20)}.com")
        self.page.enter_password("Password123")
        self.page.enter_confirm_password("Password123")
        self.page.click_submit()

        expected_url = "https://magento.softwaretestingboard.com/customer/account/"
        current_url = self.page.driver.current_url
        assert current_url == expected_url, f"Expected URL {expected_url}, but got {current_url}"

    def test_create_account_with_missing_fields(self):
        self.page.enter_first_name("John")
        self.page.enter_email("john.doe@example.com")
        self.page.enter_password("password123")
        self.page.click_submit()

        error_message = "This is a required field."
        error_elements = self.page.find_elements_by_xpath(f"//*[contains(text(), '{error_message}')]")
        assert len(error_elements) > 0, "Validation error messages are not present for missing fields"
