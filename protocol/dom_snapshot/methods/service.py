
"""CDP DOMSnapshot Methods"""

from client.service import CDPClient
from typing import TypedDict,Optional
from protocol.dom_snapshot.methods.types import *

class DOMSnapshotMethods:
    def __init__(self, client:CDPClient):
        self.client = client

    async def disable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Disables DOM snapshot agent for the given page."""
        return await self.client.send(method="DOMSnapshot.disable", params=params,session_id=session_id)

    async def enable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Enables DOM snapshot agent for the given page."""
        return await self.client.send(method="DOMSnapshot.enable", params=params,session_id=session_id)

    async def capture_snapshot(self, params: Optional[captureSnapshotParameters]=None,session_id: Optional[str] = None) -> captureSnapshotReturns:
        """Returns a document snapshot, including the full DOM tree of the root node (including iframes, template contents, and imported documents) in a flattened array, as well as layout and white-listed computed style information for the nodes. Shadow DOM in the returned DOM tree is flattened."""
        return await self.client.send(method="DOMSnapshot.captureSnapshot", params=params,session_id=session_id)
