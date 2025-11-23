
"""CDP DOMStorage Events"""

from cdp_client.events import CDPEvents
from typing import TypedDict, Optional, Callable
from dom_storage.events.types import *

class DOMStorageEvents:
    def __init__(self,events:CDPEvents):
        self.events=events
    
    def on_dom_storage_item_added(self, callback: Callable[domStorageItemAddedEvent, None]=None) -> None:
        self.events.on('domStorageItemAdded', callback)
    
    def on_dom_storage_item_removed(self, callback: Callable[domStorageItemRemovedEvent, None]=None) -> None:
        self.events.on('domStorageItemRemoved', callback)
    
    def on_dom_storage_item_updated(self, callback: Callable[domStorageItemUpdatedEvent, None]=None) -> None:
        self.events.on('domStorageItemUpdated', callback)
    
    def on_dom_storage_items_cleared(self, callback: Callable[domStorageItemsClearedEvent, None]=None) -> None:
        self.events.on('domStorageItemsCleared', callback)
     