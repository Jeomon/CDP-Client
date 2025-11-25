
"""CDP Profiler Methods"""

from client.methods import CDPMethods
from typing import TypedDict,Optional
from protocol.profiler.methods.types import *

class ProfilerMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def disable(self, params: None=None) -> Dict[str, Any]:
        return await self.methods.send(method="Profiler.disable", params=params)

    async def enable(self, params: None=None) -> Dict[str, Any]:
        return await self.methods.send(method="Profiler.enable", params=params)

    async def get_best_effort_coverage(self, params: None=None) -> getBestEffortCoverageReturns:
        """Collect coverage data for the current isolate. The coverage data may be incomplete due to garbage collection."""
        return await self.methods.send(method="Profiler.getBestEffortCoverage", params=params)

    async def set_sampling_interval(self, params: Optional[setSamplingIntervalParameters]=None) -> Dict[str, Any]:
        """Changes CPU profiler sampling interval. Must be called before CPU profiles recording started."""
        return await self.methods.send(method="Profiler.setSamplingInterval", params=params)

    async def start(self, params: None=None) -> Dict[str, Any]:
        return await self.methods.send(method="Profiler.start", params=params)

    async def start_precise_coverage(self, params: Optional[startPreciseCoverageParameters]=None) -> startPreciseCoverageReturns:
        """Enable precise code coverage. Coverage data for JavaScript executed before enabling precise code coverage may be incomplete. Enabling prevents running optimized code and resets execution counters."""
        return await self.methods.send(method="Profiler.startPreciseCoverage", params=params)

    async def stop(self, params: None=None) -> stopReturns:
        return await self.methods.send(method="Profiler.stop", params=params)

    async def stop_precise_coverage(self, params: None=None) -> Dict[str, Any]:
        """Disable precise code coverage. Disabling releases unnecessary execution count records and allows executing optimized code."""
        return await self.methods.send(method="Profiler.stopPreciseCoverage", params=params)

    async def take_precise_coverage(self, params: None=None) -> takePreciseCoverageReturns:
        """Collect coverage data for the current isolate, and resets execution counters. Precise code coverage needs to have started."""
        return await self.methods.send(method="Profiler.takePreciseCoverage", params=params)
