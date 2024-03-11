from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class BasePage():
    def __init__(self, driver):
        self._driver = driver

    def get_url(self):
        return self._driver.current_url