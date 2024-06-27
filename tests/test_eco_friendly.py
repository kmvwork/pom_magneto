import pytest
from pages.eco_friendly_page import EcoFriendlyPage


class TestEcoFriendly:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.page = EcoFriendlyPage()

    def test_category_title_present(self):
        title = self.page.get_category_title()
        assert title, "Category title should not be empty"
        assert "Eco Friendly" in title, "Category title does not contain 'Eco Friendly'"

    def test_product_list_present(self):
        products = self.page.get_product_elements()
        assert len(products) > 0, "No products found in eco-friendly category"

    def test_product_names(self):
        product_names = self.page.get_product_names()
        assert len(product_names) > 0, "No product names found in eco-friendly category"
        for name in product_names:
            assert name, "Product name should not be empty"
