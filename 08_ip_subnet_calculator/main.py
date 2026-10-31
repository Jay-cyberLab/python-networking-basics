import ipaddress as ip

def calculate_subnet(cdir):
    try:
        network = ip.ip_network(cidr,strict = False )

        if network.version != 4:
            print("\nPleases enter an IPv4 address and CDIR prefix.")
            return

        print("\n--------- Subnet Information --------")
        print(f"Network address : {network.network_address}")
        print(f"Subnet mask : {network.netmask}")
        print(f"Braodcast address : {network.broadcast_address}")
        print(f"Total addresses : {network.num_addresses}")


        if network.prefixlen <= 30:
            first_host = network.network_address + 1
            last_host = network.broadcast_address - 1
            usable_hosts = network.num_addresses - 2


            print(f"first usable host : {first_host}")
            print(f"Last usable host : {last_host}")
            print(f"Usable hosts : {usable_hosts}")

        else:
            print("Usable hosts : 0 traditional host range for /31 or /32.")


    except ValueError:
        print("\nInvalid input. Example : 192.168.1.10/24")


print("----- IP/Subnet Calclator ----")

while True:
    cidr = input("\nEnter an IPv4 address with CIDR, or type 'exit' : ").strip()


    if cidr.lower() == "exit":
        print("GoodBye!")
        break

    calculate_subnet(cidr)





