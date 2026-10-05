import json
from pathlib import Path

from fastapi import FastAPI
import uvicorn


CONFIG_FILE = Path(__file__).resolve().parent / "config.json"

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
            config = json.load(f)
    else:
        config = {}

    if "server" not in config:
        print("Server configuration")

        host = input("Host [0.0.0.0]: ").strip()
        port = input("Port [8000]: ").strip()

        config["server"] = {
            "host": host or "0.0.0.0",
            "port": int(port) if port else 8000
        }

        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4, ensure_ascii=False)

        print("Server config saved.")

    return config["server"]


if __name__ == "__main__":
    config = load_config()

    uvicorn.run(
        app,
        host=config["host"],
        port=config["port"]
    )
