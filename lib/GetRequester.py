import requests

class GetRequester:

    def __init__(self, url):
        self.url = url
        self.response = None

    def get_response_body(self):
        self.response = requests.get(self.url)
        return self.response 

    def load_json(self):
        if self.response is None:
            self.get_response_body()

        return self.response.json()