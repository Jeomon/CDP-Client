
"""CDP Performance Methods"""

from client.service import CDPClient
from typing import TypedDict,Optional
from protocol.performance.methods.types import *

class PerformanceMethods:
    def __init__(self, client:CDPClient):
        self.client = client

    async def disable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Disable collecting and reporting metrics."""
        return await self.client.send(method="Performance.disable", params=params,session_id=session_id)

    async def enable(self, params: Optional[enableParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Enable collecting and reporting metrics."""
        return await self.client.send(method="Performance.enable", params=params,session_id=session_id)

    async def get_metrics(self, params: None=None,session_id: Optional[str] = None) -> getMetricsReturns:
        """Retrieve current values of run-time metrics."""
        return await self.client.send(method="Performance.getMetrics", params=params,session_id=session_id)
