
"""CDP Target Events"""

from client.events import CDPEvents
from typing import TypedDict, Optional, Callable
from protocol.target.events.types import *

class TargetEvents:
    def __init__(self,events:CDPEvents):
        self.events=events
    
    def on_attached_to_target(self, callback: Callable[attachedToTargetEvent, None]=None) -> None:
        """Issued when attached to target because of auto-attach or `attachToTarget` command."""
        self.events.on('attachedToTarget', callback)
    
    def on_detached_from_target(self, callback: Callable[detachedFromTargetEvent, None]=None) -> None:
        """Issued when detached from target for any reason (including `detachFromTarget` command). Can be issued multiple times per target if multiple sessions have been attached to it."""
        self.events.on('detachedFromTarget', callback)
    
    def on_received_message_from_target(self, callback: Callable[receivedMessageFromTargetEvent, None]=None) -> None:
        """Notifies about a new protocol message received from the session (as reported in `attachedToTarget` event)."""
        self.events.on('receivedMessageFromTarget', callback)
    
    def on_target_created(self, callback: Callable[targetCreatedEvent, None]=None) -> None:
        """Issued when a possible inspection target is created."""
        self.events.on('targetCreated', callback)
    
    def on_target_destroyed(self, callback: Callable[targetDestroyedEvent, None]=None) -> None:
        """Issued when a target is destroyed."""
        self.events.on('targetDestroyed', callback)
    
    def on_target_crashed(self, callback: Callable[targetCrashedEvent, None]=None) -> None:
        """Issued when a target has crashed."""
        self.events.on('targetCrashed', callback)
    
    def on_target_info_changed(self, callback: Callable[targetInfoChangedEvent, None]=None) -> None:
        """Issued when some information about a target has changed. This only happens between `targetCreated` and `targetDestroyed`."""
        self.events.on('targetInfoChanged', callback)
     