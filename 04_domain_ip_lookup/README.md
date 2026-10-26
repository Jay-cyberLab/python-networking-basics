# Mini DNS Lookup Tool

A Python terminal tool for forward and reverse DNS lookups.

## Features

- Forward lookup: domain name to IPv4 and IPv6 addresses
- Reverse lookup: IP address to hostname
- Handles invalid domains and IP addresses safely
- Uses Python's built-in `socket` module

## Concepts Practiced

- DNS
- IPv4 and IPv6
- Forward and reverse DNS lookup
- Python modules
- Functions
- Sets
- Loops
- `try` / `except`
- Input validation

## Run

```bash
python3 main.py
```

## Example Output

```text
----- Mini DNS Lookup Tool -----
1. Look up a domain
2. Reverse look up an IP address
3. Exit

Choose an option: 1
Enter a domain name: python.org

Results for: python.org
IPv4: 151.101.0.223
IPv6: 2a04:4e42::223
```

> DNS results and IP addresses may differ on each network.
