
"""CDP PerformanceTimeline Events"""

from client.events import CDPEvents
from typing import TypedDict, Optional, Callable
from protocol.performance_timeline.events.types import *

class PerformanceTimelineEvents:
    def __init__(self,events:CDPEvents):
        self.events=events
    
    def on_timeline_event_added(self, callback: Callable[[timelineEventAddedEvent,Optional[str]], None]=None) -> None:
        """Sent when a performance timeline event is added. See reportPerformanceTimeline method."""
        self.events.on('timelineEventAdded', callback)
     