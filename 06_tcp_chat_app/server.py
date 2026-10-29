import socket


HOST = "127.0.0.1"
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST,PORT))
    server.listen()


    print(f"Server is listening on {HOST} : {PORT} ")
    print("Waiting for a client to connect....")


    connection, address = server.accept()

    with connection:
        print(f"Connected to : {address} ")

        while True:
            message = connection.recv(1024).decode()

            if not message or message.lower() == "exit":
                print("Client Disconneted.")
                break

            print(f"Client : {message}")

            reply = input("YOU : ")
            connection.sendall(reply.encode())

            if reply.lower() == "exit":
                print("chat ended.")
                break
