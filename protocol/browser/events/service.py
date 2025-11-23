
"""CDP Browser Events"""

from cdp_client.events import CDPEvents
from typing import TypedDict, Optional, Callable
from browser.events.types import *

class BrowserEvents:
    def __init__(self,events:CDPEvents):
        self.events=events
    
    def on_download_will_begin(self, callback: Callable[downloadWillBeginEvent, None]=None) -> None:
        """Fired when page is about to start a download."""
        self.events.on('downloadWillBegin', callback)
    
    def on_download_progress(self, callback: Callable[downloadProgressEvent, None]=None) -> None:
        """Fired when download makes progress. Last call has |done| == true."""
        self.events.on('downloadProgress', callback)
     