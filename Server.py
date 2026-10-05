import json
from pathlib import Path

from fastapi import FastAPI
import uvicorn


CONFIG_FILE = Path("server_config.json")

app = FastAPI()


@app.post("/api")
def api(data: dict):
    return {
        "status": "ok",
        "data": data
    }


def load_config():
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    print("Server configuration")

    host = input("Host [0.0.0.0]: ").strip()
    port = input("Port [8000]: ").strip()

    if not host:
        host = "0.0.0.0"

    if not port:
        port = 8000
    else:
        port = int(port)

    config = {
        "host": host,
        "port": port
    }

    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4, ensure_ascii=False)

    print(f"Config saved: {CONFIG_FILE}")

    return config


if __name__ == "__main__":
    config = load_config()

    uvicorn.run(
        app,
        host=config["host"],
        port=config["port"]
    )
