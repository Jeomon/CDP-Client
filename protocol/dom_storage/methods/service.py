
"""CDP DOMStorage Methods"""

from client.service import CDPClient
from typing import TypedDict,Optional
from protocol.dom_storage.methods.types import *

class DOMStorageMethods:
    def __init__(self, client:CDPClient):
        self.client = client

    async def clear(self, params: Optional[clearParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        return await self.client.send(method="DOMStorage.clear", params=params,session_id=session_id)

    async def disable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Disables storage tracking, prevents storage events from being sent to the client."""
        return await self.client.send(method="DOMStorage.disable", params=params,session_id=session_id)

    async def enable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Enables storage tracking, storage events will now be delivered to the client."""
        return await self.client.send(method="DOMStorage.enable", params=params,session_id=session_id)

    async def get_dom_storage_items(self, params: Optional[getDOMStorageItemsParameters]=None,session_id: Optional[str] = None) -> getDOMStorageItemsReturns:
        return await self.client.send(method="DOMStorage.getDOMStorageItems", params=params,session_id=session_id)

    async def remove_dom_storage_item(self, params: Optional[removeDOMStorageItemParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        return await self.client.send(method="DOMStorage.removeDOMStorageItem", params=params,session_id=session_id)

    async def set_dom_storage_item(self, params: Optional[setDOMStorageItemParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        return await self.client.send(method="DOMStorage.setDOMStorageItem", params=params,session_id=session_id)
