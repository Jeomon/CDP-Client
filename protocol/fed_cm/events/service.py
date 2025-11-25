
"""CDP FedCm Events"""

from client.service import CDPClient
from typing import TypedDict, Optional, Callable
from protocol.fed_cm.events.types import *

class FedCmEvents:
    def __init__(self,client:CDPClient):
        self.client=client
    
    def on_dialog_shown(self, callback: Callable[[dialogShownEvent,Optional[str]], None]=None) -> None:
        self.client.on('FedCm.dialogShown', callback)
    
    def on_dialog_closed(self, callback: Callable[[dialogClosedEvent,Optional[str]], None]=None) -> None:
        """Triggered when a dialog is closed, either by user action, JS abort, or a command below."""
        self.client.on('FedCm.dialogClosed', callback)
     