
"""CDP Log Events"""

from client.service import CDPClient
from typing import TypedDict, Optional, Callable
from protocol.log.events.types import *

class LogEvents:
    def __init__(self,client:CDPClient):
        self.client=client
    
    def on_entry_added(self, callback: Callable[[entryAddedEvent,Optional[str]], None]=None) -> None:
        """Issued when new message was logged."""
        self.client.on('entryAdded', callback)
     