
"""CDP Tracing Methods"""

from client.methods import CDPMethods
from typing import TypedDict,Optional
from protocol.tracing.methods.types import *

class TracingMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def end(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Stop trace events collection."""
        return await self.methods.send(method="Tracing.end", params=params,session_id=session_id)

    async def get_categories(self, params: None=None,session_id: Optional[str] = None) -> getCategoriesReturns:
        """Gets supported tracing categories."""
        return await self.methods.send(method="Tracing.getCategories", params=params,session_id=session_id)

    async def record_clock_sync_marker(self, params: Optional[recordClockSyncMarkerParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Record a clock sync marker in the trace."""
        return await self.methods.send(method="Tracing.recordClockSyncMarker", params=params,session_id=session_id)

    async def request_memory_dump(self, params: Optional[requestMemoryDumpParameters]=None,session_id: Optional[str] = None) -> requestMemoryDumpReturns:
        """Request a global memory dump."""
        return await self.methods.send(method="Tracing.requestMemoryDump", params=params,session_id=session_id)

    async def start(self, params: Optional[startParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Start trace events collection."""
        return await self.methods.send(method="Tracing.start", params=params,session_id=session_id)
