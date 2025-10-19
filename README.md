# Getting Remote Data Lab

## The Scenario 
It is time to practice building out your own class for retrieving remote data. In this lab, you are tasked with building a generic GetRequester class. This class will be able to take in a URL on initialization and send an HTTP GET request on command. You will also need to build a method for dealing with requests that return JSON.

## Tools and Resources 
- [GitHub Repo](https://github.com/learn-co-curriculum/flask-getting-remote-data-lab)
- [GET - Mozilla](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET)
- [HTTP methods - Mozilla](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
- [requests](https://requests.readthedocs.io/en/latest/)
- [Python JSON](https://docs.python.org/3/library/json.html)

## Instructions

### Set Up

Before we begin coding, let's complete the initial setup for this lesson: 

* Fork and Clone
  * For this lesson, you will need the following GitHub Repo: https://github.com/walbeck85/flask-getting-remote-data-lab/ 
  * Fork the repository to your GitHub account.
  * Clone the forked repository to your local machine.
* Open and Run File
  * Open the project in VSCode.
  * Run pipenv install to install all necessary dependencies.
  * Run pipenv shell to open instance of python shell

### Task 1: Define the Problem

* Build a class to interact with api
* Get the data
* Convert to json data

### Task 2: Determine the Design

* Endpoint: https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json.
  * ```get_response_body```
    * Query endpoint
  * ```load_json```
    * Convert to json data

#### Task 3: Develop, Test, and Refine the Code

* Create feature branch
* Build get_response_body to query endpoint
* Convert endpoint data to json and return the data
* Push feature branch and open a PR on GitHub
* Merge to main

#### Task 4: Document and Maintain

Best Practice documentation steps:
* Add comments to code to explain purpose and logic, clarifying intent / functionality of code to other developers.
* Update README text to reflect the functionality of the application following https://makeareadme.com.
* Delete any stale branches on GitHub
* Remove unnecessary/commented out code
* If needed, update git ignore to remove sensitive data

## Submission

Once all tests are passing and working code is pushed to the GitHub main branch, submit your GitHub repo through Canvas using CodeGrade.

# Lab Submission: Retrieving Remote Data from an API

This repository contains my implementation for the Course 8, Module 3 lab.  
The goal of this project is to demonstrate a simple but reusable Python class that retrieves data from a remote JSON API endpoint and converts it into native Python data structures. The work here aligns with the Flatiron lesson on consuming APIs and verifying responses through unit tests.

## Features

- A class `GetRequester` located in `lib/GetRequester.py` that:
  - Accepts a URL upon initialization.
  - Sends an HTTP GET request using the `requests` library.
  - Returns the raw response body through the `get_response_body()` method.
  - Converts JSON data to Python objects with the `load_json()` method.
- Complete test coverage provided by `pytest` in `lib/testing/get_requester_test.py`.
- Fully passing test suite confirming correct data retrieval and parsing behavior.

## Environment

- Python 3.8.x (tested locally with 3.8.13)
- macOS terminal using `pipenv` for environment and dependency management

If you are on another platform, use the equivalent commands for activating the environment.

## Setup

Clone and enter the project directory:

```bash
git clone <repo-url>
cd flask-getting-remote-data-lab
```

Install dependencies and activate the virtual environment:

```bash
pipenv install
pipenv shell
```

To verify dependencies are installed, you can run:

```bash
pip list
```

## File structure

```
.
├── CONTRIBUTING.md
├── LICENSE.md
├── Pipfile
├── Pipfile.lock
├── pytest.ini
├── README.md
└── lib/
    ├── GetRequester.py
    └── testing/
        ├── conftest.py
        └── get_requester_test.py
```

## How to run the script manually

From the project root with the virtual environment active:

```bash
python
```

Then inside the Python REPL:

```python
from lib.GetRequester import GetRequester

url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
gr = GetRequester(url)
print(gr.load_json())
```

You should see a list of dictionaries printed to the terminal representing the remote JSON data.

Example output:

```python
[
  {"name": "Daniel", "occupation": "LG Fridge Salesman"},
  {"name": "Joe", "occupation": "WiFi Fixer"},
  {"name": "Avi", "occupation": "DJ"},
  {"name": "Howard", "occupation": "Mountain Legend"}
]
```

## Tests

Run the tests from the project root with the virtual environment active:

```bash
pytest -q
```

Expected output:

```
..
2 passed in <time>s
```

The tests confirm:
- `get_response_body()` returns the expected raw byte response from the API.
- `load_json()` correctly converts the JSON into Python lists and dictionaries.

## Rubric alignment

- **Retrieve data successfully:** The `get_response_body()` method performs an HTTP GET and returns a valid byte response.
- **Convert to JSON:** The `load_json()` method accurately parses and returns Python data types.
- **Reusable class:** The design supports future use in Flask routes or other projects needing remote data access.
- **Testing and documentation:** All tests pass, and the code includes clear comments and docstrings.

## Branch and PR workflow

This work was completed following proper Git hygiene:
- Work performed on `feature/getrequester-class`
- Merged into `main` after all tests passed
- Current update to README completed on `feature/update-readme`
- `main` remains clean and aligned with the submitted version

## Troubleshooting

- If tests fail due to network access, verify you can reach the endpoint directly in a browser.
- If `pipenv shell` fails to activate, try `python3 -m pipenv shell`.
- If `requests` is missing, reinstall dependencies with `pipenv install`.

## Chris' checklist

1. Clone the repo and open it in VS Code or your preferred IDE.  
2. Run `pipenv install` followed by `pipenv shell` to create and activate the environment.  
3. Execute `pytest -q` to confirm both test cases pass.  
4. Optionally, run the manual script to confirm that the returned data matches the expected JSON structure.

---