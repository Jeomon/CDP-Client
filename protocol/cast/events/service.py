
"""CDP Cast Events"""

from client.service import CDPClient
from typing import TypedDict, Optional, Callable
from protocol.cast.events.types import *

class CastEvents:
    def __init__(self,client:CDPClient):
        self.client=client
    
    def on_sinks_updated(self, callback: Callable[[sinksUpdatedEvent,Optional[str]], None]=None) -> None:
        """This is fired whenever the list of available sinks changes. A sink is a device or a software surface that you can cast to."""
        self.client.on('Cast.sinksUpdated', callback)
    
    def on_issue_updated(self, callback: Callable[[issueUpdatedEvent,Optional[str]], None]=None) -> None:
        """This is fired whenever the outstanding issue/error message changes. |issueMessage| is empty if there is no issue."""
        self.client.on('Cast.issueUpdated', callback)
     