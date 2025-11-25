
"""CDP PerformanceTimeline Methods"""

from client.service import CDPClient
from typing import TypedDict,Optional
from protocol.performance_timeline.methods.types import *

class PerformanceTimelineMethods:
    def __init__(self, client:CDPClient):
        self.client = client

    async def enable(self, params: Optional[enableParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Previously buffered events would be reported before method returns. See also: timelineEventAdded"""
        return await self.client.send(method="PerformanceTimeline.enable", params=params,session_id=session_id)
