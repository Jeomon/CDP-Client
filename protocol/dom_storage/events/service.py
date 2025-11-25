
"""CDP DOMStorage Events"""

from client.service import CDPClient
from typing import TypedDict, Optional, Callable
from protocol.dom_storage.events.types import *

class DOMStorageEvents:
    def __init__(self,client:CDPClient):
        self.client=client
    
    def on_dom_storage_item_added(self, callback: Callable[[domStorageItemAddedEvent,Optional[str]], None]=None) -> None:
        self.client.on('DOMStorage.domStorageItemAdded', callback)
    
    def on_dom_storage_item_removed(self, callback: Callable[[domStorageItemRemovedEvent,Optional[str]], None]=None) -> None:
        self.client.on('DOMStorage.domStorageItemRemoved', callback)
    
    def on_dom_storage_item_updated(self, callback: Callable[[domStorageItemUpdatedEvent,Optional[str]], None]=None) -> None:
        self.client.on('DOMStorage.domStorageItemUpdated', callback)
    
    def on_dom_storage_items_cleared(self, callback: Callable[[domStorageItemsClearedEvent,Optional[str]], None]=None) -> None:
        self.client.on('DOMStorage.domStorageItemsCleared', callback)
     