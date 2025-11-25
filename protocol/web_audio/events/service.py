
"""CDP WebAudio Events"""

from client.events import CDPEvents
from typing import TypedDict, Optional, Callable
from protocol.web_audio.events.types import *

class WebAudioEvents:
    def __init__(self,events:CDPEvents):
        self.events=events
    
    def on_context_created(self, callback: Callable[[contextCreatedEvent,Optional[str]], None]=None) -> None:
        """Notifies that a new BaseAudioContext has been created."""
        self.events.on('contextCreated', callback)
    
    def on_context_will_be_destroyed(self, callback: Callable[[contextWillBeDestroyedEvent,Optional[str]], None]=None) -> None:
        """Notifies that an existing BaseAudioContext will be destroyed."""
        self.events.on('contextWillBeDestroyed', callback)
    
    def on_context_changed(self, callback: Callable[[contextChangedEvent,Optional[str]], None]=None) -> None:
        """Notifies that existing BaseAudioContext has changed some properties (id stays the same).."""
        self.events.on('contextChanged', callback)
    
    def on_audio_listener_created(self, callback: Callable[[audioListenerCreatedEvent,Optional[str]], None]=None) -> None:
        """Notifies that the construction of an AudioListener has finished."""
        self.events.on('audioListenerCreated', callback)
    
    def on_audio_listener_will_be_destroyed(self, callback: Callable[[audioListenerWillBeDestroyedEvent,Optional[str]], None]=None) -> None:
        """Notifies that a new AudioListener has been created."""
        self.events.on('audioListenerWillBeDestroyed', callback)
    
    def on_audio_node_created(self, callback: Callable[[audioNodeCreatedEvent,Optional[str]], None]=None) -> None:
        """Notifies that a new AudioNode has been created."""
        self.events.on('audioNodeCreated', callback)
    
    def on_audio_node_will_be_destroyed(self, callback: Callable[[audioNodeWillBeDestroyedEvent,Optional[str]], None]=None) -> None:
        """Notifies that an existing AudioNode has been destroyed."""
        self.events.on('audioNodeWillBeDestroyed', callback)
    
    def on_audio_param_created(self, callback: Callable[[audioParamCreatedEvent,Optional[str]], None]=None) -> None:
        """Notifies that a new AudioParam has been created."""
        self.events.on('audioParamCreated', callback)
    
    def on_audio_param_will_be_destroyed(self, callback: Callable[[audioParamWillBeDestroyedEvent,Optional[str]], None]=None) -> None:
        """Notifies that an existing AudioParam has been destroyed."""
        self.events.on('audioParamWillBeDestroyed', callback)
    
    def on_nodes_connected(self, callback: Callable[[nodesConnectedEvent,Optional[str]], None]=None) -> None:
        """Notifies that two AudioNodes are connected."""
        self.events.on('nodesConnected', callback)
    
    def on_nodes_disconnected(self, callback: Callable[[nodesDisconnectedEvent,Optional[str]], None]=None) -> None:
        """Notifies that AudioNodes are disconnected. The destination can be null, and it means all the outgoing connections from the source are disconnected."""
        self.events.on('nodesDisconnected', callback)
    
    def on_node_param_connected(self, callback: Callable[[nodeParamConnectedEvent,Optional[str]], None]=None) -> None:
        """Notifies that an AudioNode is connected to an AudioParam."""
        self.events.on('nodeParamConnected', callback)
    
    def on_node_param_disconnected(self, callback: Callable[[nodeParamDisconnectedEvent,Optional[str]], None]=None) -> None:
        """Notifies that an AudioNode is disconnected to an AudioParam."""
        self.events.on('nodeParamDisconnected', callback)
     