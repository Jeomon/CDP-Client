
"""CDP FedCm Methods"""

from client.methods import CDPMethods
from typing import TypedDict,Optional
from protocol.fed_cm.methods.types import *

class FedCmMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def enable(self, params: Optional[enableParameters]=None) -> Dict[str, Any]:
        return await self.methods.send(method="FedCm.enable", params=params)

    async def disable(self, params: None=None) -> Dict[str, Any]:
        return await self.methods.send(method="FedCm.disable", params=params)

    async def select_account(self, params: Optional[selectAccountParameters]=None) -> Dict[str, Any]:
        return await self.methods.send(method="FedCm.selectAccount", params=params)

    async def click_dialog_button(self, params: Optional[clickDialogButtonParameters]=None) -> Dict[str, Any]:
        return await self.methods.send(method="FedCm.clickDialogButton", params=params)

    async def open_url(self, params: Optional[openUrlParameters]=None) -> Dict[str, Any]:
        return await self.methods.send(method="FedCm.openUrl", params=params)

    async def dismiss_dialog(self, params: Optional[dismissDialogParameters]=None) -> Dict[str, Any]:
        return await self.methods.send(method="FedCm.dismissDialog", params=params)

    async def reset_cooldown(self, params: None=None) -> Dict[str, Any]:
        """Resets the cooldown time, if any, to allow the next FedCM call to show a dialog even if one was recently dismissed by the user."""
        return await self.methods.send(method="FedCm.resetCooldown", params=params)
