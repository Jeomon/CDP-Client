
"""CDP Log Events"""

from client.events import CDPEvents
from typing import TypedDict, Optional, Callable
from protocol.log.events.types import *

class LogEvents:
    def __init__(self,events:CDPEvents):
        self.events=events
    
    def on_entry_added(self, callback: Callable[entryAddedEvent, None]=None) -> None:
        """Issued when new message was logged."""
        self.events.on('entryAdded', callback)
     