
"""CDP Overlay Events"""

from client.service import CDPClient
from typing import TypedDict, Optional, Callable
from protocol.overlay.events.types import *

class OverlayEvents:
    def __init__(self,client:CDPClient):
        self.client=client
    
    def on_inspect_node_requested(self, callback: Callable[[inspectNodeRequestedEvent,Optional[str]], None]=None) -> None:
        """Fired when the node should be inspected. This happens after call to `setInspectMode` or when user manually inspects an element."""
        self.client.on('inspectNodeRequested', callback)
    
    def on_node_highlight_requested(self, callback: Callable[[nodeHighlightRequestedEvent,Optional[str]], None]=None) -> None:
        """Fired when the node should be highlighted. This happens after call to `setInspectMode`."""
        self.client.on('nodeHighlightRequested', callback)
    
    def on_screenshot_requested(self, callback: Callable[[screenshotRequestedEvent,Optional[str]], None]=None) -> None:
        """Fired when user asks to capture screenshot of some area on the page."""
        self.client.on('screenshotRequested', callback)
    
    def on_inspect_mode_canceled(self, callback: Callable[[inspectModeCanceledEvent,Optional[str]], None]=None) -> None:
        """Fired when user cancels the inspect mode."""
        self.client.on('inspectModeCanceled', callback)
     