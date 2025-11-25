
"""CDP Target Events"""

from client.service import CDPClient
from typing import TypedDict, Optional, Callable
from protocol.target.events.types import *

class TargetEvents:
    def __init__(self,client:CDPClient):
        self.client=client
    
    def on_attached_to_target(self, callback: Callable[[attachedToTargetEvent,Optional[str]], None]=None) -> None:
        """Issued when attached to target because of auto-attach or `attachToTarget` command."""
        self.client.on('attachedToTarget', callback)
    
    def on_detached_from_target(self, callback: Callable[[detachedFromTargetEvent,Optional[str]], None]=None) -> None:
        """Issued when detached from target for any reason (including `detachFromTarget` command). Can be issued multiple times per target if multiple sessions have been attached to it."""
        self.client.on('detachedFromTarget', callback)
    
    def on_received_message_from_target(self, callback: Callable[[receivedMessageFromTargetEvent,Optional[str]], None]=None) -> None:
        """Notifies about a new protocol message received from the session (as reported in `attachedToTarget` event)."""
        self.client.on('receivedMessageFromTarget', callback)
    
    def on_target_created(self, callback: Callable[[targetCreatedEvent,Optional[str]], None]=None) -> None:
        """Issued when a possible inspection target is created."""
        self.client.on('targetCreated', callback)
    
    def on_target_destroyed(self, callback: Callable[[targetDestroyedEvent,Optional[str]], None]=None) -> None:
        """Issued when a target is destroyed."""
        self.client.on('targetDestroyed', callback)
    
    def on_target_crashed(self, callback: Callable[[targetCrashedEvent,Optional[str]], None]=None) -> None:
        """Issued when a target has crashed."""
        self.client.on('targetCrashed', callback)
    
    def on_target_info_changed(self, callback: Callable[[targetInfoChangedEvent,Optional[str]], None]=None) -> None:
        """Issued when some information about a target has changed. This only happens between `targetCreated` and `targetDestroyed`."""
        self.client.on('targetInfoChanged', callback)
     