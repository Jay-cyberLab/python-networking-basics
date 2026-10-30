import socket


HOST = "127.0.0.1"

COMMON_PORTS = {
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    5000: "Local Chat App"
}


def is_port_open(port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.settimeout(1)
            return client.connect_ex((HOST, port)) == 0

    except socket.error:
        return False


def check_single_port():
    user_input = input("Enter a port number: ").strip()

    if user_input.isdigit():
        port = int(user_input)

        if 1 <= port <= 65535:
            if is_port_open(port):
                print(f"\nPort {port}: Open")
            else:
                print(f"\nPort {port}: Closed")
        else:
            print("Port number must be between 1 and 65535.")
    else:
        print("Please enter a valid port number.")


def check_common_ports():
    print(f"\n----- Common Ports on {HOST} -----")

    for port, service in COMMON_PORTS.items():
        if is_port_open(port):
            status = "Open"
        else:
            status = "Closed"

        print(f"{port} ({service}): {status}")


while True:
    print("\n----- Local Port Checker -----")
    print("1. Check one local port")
    print("2. Check common local ports")
    print("3. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        check_single_port()
    elif choice == "2":
        check_common_ports()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Choose 1, 2, or 3.")
