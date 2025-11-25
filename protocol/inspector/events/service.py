
"""CDP Inspector Events"""

from client.events import CDPEvents
from typing import TypedDict, Optional, Callable
from protocol.inspector.events.types import *

class InspectorEvents:
    def __init__(self,events:CDPEvents):
        self.events=events
    
    def on_detached(self, callback: Callable[[detachedEvent,Optional[str]], None]=None) -> None:
        """Fired when remote debugging connection is about to be terminated. Contains detach reason."""
        self.events.on('detached', callback)
    
    def on_target_crashed(self, callback: Callable[[targetCrashedEvent,Optional[str]], None]=None) -> None:
        """Fired when debugging target has crashed"""
        self.events.on('targetCrashed', callback)
    
    def on_target_reloaded_after_crash(self, callback: Callable[[targetReloadedAfterCrashEvent,Optional[str]], None]=None) -> None:
        """Fired when debugging target has reloaded after crash"""
        self.events.on('targetReloadedAfterCrash', callback)
    
    def on_worker_script_loaded(self, callback: Callable[[workerScriptLoadedEvent,Optional[str]], None]=None) -> None:
        """Fired on worker targets when main worker script and any imported scripts have been evaluated."""
        self.events.on('workerScriptLoaded', callback)
     