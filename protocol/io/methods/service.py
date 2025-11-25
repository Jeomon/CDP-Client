
"""CDP IO Methods"""

from client.service import CDPClient
from typing import TypedDict,Optional
from protocol.io.methods.types import *

class IOMethods:
    def __init__(self, client:CDPClient):
        self.client = client

    async def close(self, params: Optional[closeParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Close the stream, discard any temporary backing storage."""
        return await self.client.send(method="IO.close", params=params,session_id=session_id)

    async def read(self, params: Optional[readParameters]=None,session_id: Optional[str] = None) -> readReturns:
        """Read a chunk of the stream"""
        return await self.client.send(method="IO.read", params=params,session_id=session_id)

    async def resolve_blob(self, params: Optional[resolveBlobParameters]=None,session_id: Optional[str] = None) -> resolveBlobReturns:
        """Return UUID of Blob object specified by a remote object id."""
        return await self.client.send(method="IO.resolveBlob", params=params,session_id=session_id)
