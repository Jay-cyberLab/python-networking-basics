# Local Port Checker

A Python terminal tool that checks whether TCP ports are open or closed on the local computer.

## Features

- Checks ports only on `127.0.0.1` (localhost)
- Check one chosen port
- Check common ports from a menu
- Displays the related service name
- Validates port numbers from `1` to `65535`

## Common Ports

- `22` — SSH
- `80` — HTTP
- `443` — HTTPS
- `5000` — Local TCP Chat App

## Concepts Practiced

- TCP ports
- Localhost (`127.0.0.1`)
- Python's built-in `socket` module
- `connect_ex()`
- Dictionaries
- Functions
- Loops and input validation

## Run

```bash
python3 main.py
```

> This project checks only the local machine for safe learning and testing.
