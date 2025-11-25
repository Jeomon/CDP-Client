
"""CDP FileSystem Methods"""

from client.service import CDPClient
from typing import TypedDict,Optional
from protocol.file_system.methods.types import *

class FileSystemMethods:
    def __init__(self, client:CDPClient):
        self.client = client

    async def get_directory(self, params: Optional[getDirectoryParameters]=None,session_id: Optional[str] = None) -> getDirectoryReturns:
        return await self.client.send(method="FileSystem.getDirectory", params=params,session_id=session_id)
