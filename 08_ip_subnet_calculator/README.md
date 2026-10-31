# IP/Subnet Calculator

A Python terminal tool that calculates IPv4 subnet information from an IP address and CIDR prefix.

## Features

- Accepts IPv4 addresses with CIDR notation
- Displays network address and subnet mask
- Displays broadcast address
- Calculates the first and last usable host address
- Calculates total and usable addresses
- Handles invalid input safely

## Example Input

```text
192.168.1.10/24
```

## Example Output

```text
Network address: 192.168.1.0
Subnet mask: 255.255.255.0
Broadcast address: 192.168.1.255
First usable host: 192.168.1.1
Last usable host: 192.168.1.254
Usable hosts: 254
```

## Concepts Practiced

- IPv4 addresses
- CIDR notation
- Subnet masks
- Network and broadcast addresses
- Python's built-in `ipaddress` module
- Functions, loops, and exception handling

## Run

```bash
python3 main.py
```
