from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class EcoFriendlyPage(BasePage):
    PRODUCT_LIST = (By.CSS_SELECTOR, "ol.products li.product-item")
    PRODUCT_NAME = (By.CSS_SELECTOR, "a.product-item-link")

    def get_product_names(self):
        products = self.find_elements(*self.PRODUCT_LIST)
        return [product.find_element(*self.PRODUCT_NAME).text for product in products]
