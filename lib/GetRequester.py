import requests
import json

class GetRequester:
    url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"

    def __init__(self, url=None):
        self.url = url or self.url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        return json.loads(self.get_response_body())