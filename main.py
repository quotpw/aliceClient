import json

import time
from typing import Optional

import websockets
import asyncio
from websockets.legacy.client import WebSocketClientProtocol

from op.constants import OP_TO_FUNCTION


def handle_op(op: int, kwargs: Optional[dict]) -> Optional[dict]:
    if kwargs is None:
        kwargs = {}

    function = OP_TO_FUNCTION.get(op)
    if function is not None:
        try:
            return function(**kwargs)
        except Exception as err:
            return {"error": str(err)}
    else:
        return {"error": "Unknown op code"}


async def client_listen():
    async with websockets.connect('ws://localhost:8005/ws', ping_interval=None) as websocket:#192.168.1.10
        websocket: WebSocketClientProtocol = websocket

        while True:
            message = json.loads(await websocket.recv())
            print("Received:", message)

            response = handle_op(message["op"], message.get("kwargs"))
            print("Response:", response)

            if response is not None:
                await websocket.send(json.dumps(response))


if __name__ == '__main__':
    while True:
        try:
            asyncio.get_event_loop().run_until_complete(client_listen())
        except Exception as e:
            print(e)
            time.sleep(2)
        continue
