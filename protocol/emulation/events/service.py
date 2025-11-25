
"""CDP Emulation Events"""

from client.events import CDPEvents
from typing import TypedDict, Optional, Callable
from protocol.emulation.events.types import *

class EmulationEvents:
    def __init__(self,events:CDPEvents):
        self.events=events
    
    def on_virtual_time_budget_expired(self, callback: Callable[virtualTimeBudgetExpiredEvent, None]=None) -> None:
        """Notification sent after the virtual time budget for the current VirtualTimePolicy has run out."""
        self.events.on('virtualTimeBudgetExpired', callback)
     