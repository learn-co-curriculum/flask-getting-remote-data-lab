
import requests
import json


class GetRequester:
    """Fetch remote data and parse JSON responses."""

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # Return the raw response body as bytes.
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        # Parse the response body into Python data.
        response_body = self.get_response_body()
        return json.loads(response_body)
