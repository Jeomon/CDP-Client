
"""CDP Overlay Events"""

from client.events import CDPEvents
from typing import TypedDict, Optional, Callable
from protocol.overlay.events.types import *

class OverlayEvents:
    def __init__(self,events:CDPEvents):
        self.events=events
    
    def on_inspect_node_requested(self, callback: Callable[[inspectNodeRequestedEvent,Optional[str]], None]=None) -> None:
        """Fired when the node should be inspected. This happens after call to `setInspectMode` or when user manually inspects an element."""
        self.events.on('inspectNodeRequested', callback)
    
    def on_node_highlight_requested(self, callback: Callable[[nodeHighlightRequestedEvent,Optional[str]], None]=None) -> None:
        """Fired when the node should be highlighted. This happens after call to `setInspectMode`."""
        self.events.on('nodeHighlightRequested', callback)
    
    def on_screenshot_requested(self, callback: Callable[[screenshotRequestedEvent,Optional[str]], None]=None) -> None:
        """Fired when user asks to capture screenshot of some area on the page."""
        self.events.on('screenshotRequested', callback)
    
    def on_inspect_mode_canceled(self, callback: Callable[[inspectModeCanceledEvent,Optional[str]], None]=None) -> None:
        """Fired when user cancels the inspect mode."""
        self.events.on('inspectModeCanceled', callback)
     