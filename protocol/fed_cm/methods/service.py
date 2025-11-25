
"""CDP FedCm Methods"""

from client.service import CDPClient
from typing import TypedDict,Optional
from protocol.fed_cm.methods.types import *

class FedCmMethods:
    def __init__(self, client:CDPClient):
        self.client = client

    async def enable(self, params: Optional[enableParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        return await self.client.send(method="FedCm.enable", params=params,session_id=session_id)

    async def disable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        return await self.client.send(method="FedCm.disable", params=params,session_id=session_id)

    async def select_account(self, params: Optional[selectAccountParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        return await self.client.send(method="FedCm.selectAccount", params=params,session_id=session_id)

    async def click_dialog_button(self, params: Optional[clickDialogButtonParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        return await self.client.send(method="FedCm.clickDialogButton", params=params,session_id=session_id)

    async def open_url(self, params: Optional[openUrlParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        return await self.client.send(method="FedCm.openUrl", params=params,session_id=session_id)

    async def dismiss_dialog(self, params: Optional[dismissDialogParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        return await self.client.send(method="FedCm.dismissDialog", params=params,session_id=session_id)

    async def reset_cooldown(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Resets the cooldown time, if any, to allow the next FedCM call to show a dialog even if one was recently dismissed by the user."""
        return await self.client.send(method="FedCm.resetCooldown", params=params,session_id=session_id)
