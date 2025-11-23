
"""CDP PerformanceTimeline Events"""

from cdp_client.events import CDPEvents
from typing import TypedDict, Optional, Callable
from performance_timeline.events.types import *

class PerformanceTimelineEvents:
    def __init__(self,events:CDPEvents):
        self.events=events
    
    def on_timeline_event_added(self, callback: Callable[timelineEventAddedEvent, None]=None) -> None:
        """Sent when a performance timeline event is added. See reportPerformanceTimeline method."""
        self.events.on('timelineEventAdded', callback)
     