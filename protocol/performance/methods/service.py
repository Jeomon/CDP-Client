
"""CDP Performance Methods"""

from client.methods import CDPMethods
from typing import TypedDict,Optional
from protocol.performance.methods.types import *

class PerformanceMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def disable(self, params: None=None) -> Dict[str, Any]:
        """Disable collecting and reporting metrics."""
        return await self.methods.send(method="Performance.disable", params=params)

    async def enable(self, params: Optional[enableParameters]=None) -> Dict[str, Any]:
        """Enable collecting and reporting metrics."""
        return await self.methods.send(method="Performance.enable", params=params)

    async def get_metrics(self, params: None=None) -> getMetricsReturns:
        """Retrieve current values of run-time metrics."""
        return await self.methods.send(method="Performance.getMetrics", params=params)
