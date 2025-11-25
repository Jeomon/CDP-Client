
"""CDP Accessibility Events"""

from client.events import CDPEvents
from typing import TypedDict, Optional, Callable
from protocol.accessibility.events.types import *

class AccessibilityEvents:
    def __init__(self,events:CDPEvents):
        self.events=events
    
    def on_load_complete(self, callback: Callable[loadCompleteEvent, None]=None) -> None:
        """The loadComplete event mirrors the load complete event sent by the browser to assistive technology when the web page has finished loading."""
        self.events.on('loadComplete', callback)
    
    def on_nodes_updated(self, callback: Callable[nodesUpdatedEvent, None]=None) -> None:
        """The nodesUpdated event is sent every time a previously requested node has changed the in tree."""
        self.events.on('nodesUpdated', callback)
     