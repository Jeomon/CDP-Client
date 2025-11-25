
"""CDP SystemInfo Methods"""

from client.methods import CDPMethods
from typing import TypedDict,Optional
from protocol.system_info.methods.types import *

class SystemInfoMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def get_info(self, params: None=None) -> getInfoReturns:
        """Returns information about the system."""
        return await self.methods.send(method="SystemInfo.getInfo", params=params)

    async def get_feature_state(self, params: Optional[getFeatureStateParameters]=None) -> getFeatureStateReturns:
        """Returns information about the feature state."""
        return await self.methods.send(method="SystemInfo.getFeatureState", params=params)

    async def get_process_info(self, params: None=None) -> getProcessInfoReturns:
        """Returns information about all running processes."""
        return await self.methods.send(method="SystemInfo.getProcessInfo", params=params)
