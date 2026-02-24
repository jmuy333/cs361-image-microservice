import requests
import sys


def call_random_photos(base_url: str, query: str, amount: int) -> None:
    # Endpoint url to get random photos
    url = f"{base_url}/photos/random"
    params = {"query": query, "amount": amount}

    try:
        resp = requests.get(url, params=params, timeout=10)
    except requests.RequestException as e:
        print(f"[NETWORK ERROR] Could not reach microservice: {e}")
        return

    print("\nHTTP Response: ")
    print("URL:", resp.url)
    print("Status:", resp.status_code)
    print("Headers Content-Type:", resp.headers.get("Content-Type"))

    print("\nRaw: ")
    print(resp.text)

    try:
        data = resp.json()
    except ValueError:
        print("\n[NOTE] Body is not JSON.")
        return

    print("\nJSON: ")
    print(data)


def main():
    # Localhost url
    base_url = "http://127.0.0.1:5000"
    query = "test"
    amount = 5

    # Extract the paramters that were provided by client
    if len(sys.argv) >= 2:
        query = sys.argv[1]
    if len(sys.argv) >= 3:
        # Need to verify amount is an int 
        try:
            amount = int(sys.argv[2])
        except ValueError:
            print("ERR: amount must be an integer.")
            return

    print("Image Microservice Test Client: ")
    call_random_photos(base_url, query, amount)


if __name__ == "__main__":
    main()