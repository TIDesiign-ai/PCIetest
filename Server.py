from fastapi import FastAPI

app = FastAPI()


@app.post("/api")
def api(data: dict):
    print("受信:", data)

    return {
        "status": "ok",
        "message": "受信しました",
        "data": data
    }
