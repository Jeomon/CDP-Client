
"""CDP Tracing Events"""

from client.events import CDPEvents
from typing import TypedDict, Optional, Callable
from protocol.tracing.events.types import *

class TracingEvents:
    def __init__(self,events:CDPEvents):
        self.events=events
    
    def on_buffer_usage(self, callback: Callable[[bufferUsageEvent,Optional[str]], None]=None) -> None:
        self.events.on('bufferUsage', callback)
    
    def on_data_collected(self, callback: Callable[[dataCollectedEvent,Optional[str]], None]=None) -> None:
        """Contains a bucket of collected trace events. When tracing is stopped collected events will be sent as a sequence of dataCollected events followed by tracingComplete event."""
        self.events.on('dataCollected', callback)
    
    def on_tracing_complete(self, callback: Callable[[tracingCompleteEvent,Optional[str]], None]=None) -> None:
        """Signals that tracing is stopped and there is no trace buffers pending flush, all data were delivered via dataCollected events."""
        self.events.on('tracingComplete', callback)
     