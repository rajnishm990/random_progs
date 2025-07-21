from fastapi import FastAPI , WebSocket 
from .utils import get_metrics
import asyncio

app = FastAPI()

app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    while True:
        data = get_metrics()
        await websocket.send_json(data)
        await asyncio.sleep(1)
        

