
"""CDP DOMDebugger Methods"""

from client.methods import CDPMethods
from typing import TypedDict,Optional
from protocol.dom_debugger.methods.types import *

class DOMDebuggerMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def get_event_listeners(self, params: Optional[getEventListenersParameters]=None,session_id: Optional[str] = None) -> getEventListenersReturns:
        """Returns event listeners of the given object."""
        return await self.methods.send(method="DOMDebugger.getEventListeners", params=params,session_id=session_id)

    async def remove_dom_breakpoint(self, params: Optional[removeDOMBreakpointParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Removes DOM breakpoint that was set using `setDOMBreakpoint`."""
        return await self.methods.send(method="DOMDebugger.removeDOMBreakpoint", params=params,session_id=session_id)

    async def remove_event_listener_breakpoint(self, params: Optional[removeEventListenerBreakpointParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Removes breakpoint on particular DOM event."""
        return await self.methods.send(method="DOMDebugger.removeEventListenerBreakpoint", params=params,session_id=session_id)

    async def remove_xhr_breakpoint(self, params: Optional[removeXHRBreakpointParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Removes breakpoint from XMLHttpRequest."""
        return await self.methods.send(method="DOMDebugger.removeXHRBreakpoint", params=params,session_id=session_id)

    async def set_break_on_csp_violation(self, params: Optional[setBreakOnCSPViolationParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Sets breakpoint on particular CSP violations."""
        return await self.methods.send(method="DOMDebugger.setBreakOnCSPViolation", params=params,session_id=session_id)

    async def set_dom_breakpoint(self, params: Optional[setDOMBreakpointParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Sets breakpoint on particular operation with DOM."""
        return await self.methods.send(method="DOMDebugger.setDOMBreakpoint", params=params,session_id=session_id)

    async def set_event_listener_breakpoint(self, params: Optional[setEventListenerBreakpointParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Sets breakpoint on particular DOM event."""
        return await self.methods.send(method="DOMDebugger.setEventListenerBreakpoint", params=params,session_id=session_id)

    async def set_xhr_breakpoint(self, params: Optional[setXHRBreakpointParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Sets breakpoint on XMLHttpRequest."""
        return await self.methods.send(method="DOMDebugger.setXHRBreakpoint", params=params,session_id=session_id)
