# DNS Record Viewer

A Python terminal tool that displays common DNS records for a domain.

## Record Types

- `A` — IPv4 address records
- `AAAA` — IPv6 address records
- `MX` — mail server records
- `NS` — authoritative name server records

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependency:

```bash
python -m pip install -r requirements.txt
```

## Run

```bash
python main.py
```

## Concepts Practiced

- DNS record types
- Python packages
- Virtual environments
- `dnspython`
- Loops, functions, and exception handling
- DNS errors such as missing records and nonexistent domains

> DNS records can vary by domain and may change over time.

