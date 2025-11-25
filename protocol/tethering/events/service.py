
"""CDP Tethering Events"""

from client.service import CDPClient
from typing import TypedDict, Optional, Callable
from protocol.tethering.events.types import *

class TetheringEvents:
    def __init__(self,client:CDPClient):
        self.client=client
    
    def on_accepted(self, callback: Callable[[acceptedEvent,Optional[str]], None]=None) -> None:
        """Informs that port was successfully bound and got a specified connection id."""
        self.client.on('Tethering.accepted', callback)
     