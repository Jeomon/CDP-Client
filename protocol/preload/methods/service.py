
"""CDP Preload Methods"""

from client.methods import CDPMethods
from typing import TypedDict,Optional
from protocol.preload.methods.types import *

class PreloadMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def enable(self, params: None=None) -> Dict[str, Any]:
        return await self.methods.send(method="Preload.enable", params=params)

    async def disable(self, params: None=None) -> Dict[str, Any]:
        return await self.methods.send(method="Preload.disable", params=params)
