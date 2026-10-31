import dns.exception
import dns.resolver


RECORD_TYPES = ["A", "AAAA", "MX", "NS"]


def lookup_records(domain):
    print(f"\n----- DNS Records for {domain} -----")

    for record_type in RECORD_TYPES:
        print(f"\n{record_type} records:")

        try:
            answers = dns.resolver.resolve(domain, record_type)

            for answer in answers:
                print(answer.to_text())

        except dns.resolver.NoAnswer:
            print("No record found.")

        except dns.resolver.NXDOMAIN:
            print("This domain does not exist.")
            return

        except dns.exception.Timeout:
            print("DNS request timed out.")

        except dns.resolver.NoNameservers:
            print("No DNS server could answer the request.")


print("----- DNS Record Viewer -----")

while True:
    domain = input("\nEnter a domain name, or type 'exit': ").strip()

    if domain.lower() == "exit":
        print("Goodbye!")
        break

    if domain == "":
        print("Domain cannot be empty.")
    else:
        lookup_records(domain)
