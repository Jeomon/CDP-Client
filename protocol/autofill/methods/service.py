
"""CDP Autofill Methods"""

from client.service import CDPClient
from typing import TypedDict,Optional
from protocol.autofill.methods.types import *

class AutofillMethods:
    def __init__(self, client:CDPClient):
        self.client = client

    async def trigger(self, params: Optional[triggerParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Trigger autofill on a form identified by the fieldId. If the field and related form cannot be autofilled, returns an error."""
        return await self.client.send(method="Autofill.trigger", params=params,session_id=session_id)

    async def set_addresses(self, params: Optional[setAddressesParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Set addresses so that developers can verify their forms implementation."""
        return await self.client.send(method="Autofill.setAddresses", params=params,session_id=session_id)

    async def disable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Disables autofill domain notifications."""
        return await self.client.send(method="Autofill.disable", params=params,session_id=session_id)

    async def enable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Enables autofill domain notifications."""
        return await self.client.send(method="Autofill.enable", params=params,session_id=session_id)
