import socket


HOST = "127.0.0.1"
PORT = 5000


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))

    print("Connected to the server.")
    print("Type 'exit' to end the chat.")

    while True:
        message = input("You: ")
        client.sendall(message.encode())

        if message.lower() == "exit":
            print("Chat ended.")
            break

        reply = client.recv(1024).decode()

        if not reply or reply.lower() == "exit":
            print("Server disconnected.")
            break

        print(f"Server: {reply}")
