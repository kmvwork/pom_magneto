from selenium.webdriver.common.by import By


class EcoFriendlyLocators:
    CATEGORY_TITLE = (By.CSS_SELECTOR, "h1.page-title")
    PRODUCT_LIST = (By.CSS_SELECTOR, "ol.products li.product-item")
    PRODUCT_NAME = (By.CSS_SELECTOR, "a.product-item-link")
