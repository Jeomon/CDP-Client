
"""CDP WebAuthn Events"""

from client.service import CDPClient
from typing import TypedDict, Optional, Callable
from protocol.web_authn.events.types import *

class WebAuthnEvents:
    def __init__(self,client:CDPClient):
        self.client=client
    
    def on_credential_added(self, callback: Callable[[credentialAddedEvent,Optional[str]], None]=None) -> None:
        """Triggered when a credential is added to an authenticator."""
        self.client.on('WebAuthn.credentialAdded', callback)
    
    def on_credential_deleted(self, callback: Callable[[credentialDeletedEvent,Optional[str]], None]=None) -> None:
        """Triggered when a credential is deleted, e.g. through PublicKeyCredential.signalUnknownCredential()."""
        self.client.on('WebAuthn.credentialDeleted', callback)
    
    def on_credential_updated(self, callback: Callable[[credentialUpdatedEvent,Optional[str]], None]=None) -> None:
        """Triggered when a credential is updated, e.g. through PublicKeyCredential.signalCurrentUserDetails()."""
        self.client.on('WebAuthn.credentialUpdated', callback)
    
    def on_credential_asserted(self, callback: Callable[[credentialAssertedEvent,Optional[str]], None]=None) -> None:
        """Triggered when a credential is used in a webauthn assertion."""
        self.client.on('WebAuthn.credentialAsserted', callback)
     