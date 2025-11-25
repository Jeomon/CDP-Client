
"""CDP Input Events"""

from client.service import CDPClient
from typing import TypedDict, Optional, Callable
from protocol.input.events.types import *

class InputEvents:
    def __init__(self,client:CDPClient):
        self.client=client
    
    def on_drag_intercepted(self, callback: Callable[[dragInterceptedEvent,Optional[str]], None]=None) -> None:
        """Emitted only when `Input.setInterceptDrags` is enabled. Use this data with `Input.dispatchDragEvent` to restore normal drag and drop behavior."""
        self.client.on('dragIntercepted', callback)
     