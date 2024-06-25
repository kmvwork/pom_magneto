import pytest
from pages.create_account_page import CreateAccountPage


@pytest.mark.usefixtures("setup")
class TestCreateAccount:

    @pytest.fixture(autouse=True)
    def setup_page(self):
        self.page = CreateAccountPage(self.driver)
        self.page.open("https://magento.softwaretestingboard.com/customer/account/create/")

    def test_first_name_field_present(self):
        assert self.page.find_element(*CreateAccountPage.FIRST_NAME)

    def test_create_account_with_valid_data(self):
        self.page.enter_first_name("John")
        self.page.enter_last_name("Doe")
        self.page.enter_email("john.doe@example.com")
        self.page.enter_password("password123")
        self.page.enter_confirm_password("password123")
        self.page.click_submit()
        # Add assert to verify successful account creation

    def test_create_account_with_missing_fields(self):
        self.page.enter_first_name("John")
        self.page.enter_email("john.doe@example.com")
        self.page.enter_password("password123")
        self.page.click_submit()
        # Add assert to verify validation error
