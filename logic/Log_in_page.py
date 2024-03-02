import time
from selenium.webdriver.common.by import By
from infra.Base_Page import BasePage


class LoginPage(BasePage):
    EMAIL_FIELD = (By.XPATH, "//input[@id='element-0']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='element-3']")
    LOGIN_BUTTON = (By.XPATH, "//button[./span[contains(text(),'Log in')]]")

    def __init__(self, driver):
        super().__init__(driver)
        self.initPage()

    def initPage(self):
        self._driver.implicitly_wait(2)  # Waits up to 2 seconds
        self.email_field = self._driver.find_element(*self.EMAIL_FIELD)
        self.password_field = self._driver.find_element(*self.PASSWORD_FIELD)
        self.login_button = self._driver.find_element(*self.LOGIN_BUTTON)

    def fill_input(self, userinput):
        self.email_field.send_keys(userinput)

    def fill_password(self, userpassord):
        self.password_field.send_keys(userpassord)

    def wrong_massage(self):
        self.wrong_massage = self._driver.find_element(By.CLASS_NAME, "a83bd4e0")
        self._driver.implicitly_wait(2)

    def login_click(self):
        self.login_button.click()
        time.sleep(5)

    def fllow_log_in_test(self, userinput, userpassord):
        self.fill_input(userinput)
        self.fill_password(userpassord)
        self.login_click()
