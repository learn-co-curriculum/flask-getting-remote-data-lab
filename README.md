# Company Directory Dashboard

A `GetRequester` class for fetching and parsing remote JSON data, built for a Flask app that pulls a live employee directory from a remote API.

## What It Does

- `GetRequester(url)` — initialize with the URL of a remote JSON endpoint.
- `get_response_body()` — sends an HTTP GET request to the endpoint and returns the raw response body.
- `load_json()` — fetches the response and parses it into Python data structures (lists/dicts).

Flask routes can call `load_json()` to pull the latest employee list on each page load and render it with Jinja templates.

## Setup

```
pipenv install
pipenv shell
```

## Testing

```
pytest
```
