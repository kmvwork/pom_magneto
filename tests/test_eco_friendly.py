import pytest
from pages.eco_friendly_page import EcoFriendlyPage


@pytest.mark.usefixtures("setup")
class TestEcoFriendly:

    @pytest.fixture(autouse=True)
    def setup_page(self):
        self.page = EcoFriendlyPage(self.driver)
        self.page.open("https://magento.softwaretestingboard.com/collections/eco-friendly.html")

    def test_product_list_present(self):
        assert self.page.find_elements(*EcoFriendlyPage.PRODUCT_LIST)

    def test_product_names(self):
        product_names = self.page.get_product_names()
        assert len(product_names) > 0

    def test_first_product_name(self):
        product_names = self.page.get_product_names()
        assert "Ana Running Short" in product_names[0]  # Replace with actual expected product name
