from typing import Optional, Dict, Any, Callable,Annotated
from operator import add
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
        self.id_counter: Annotated[int, add] = 0
        self.pending_requests: Dict[int, asyncio.Future] = {}
        self.event_handlers: Dict[str, Callable[[Any], None]] = {}

    async def __aenter__(self):
        self.ws = await websockets.connect(self.url,max_size=100*1024*1024)
        self.listen_task = asyncio.create_task(self.listen())
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        for future in self.pending_requests.values():
            if not future.done():
                future.set_exception(Exception("WebSocket connection closed"))
        self.pending_requests.clear()
        if self.listen_task:
            try:
                self.listen_task.cancel()
                await self.listen_task
            except asyncio.CancelledError:
                pass
            finally:
                self.listen_task = None
        if self.ws:
            await self.ws.close()
            self.ws = None

    async def send(self, method: str, params: Optional[dict] = None,session_id: Optional[str] = None) -> Any:
        self.id_counter+=1
        future = asyncio.Future()
        self.pending_requests[self.id_counter] = future
        
        try:
            message = {"id": self.id_counter, "method": method, "params": params or {}}
            if session_id:
                message['sessionId'] = session_id
            await self.ws.send(json.dumps(message))
            return await future
        except Exception as e:
            self.pending_requests.pop(self.id_counter, None)
            raise e

    def on(self, event: str, callback: Callable[[Any], None]) -> None:
        if event not in self.event_handlers:
            self.register(event, callback)

    def register(self, event: str, callback: Callable[[Any], None]) -> None:
        self.event_handlers[event] = callback

    def unregister(self, event: str) -> None:
        if event in self.event_handlers:
            del self.event_handlers[event]

    async def listen(self):
        while True:
            try:
                message = await self.ws.recv()
                data = json.loads(message)
                if "id" in data:
                    # Method
                    request_id=data["id"]
                    logging.debug(f"Received method: {data}")
                    if request_id not in self.pending_requests:
                        continue
                    future = self.pending_requests.pop(request_id)
                    if not future.done():
                        if "error" in data:
                            future.set_exception(Exception(data.get("error")))
                        else:
                            future.set_result(data.get("result"))
                elif 'method' in data:
                    # Event
                    method=data.get("method")
                    params = data.get("params", {})
                    session_id=data.get("sessionId")
                    logging.debug(f"Received event: {data}")
                    if method not in self.event_handlers:
                        continue
                    try:
                        handler = self.event_handlers[method]
                        if asyncio.iscoroutinefunction(handler):
                            await handler(params,session_id)
                        else:
                            handler(params,session_id)
                    except Exception as e:
                        logging.error(f"Error in event handler: {e}")
                        continue
            except websockets.exceptions.ConnectionClosed:
                logging.error("WebSocket connection closed")
                break
            except Exception as e:
                logging.error(f"Error in listen loop: {e}")
                break