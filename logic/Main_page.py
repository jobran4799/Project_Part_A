import time
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from infra.UI.Base_Page import BasePage


class MainPage(BasePage):
    USER_NAME =(By.XPATH, "//span[text() = 'Beyonddev']")

    TASK_INPUT = (By.XPATH, "//div[@class='fb8d74bb _14423c92 _297575f4 c4a9b3ab _5f8879d9']//button [@tabindex='0']")
    ADD_TASK_NAME = (By.XPATH, "//div[@class = 'UjpFDa7 no-focus-marker XOgsZVX']//p[@class='is-empty is-editor-empty']")

    DELETION_INPUT = (By.XPATH,"//div[contains(@class, '_560c1e08')]/div[contains(@class, 'task_content') and text()='test on todoist task']")
    MORE_MENU = (By.XPATH,"//div/div/button[@data-testid='more_menu']")
    DELETE_REQUST = (By.XPATH,"// div[ @class ='a83bd4e0 a8d37c6e _2f303ac3 fb8d74bb _211eebc7' and text()='Delete']")
    CONFIRMATION_DELETE = (By.XPATH, "//form/footer/div/button[./span[contains(text(),'Delete')]]")

    TASK_TO_EDIT = (By.XPATH,"//div[contains(@class, '_560c1e08')]/div[contains(@class, 'task_content') and text()='test task editing']")
    CLIC_ON_EDIT = (By.XPATH,  "//div[@class='YjMLlDP task_list_item__actions task_list_item__actions--active']/button[@aria-label='Edit']")
    ADD_DESCRPTION = (By.XPATH, "//p[@data-placeholder='Description' and contains(@class, 'is-empty') and contains(@class, 'is-editor-empty')]/br[@class='ProseMirror-trailingBreak']")
    CONFIRM_EDIT = (By.XPATH, "//button[@data-testid='task-editor-submit-button']")

    FIND_TASK_NO_PRIORITY = (By.XPATH, "//div[contains(@class, '_560c1e08')]/div[contains(@class, 'task_content') and text()='task to change priority']")
    MENU_FOR_PRIORITY = (By.XPATH, "//div/div/button[@data-testid='more_menu']")
    NUM_PRIORITY = (By.XPATH, "//div[@class='fb8d74bb _14423c92 c7813d79 _6a4f69f7 _5f8879d9 _43e5f8e9']/button[@aria-label='Priority 2']")

    FIND_SET_DUE_DATE = (By.XPATH,"//div[contains(@class, '_560c1e08')]/div[contains(@class, 'task_content') and text()='task set due data']")
    CLICK_ON_DUE_DATE = (By.XPATH, "//div[@class='YjMLlDP task_list_item__actions task_list_item__actions--active']/button[@aria-label='Due date']")
    CHOOSE_DATE = (By.XPATH, "//span[@class='calendar__day__date__number' and text()= 8]")

    FIND_COMPLETE_TASK = (By.XPATH, "//div[contains(@class, '_560c1e08')]/div[contains(@class, 'task_content') and text()='test Completed task']")
    SET_AS_COMPLETE = (By.XPATH,  "//button[@class='task_checkbox qfNv_xy priority_1 VlPtS9Y YGJQoir']")

    FIND_MY_PROJECTS = (By.XPATH,"//button[@aria-label='My projects menu']")
    FIND_CLICKER_TO_ADD_PROJECT = (By.XPATH, "//div[@class='a83bd4e0 e214ff2e fb8d74bb' and text()='Add project']")
    INPUT_TEXT_ADD_PROJECT = (By.XPATH, "//input[@id='edit_project_modal_field_name']")
    ADD_PROJECT_TO_FAVORITE = (By.XPATH, "//div[contains(@class, '_618235b7') and contains(@class, 'fb8d74bb') and contains(@class, '_18f74af9') and contains(@class, '_68aab614')]/input[@name='is_favorite']")

    PROJECT_LIST_BUTTON = (By.XPATH, "//div[contains(@class, 'qMjaCbb') and contains(@class, 'a83bd4e0') and contains(@class, '_7be5c531') and contains(@class, '_6a3e5ade') and contains(@class, '_2f303ac3') and contains(@class, 'fb8d74bb') and contains(@class, '_211eebc7') and text()='My Projects']")

    def __init__(self, driver):
        super().__init__(driver)
        # self.init()

    def init(self):
        self.user_name = self._driver.find_element(*self.USER_NAME)


    def username_is_displayed(self):
        return self.user_name.is_displayed()

    def fill_input(self, task_input, task_TaskName):
        time.sleep(2)
        task_input.send_keys(task_TaskName)
        time.sleep(2)

    def click_enter(self, write_input):
        write_input.send_keys(Keys.ENTER)


    def clicker_button(self, click):
        click.click()



    def find_task_inputs_to_add_task(self):
        self.task_input = self._driver.find_element(*self.TASK_INPUT)

    def find_add_task_name_to_add_task(self):
        self.add_task_name = self._driver.find_element(*self.ADD_TASK_NAME)

    def creat_task(self, text_task_name):
        self.find_task_inputs_to_add_task()
        self.clicker_button(self.task_input)
        time.sleep(2)
        self.find_add_task_name_to_add_task()
        self.fill_input(self.add_task_name, text_task_name)
        time.sleep(2)
        self.click_enter(self.add_task_name)

    def find_task_inputs_to_delete_task(self):
        self.task_delete_input = self._driver.find_element(*self.DELETION_INPUT)

    def find_more_menu_clicker(self):
        self.menu_clicker = self._driver.find_element(*self.MORE_MENU)

    def find_delete_requste(self):
        self.delete_requeste = self._driver.find_element(*self.DELETE_REQUST)

    def find_confrmation_delete_requste(self):
        self.confirm_delete_requeste = self._driver.find_element(*self.CONFIRMATION_DELETE)

    def actions_perform(self, task_input):
        actions = ActionChains(self._driver)
        actions.move_to_element(task_input).perform()

    def delete_task(self):
        self.find_task_inputs_to_delete_task()
        self.actions_perform(self.task_delete_input)
        time.sleep(2)
        self.find_more_menu_clicker()
        time.sleep(2)
        self.clicker_button(self.menu_clicker)
        time.sleep(2)
        self.find_delete_requste()
        time.sleep(2)
        self.clicker_button(self.delete_requeste)
        time.sleep(2)
        self.find_confrmation_delete_requste()
        time.sleep(2)
        self.clicker_button(self.confirm_delete_requeste)

    def find_task_inputs_to_edit_task(self):
        self.inputs_to_edit_task = self._driver.find_element(*self.TASK_TO_EDIT)

    def find_click_on_edit(self):
        self.click_on_edit = self._driver.find_element(*self.CLIC_ON_EDIT)

    def find_add_descrption(self):
        self.add_descrption = self._driver.find_element(*self.ADD_DESCRPTION)

    def find_confirm_edit(self):
        self.confirm_edit = self._driver.find_element(*self.CONFIRM_EDIT)

    def edit_task(self, text_edit):
        self.find_task_inputs_to_edit_task()
        self.actions_perform(self.inputs_to_edit_task)
        time.sleep(2)
        self.find_click_on_edit()
        time.sleep(2)
        self.clicker_button(self.click_on_edit)
        time.sleep(2)
        self.find_add_descrption()
        time.sleep(2)
        self.add_descrption.send_keys(text_edit)
        time.sleep(2)
        self.find_confirm_edit()
        time.sleep(2)
        self.actions_perform(self.confirm_edit)
        self.clicker_button(self.confirm_edit)


    def find_task_for_priority(self):
        self.task_for_priority = self._driver.find_element(*self.FIND_TASK_NO_PRIORITY)

    def find_menu_priority(self):
        self.menu_priority = self._driver.find_element(*self.MENU_FOR_PRIORITY)

    def find_choose_num_of_priority(self):
        self.confirm_edit_priority = self._driver.find_element(*self.NUM_PRIORITY)

    def priority_task(self):
        self.find_task_for_priority()
        self.actions_perform(self.task_for_priority)
        time.sleep(2)
        self.find_menu_priority()
        time.sleep(2)
        self.clicker_button(self.menu_priority)
        time.sleep(2)
        self.find_choose_num_of_priority()
        time.sleep(2)
        self.clicker_button(self.confirm_edit_priority)

    def find_task_set_due_date(self):
        self.task_set_due_date = self._driver.find_element(*self.FIND_SET_DUE_DATE)

    def find_click_on_due_date(self):
        self.click_on_due_date = self._driver.find_element(*self.CLICK_ON_DUE_DATE)

    def find_choose_date(self):
        self.choose_date = self._driver.find_element(*self.CHOOSE_DATE)

    def set_due_date_task(self):
        self.find_task_set_due_date()
        self.actions_perform(self.task_set_due_date)
        time.sleep(2)
        self.find_click_on_due_date()
        time.sleep(2)
        self.clicker_button(self.click_on_due_date)
        time.sleep(2)
        self.find_choose_date()
        time.sleep(2)
        self.clicker_button(self.choose_date)

    def find_task_complition(self):
        self.find_completed_task = self._driver.find_element(*self.FIND_COMPLETE_TASK)

    def find_click_completed(self):
        self.completed_task = self._driver.find_element(*self.SET_AS_COMPLETE)

    def set_complation_task(self):
        self.find_task_complition()
        self.actions_perform(self.find_completed_task)
        time.sleep(2)
        self.find_click_completed()
        time.sleep(2)
        self.clicker_button(self.completed_task)

    def find_projects_list(self):
        self.project_list = self._driver.find_element(*self.FIND_MY_PROJECTS)

    def find_add_project_clicker(self):
        self.clicker_add_project = self._driver.find_element(*self.FIND_CLICKER_TO_ADD_PROJECT)

    def find_input_project_name(self):
        self.input_project_name = self._driver.find_element(*self.INPUT_TEXT_ADD_PROJECT)

    def find_clicker_to_favorite(self):
        self.add_project_to_favorite = self._driver.find_element(*self.ADD_PROJECT_TO_FAVORITE)

    def action_prform_clicker(self, add_to_favorite):
        actions = ActionChains(self._driver)
        actions.move_to_element(add_to_favorite).click().perform()

    def create_project(self, text_task_name, add_to_favorite):
        self.find_projects_list()
        self.clicker_button(self.project_list)
        time.sleep(2)
        self.find_add_project_clicker()
        self.clicker_button(self.clicker_add_project)
        time.sleep(2)
        self.find_input_project_name()
        self.fill_input(self.input_project_name, text_task_name)
        time.sleep(2)
        if add_to_favorite:
            self.find_clicker_to_favorite()
            self.action_prform_clicker(self.add_project_to_favorite)
        time.sleep(2)
        self.click_enter(self.input_project_name)

    def find_clicker_to_project_list(self):
        self.clicker_to_project_list = self._driver.find_element(*self.PROJECT_LIST_BUTTON)

    def delete_project(self):
        self.find_clicker_to_project_list()
        time.sleep(2)
        self.clicker_button(self.clicker_to_project_list)















