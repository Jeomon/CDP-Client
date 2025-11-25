
"""CDP Animation Events"""

from client.service import CDPClient
from typing import TypedDict, Optional, Callable
from protocol.animation.events.types import *

class AnimationEvents:
    def __init__(self,client:CDPClient):
        self.client=client
    
    def on_animation_canceled(self, callback: Callable[[animationCanceledEvent,Optional[str]], None]=None) -> None:
        """Event for when an animation has been cancelled."""
        self.client.on('animationCanceled', callback)
    
    def on_animation_created(self, callback: Callable[[animationCreatedEvent,Optional[str]], None]=None) -> None:
        """Event for each animation that has been created."""
        self.client.on('animationCreated', callback)
    
    def on_animation_started(self, callback: Callable[[animationStartedEvent,Optional[str]], None]=None) -> None:
        """Event for animation that has been started."""
        self.client.on('animationStarted', callback)
    
    def on_animation_updated(self, callback: Callable[[animationUpdatedEvent,Optional[str]], None]=None) -> None:
        """Event for animation that has been updated."""
        self.client.on('animationUpdated', callback)
     