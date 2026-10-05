import json
import requests


with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

SERVER_URL = config["server_url"]


def send(data: dict) -> dict:
    response = requests.post(
        f"{SERVER_URL}/api",
        json=data,
        timeout=10
    )

    response.raise_for_status()

    return response.json()


result = send({
    "message": "Hello Server",
    "value": 123
})

print(result)
