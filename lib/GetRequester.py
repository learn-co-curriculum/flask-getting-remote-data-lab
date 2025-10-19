import requests
import json

class GetRequester:
    """A tiny helper for performing HTTP GET requests and parsing JSON."""

    def __init__(self, url):
        # Store the URL used for requests
        self.url = url

    def get_response_body(self):
        """Return the raw response body (bytes) from a GET request to self.url."""
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        """Return the response body parsed from JSON into native Python objects."""
        return json.loads(self.get_response_body())