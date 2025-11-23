
"""CDP HeadlessExperimental Methods"""

from cdp_client.methods import CDPMethods
from typing import TypedDict,Optional
from headless_experimental.methods.types import *

class HeadlessExperimentalMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def begin_frame(self, params: Optional[beginFrameParameters]=None) -> beginFrameReturns:
        """Sends a BeginFrame to the target and returns when the frame was completed. Optionally captures a screenshot from the resulting frame. Requires that the target was created with enabled BeginFrameControl. Designed for use with --run-all-compositor-stages-before-draw, see also https://goo.gle/chrome-headless-rendering for more background."""
        return await self.methods.send(method="HeadlessExperimental.beginFrame", params=params)
