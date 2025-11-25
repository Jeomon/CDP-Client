
"""CDP WebAudio Methods"""

from client.methods import CDPMethods
from typing import TypedDict,Optional
from protocol.web_audio.methods.types import *

class WebAudioMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def enable(self, params: None=None) -> Dict[str, Any]:
        """Enables the WebAudio domain and starts sending context lifetime events."""
        return await self.methods.send(method="WebAudio.enable", params=params)

    async def disable(self, params: None=None) -> Dict[str, Any]:
        """Disables the WebAudio domain."""
        return await self.methods.send(method="WebAudio.disable", params=params)

    async def get_realtime_data(self, params: Optional[getRealtimeDataParameters]=None) -> getRealtimeDataReturns:
        """Fetch the realtime data from the registered contexts."""
        return await self.methods.send(method="WebAudio.getRealtimeData", params=params)
