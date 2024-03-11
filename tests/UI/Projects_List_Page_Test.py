import unittest
from infra.UI.Brawser_Wrapper import BrowserWrapper
from logic.UI.Log_in_page import LoginPage
from logic.UI.Main_page import MainPage
from logic.UI.Project_List_Page import ProjectListPage


class Project_List_Page_Test(unittest.TestCase):
    def setUp(self):
        self.browser_wrapper = BrowserWrapper()
        self.driver = self.browser_wrapper.get_driver(self.browser)

    def test_Project_deletion(self):
        login = LoginPage(self.driver)
        login.fllow_log_in_test("beyonddevtestproject@gmail.com", "Zxcvbnm123")
        main_page = MainPage(self.driver)
        main_page.delete_project()
        list_project = ProjectListPage(self.driver)
        list_project.delete_task()
        self.assertTrue(main_page, "No match between the tasks name")

    def tearDown(self):
        self.driver.quit()
