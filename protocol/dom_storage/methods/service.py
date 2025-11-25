
"""CDP DOMStorage Methods"""

from client.methods import CDPMethods
from typing import TypedDict,Optional
from protocol.dom_storage.methods.types import *

class DOMStorageMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def clear(self, params: Optional[clearParameters]=None) -> Dict[str, Any]:
        return await self.methods.send(method="DOMStorage.clear", params=params)

    async def disable(self, params: None=None) -> Dict[str, Any]:
        """Disables storage tracking, prevents storage events from being sent to the client."""
        return await self.methods.send(method="DOMStorage.disable", params=params)

    async def enable(self, params: None=None) -> Dict[str, Any]:
        """Enables storage tracking, storage events will now be delivered to the client."""
        return await self.methods.send(method="DOMStorage.enable", params=params)

    async def get_dom_storage_items(self, params: Optional[getDOMStorageItemsParameters]=None) -> getDOMStorageItemsReturns:
        return await self.methods.send(method="DOMStorage.getDOMStorageItems", params=params)

    async def remove_dom_storage_item(self, params: Optional[removeDOMStorageItemParameters]=None) -> Dict[str, Any]:
        return await self.methods.send(method="DOMStorage.removeDOMStorageItem", params=params)

    async def set_dom_storage_item(self, params: Optional[setDOMStorageItemParameters]=None) -> Dict[str, Any]:
        return await self.methods.send(method="DOMStorage.setDOMStorageItem", params=params)
