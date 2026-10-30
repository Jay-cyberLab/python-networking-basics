
import socket


HOST = "127.0.0.1"


def check_port(port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.settimeout(1)

            result = client.connect_ex((HOST, port))

            if result == 0:
                print(f"\nPort {port}: Open")
            else:
                print(f"\nPort {port}: Closed")

    except socket.error as error:
        print(f"\nCould not check the port: {error}")


print("----- Local Port Checker -----")
print(f"Checking ports only on {HOST}")

while True:
    user_input = input("\nEnter a port number, or type 'exit': ").strip()

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    if user_input.isdigit():
        port = int(user_input)

        if 1 <= port <= 65535:
            check_port(port)
        else:
            print("Port number must be between 1 and 65535.")
    else:
        print("Please enter a valid port number.")
