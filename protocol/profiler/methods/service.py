
"""CDP Profiler Methods"""

from client.methods import CDPMethods
from typing import TypedDict,Optional
from protocol.profiler.methods.types import *

class ProfilerMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def disable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        return await self.methods.send(method="Profiler.disable", params=params,session_id=session_id)

    async def enable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        return await self.methods.send(method="Profiler.enable", params=params,session_id=session_id)

    async def get_best_effort_coverage(self, params: None=None,session_id: Optional[str] = None) -> getBestEffortCoverageReturns:
        """Collect coverage data for the current isolate. The coverage data may be incomplete due to garbage collection."""
        return await self.methods.send(method="Profiler.getBestEffortCoverage", params=params,session_id=session_id)

    async def set_sampling_interval(self, params: Optional[setSamplingIntervalParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Changes CPU profiler sampling interval. Must be called before CPU profiles recording started."""
        return await self.methods.send(method="Profiler.setSamplingInterval", params=params,session_id=session_id)

    async def start(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        return await self.methods.send(method="Profiler.start", params=params,session_id=session_id)

    async def start_precise_coverage(self, params: Optional[startPreciseCoverageParameters]=None,session_id: Optional[str] = None) -> startPreciseCoverageReturns:
        """Enable precise code coverage. Coverage data for JavaScript executed before enabling precise code coverage may be incomplete. Enabling prevents running optimized code and resets execution counters."""
        return await self.methods.send(method="Profiler.startPreciseCoverage", params=params,session_id=session_id)

    async def stop(self, params: None=None,session_id: Optional[str] = None) -> stopReturns:
        return await self.methods.send(method="Profiler.stop", params=params,session_id=session_id)

    async def stop_precise_coverage(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Disable precise code coverage. Disabling releases unnecessary execution count records and allows executing optimized code."""
        return await self.methods.send(method="Profiler.stopPreciseCoverage", params=params,session_id=session_id)

    async def take_precise_coverage(self, params: None=None,session_id: Optional[str] = None) -> takePreciseCoverageReturns:
        """Collect coverage data for the current isolate, and resets execution counters. Precise code coverage needs to have started."""
        return await self.methods.send(method="Profiler.takePreciseCoverage", params=params,session_id=session_id)
