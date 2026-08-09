import requests
import json


class GetRequester:

    def __init__(self, url):
        self.url = url

    # Send a GET request and return the raw response body.
    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    # Convert the JSON response into Python data structures.
    def load_json(self):
        return json.loads(self.get_response_body())