
"""CDP BackgroundService Events"""

from client.service import CDPClient
from typing import TypedDict, Optional, Callable
from protocol.background_service.events.types import *

class BackgroundServiceEvents:
    def __init__(self,client:CDPClient):
        self.client=client
    
    def on_recording_state_changed(self, callback: Callable[[recordingStateChangedEvent,Optional[str]], None]=None) -> None:
        """Called when the recording state for the service has been updated."""
        self.client.on('recordingStateChanged', callback)
    
    def on_background_service_event_received(self, callback: Callable[[backgroundServiceEventReceivedEvent,Optional[str]], None]=None) -> None:
        """Called with all existing backgroundServiceEvents when enabled, and all new events afterwards if enabled and recording."""
        self.client.on('backgroundServiceEventReceived', callback)
     