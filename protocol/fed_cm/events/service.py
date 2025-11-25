
"""CDP FedCm Events"""

from client.events import CDPEvents
from typing import TypedDict, Optional, Callable
from protocol.fed_cm.events.types import *

class FedCmEvents:
    def __init__(self,events:CDPEvents):
        self.events=events
    
    def on_dialog_shown(self, callback: Callable[dialogShownEvent, None]=None) -> None:
        self.events.on('dialogShown', callback)
    
    def on_dialog_closed(self, callback: Callable[dialogClosedEvent, None]=None) -> None:
        """Triggered when a dialog is closed, either by user action, JS abort, or a command below."""
        self.events.on('dialogClosed', callback)
     