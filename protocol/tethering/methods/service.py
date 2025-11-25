
"""CDP Tethering Methods"""

from client.service import CDPClient
from typing import TypedDict,Optional
from protocol.tethering.methods.types import *

class TetheringMethods:
    def __init__(self, client:CDPClient):
        self.client = client

    async def bind(self, params: Optional[bindParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Request browser port binding."""
        return await self.client.send(method="Tethering.bind", params=params,session_id=session_id)

    async def unbind(self, params: Optional[unbindParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Request browser port unbinding."""
        return await self.client.send(method="Tethering.unbind", params=params,session_id=session_id)
