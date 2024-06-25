import pytest
from pages.sale_page import SalePage


@pytest.mark.usefixtures("setup")
class TestSale:

    @pytest.fixture(autouse=True)
    def setup_page(self):
        self.page = SalePage(self.driver)
        self.page.open("https://magento.softwaretestingboard.com/sale.html")

    def test_banner_present(self):
        banners = self.page.get_banner_elements()
        assert len(banners) > 0, "No banners found on the sale page"

    def test_title_present(self):
        title = self.page.get_title()
        assert title, "Title should not be empty"
        assert "Sale" in title, "Title does not contain 'Sale'"

    def test_woman_sales_button(self):
        button = self.page.get_woman_sales_button()
        assert button.text == 'Shop Women’s Deals', "No woman sales button"
