
"""CDP DeviceAccess Events"""

from client.events import CDPEvents
from typing import TypedDict, Optional, Callable
from protocol.device_access.events.types import *

class DeviceAccessEvents:
    def __init__(self,events:CDPEvents):
        self.events=events
    
    def on_device_request_prompted(self, callback: Callable[deviceRequestPromptedEvent, None]=None) -> None:
        """A device request opened a user prompt to select a device. Respond with the selectPrompt or cancelPrompt command."""
        self.events.on('deviceRequestPrompted', callback)
     