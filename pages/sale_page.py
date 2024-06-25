from selenium.webdriver.common.by import By
from .base_page import BasePage


class SalePage(BasePage):
    BANNER = (By.CSS_SELECTOR, ".block-promo")
    TITLE = (By.CSS_SELECTOR, "h1.page-title span")
    WOMAN_SALES_BUTTON = (By.XPATH, "//span[text()='Shop Women’s Deals']")

    def get_banner_elements(self):
        return self.find_elements(*self.BANNER)

    def get_title(self):
        return self.find_element(*self.TITLE).text

    def get_woman_sales_button(self):
        return self.find_element(*self.WOMAN_SALES_BUTTON)
