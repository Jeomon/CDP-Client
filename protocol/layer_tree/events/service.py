
"""CDP LayerTree Events"""

from cdp_client.events import CDPEvents
from typing import TypedDict, Optional, Callable
from layer_tree.events.types import *

class LayerTreeEvents:
    def __init__(self,events:CDPEvents):
        self.events=events
    
    def on_layer_painted(self, callback: Callable[layerPaintedEvent, None]=None) -> None:
        self.events.on('layerPainted', callback)
    
    def on_layer_tree_did_change(self, callback: Callable[layerTreeDidChangeEvent, None]=None) -> None:
        self.events.on('layerTreeDidChange', callback)
     