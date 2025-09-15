import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        """
        Sends a GET request to self.url and returns the raw response body as bytes.
        """
        response = requests.get(self.url)
        if not response.ok:
            raise Exception(f"Request failed: {response.status_code}")
        else:
            return response.content


    def load_json(self):
        """
        Uses get_response_body() to fetch the content, then parses
        and returns the corresponding data structure.
        """
        data = self.get_response_body()
        return json.loads(data)
        
