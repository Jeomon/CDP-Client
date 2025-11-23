
"""CDP Tracing Methods"""

from cdp_client.methods import CDPMethods
from typing import TypedDict,Optional
from tracing.methods.types import *

class TracingMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def end(self, params: None=None) -> Dict[str, Any]:
        """Stop trace events collection."""
        return await self.methods.send(method="Tracing.end", params=params)

    async def get_categories(self, params: None=None) -> getCategoriesReturns:
        """Gets supported tracing categories."""
        return await self.methods.send(method="Tracing.getCategories", params=params)

    async def record_clock_sync_marker(self, params: Optional[recordClockSyncMarkerParameters]=None) -> Dict[str, Any]:
        """Record a clock sync marker in the trace."""
        return await self.methods.send(method="Tracing.recordClockSyncMarker", params=params)

    async def request_memory_dump(self, params: Optional[requestMemoryDumpParameters]=None) -> requestMemoryDumpReturns:
        """Request a global memory dump."""
        return await self.methods.send(method="Tracing.requestMemoryDump", params=params)

    async def start(self, params: Optional[startParameters]=None) -> Dict[str, Any]:
        """Start trace events collection."""
        return await self.methods.send(method="Tracing.start", params=params)
