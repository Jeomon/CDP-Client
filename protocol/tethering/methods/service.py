
"""CDP Tethering Methods"""

from client.methods import CDPMethods
from typing import TypedDict,Optional
from protocol.tethering.methods.types import *

class TetheringMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def bind(self, params: Optional[bindParameters]=None) -> Dict[str, Any]:
        """Request browser port binding."""
        return await self.methods.send(method="Tethering.bind", params=params)

    async def unbind(self, params: Optional[unbindParameters]=None) -> Dict[str, Any]:
        """Request browser port unbinding."""
        return await self.methods.send(method="Tethering.unbind", params=params)
