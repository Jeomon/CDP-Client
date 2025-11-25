
"""CDP Tracing Events"""

from client.service import CDPClient
from typing import TypedDict, Optional, Callable
from protocol.tracing.events.types import *

class TracingEvents:
    def __init__(self,client:CDPClient):
        self.client=client
    
    def on_buffer_usage(self, callback: Callable[[bufferUsageEvent,Optional[str]], None]=None) -> None:
        self.client.on('bufferUsage', callback)
    
    def on_data_collected(self, callback: Callable[[dataCollectedEvent,Optional[str]], None]=None) -> None:
        """Contains a bucket of collected trace events. When tracing is stopped collected events will be sent as a sequence of dataCollected events followed by tracingComplete event."""
        self.client.on('dataCollected', callback)
    
    def on_tracing_complete(self, callback: Callable[[tracingCompleteEvent,Optional[str]], None]=None) -> None:
        """Signals that tracing is stopped and there is no trace buffers pending flush, all data were delivered via dataCollected events."""
        self.client.on('tracingComplete', callback)
     