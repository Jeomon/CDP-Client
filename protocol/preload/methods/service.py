
"""CDP Preload Methods"""

from client.service import CDPClient
from typing import TypedDict,Optional
from protocol.preload.methods.types import *

class PreloadMethods:
    def __init__(self, client:CDPClient):
        self.client = client

    async def enable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        return await self.client.send(method="Preload.enable", params=params,session_id=session_id)

    async def disable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        return await self.client.send(method="Preload.disable", params=params,session_id=session_id)
