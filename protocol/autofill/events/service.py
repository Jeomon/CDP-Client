
"""CDP Autofill Events"""

from client.events import CDPEvents
from typing import TypedDict, Optional, Callable
from protocol.autofill.events.types import *

class AutofillEvents:
    def __init__(self,events:CDPEvents):
        self.events=events
    
    def on_address_form_filled(self, callback: Callable[addressFormFilledEvent, None]=None) -> None:
        """Emitted when an address form is filled."""
        self.events.on('addressFormFilled', callback)
     