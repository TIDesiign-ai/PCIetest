import json
from pathlib import Path

import requests


CONFIG_FILE = Path(__file__).resolve().parent / "config.json"


def load_config():
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            config = json.load(f)
    else:
        config = {}

    if "client" not in config:
        server_url = input("Server URL: ").strip()

        config["client"] = {
            "server_url": server_url
        }

        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4, ensure_ascii=False)

        print("Client config saved.")

    return config["client"]


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

    message = input("Message: ")

    result = send(
        {"message": message},
        config["server_url"]
    )

    print(json.dumps(
        result,
        indent=4,
        ensure_ascii=False
    ))
