from selenium.webdriver.common.by import By


class SaleLocators:
    BANNER = (By.CSS_SELECTOR, ".block-promo")
    TITLE = (By.CSS_SELECTOR, "h1.page-title span")
    WOMAN_SALES_BUTTON = (By.XPATH, "//span[text()='Shop Women’s Deals']")
