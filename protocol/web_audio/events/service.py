
"""CDP WebAudio Events"""

from client.service import CDPClient
from typing import TypedDict, Optional, Callable
from protocol.web_audio.events.types import *

class WebAudioEvents:
    def __init__(self,client:CDPClient):
        self.client=client
    
    def on_context_created(self, callback: Callable[[contextCreatedEvent,Optional[str]], None]=None) -> None:
        """Notifies that a new BaseAudioContext has been created."""
        self.client.on('WebAudio.contextCreated', callback)
    
    def on_context_will_be_destroyed(self, callback: Callable[[contextWillBeDestroyedEvent,Optional[str]], None]=None) -> None:
        """Notifies that an existing BaseAudioContext will be destroyed."""
        self.client.on('WebAudio.contextWillBeDestroyed', callback)
    
    def on_context_changed(self, callback: Callable[[contextChangedEvent,Optional[str]], None]=None) -> None:
        """Notifies that existing BaseAudioContext has changed some properties (id stays the same).."""
        self.client.on('WebAudio.contextChanged', callback)
    
    def on_audio_listener_created(self, callback: Callable[[audioListenerCreatedEvent,Optional[str]], None]=None) -> None:
        """Notifies that the construction of an AudioListener has finished."""
        self.client.on('WebAudio.audioListenerCreated', callback)
    
    def on_audio_listener_will_be_destroyed(self, callback: Callable[[audioListenerWillBeDestroyedEvent,Optional[str]], None]=None) -> None:
        """Notifies that a new AudioListener has been created."""
        self.client.on('WebAudio.audioListenerWillBeDestroyed', callback)
    
    def on_audio_node_created(self, callback: Callable[[audioNodeCreatedEvent,Optional[str]], None]=None) -> None:
        """Notifies that a new AudioNode has been created."""
        self.client.on('WebAudio.audioNodeCreated', callback)
    
    def on_audio_node_will_be_destroyed(self, callback: Callable[[audioNodeWillBeDestroyedEvent,Optional[str]], None]=None) -> None:
        """Notifies that an existing AudioNode has been destroyed."""
        self.client.on('WebAudio.audioNodeWillBeDestroyed', callback)
    
    def on_audio_param_created(self, callback: Callable[[audioParamCreatedEvent,Optional[str]], None]=None) -> None:
        """Notifies that a new AudioParam has been created."""
        self.client.on('WebAudio.audioParamCreated', callback)
    
    def on_audio_param_will_be_destroyed(self, callback: Callable[[audioParamWillBeDestroyedEvent,Optional[str]], None]=None) -> None:
        """Notifies that an existing AudioParam has been destroyed."""
        self.client.on('WebAudio.audioParamWillBeDestroyed', callback)
    
    def on_nodes_connected(self, callback: Callable[[nodesConnectedEvent,Optional[str]], None]=None) -> None:
        """Notifies that two AudioNodes are connected."""
        self.client.on('WebAudio.nodesConnected', callback)
    
    def on_nodes_disconnected(self, callback: Callable[[nodesDisconnectedEvent,Optional[str]], None]=None) -> None:
        """Notifies that AudioNodes are disconnected. The destination can be null, and it means all the outgoing connections from the source are disconnected."""
        self.client.on('WebAudio.nodesDisconnected', callback)
    
    def on_node_param_connected(self, callback: Callable[[nodeParamConnectedEvent,Optional[str]], None]=None) -> None:
        """Notifies that an AudioNode is connected to an AudioParam."""
        self.client.on('WebAudio.nodeParamConnected', callback)
    
    def on_node_param_disconnected(self, callback: Callable[[nodeParamDisconnectedEvent,Optional[str]], None]=None) -> None:
        """Notifies that an AudioNode is disconnected to an AudioParam."""
        self.client.on('WebAudio.nodeParamDisconnected', callback)
     