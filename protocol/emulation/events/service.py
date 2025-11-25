
"""CDP Emulation Events"""

from client.service import CDPClient
from typing import TypedDict, Optional, Callable
from protocol.emulation.events.types import *

class EmulationEvents:
    def __init__(self,client:CDPClient):
        self.client=client
    
    def on_virtual_time_budget_expired(self, callback: Callable[[virtualTimeBudgetExpiredEvent,Optional[str]], None]=None) -> None:
        """Notification sent after the virtual time budget for the current VirtualTimePolicy has run out."""
        self.client.on('Emulation.virtualTimeBudgetExpired', callback)
     