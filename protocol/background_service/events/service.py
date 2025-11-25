
"""CDP BackgroundService Events"""

from client.events import CDPEvents
from typing import TypedDict, Optional, Callable
from protocol.background_service.events.types import *

class BackgroundServiceEvents:
    def __init__(self,events:CDPEvents):
        self.events=events
    
    def on_recording_state_changed(self, callback: Callable[[recordingStateChangedEvent,Optional[str]], None]=None) -> None:
        """Called when the recording state for the service has been updated."""
        self.events.on('recordingStateChanged', callback)
    
    def on_background_service_event_received(self, callback: Callable[[backgroundServiceEventReceivedEvent,Optional[str]], None]=None) -> None:
        """Called with all existing backgroundServiceEvents when enabled, and all new events afterwards if enabled and recording."""
        self.events.on('backgroundServiceEventReceived', callback)
     