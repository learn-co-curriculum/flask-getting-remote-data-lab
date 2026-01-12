import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url).content
        return response

    def load_json(self):
        converted_data = requests.get(self.url).json()
        return converted_data