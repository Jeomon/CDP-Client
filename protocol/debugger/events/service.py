
"""CDP Debugger Events"""

from cdp_client.events import CDPEvents
from typing import TypedDict, Optional, Callable
from debugger.events.types import *

class DebuggerEvents:
    def __init__(self,events:CDPEvents):
        self.events=events
    
    def on_breakpoint_resolved(self, callback: Callable[breakpointResolvedEvent, None]=None) -> None:
        """Fired when breakpoint is resolved to an actual script and location. Deprecated in favor of `resolvedBreakpoints` in the `scriptParsed` event."""
        self.events.on('breakpointResolved', callback)
    
    def on_paused(self, callback: Callable[pausedEvent, None]=None) -> None:
        """Fired when the virtual machine stopped on breakpoint or exception or any other stop criteria."""
        self.events.on('paused', callback)
    
    def on_resumed(self, callback: Callable[resumedEvent, None]=None) -> None:
        """Fired when the virtual machine resumed execution."""
        self.events.on('resumed', callback)
    
    def on_script_failed_to_parse(self, callback: Callable[scriptFailedToParseEvent, None]=None) -> None:
        """Fired when virtual machine fails to parse the script."""
        self.events.on('scriptFailedToParse', callback)
    
    def on_script_parsed(self, callback: Callable[scriptParsedEvent, None]=None) -> None:
        """Fired when virtual machine parses script. This event is also fired for all known and uncollected scripts upon enabling debugger."""
        self.events.on('scriptParsed', callback)
     