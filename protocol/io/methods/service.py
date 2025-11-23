
"""CDP IO Methods"""

from cdp_client.methods import CDPMethods
from typing import TypedDict,Optional
from io.methods.types import *

class IOMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def close(self, params: Optional[closeParameters]=None) -> Dict[str, Any]:
        """Close the stream, discard any temporary backing storage."""
        return await self.methods.send(method="IO.close", params=params)

    async def read(self, params: Optional[readParameters]=None) -> readReturns:
        """Read a chunk of the stream"""
        return await self.methods.send(method="IO.read", params=params)

    async def resolve_blob(self, params: Optional[resolveBlobParameters]=None) -> resolveBlobReturns:
        """Return UUID of Blob object specified by a remote object id."""
        return await self.methods.send(method="IO.resolveBlob", params=params)
