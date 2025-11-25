
"""CDP Debugger Events"""

from client.service import CDPClient
from typing import TypedDict, Optional, Callable
from protocol.debugger.events.types import *

class DebuggerEvents:
    def __init__(self,client:CDPClient):
        self.client=client
    
    def on_breakpoint_resolved(self, callback: Callable[[breakpointResolvedEvent,Optional[str]], None]=None) -> None:
        """Fired when breakpoint is resolved to an actual script and location. Deprecated in favor of `resolvedBreakpoints` in the `scriptParsed` event."""
        self.client.on('breakpointResolved', callback)
    
    def on_paused(self, callback: Callable[[pausedEvent,Optional[str]], None]=None) -> None:
        """Fired when the virtual machine stopped on breakpoint or exception or any other stop criteria."""
        self.client.on('paused', callback)
    
    def on_resumed(self, callback: Callable[[resumedEvent,Optional[str]], None]=None) -> None:
        """Fired when the virtual machine resumed execution."""
        self.client.on('resumed', callback)
    
    def on_script_failed_to_parse(self, callback: Callable[[scriptFailedToParseEvent,Optional[str]], None]=None) -> None:
        """Fired when virtual machine fails to parse the script."""
        self.client.on('scriptFailedToParse', callback)
    
    def on_script_parsed(self, callback: Callable[[scriptParsedEvent,Optional[str]], None]=None) -> None:
        """Fired when virtual machine parses script. This event is also fired for all known and uncollected scripts upon enabling debugger."""
        self.client.on('scriptParsed', callback)
     