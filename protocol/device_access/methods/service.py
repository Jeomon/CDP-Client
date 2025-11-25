
"""CDP DeviceAccess Methods"""

from client.service import CDPClient
from typing import TypedDict,Optional
from protocol.device_access.methods.types import *

class DeviceAccessMethods:
    def __init__(self, client:CDPClient):
        self.client = client

    async def enable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Enable events in this domain."""
        return await self.client.send(method="DeviceAccess.enable", params=params,session_id=session_id)

    async def disable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Disable events in this domain."""
        return await self.client.send(method="DeviceAccess.disable", params=params,session_id=session_id)

    async def select_prompt(self, params: Optional[selectPromptParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Select a device in response to a DeviceAccess.deviceRequestPrompted event."""
        return await self.client.send(method="DeviceAccess.selectPrompt", params=params,session_id=session_id)

    async def cancel_prompt(self, params: Optional[cancelPromptParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Cancel a prompt in response to a DeviceAccess.deviceRequestPrompted event."""
        return await self.client.send(method="DeviceAccess.cancelPrompt", params=params,session_id=session_id)
