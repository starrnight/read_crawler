"""
页面抓取器
"""
from django.conf import settings
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class Crawler:
    """
    抓取器
    """

    @classmethod
    def chrome_driver(cls):
        """
        google chrome驱动
        """
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        service = Service(executable_path=settings.DRIVER_PATH)
        return webdriver.Chrome(chrome_options=chrome_options,
                                service=service)


class Biquge:
    """

    """

    def biquge(self):
        """
        开始抓取
        """
        driver = Crawler.chrome_driver()
        driver.get('https://www.baidu.com')
        driver.implicitly_wait(10)

        search_box = driver.find_element(By.ID, "kw")
        search_button = driver.find_element(By.ID, "su")

        search_box.send_keys("Selenium")
        search_button.click()

        driver.quit()
