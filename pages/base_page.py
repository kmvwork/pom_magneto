from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver=None, url=None):
        if driver:
            self.driver = driver
        else:
            self.driver = self.init_driver()
        self.wait = WebDriverWait(self.driver, 10)
        if url:
            self.url = url
            self.open()

    def init_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-gpu")

        chrome_options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
        chrome_options.page_load_strategy = 'eager'

        driver = webdriver.Chrome(options=chrome_options)
        return driver

    def open(self):
        self.driver.get(self.url)
        self.random_delay()

    def find_element(self, *locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.random_delay()
        return element

    def find_elements(self, *locator):
        elements = self.wait.until(EC.presence_of_all_elements_located(locator))
        self.random_delay()
        return elements

    def find_elements_by_xpath(self, xpath):
        elements = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
        self.random_delay()
        return elements

    def random_delay(self):
        import random
        import time
        time.sleep(random.uniform(1, 2))
