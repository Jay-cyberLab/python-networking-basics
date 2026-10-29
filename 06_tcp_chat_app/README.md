# Local TCP Chat App

A simple client-server chat application built with Python sockets.

## Features

- Uses TCP sockets for reliable communication
- Separate server and client programs
- Runs safely on `127.0.0.1` (localhost)
- Sends and receives text messages
- Type `exit` to end the chat

## Concepts Practiced

- Client-server architecture
- TCP
- IP addresses and ports
- Python's built-in `socket` module
- `bind()`, `listen()`, `accept()`, and `connect()`
- Sending bytes with `sendall()`
- Receiving bytes with `recv()`
- Converting text with `.encode()` and `.decode()`

## Run

Open two terminals.

### Terminal 1: Start the server

```bash
python3 server.py
```

### Terminal 2: Start the client

```bash
python3 client.py
```

Both programs use `127.0.0.1:5000`, meaning the chat stays on your own computer.
