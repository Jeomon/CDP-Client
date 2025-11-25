
"""CDP Inspector Methods"""

from client.methods import CDPMethods
from typing import TypedDict,Optional
from protocol.inspector.methods.types import *

class InspectorMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def disable(self, params: None=None) -> Dict[str, Any]:
        """Disables inspector domain notifications."""
        return await self.methods.send(method="Inspector.disable", params=params)

    async def enable(self, params: None=None) -> Dict[str, Any]:
        """Enables inspector domain notifications."""
        return await self.methods.send(method="Inspector.enable", params=params)
