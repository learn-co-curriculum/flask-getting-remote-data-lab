from urllib import response

import requests
import json

class GetRequester:
    """
    A reusable class for sending HTTP GET requests and
    converting JSON responses into Python objects.
    """

    def __init__(self, url):
        """
        Initialize the requester with the endpoint URL.
        """
        self.url = url

    def get_response_body(self):
        """
        Send a GET request to the specified URL and return
        the response body.
        """
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        """
        Retrieve the response body and convert the JSON
        data into Python objects.
        """
        response = self.get_response_body()
        return json.loads(response)