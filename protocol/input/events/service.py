
"""CDP Input Events"""

from client.events import CDPEvents
from typing import TypedDict, Optional, Callable
from protocol.input.events.types import *

class InputEvents:
    def __init__(self,events:CDPEvents):
        self.events=events
    
    def on_drag_intercepted(self, callback: Callable[[dragInterceptedEvent,Optional[str]], None]=None) -> None:
        """Emitted only when `Input.setInterceptDrags` is enabled. Use this data with `Input.dispatchDragEvent` to restore normal drag and drop behavior."""
        self.events.on('dragIntercepted', callback)
     