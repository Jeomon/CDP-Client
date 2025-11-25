
"""CDP BackgroundService Methods"""

from client.methods import CDPMethods
from typing import TypedDict,Optional
from protocol.background_service.methods.types import *

class BackgroundServiceMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def start_observing(self, params: Optional[startObservingParameters]=None) -> Dict[str, Any]:
        """Enables event updates for the service."""
        return await self.methods.send(method="BackgroundService.startObserving", params=params)

    async def stop_observing(self, params: Optional[stopObservingParameters]=None) -> Dict[str, Any]:
        """Disables event updates for the service."""
        return await self.methods.send(method="BackgroundService.stopObserving", params=params)

    async def set_recording(self, params: Optional[setRecordingParameters]=None) -> Dict[str, Any]:
        """Set the recording state for the service."""
        return await self.methods.send(method="BackgroundService.setRecording", params=params)

    async def clear_events(self, params: Optional[clearEventsParameters]=None) -> Dict[str, Any]:
        """Clears all stored data for the service."""
        return await self.methods.send(method="BackgroundService.clearEvents", params=params)
