import asyncio
import socket
import time

import requests
from fastapi import FastAPI
import uvicorn

app = FastAPI()

# 相手PCのIPアドレス
TARGET_IP = "192.168.1.20"
TARGET_PORT = 8000

INTERVAL = 1.0


@app.get("/")
def root():
    return {
        "status": "ok",
        "hostname": socket.gethostname(),
    }


@app.post("/packet")
def receive_packet(data: dict):
    print(
        f"[RECEIVE] "
        f"{data.get('sender')} "
        f"seq={data.get('seq')} "
        f"time={data.get('time')}"
    )

    return {
        "status": "ok",
        "receiver": socket.gethostname(),
        "received_seq": data.get("seq"),
    }


async def send_packets():
    seq = 0
    hostname = socket.gethostname()

    # FastAPI起動を少し待つ
    await asyncio.sleep(2)

    print(f"=== Packet test started ===")
    print(f"Target: {TARGET_IP}:{TARGET_PORT}")
    print(f"Interval: {INTERVAL}s")

    while True:
        seq += 1

        packet = {
            "sender": hostname,
            "seq": seq,
            "time": time.time(),
        }

        try:
            response = await asyncio.to_thread(
                requests.post,
                f"http://{TARGET_IP}:{TARGET_PORT}/packet",
                json=packet,
                timeout=3,
            )

            result = response.json()

            print(
                f"[SEND] seq={seq} "
                f"-> {TARGET_IP} "
                f"[ACK] {result}"
            )

        except Exception as e:
            print(
                f"[ERROR] seq={seq} "
                f"-> {TARGET_IP}: {e}"
            )

        await asyncio.sleep(INTERVAL)


@app.on_event("startup")
async def startup():
    asyncio.create_task(send_packets())


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
    )
