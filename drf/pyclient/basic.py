import requests
import json
endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.post(
    endpoint,
    json={
        "model_id": 123,
        "title": "New Product",
        "content": "Hello World",
        "price": 123.45,
    },
)
print(get_response.text)
print(get_response.headers)