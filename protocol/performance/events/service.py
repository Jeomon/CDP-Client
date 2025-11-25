
"""CDP Performance Events"""

from client.service import CDPClient
from typing import TypedDict, Optional, Callable
from protocol.performance.events.types import *

class PerformanceEvents:
    def __init__(self,client:CDPClient):
        self.client=client
    
    def on_metrics(self, callback: Callable[[metricsEvent,Optional[str]], None]=None) -> None:
        """Current values of the metrics."""
        self.client.on('metrics', callback)
     