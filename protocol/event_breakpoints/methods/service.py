
"""CDP EventBreakpoints Methods"""

from cdp_client.methods import CDPMethods
from typing import TypedDict,Optional
from event_breakpoints.methods.types import *

class EventBreakpointsMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def set_instrumentation_breakpoint(self, params: Optional[setInstrumentationBreakpointParameters]=None) -> Dict[str, Any]:
        """Sets breakpoint on particular native event."""
        return await self.methods.send(method="EventBreakpoints.setInstrumentationBreakpoint", params=params)

    async def remove_instrumentation_breakpoint(self, params: Optional[removeInstrumentationBreakpointParameters]=None) -> Dict[str, Any]:
        """Removes breakpoint on particular native event."""
        return await self.methods.send(method="EventBreakpoints.removeInstrumentationBreakpoint", params=params)

    async def disable(self, params: None=None) -> Dict[str, Any]:
        """Removes all breakpoints"""
        return await self.methods.send(method="EventBreakpoints.disable", params=params)
