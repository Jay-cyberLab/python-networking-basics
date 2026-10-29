from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
import time


def check_website(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url

    request = Request(
        url,
        headers={"User-Agent": "Python Website Status Checker"}
    )

    start_time = time.perf_counter()

    try:
        with urlopen(request, timeout=10) as response:
            response_time = (time.perf_counter() - start_time) * 1000

            print(f"\nWebsite: {url}")
            print(f"Status code: {response.status}")
            print(f"Status message: {response.reason}")
            print(f"Response time: {response_time:.0f} ms")
            print("Website is reachable.")

    except HTTPError as error:
        response_time = (time.perf_counter() - start_time) * 1000

        print(f"\nWebsite: {url}")
        print(f"Status code: {error.code}")
        print(f"Response time: {response_time:.0f} ms")
        print("The website responded, but the request was not successful.")

    except URLError as error:
        print(f"\nCould not reach {url}.")
        print(f"Reason: {error.reason}")

print("-------------Website Status Checker--------------")

while True:
    url = input("\nEnter a website, or type 'exit' : ").strip()

    if url.lower() == "exit":
        print("GoodBye!")
        break
    else:
        check_website(url)

