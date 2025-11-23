
"""CDP Animation Events"""

from cdp_client.events import CDPEvents
from typing import TypedDict, Optional, Callable
from animation.events.types import *

class AnimationEvents:
    def __init__(self,events:CDPEvents):
        self.events=events
    
    def on_animation_canceled(self, callback: Callable[animationCanceledEvent, None]=None) -> None:
        """Event for when an animation has been cancelled."""
        self.events.on('animationCanceled', callback)
    
    def on_animation_created(self, callback: Callable[animationCreatedEvent, None]=None) -> None:
        """Event for each animation that has been created."""
        self.events.on('animationCreated', callback)
    
    def on_animation_started(self, callback: Callable[animationStartedEvent, None]=None) -> None:
        """Event for animation that has been started."""
        self.events.on('animationStarted', callback)
    
    def on_animation_updated(self, callback: Callable[animationUpdatedEvent, None]=None) -> None:
        """Event for animation that has been updated."""
        self.events.on('animationUpdated', callback)
     