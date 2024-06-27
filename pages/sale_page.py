from pages.base_page import BasePage
from locators.sale_locators import SaleLocators


class SalePage(BasePage):
    def __init__(self, driver=None):
        super().__init__(driver, "https://magento.softwaretestingboard.com/sale.html")

    def get_banner_elements(self):
        return self.find_elements(*SaleLocators.BANNER)

    def get_title(self):
        return self.find_element(*SaleLocators.TITLE).text

    def get_woman_sales_button(self):
        return self.find_element(*SaleLocators.WOMAN_SALES_BUTTON)
