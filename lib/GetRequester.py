import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url
        self.response = None

    def get_response_body(self):
        # Send request and store response
        self.response = requests.get(self.url)
        return self.response.content  # bytes, not text

    def load_json(self):
        # Ensure response exists
        if self.response is None:
            self.get_response_body()

        # Convert JSON bytes/string into Python list
        return json.loads(self.response.content)