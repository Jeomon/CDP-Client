
"""CDP Inspector Methods"""

from client.service import CDPClient
from typing import TypedDict,Optional
from protocol.inspector.methods.types import *

class InspectorMethods:
    def __init__(self, client:CDPClient):
        self.client = client

    async def disable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Disables inspector domain notifications."""
        return await self.client.send(method="Inspector.disable", params=params,session_id=session_id)

    async def enable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Enables inspector domain notifications."""
        return await self.client.send(method="Inspector.enable", params=params,session_id=session_id)
