
"""CDP Audits Events"""

from client.service import CDPClient
from typing import TypedDict, Optional, Callable
from protocol.audits.events.types import *

class AuditsEvents:
    def __init__(self,client:CDPClient):
        self.client=client
    
    def on_issue_added(self, callback: Callable[[issueAddedEvent,Optional[str]], None]=None) -> None:
        self.client.on('Audits.issueAdded', callback)
     