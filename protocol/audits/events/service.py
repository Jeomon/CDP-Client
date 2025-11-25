
"""CDP Audits Events"""

from client.events import CDPEvents
from typing import TypedDict, Optional, Callable
from protocol.audits.events.types import *

class AuditsEvents:
    def __init__(self,events:CDPEvents):
        self.events=events
    
    def on_issue_added(self, callback: Callable[[issueAddedEvent,Optional[str]], None]=None) -> None:
        self.events.on('issueAdded', callback)
     