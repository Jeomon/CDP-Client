
"""CDP PerformanceTimeline Methods"""

from cdp_client.methods import CDPMethods
from typing import TypedDict,Optional
from performance_timeline.methods.types import *

class PerformanceTimelineMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def enable(self, params: Optional[enableParameters]=None) -> Dict[str, Any]:
        """Previously buffered events would be reported before method returns. See also: timelineEventAdded"""
        return await self.methods.send(method="PerformanceTimeline.enable", params=params)
