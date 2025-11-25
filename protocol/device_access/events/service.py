
"""CDP DeviceAccess Events"""

from client.service import CDPClient
from typing import TypedDict, Optional, Callable
from protocol.device_access.events.types import *

class DeviceAccessEvents:
    def __init__(self,client:CDPClient):
        self.client=client
    
    def on_device_request_prompted(self, callback: Callable[[deviceRequestPromptedEvent,Optional[str]], None]=None) -> None:
        """A device request opened a user prompt to select a device. Respond with the selectPrompt or cancelPrompt command."""
        self.client.on('DeviceAccess.deviceRequestPrompted', callback)
     