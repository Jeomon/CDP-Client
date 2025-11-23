
"""CDP DOMSnapshot Methods"""

from cdp_client.methods import CDPMethods
from typing import TypedDict,Optional
from dom_snapshot.methods.types import *

class DOMSnapshotMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def disable(self, params: None=None) -> Dict[str, Any]:
        """Disables DOM snapshot agent for the given page."""
        return await self.methods.send(method="DOMSnapshot.disable", params=params)

    async def enable(self, params: None=None) -> Dict[str, Any]:
        """Enables DOM snapshot agent for the given page."""
        return await self.methods.send(method="DOMSnapshot.enable", params=params)

    async def capture_snapshot(self, params: Optional[captureSnapshotParameters]=None) -> captureSnapshotReturns:
        """Returns a document snapshot, including the full DOM tree of the root node (including iframes, template contents, and imported documents) in a flattened array, as well as layout and white-listed computed style information for the nodes. Shadow DOM in the returned DOM tree is flattened."""
        return await self.methods.send(method="DOMSnapshot.captureSnapshot", params=params)
