import requests

response = requests.get(
    "http://127.0.0.1:5000/search",
    params={"query": "tower", "amount": 5}
)
print(response.json())