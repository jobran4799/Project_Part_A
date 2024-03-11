# This is a sample Python script.
import unittest

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from infra.API_wrapper import APIWrapper
from logic.API_labels import labels
from logic.API_projects import Project
from logic.API_sections import Section
from logic.API_tasks import Tasks


class api_parallel_tests(unittest.TestCase):
    def setUp(self):
        self.my_api = APIWrapper()

    def test_get_all_collaborators(self):
        test_p = Project(self.my_api)
        my_c_api = test_p.Get_project_all_collaborators("2329611387")
        json_response = my_c_api.json()
        self.assertTrue(my_c_api.ok, "not ok")
        self.assertEqual(json_response[0]["name"], "Beyonddev", "not equals")
        self.assertEqual(json_response[0]["email"], "beyonddevtestproject@gmail.com", "not equals")

    def test_add_section_to_project(self):
        test_p = Section(self.my_api)
        body = {"project_id": "2329678566",
                "name": "section to delete"}
        my_c_api = test_p.add_section_to_project_by_id("2329678566", body)
        json_response = my_c_api.json()
        self.assertTrue(my_c_api.ok, "not ok")
        self.assertEqual(json_response["project_id"], "2329678566", "not equals")
        self.assertEqual(json_response["name"], "section to delete", "not equals")

    def test_get_data_section_list(self):
        test_p = Section(self.my_api)
        my_c_api = test_p.get_all_sections("2329678566")
        json_response = my_c_api.json()
        self.assertTrue(my_c_api.ok, "not ok")
        self.assertEqual(json_response[0]["order"], 1, "not equals")
        self.assertEqual(json_response[0]["name"], "check section", "not equals")
        self.assertEqual(json_response[1]["id"], "149886499", "not equals")
        self.assertEqual(json_response[1]["name"], "postman", "not equals")



    def test_name_section_update(self):
        test_p = Section(self.my_api)
        body = {"name": "Supermarket"}
        my_c_api = test_p.update_name_section("149961566", body)
        json_response = my_c_api.json()
        self.assertTrue(my_c_api.ok, "not ok")
        self.assertEqual(json_response["name"], "Supermarket", "not equals")


    def test_get_active_tasks(self):
        test_p = Tasks(self.my_api)
        my_c_api = test_p.get_active_tasks()
        json_response = my_c_api.json()
        due_date = json_response[9]["due"]
        date = due_date["date"]
        self.assertTrue(my_c_api.ok, "not deleted")
        self.assertEqual(json_response[9]["content"], "task set due data", "not equals")
        self.assertEqual(date, "2024-03-08", "not equals")


    def test_update_tasks(self):
        test_p = Tasks(self.my_api)
        body = {"content": "Buy Coffee"}
        my_c_api = test_p.update_tasks("7775320373", body)
        json_response = my_c_api.json()
        self.assertTrue(my_c_api.ok, "not deleted")
        self.assertEqual(json_response["content"], "Buy Coffee", "not equals")

    # def test_create_new_personal_label(self):
    #     test_p = labels(self.my_api)
    #     body = {"name": "buffel"}
    #     my_c_api = test_p.create_new_personal_label(body)
    #     json_response = my_c_api.json()
    #     self.assertTrue(my_c_api.ok, "not deleted")
    #     self.assertEqual(json_response["name"], "buffel", "not equals")

    def test_update_a_personal_label(self):
        test_p = labels(self.my_api)
        body = {"name": "milk"}
        my_c_api = test_p.update_a_personal_label("2171988630", body)
        json_response = my_c_api.json()
        self.assertTrue(my_c_api.ok, "not deleted")
        self.assertEqual(json_response["name"], "milk", "not equals")



