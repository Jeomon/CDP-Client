
"""CDP DOMStorage Events"""

from client.events import CDPEvents
from typing import TypedDict, Optional, Callable
from protocol.dom_storage.events.types import *

class DOMStorageEvents:
    def __init__(self,events:CDPEvents):
        self.events=events
    
    def on_dom_storage_item_added(self, callback: Callable[[domStorageItemAddedEvent,Optional[str]], None]=None) -> None:
        self.events.on('domStorageItemAdded', callback)
    
    def on_dom_storage_item_removed(self, callback: Callable[[domStorageItemRemovedEvent,Optional[str]], None]=None) -> None:
        self.events.on('domStorageItemRemoved', callback)
    
    def on_dom_storage_item_updated(self, callback: Callable[[domStorageItemUpdatedEvent,Optional[str]], None]=None) -> None:
        self.events.on('domStorageItemUpdated', callback)
    
    def on_dom_storage_items_cleared(self, callback: Callable[[domStorageItemsClearedEvent,Optional[str]], None]=None) -> None:
        self.events.on('domStorageItemsCleared', callback)
     