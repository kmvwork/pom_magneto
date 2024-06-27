import pytest
from pages.sale_page import SalePage


class TestSale:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.page = SalePage()

    def test_banner_present(self):
        banners = self.page.get_banner_elements()
        assert len(banners) > 0, "No banners found on the sale page"

    def test_title_present(self):
        title = self.page.get_title()
        assert title, "Title should not be empty"
        assert "Sale" in title, "Title does not contain 'Sale'"

    def test_filters_present(self):
        button = self.page.get_woman_sales_button()
        assert button.text == 'Shop Women’s Deals', "No woman sales button"
