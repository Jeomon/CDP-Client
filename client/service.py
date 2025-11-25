from typing import Optional, Dict, Any, Callable
import websockets
import asyncio
import logging
import json

from .methods import CDPMethods
from .events import CDPEvents

class CDPClient:
    def __init__(self, url: str):
        self.url = url
        self.ws :Optional[websockets.ClientConnection] = None
        self.listen_task :Optional[asyncio.Task] = None
        self.methods = CDPMethods(self)
        self.events = CDPEvents(self)
        self.id_counter = 0
        self.pending_requests: Dict[int, asyncio.Future] = {}
        self.event_handlers: Dict[str, list[Callable[[Any], None]]] = {}

    async def start(self):
        self.ws = await websockets.connect(
            self.url,
            max_size=100*1024*1024  # 100MB max message size
        )
        self.listen_task = asyncio.create_task(self.listen())
        return self

    async def stop(self):
        if self.listen_task:
            try:
                self.listen_task.cancel()
                self.listen_task
            except asyncio.CancelledError:
                pass
        if self.ws:
            await self.ws.close()

    async def send(self, method: str, params: Optional[dict] = None) -> Any:
        self.id_counter += 1
        request_id = self.id_counter
        future = asyncio.Future()
        self.pending_requests[request_id] = future
        
        try:
            message = json.dumps({"id": request_id, "method": method, "params": params or {}})
            await self.ws.send(message)
            return await future
        except Exception as e:
            self.pending_requests.pop(request_id, None)
            raise e

    def on(self, event: str, callback: Callable[[Any], None]) -> None:
        if event not in self.event_handlers:
            self.event_handlers[event] = []
        self.event_handlers[event].append(callback)

    async def listen(self):
        while True:
            try:
                message = await self.ws.recv()
                data = json.loads(message)
                if "id" in data and data["id"] in self.pending_requests:
                    # Response
                    request_id = data["id"]
                    future = self.pending_requests.pop(request_id)
                    if not future.done():
                        if "error" in data:
                            future.set_exception(Exception(data.get("error")))
                        else:
                            future.set_result(data.get("result"))
                elif method:=data.get("method"):
                    # Event
                    params = data.get("params", {})
                    if method in self.event_handlers:
                        for handler in self.event_handlers[method]:
                            try:
                                handler(params)
                            except Exception as e:
                                logging.error(f"Error in event handler for {method}: {e}")
            except websockets.exceptions.ConnectionClosed:
                logging.error("WebSocket connection closed")
                break
            except Exception as e:
                logging.error(f"Error in listen loop: {e}")
                break