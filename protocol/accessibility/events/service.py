
"""CDP Accessibility Events"""

from client.service import CDPClient
from typing import TypedDict, Optional, Callable
from protocol.accessibility.events.types import *

class AccessibilityEvents:
    def __init__(self,client:CDPClient):
        self.client=client
    
    def on_load_complete(self, callback: Callable[[loadCompleteEvent,Optional[str]], None]=None) -> None:
        """The loadComplete event mirrors the load complete event sent by the browser to assistive technology when the web page has finished loading."""
        self.client.on('Accessibility.loadComplete', callback)
    
    def on_nodes_updated(self, callback: Callable[[nodesUpdatedEvent,Optional[str]], None]=None) -> None:
        """The nodesUpdated event is sent every time a previously requested node has changed the in tree."""
        self.client.on('Accessibility.nodesUpdated', callback)
     