import json

try:
    with open('../../Config_Manegre/config.json') as f:
        data = json.load(f)
except FileNotFoundError:
    print("Error: 'config.json' file not found. Make sure the file exists in the correct location.")
    raise  # Raise the error to halt execution if the file is essential for the script to run


class Section:
    def __init__(self, api_ob):
        self.my_api = api_ob


    def add_section_to_project_by_id(self, id, section_name_body):
        id_to_send = f"?id={id}"
        res = self.my_api.make_post_request_with_id(data["url_sections_api"], id_to_send, data=section_name_body)
        return res

    def get_all_sections(self, id):
        id_to_send = f"?project_id={id}"
        res = self.my_api.api_get_request_by_id(data["url_sections_api"], id_to_send)
        return res

    def get_single_section(self, id):
        id_to_send = f"/{id}"
        res = self.my_api.api_get_request_by_id(data["url_sections_api"], id_to_send)
        return res

    def update_name_section(self, id, body):
        id_to_send = f"/{id}"
        res = self.my_api.make_post_request_with_id(data["url_sections_api"], id_to_send, body)
        return res

    def delete_section(self, id):
        id_to_send = f"/{id}"
        res = self.my_api.make_delete_request(data["url_sections_api"], id_to_send)
        return res



