
"""CDP DOM Events"""

from cdp_client.events import CDPEvents
from typing import TypedDict, Optional, Callable
from dom.events.types import *

class DOMEvents:
    def __init__(self,events:CDPEvents):
        self.events=events
    
    def on_attribute_modified(self, callback: Callable[attributeModifiedEvent, None]=None) -> None:
        """Fired when `Element`'s attribute is modified."""
        self.events.on('attributeModified', callback)
    
    def on_attribute_removed(self, callback: Callable[attributeRemovedEvent, None]=None) -> None:
        """Fired when `Element`'s attribute is removed."""
        self.events.on('attributeRemoved', callback)
    
    def on_character_data_modified(self, callback: Callable[characterDataModifiedEvent, None]=None) -> None:
        """Mirrors `DOMCharacterDataModified` event."""
        self.events.on('characterDataModified', callback)
    
    def on_child_node_count_updated(self, callback: Callable[childNodeCountUpdatedEvent, None]=None) -> None:
        """Fired when `Container`'s child node count has changed."""
        self.events.on('childNodeCountUpdated', callback)
    
    def on_child_node_inserted(self, callback: Callable[childNodeInsertedEvent, None]=None) -> None:
        """Mirrors `DOMNodeInserted` event."""
        self.events.on('childNodeInserted', callback)
    
    def on_child_node_removed(self, callback: Callable[childNodeRemovedEvent, None]=None) -> None:
        """Mirrors `DOMNodeRemoved` event."""
        self.events.on('childNodeRemoved', callback)
    
    def on_distributed_nodes_updated(self, callback: Callable[distributedNodesUpdatedEvent, None]=None) -> None:
        """Called when distribution is changed."""
        self.events.on('distributedNodesUpdated', callback)
    
    def on_document_updated(self, callback: Callable[documentUpdatedEvent, None]=None) -> None:
        """Fired when `Document` has been totally updated. Node ids are no longer valid."""
        self.events.on('documentUpdated', callback)
    
    def on_inline_style_invalidated(self, callback: Callable[inlineStyleInvalidatedEvent, None]=None) -> None:
        """Fired when `Element`'s inline style is modified via a CSS property modification."""
        self.events.on('inlineStyleInvalidated', callback)
    
    def on_pseudo_element_added(self, callback: Callable[pseudoElementAddedEvent, None]=None) -> None:
        """Called when a pseudo element is added to an element."""
        self.events.on('pseudoElementAdded', callback)
    
    def on_top_layer_elements_updated(self, callback: Callable[topLayerElementsUpdatedEvent, None]=None) -> None:
        """Called when top layer elements are changed."""
        self.events.on('topLayerElementsUpdated', callback)
    
    def on_scrollable_flag_updated(self, callback: Callable[scrollableFlagUpdatedEvent, None]=None) -> None:
        """Fired when a node's scrollability state changes."""
        self.events.on('scrollableFlagUpdated', callback)
    
    def on_affected_by_starting_styles_flag_updated(self, callback: Callable[affectedByStartingStylesFlagUpdatedEvent, None]=None) -> None:
        """Fired when a node's starting styles changes."""
        self.events.on('affectedByStartingStylesFlagUpdated', callback)
    
    def on_pseudo_element_removed(self, callback: Callable[pseudoElementRemovedEvent, None]=None) -> None:
        """Called when a pseudo element is removed from an element."""
        self.events.on('pseudoElementRemoved', callback)
    
    def on_set_child_nodes(self, callback: Callable[setChildNodesEvent, None]=None) -> None:
        """Fired when backend wants to provide client with the missing DOM structure. This happens upon most of the calls requesting node ids."""
        self.events.on('setChildNodes', callback)
    
    def on_shadow_root_popped(self, callback: Callable[shadowRootPoppedEvent, None]=None) -> None:
        """Called when shadow root is popped from the element."""
        self.events.on('shadowRootPopped', callback)
    
    def on_shadow_root_pushed(self, callback: Callable[shadowRootPushedEvent, None]=None) -> None:
        """Called when shadow root is pushed into the element."""
        self.events.on('shadowRootPushed', callback)
     