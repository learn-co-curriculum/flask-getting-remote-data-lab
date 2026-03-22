import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response

    def load_json(self):
        response = self.get_response_body()
        return response.json()
    
if __name__ == "__main__":
    url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
    requester = GetRequester(url)

    # Get raw response
    response = requester.get_response_body()
    if response:
        print(f"Status code: {response.status_code}")

    # Get JSON data
    data = requester.load_json()
    if data:
        print("JSON data received:")
        print(data)
