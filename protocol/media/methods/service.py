
"""CDP Media Methods"""

from client.methods import CDPMethods
from typing import TypedDict,Optional
from protocol.media.methods.types import *

class MediaMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def enable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Enables the Media domain"""
        return await self.methods.send(method="Media.enable", params=params,session_id=session_id)

    async def disable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Disables the Media domain."""
        return await self.methods.send(method="Media.disable", params=params,session_id=session_id)
