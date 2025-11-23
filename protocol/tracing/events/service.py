
"""CDP Tracing Events"""

from cdp_client.events import CDPEvents
from typing import TypedDict, Optional, Callable
from tracing.events.types import *

class TracingEvents:
    def __init__(self,events:CDPEvents):
        self.events=events
    
    def on_buffer_usage(self, callback: Callable[bufferUsageEvent, None]=None) -> None:
        self.events.on('bufferUsage', callback)
    
    def on_data_collected(self, callback: Callable[dataCollectedEvent, None]=None) -> None:
        """Contains a bucket of collected trace events. When tracing is stopped collected events will be sent as a sequence of dataCollected events followed by tracingComplete event."""
        self.events.on('dataCollected', callback)
    
    def on_tracing_complete(self, callback: Callable[tracingCompleteEvent, None]=None) -> None:
        """Signals that tracing is stopped and there is no trace buffers pending flush, all data were delivered via dataCollected events."""
        self.events.on('tracingComplete', callback)
     