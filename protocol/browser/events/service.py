
"""CDP Browser Events"""

from client.service import CDPClient
from typing import TypedDict, Optional, Callable
from protocol.browser.events.types import *

class BrowserEvents:
    def __init__(self,client:CDPClient):
        self.client=client
    
    def on_download_will_begin(self, callback: Callable[[downloadWillBeginEvent,Optional[str]], None]=None) -> None:
        """Fired when page is about to start a download."""
        self.client.on('Browser.downloadWillBegin', callback)
    
    def on_download_progress(self, callback: Callable[[downloadProgressEvent,Optional[str]], None]=None) -> None:
        """Fired when download makes progress. Last call has |done| == true."""
        self.client.on('Browser.downloadProgress', callback)
     