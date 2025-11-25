
"""CDP Autofill Events"""

from client.service import CDPClient
from typing import TypedDict, Optional, Callable
from protocol.autofill.events.types import *

class AutofillEvents:
    def __init__(self,client:CDPClient):
        self.client=client
    
    def on_address_form_filled(self, callback: Callable[[addressFormFilledEvent,Optional[str]], None]=None) -> None:
        """Emitted when an address form is filled."""
        self.client.on('addressFormFilled', callback)
     