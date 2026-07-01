# Flask Get Requester

A reusable Python class for retrieving data from remote APIs using HTTP GET requests. The project demonstrates how to fetch data from a remote endpoint, access the raw response body, and convert JSON responses into Python data structures for use in Flask applications or other Python projects.

## Features

* Send HTTP GET requests to a remote API endpoint.
* Retrieve the raw response body as bytes.
* Parse JSON responses into Python dictionaries and lists.
* Encapsulate request logic in a reusable `GetRequester` class.
* Well-documented code with comments explaining the purpose and logic of each method.

## Technologies Used

* Python 3
* Requests
* JSON
* Pytest

## Project Structure

```text
flask-getting-remote-data-lab/
├── lib/
│   ├── GetRequester.py
│   └── testing/
├── Pipfile
├── Pipfile.lock
├── pytest.ini
└── README.md
```

## Installation

1. Clone the repository.

```bash
git clone git@github.com:wanja-juma/flask-getting-remote-data-lab.git
```

2. Navigate to the project directory.

```bash
cd flask-getting-remote-data-lab
```

3. Install the project dependencies.

```bash
pipenv install
```

4. Activate the virtual environment.

```bash
pipenv shell
```

## Usage

Import the `GetRequester` class and provide the URL of the remote endpoint.

```python
from lib.GetRequester import GetRequester

url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"

requester = GetRequester(url)
```

### Retrieve the Raw Response Body

The `get_response_body()` method sends an HTTP GET request and returns the response body as bytes.

```python
response = requester.get_response_body()
print(response)
```

### Load JSON Data

The `load_json()` method retrieves the response body and converts the JSON into native Python data structures.

```python
data = requester.load_json()
print(data)
```

## Remote Endpoint

The application retrieves employee data from the following endpoint:

```text
https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json
```

## Running the Tests

Execute the test suite using Pytest:

```bash
pytest
```

A successful run should report all tests passing.

## Display Screenshot

Screenshot 2026-07-02 023358.png

## Example Workflow

1. Create a `GetRequester` instance with the endpoint URL.
2. Call `get_response_body()` to retrieve the raw response.
3. Call `load_json()` to convert the JSON response into Python objects.
4. Use the returned data in your Flask application, templates, or other Python code.

## Author

Ruth Juma
