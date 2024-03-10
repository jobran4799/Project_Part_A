import json

from infra.API_wrapper import APIWrapper

try:
    with open('../Config_Manegre/config.json') as f:
        data = json.load(f)
except FileNotFoundError:
    print("Error: 'config.json' file not found. Make sure the file exists in the correct location.")
    raise  # Raise the error to halt execution if the file is essential for the script to run


class labels:
    def __init__(self, api_ob):
        self.my_api = api_ob


    def get_personal_label(self, id):
        id_to_send = f"/{id}"
        res = self.my_api.api_get_request_by_id(data["url_label_api"], id_to_send)
        return res

    def create_new_personal_label(self, body):
        res = self.my_api.make_post_request(data["url_label_api"], body)
        return res

    def update_a_personal_label(self, id, body):
        id_to_send = f"/{id}"
        res = self.my_api.make_post_request_with_id(data["url_label_api"], id_to_send, body)
        return res

    def delete_label(self, id):
        id_to_send = f"/{id}"
        res = self.my_api.make_delete_request(data["url_label_api"], id_to_send)
        return res




