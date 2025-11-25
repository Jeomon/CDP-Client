
"""CDP SystemInfo Methods"""

from client.service import CDPClient
from typing import TypedDict,Optional
from protocol.system_info.methods.types import *

class SystemInfoMethods:
    def __init__(self, client:CDPClient):
        self.client = client

    async def get_info(self, params: None=None,session_id: Optional[str] = None) -> getInfoReturns:
        """Returns information about the system."""
        return await self.client.send(method="SystemInfo.getInfo", params=params,session_id=session_id)

    async def get_feature_state(self, params: Optional[getFeatureStateParameters]=None,session_id: Optional[str] = None) -> getFeatureStateReturns:
        """Returns information about the feature state."""
        return await self.client.send(method="SystemInfo.getFeatureState", params=params,session_id=session_id)

    async def get_process_info(self, params: None=None,session_id: Optional[str] = None) -> getProcessInfoReturns:
        """Returns information about all running processes."""
        return await self.client.send(method="SystemInfo.getProcessInfo", params=params,session_id=session_id)
