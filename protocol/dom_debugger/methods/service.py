
"""CDP DOMDebugger Methods"""

from client.methods import CDPMethods
from typing import TypedDict,Optional
from protocol.dom_debugger.methods.types import *

class DOMDebuggerMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def get_event_listeners(self, params: Optional[getEventListenersParameters]=None) -> getEventListenersReturns:
        """Returns event listeners of the given object."""
        return await self.methods.send(method="DOMDebugger.getEventListeners", params=params)

    async def remove_dom_breakpoint(self, params: Optional[removeDOMBreakpointParameters]=None) -> Dict[str, Any]:
        """Removes DOM breakpoint that was set using `setDOMBreakpoint`."""
        return await self.methods.send(method="DOMDebugger.removeDOMBreakpoint", params=params)

    async def remove_event_listener_breakpoint(self, params: Optional[removeEventListenerBreakpointParameters]=None) -> Dict[str, Any]:
        """Removes breakpoint on particular DOM event."""
        return await self.methods.send(method="DOMDebugger.removeEventListenerBreakpoint", params=params)

    async def remove_xhr_breakpoint(self, params: Optional[removeXHRBreakpointParameters]=None) -> Dict[str, Any]:
        """Removes breakpoint from XMLHttpRequest."""
        return await self.methods.send(method="DOMDebugger.removeXHRBreakpoint", params=params)

    async def set_break_on_csp_violation(self, params: Optional[setBreakOnCSPViolationParameters]=None) -> Dict[str, Any]:
        """Sets breakpoint on particular CSP violations."""
        return await self.methods.send(method="DOMDebugger.setBreakOnCSPViolation", params=params)

    async def set_dom_breakpoint(self, params: Optional[setDOMBreakpointParameters]=None) -> Dict[str, Any]:
        """Sets breakpoint on particular operation with DOM."""
        return await self.methods.send(method="DOMDebugger.setDOMBreakpoint", params=params)

    async def set_event_listener_breakpoint(self, params: Optional[setEventListenerBreakpointParameters]=None) -> Dict[str, Any]:
        """Sets breakpoint on particular DOM event."""
        return await self.methods.send(method="DOMDebugger.setEventListenerBreakpoint", params=params)

    async def set_xhr_breakpoint(self, params: Optional[setXHRBreakpointParameters]=None) -> Dict[str, Any]:
        """Sets breakpoint on XMLHttpRequest."""
        return await self.methods.send(method="DOMDebugger.setXHRBreakpoint", params=params)
