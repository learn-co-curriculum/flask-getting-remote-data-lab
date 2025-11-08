import requests
import json

class GetRequester:
    def __init__(self, url):
        # Store the endpoint URL for later use
        self.url = url

    def get_response_body(self):
        # Perform the GET request
        response = requests.get(self.url, timeout=10)
        # Raise an HTTPError for bad responses (4xx/5xx)
        response.raise_for_status()
        # Return raw bytes 
        return response.content

    def load_json(self):
        """
        Fetch the response and convert it from JSON into native Python data (dict/list).
        Uses json.loads on the raw bytes returned by get_response_body().
        """
        raw_body = self.get_response_body()  # bytes
        # json.loads can accept bytes; alternatively use response.json()
        data = json.loads(raw_body)
        return data