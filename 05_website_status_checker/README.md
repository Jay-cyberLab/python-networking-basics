# Website Status Checker

A Python terminal tool that checks whether a website is reachable and measures its response time.

## Features

- Accepts a domain or full URL
- Automatically adds `https://` when needed
- Displays HTTP status codes and messages
- Measures response time in milliseconds
- Handles unreachable websites and invalid domains safely
- Times out after 10 seconds

## Concepts Practiced

- HTTP and HTTPS
- HTTP status codes: `200`, `404`, `503`
- Python's built-in `urllib` module
- HTTP requests
- Exception handling with `HTTPError` and `URLError`
- Response-time measurement with the `time` module

## Run

```bash
python3 main.py
```

## Example Output

```text
Website: https://example.com
Status code: 200
Status message: OK
Response time: 185 ms
Website is reachable.
```

> Response times and status codes can vary by network and website availability.
