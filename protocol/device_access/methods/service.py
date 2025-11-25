
"""CDP DeviceAccess Methods"""

from client.methods import CDPMethods
from typing import TypedDict,Optional
from protocol.device_access.methods.types import *

class DeviceAccessMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def enable(self, params: None=None) -> Dict[str, Any]:
        """Enable events in this domain."""
        return await self.methods.send(method="DeviceAccess.enable", params=params)

    async def disable(self, params: None=None) -> Dict[str, Any]:
        """Disable events in this domain."""
        return await self.methods.send(method="DeviceAccess.disable", params=params)

    async def select_prompt(self, params: Optional[selectPromptParameters]=None) -> Dict[str, Any]:
        """Select a device in response to a DeviceAccess.deviceRequestPrompted event."""
        return await self.methods.send(method="DeviceAccess.selectPrompt", params=params)

    async def cancel_prompt(self, params: Optional[cancelPromptParameters]=None) -> Dict[str, Any]:
        """Cancel a prompt in response to a DeviceAccess.deviceRequestPrompted event."""
        return await self.methods.send(method="DeviceAccess.cancelPrompt", params=params)
