
"""CDP Cast Events"""

from cdp_client.events import CDPEvents
from typing import TypedDict, Optional, Callable
from cast.events.types import *

class CastEvents:
    def __init__(self,events:CDPEvents):
        self.events=events
    
    def on_sinks_updated(self, callback: Callable[sinksUpdatedEvent, None]=None) -> None:
        """This is fired whenever the list of available sinks changes. A sink is a device or a software surface that you can cast to."""
        self.events.on('sinksUpdated', callback)
    
    def on_issue_updated(self, callback: Callable[issueUpdatedEvent, None]=None) -> None:
        """This is fired whenever the outstanding issue/error message changes. |issueMessage| is empty if there is no issue."""
        self.events.on('issueUpdated', callback)
     