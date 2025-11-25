
"""CDP DeviceOrientation Methods"""

from client.service import CDPClient
from typing import TypedDict,Optional
from protocol.device_orientation.methods.types import *

class DeviceOrientationMethods:
    def __init__(self, client:CDPClient):
        self.client = client

    async def clear_device_orientation_override(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Clears the overridden Device Orientation."""
        return await self.client.send(method="DeviceOrientation.clearDeviceOrientationOverride", params=params,session_id=session_id)

    async def set_device_orientation_override(self, params: Optional[setDeviceOrientationOverrideParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Overrides the Device Orientation."""
        return await self.client.send(method="DeviceOrientation.setDeviceOrientationOverride", params=params,session_id=session_id)
