
"""CDP Security Events"""

from client.events import CDPEvents
from typing import TypedDict, Optional, Callable
from protocol.security.events.types import *

class SecurityEvents:
    def __init__(self,events:CDPEvents):
        self.events=events
    
    def on_certificate_error(self, callback: Callable[[certificateErrorEvent,Optional[str]], None]=None) -> None:
        """There is a certificate error. If overriding certificate errors is enabled, then it should be handled with the `handleCertificateError` command. Note: this event does not fire if the certificate error has been allowed internally. Only one client per target should override certificate errors at the same time."""
        self.events.on('certificateError', callback)
    
    def on_visible_security_state_changed(self, callback: Callable[[visibleSecurityStateChangedEvent,Optional[str]], None]=None) -> None:
        """The security state of the page changed."""
        self.events.on('visibleSecurityStateChanged', callback)
    
    def on_security_state_changed(self, callback: Callable[[securityStateChangedEvent,Optional[str]], None]=None) -> None:
        """The security state of the page changed. No longer being sent."""
        self.events.on('securityStateChanged', callback)
     