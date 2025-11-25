
"""CDP Runtime Events"""

from client.events import CDPEvents
from typing import TypedDict, Optional, Callable
from protocol.runtime.events.types import *

class RuntimeEvents:
    def __init__(self,events:CDPEvents):
        self.events=events
    
    def on_binding_called(self, callback: Callable[[bindingCalledEvent,Optional[str]], None]=None) -> None:
        """Notification is issued every time when binding is called."""
        self.events.on('bindingCalled', callback)
    
    def on_console_api_called(self, callback: Callable[[consoleAPICalledEvent,Optional[str]], None]=None) -> None:
        """Issued when console API was called."""
        self.events.on('consoleAPICalled', callback)
    
    def on_exception_revoked(self, callback: Callable[[exceptionRevokedEvent,Optional[str]], None]=None) -> None:
        """Issued when unhandled exception was revoked."""
        self.events.on('exceptionRevoked', callback)
    
    def on_exception_thrown(self, callback: Callable[[exceptionThrownEvent,Optional[str]], None]=None) -> None:
        """Issued when exception was thrown and unhandled."""
        self.events.on('exceptionThrown', callback)
    
    def on_execution_context_created(self, callback: Callable[[executionContextCreatedEvent,Optional[str]], None]=None) -> None:
        """Issued when new execution context is created."""
        self.events.on('executionContextCreated', callback)
    
    def on_execution_context_destroyed(self, callback: Callable[[executionContextDestroyedEvent,Optional[str]], None]=None) -> None:
        """Issued when execution context is destroyed."""
        self.events.on('executionContextDestroyed', callback)
    
    def on_execution_contexts_cleared(self, callback: Callable[[executionContextsClearedEvent,Optional[str]], None]=None) -> None:
        """Issued when all executionContexts were cleared in browser"""
        self.events.on('executionContextsCleared', callback)
    
    def on_inspect_requested(self, callback: Callable[[inspectRequestedEvent,Optional[str]], None]=None) -> None:
        """Issued when object should be inspected (for example, as a result of inspect() command line API call)."""
        self.events.on('inspectRequested', callback)
     