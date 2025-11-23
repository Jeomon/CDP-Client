
"""CDP DeviceOrientation Methods"""

from cdp_client.methods import CDPMethods
from typing import TypedDict,Optional
from device_orientation.methods.types import *

class DeviceOrientationMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def clear_device_orientation_override(self, params: None=None) -> Dict[str, Any]:
        """Clears the overridden Device Orientation."""
        return await self.methods.send(method="DeviceOrientation.clearDeviceOrientationOverride", params=params)

    async def set_device_orientation_override(self, params: Optional[setDeviceOrientationOverrideParameters]=None) -> Dict[str, Any]:
        """Overrides the Device Orientation."""
        return await self.methods.send(method="DeviceOrientation.setDeviceOrientationOverride", params=params)
