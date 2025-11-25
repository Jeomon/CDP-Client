
"""CDP Performance Events"""

from client.events import CDPEvents
from typing import TypedDict, Optional, Callable
from protocol.performance.events.types import *

class PerformanceEvents:
    def __init__(self,events:CDPEvents):
        self.events=events
    
    def on_metrics(self, callback: Callable[[metricsEvent,Optional[str]], None]=None) -> None:
        """Current values of the metrics."""
        self.events.on('metrics', callback)
     