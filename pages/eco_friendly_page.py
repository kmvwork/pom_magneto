from .base_page import BasePage
from locators.eco_friendly_locators import EcoFriendlyLocators


class EcoFriendlyPage(BasePage):
    def __init__(self, driver=None):
        super().__init__(driver, "https://magento.softwaretestingboard.com/collections/eco-friendly.html")

    def get_category_title(self):
        return self.find_element(*EcoFriendlyLocators.CATEGORY_TITLE).text

    def get_product_elements(self):
        return self.find_elements(*EcoFriendlyLocators.PRODUCT_LIST)

    def get_product_names(self):
        products = self.get_product_elements()
        return [product.find_element(*EcoFriendlyLocators.PRODUCT_NAME).text for product in products]
