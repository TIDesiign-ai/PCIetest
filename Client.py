import json
from pathlib import Path

import requests


CONFIG_FILE = Path("client_config.json")


def load_config():
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    server_url = input("Server URL: ").strip()

    config = {
        "server_url": server_url
    }

    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4, ensure_ascii=False)

    print("Config saved.")

    return config


def send(data: dict, server_url: str):
    response = requests.post(
        f"{server_url}/api",
        json=data,
        timeout=10
    )

    response.raise_for_status()

    return response.json()


if __name__ == "__main__":
    config = load_config()
    server_url = config["server_url"]

    message = input("Message: ")

    data = {
        "message": message
    }

    result = send(data, server_url)

    print("Response:")
    print(json.dumps(result, indent=4, ensure_ascii=False))
