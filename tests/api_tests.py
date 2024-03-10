# This is a sample Python script.
import unittest

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from infra.API_wrapper import APIWrapper
from logic.API_labels import labels
from logic.API_projects import Project
from logic.API_sections import Section
from logic.API_tasks import Tasks


class MainTester(unittest.TestCase):
    def setUp(self):
        self.my_api = APIWrapper()


    def test_creat_project(self):
        test_p = Project(self.my_api)
        body ={"name": "Shopping List"}
        my_c_api = test_p.Create_a_new_project(body)
        json_response = my_c_api.json()
        self.assertTrue(my_c_api.ok, "not ok")
        self.assertEqual(json_response["name"], "Shopping List", "not equals")

    def test_update_project(self):
        test_p = Project(self.my_api)
        body = {"name": "Things To Buy"}
        my_c_api = test_p.update_project_by_id("2329913117", body)
        json_response = my_c_api.json()
        self.assertTrue(my_c_api.ok, "not ok")
        self.assertEqual(json_response[1]["name"], "Things To Buy", "not equals")

    def test_delete_project(self):
        test_p = Project(self.my_api)
        my_c_api = test_p.delete_project_by_id("2329913117")
        self.assertTrue(my_c_api.ok, "not ok")

    def test_get_project_list(self):
        test_p = Project(self.my_api)
        my_c_api = test_p.get_project_by_id("2329611387")
        json_response = my_c_api.json()
        self.assertTrue(my_c_api.ok, "not ok")
        self.assertEqual(json_response[0]["color"], "charcoal", "not equals")
        self.assertEqual(json_response[1]["order"], 1, "not equals")
        self.assertEqual(json_response[1]["name"], "test add Project task", "not equals")

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

    def test_get_data_section(self):
        test_p = Section(self.my_api)
        my_c_api = test_p.get_single_section("149886499")
        json_response = my_c_api.json()
        self.assertTrue(my_c_api.ok, "not ok")
        self.assertEqual(json_response["project_id"], "2329678566", "not equals")
        self.assertEqual(json_response["name"], "postman", "not equals")

    def test_name_section_update(self):
        test_p = Section(self.my_api)
        body = {"name": "Supermarket"}
        my_c_api = test_p.update_name_section("149961566", body)
        json_response = my_c_api.json()
        self.assertTrue(my_c_api.ok, "not ok")
        self.assertEqual(json_response["name"], "Supermarket", "not equals")

    def test_delete_section(self):
        test_p = Section(self.my_api)
        my_c_api = test_p.delete_section("149962796")
        self.assertTrue(my_c_api.ok, "not deleted")

    def test_get_active_tasks(self):
        test_p = Tasks(self.my_api)
        my_c_api = test_p.get_active_tasks()
        json_response = my_c_api.json()
        due_date = json_response[9]["due"]
        date = due_date["date"]
        self.assertTrue(my_c_api.ok, "not deleted")
        self.assertEqual(json_response[9]["content"], "task set due data", "not equals")
        self.assertEqual(date, "2024-03-08", "not equals")

    def test_create_new_tasks(self):
        test_p = Tasks(self.my_api)
        body = {"content": "Buy Milk", "due_string": "tomorrow at 12:00", "due_lang": "en", "priority": 4}
        my_c_api = test_p.create_tasks(body)
        json_response = my_c_api.json()
        self.assertTrue(my_c_api.ok, "not deleted")
        self.assertEqual(json_response["content"], "Buy Milk", "not equals")
        self.assertEqual(json_response["priority"], 4, "not equals")

    def test_update_tasks(self):
        test_p = Tasks(self.my_api)
        body = {"content": "Buy Coffee"}
        my_c_api = test_p.update_tasks("7775320373", body)
        json_response = my_c_api.json()
        self.assertTrue(my_c_api.ok, "not deleted")
        self.assertEqual(json_response["content"], "Buy Coffee", "not equals")

    def test_delete_tasks(self):
        test_p = Tasks(self.my_api)
        my_c_api = test_p.delete_tasks("7775337313")
        self.assertTrue(my_c_api.ok, "not deleted")


    def test_get_personal_label(self):
        test_p = labels(self.my_api)
        my_c_api = test_p.get_personal_label("2171988630")
        json_response = my_c_api.json()
        self.assertTrue(my_c_api.ok, "not deleted")
        self.assertEqual(json_response["name"], "Food", "not equals")
        self.assertEqual(json_response["is_favorite"], False, "not equals")

    def test_create_new_personal_label(self):
        test_p = labels(self.my_api)
        body = {"name": "buffel"}
        my_c_api = test_p.create_new_personal_label(body)
        json_response = my_c_api.json()
        self.assertTrue(my_c_api.ok, "not deleted")
        self.assertEqual(json_response["name"], "buffel", "not equals")

    def test_update_a_personal_label(self):
        test_p = labels(self.my_api)
        body = {"name": "milk"}
        my_c_api = test_p.update_a_personal_label("2171988630", body)
        json_response = my_c_api.json()
        self.assertTrue(my_c_api.ok, "not deleted")
        self.assertEqual(json_response["name"], "milk", "not equals")

    def test_delete_label(self):
        test_p = labels(self.my_api)
        my_c_api = test_p.delete_label("2171988718")
        self.assertTrue(my_c_api.ok, "not deleted")


