
"""CDP Cast Methods"""

from client.methods import CDPMethods
from typing import TypedDict,Optional
from protocol.cast.methods.types import *

class CastMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def enable(self, params: Optional[enableParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Starts observing for sinks that can be used for tab mirroring, and if set, sinks compatible with |presentationUrl| as well. When sinks are found, a |sinksUpdated| event is fired. Also starts observing for issue messages. When an issue is added or removed, an |issueUpdated| event is fired."""
        return await self.methods.send(method="Cast.enable", params=params,session_id=session_id)

    async def disable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Stops observing for sinks and issues."""
        return await self.methods.send(method="Cast.disable", params=params,session_id=session_id)

    async def set_sink_to_use(self, params: Optional[setSinkToUseParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Sets a sink to be used when the web page requests the browser to choose a sink via Presentation API, Remote Playback API, or Cast SDK."""
        return await self.methods.send(method="Cast.setSinkToUse", params=params,session_id=session_id)

    async def start_desktop_mirroring(self, params: Optional[startDesktopMirroringParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Starts mirroring the desktop to the sink."""
        return await self.methods.send(method="Cast.startDesktopMirroring", params=params,session_id=session_id)

    async def start_tab_mirroring(self, params: Optional[startTabMirroringParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Starts mirroring the tab to the sink."""
        return await self.methods.send(method="Cast.startTabMirroring", params=params,session_id=session_id)

    async def stop_casting(self, params: Optional[stopCastingParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Stops the active Cast session on the sink."""
        return await self.methods.send(method="Cast.stopCasting", params=params,session_id=session_id)
