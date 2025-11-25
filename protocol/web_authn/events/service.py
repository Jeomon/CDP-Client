
"""CDP WebAuthn Events"""

from client.events import CDPEvents
from typing import TypedDict, Optional, Callable
from protocol.web_authn.events.types import *

class WebAuthnEvents:
    def __init__(self,events:CDPEvents):
        self.events=events
    
    def on_credential_added(self, callback: Callable[[credentialAddedEvent,Optional[str]], None]=None) -> None:
        """Triggered when a credential is added to an authenticator."""
        self.events.on('credentialAdded', callback)
    
    def on_credential_deleted(self, callback: Callable[[credentialDeletedEvent,Optional[str]], None]=None) -> None:
        """Triggered when a credential is deleted, e.g. through PublicKeyCredential.signalUnknownCredential()."""
        self.events.on('credentialDeleted', callback)
    
    def on_credential_updated(self, callback: Callable[[credentialUpdatedEvent,Optional[str]], None]=None) -> None:
        """Triggered when a credential is updated, e.g. through PublicKeyCredential.signalCurrentUserDetails()."""
        self.events.on('credentialUpdated', callback)
    
    def on_credential_asserted(self, callback: Callable[[credentialAssertedEvent,Optional[str]], None]=None) -> None:
        """Triggered when a credential is used in a webauthn assertion."""
        self.events.on('credentialAsserted', callback)
     