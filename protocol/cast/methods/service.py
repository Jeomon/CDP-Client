
"""CDP Cast Methods"""

from client.methods import CDPMethods
from typing import TypedDict,Optional
from protocol.cast.methods.types import *

class CastMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def enable(self, params: Optional[enableParameters]=None) -> Dict[str, Any]:
        """Starts observing for sinks that can be used for tab mirroring, and if set, sinks compatible with |presentationUrl| as well. When sinks are found, a |sinksUpdated| event is fired. Also starts observing for issue messages. When an issue is added or removed, an |issueUpdated| event is fired."""
        return await self.methods.send(method="Cast.enable", params=params)

    async def disable(self, params: None=None) -> Dict[str, Any]:
        """Stops observing for sinks and issues."""
        return await self.methods.send(method="Cast.disable", params=params)

    async def set_sink_to_use(self, params: Optional[setSinkToUseParameters]=None) -> Dict[str, Any]:
        """Sets a sink to be used when the web page requests the browser to choose a sink via Presentation API, Remote Playback API, or Cast SDK."""
        return await self.methods.send(method="Cast.setSinkToUse", params=params)

    async def start_desktop_mirroring(self, params: Optional[startDesktopMirroringParameters]=None) -> Dict[str, Any]:
        """Starts mirroring the desktop to the sink."""
        return await self.methods.send(method="Cast.startDesktopMirroring", params=params)

    async def start_tab_mirroring(self, params: Optional[startTabMirroringParameters]=None) -> Dict[str, Any]:
        """Starts mirroring the tab to the sink."""
        return await self.methods.send(method="Cast.startTabMirroring", params=params)

    async def stop_casting(self, params: Optional[stopCastingParameters]=None) -> Dict[str, Any]:
        """Stops the active Cast session on the sink."""
        return await self.methods.send(method="Cast.stopCasting", params=params)
