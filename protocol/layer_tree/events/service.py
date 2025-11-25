
"""CDP LayerTree Events"""

from client.service import CDPClient
from typing import TypedDict, Optional, Callable
from protocol.layer_tree.events.types import *

class LayerTreeEvents:
    def __init__(self,client:CDPClient):
        self.client=client
    
    def on_layer_painted(self, callback: Callable[[layerPaintedEvent,Optional[str]], None]=None) -> None:
        self.client.on('LayerTree.layerPainted', callback)
    
    def on_layer_tree_did_change(self, callback: Callable[[layerTreeDidChangeEvent,Optional[str]], None]=None) -> None:
        self.client.on('LayerTree.layerTreeDidChange', callback)
     