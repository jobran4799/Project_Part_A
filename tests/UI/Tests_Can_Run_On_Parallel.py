import unittest

from infra.UI.Brawser_Wrapper import BrowserWrapper
from logic.UI.Log_in_page import LoginPage
from logic.UI.Main_page import MainPage


class test_run_on_parallel(unittest.TestCase):
    def setUp(self):
        self.browser_wrapper = BrowserWrapper()
        self.driver = self.browser_wrapper.get_driver(self.browser)

    def test_invalid_password_login(self):
        test_invalid_login = LoginPage(self.driver)
        test_invalid_login.fllow_log_in_test("beyonddevtestproject@gmail.com", "Zxcvbnm678")
        test_invalid_login.wrong_massage()
        self.assertTrue(test_invalid_login.wrong_massage.text.strip() == "Wrong email or password.",
                        "Message does not match")



    def test_Task_priority(self):
        login = LoginPage(self.driver)
        login.fllow_log_in_test("beyonddevtestproject@gmail.com", "Zxcvbnm123")
        main_page = MainPage(self.driver)
        main_page.priority_task()
        self.assertTrue(main_page, "priority does not modified")

    def test_Project_creation(self):
        login = LoginPage(self.driver)
        login.fllow_log_in_test("beyonddevtestproject@gmail.com", "Zxcvbnm123")
        main_page = MainPage(self.driver)
        main_page.create_project("test add Project", True)
        self.assertTrue(main_page, "No match between the tasks name")

    def tearDown(self):
        self.driver.quit()