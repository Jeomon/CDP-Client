
"""CDP PerformanceTimeline Events"""

from client.service import CDPClient
from typing import TypedDict, Optional, Callable
from protocol.performance_timeline.events.types import *

class PerformanceTimelineEvents:
    def __init__(self,client:CDPClient):
        self.client=client
    
    def on_timeline_event_added(self, callback: Callable[[timelineEventAddedEvent,Optional[str]], None]=None) -> None:
        """Sent when a performance timeline event is added. See reportPerformanceTimeline method."""
        self.client.on('timelineEventAdded', callback)
     