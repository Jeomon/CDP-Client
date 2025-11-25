
"""CDP Preload Methods"""

from client.methods import CDPMethods
from typing import TypedDict,Optional
from protocol.preload.methods.types import *

class PreloadMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def enable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        return await self.methods.send(method="Preload.enable", params=params,session_id=session_id)

    async def disable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        return await self.methods.send(method="Preload.disable", params=params,session_id=session_id)
