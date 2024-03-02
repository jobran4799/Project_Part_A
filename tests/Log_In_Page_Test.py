import unittest
from infra.Brawser_Wrapper import BrowserWrapper
from logic.Log_in_page import LoginPage
from logic.Main_page import MainPage


class Login_page_test(unittest.TestCase):
    def setUp(self):
        self.browser_wrapper = BrowserWrapper()
        self.driver = self.browser_wrapper.get_driver(self.browser)

    def test_navigate_to_todoist_web(self):
        test_navigate = LoginPage(self.driver)
        self.assertEqual(test_navigate.get_url(), "https://app.todoist.com/auth/login", "url does no match")

    def test_valid_login(self):
        login = LoginPage(self.driver)
        login.fllow_log_in_test("beyonddevtestproject@gmail.com", "Zxcvbnm123")
        self.main_page = MainPage(self.driver)
        self.main_page.init()
        self.assertTrue(self.main_page.username_is_displayed(), "write somthing")

    def test_invalid_password_login(self):
        test_invalid_login = LoginPage(self.driver)
        test_invalid_login.fllow_log_in_test("beyonddevtestproject@gmail.com", "Zxcvbnm678")
        test_invalid_login.wrong_massage()
        self.assertTrue(test_invalid_login.wrong_massage.text.strip() == "Wrong email or password.",
                        "Message does not match")

    def test_invalid_username_login(self):
        test_invalid_login = LoginPage(self.driver)
        test_invalid_login.fllow_log_in_test("beyonddevproject@gmail.com", "Zxcvbnm123")
        test_invalid_login.wrong_massage()
        self.assertTrue(test_invalid_login.wrong_massage.text.strip() == "Wrong email or password.",
                        "Message does not match")

    def tearDown(self):
        self.driver.quit()
