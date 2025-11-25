
"""CDP EventBreakpoints Methods"""

from client.methods import CDPMethods
from typing import TypedDict,Optional
from protocol.event_breakpoints.methods.types import *

class EventBreakpointsMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def set_instrumentation_breakpoint(self, params: Optional[setInstrumentationBreakpointParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Sets breakpoint on particular native event."""
        return await self.methods.send(method="EventBreakpoints.setInstrumentationBreakpoint", params=params,session_id=session_id)

    async def remove_instrumentation_breakpoint(self, params: Optional[removeInstrumentationBreakpointParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Removes breakpoint on particular native event."""
        return await self.methods.send(method="EventBreakpoints.removeInstrumentationBreakpoint", params=params,session_id=session_id)

    async def disable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Removes all breakpoints"""
        return await self.methods.send(method="EventBreakpoints.disable", params=params,session_id=session_id)
