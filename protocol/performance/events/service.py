
"""CDP Performance Events"""

from cdp_client.events import CDPEvents
from typing import TypedDict, Optional, Callable
from performance.events.types import *

class PerformanceEvents:
    def __init__(self,events:CDPEvents):
        self.events=events
    
    def on_metrics(self, callback: Callable[metricsEvent, None]=None) -> None:
        """Current values of the metrics."""
        self.events.on('metrics', callback)
     