import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from infra.UI.Base_Page import BasePage


class ProjectListPage(BasePage):
    FIND_TASK_TO_DELETE =(By.XPATH,"//div[@class='fb8d74bb _14423c92 _5f8879d9 _202b0c8c b76144ce a65d9c55 _2580a74b']/div[@id='2329550905-label' and text()='test add Project task']")
                          # "// div[ @ id = '2329467957-label' and text() = 'test add Project task']")
    FIND_MORE_ACTIONS_BUTTON = (By.XPATH, "//button[@aria-label='More project actions']")
    FIND_DELETE_REQUSET = (By.XPATH, "//div[contains(@class, 'a83bd4e0') and contains(@class, 'a8d37c6e') and contains(@class, '_2f303ac3') and contains(@class, 'fb8d74bb') and contains(@class, '_211eebc7') and text()='Delete']")
    FIND_DELETE_CONFRMATION = (By.XPATH,"//button[@class='_8313bd46 _7a4dbd5f _5e45d59f fb8d74bb _56a651f6']")


    def clicker_button(self, click):
        click.click()

    def find_project_to_delete(self):
        self.project_to_delete = self._driver.find_element(*self.FIND_TASK_TO_DELETE)

    def find_more_action_clicker(self, task):
        self.more_action_clicker = task.find_element(*self.FIND_MORE_ACTIONS_BUTTON)

    def find_delete_requste(self,task):
        self.delete_requeste = task.find_element(*self.FIND_DELETE_REQUSET)

    def find_confrmation_delete_requste(self,task):
        self.confirm_delete_requeste = task.find_element(*self.FIND_DELETE_CONFRMATION)

    def actions_perform(self,task_input):
        actions = ActionChains(self._driver)
        actions.move_to_element(task_input).perform()

    def delete_task(self):
        self.find_project_to_delete()
        self.actions_perform(self.project_to_delete)
        time.sleep(2)
        self.find_more_action_clicker(self.project_to_delete)
        time.sleep(2)
        self.clicker_button(self.more_action_clicker)
        time.sleep(2)
        self.find_delete_requste(self.project_to_delete)
        time.sleep(2)
        self.clicker_button(self.delete_requeste)
        time.sleep(2)
        self.find_confrmation_delete_requste(self.project_to_delete)
        time.sleep(5)
        self.clicker_button(self.confirm_delete_requeste)










