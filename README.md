# Getting Remote Data Lab

## Overview
This lab builds a simple `GetRequester` class for retrieving remote JSON data over HTTP. The class is initialized with a URL and provides methods to fetch raw response data and load JSON from the endpoint.

## Features
- `GetRequester(url)` initializes with the endpoint URL
- `get_response_body()` sends a GET request and returns the raw response body
- `load_json()` sends a GET request and returns parsed JSON data

## Endpoint
The lab uses this sample endpoint:

`https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json`

## Installation
1. Clone the repository.
2. Install dependencies with Pipenv:
   ```bash
   pipenv install
   ```
3. Activate the virtual environment:
   ```bash
   pipenv shell
   ```

## Usage
From the project root, open Python and use the class:

```python
from lib.GetRequester import GetRequester

url = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'
requester = GetRequester(url)

raw_body = requester.get_response_body()
print(raw_body)

json_data = requester.load_json()
print(json_data)
```

## Testing
Run the test suite with `pytest` from the project root:

```bash
pytest
```

## Notes
- The implementation uses `requests` to make HTTP GET requests.
- `load_json()` returns the endpoint data as a Python list of dictionaries.
- `get_response_body()` returns the raw response content.
