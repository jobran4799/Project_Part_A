import unittest
import time
from infra.UI.Brawser_Wrapper import BrowserWrapper
from logic.UI.Log_in_page import LoginPage
from logic.UI.Main_page import MainPage


class Main_page_test(unittest.TestCase):
    def setUp(self):
        self.browser_wrapper = BrowserWrapper()
        self.driver = self.browser_wrapper.get_driver(self.browser)

    def test_Task_creation(self):
        login = LoginPage(self.driver)
        login.fllow_log_in_test("beyonddevtestproject@gmail.com", "Zxcvbnm123")
        main_page = MainPage(self.driver)
        main_page.creat_task("add test on todoist task")
        time.sleep(2)

        self.assertTrue(main_page, "No match between the tasks name")

    def test_Task_deletion(self):
        login = LoginPage(self.driver)
        login.fllow_log_in_test("beyonddevtestproject@gmail.com", "Zxcvbnm123")
        main_page = MainPage(self.driver)
        main_page.delete_task()
        time.sleep(2)
        self.assertTrue(main_page, "task is still exist")

    def test_Task_compilation(self):
        login = LoginPage(self.driver)
        login.fllow_log_in_test("beyonddevtestproject@gmail.com", "Zxcvbnm123")
        main_page = MainPage(self.driver)
        main_page.set_complation_task()
        time.sleep(2)
        self.assertTrue(main_page, "task is not completed")
        # Wait for the task to be added

    def test_Task_editing(self):
        login = LoginPage(self.driver)
        login.fllow_log_in_test("beyonddevtestproject@gmail.com", "Zxcvbnm123")
        main_page = MainPage(self.driver)
        main_page.edit_task("test edit is working")
        time.sleep(2)
        self.assertTrue(main_page, "task is not add descrption")

    def test_Task_priority(self):
        login = LoginPage(self.driver)
        login.fllow_log_in_test("beyonddevtestproject@gmail.com", "Zxcvbnm123")
        main_page = MainPage(self.driver)
        main_page.priority_task()
        self.assertTrue(main_page, "priority does not modified")

    def test_Task_set_due_data(self):
        login = LoginPage(self.driver)
        login.fllow_log_in_test("beyonddevtestproject@gmail.com", "Zxcvbnm123")
        main_page = MainPage(self.driver)
        main_page.set_due_date_task()
        self.assertTrue(main_page, "data did not be modified")

    def test_Project_creation(self):
        login = LoginPage(self.driver)
        login.fllow_log_in_test("beyonddevtestproject@gmail.com", "Zxcvbnm123")
        main_page = MainPage(self.driver)
        main_page.create_project("test add Project", True)
        self.assertTrue(main_page, "No match between the tasks name")

    def tearDown(self):
        self.driver.quit()
