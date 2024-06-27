# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import random
# import time
#
#
# @pytest.fixture(scope="class")
# def setup(request):
#     chrome_options = Options()
#     chrome_options.add_argument("--start-maximized")
#     chrome_options.add_argument(
#         "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
#     chrome_options.add_argument("--disable-blink-features=AutomationControlled")
#     # chrome_options.add_argument("--headless")  # Отключите режим без головы, если включен
#
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.maximize_window()
#
#     # Отключение автоматического управления
#     driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
#
#     request.cls.driver = driver
#     yield driver
#     driver.quit()
#
#
# # Функция для случайных задержек
# def random_delay():
#     time.sleep(random.uniform(2, 5))
