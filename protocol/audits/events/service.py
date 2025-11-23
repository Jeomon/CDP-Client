
"""CDP Audits Events"""

from cdp_client.events import CDPEvents
from typing import TypedDict, Optional, Callable
from audits.events.types import *

class AuditsEvents:
    def __init__(self,events:CDPEvents):
        self.events=events
    
    def on_issue_added(self, callback: Callable[issueAddedEvent, None]=None) -> None:
        self.events.on('issueAdded', callback)
     