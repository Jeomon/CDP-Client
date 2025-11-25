
"""CDP BackgroundService Methods"""

from client.service import CDPClient
from typing import TypedDict,Optional
from protocol.background_service.methods.types import *

class BackgroundServiceMethods:
    def __init__(self, client:CDPClient):
        self.client = client

    async def start_observing(self, params: Optional[startObservingParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Enables event updates for the service."""
        return await self.client.send(method="BackgroundService.startObserving", params=params,session_id=session_id)

    async def stop_observing(self, params: Optional[stopObservingParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Disables event updates for the service."""
        return await self.client.send(method="BackgroundService.stopObserving", params=params,session_id=session_id)

    async def set_recording(self, params: Optional[setRecordingParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Set the recording state for the service."""
        return await self.client.send(method="BackgroundService.setRecording", params=params,session_id=session_id)

    async def clear_events(self, params: Optional[clearEventsParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Clears all stored data for the service."""
        return await self.client.send(method="BackgroundService.clearEvents", params=params,session_id=session_id)
