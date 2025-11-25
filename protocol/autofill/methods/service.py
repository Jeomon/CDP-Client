
"""CDP Autofill Methods"""

from client.methods import CDPMethods
from typing import TypedDict,Optional
from protocol.autofill.methods.types import *

class AutofillMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def trigger(self, params: Optional[triggerParameters]=None) -> Dict[str, Any]:
        """Trigger autofill on a form identified by the fieldId. If the field and related form cannot be autofilled, returns an error."""
        return await self.methods.send(method="Autofill.trigger", params=params)

    async def set_addresses(self, params: Optional[setAddressesParameters]=None) -> Dict[str, Any]:
        """Set addresses so that developers can verify their forms implementation."""
        return await self.methods.send(method="Autofill.setAddresses", params=params)

    async def disable(self, params: None=None) -> Dict[str, Any]:
        """Disables autofill domain notifications."""
        return await self.methods.send(method="Autofill.disable", params=params)

    async def enable(self, params: None=None) -> Dict[str, Any]:
        """Enables autofill domain notifications."""
        return await self.methods.send(method="Autofill.enable", params=params)
