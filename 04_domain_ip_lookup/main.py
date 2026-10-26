import socket


def lookup_domain(domain):
    try:
        results = socket.getaddrinfo(domain, None)
        addresses = set()

        for family, _, _, _, socket_address in results:
            ip_address = socket_address[0]

            if family == socket.AF_INET:
                address_type = "IPv4"
            elif family == socket.AF_INET6:
                address_type = "IPv6"
            else:
                continue

            addresses.add((address_type, ip_address))

        print(f"\nResults for: {domain}")

        for address_type, ip_address in sorted(addresses):
            print(f"{address_type}: {ip_address}")

    except socket.gaierror:
        print("\nCould not find that domain. Check the spelling and try again.")


def reverse_lookup(ip_address):
    try:
        hostname, aliases, addresses = socket.gethostbyaddr(ip_address)

        print(f"\nIP address: {ip_address}")
        print(f"Hostname: {hostname}")

        if len(aliases) > 0:
            print(f"Aliases: {', '.join(aliases)}")

    except (socket.herror, socket.gaierror):
        print("\nCould not find a hostname for that IP address.")


while True:
    print("\n----- Mini DNS Lookup Tool -----")
    print("1. Look up a domain")
    print("2. Reverse look up an IP address")
    print("3. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        domain = input("Enter a domain name: ").strip()

        if domain != "":
            lookup_domain(domain)
        else:
            print("Domain cannot be empty.")

    elif choice == "2":
        ip_address = input("Enter an IP address: ").strip()

        if ip_address != "":
            reverse_lookup(ip_address)
        else:
            print("IP address cannot be empty.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Choose 1, 2, or 3.")
