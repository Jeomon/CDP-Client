
"""CDP Tethering Events"""

from client.events import CDPEvents
from typing import TypedDict, Optional, Callable
from protocol.tethering.events.types import *

class TetheringEvents:
    def __init__(self,events:CDPEvents):
        self.events=events
    
    def on_accepted(self, callback: Callable[acceptedEvent, None]=None) -> None:
        """Informs that port was successfully bound and got a specified connection id."""
        self.events.on('accepted', callback)
     