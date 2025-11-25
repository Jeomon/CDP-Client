
"""CDP FileSystem Methods"""

from client.methods import CDPMethods
from typing import TypedDict,Optional
from protocol.file_system.methods.types import *

class FileSystemMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def get_directory(self, params: Optional[getDirectoryParameters]=None,session_id: Optional[str] = None) -> getDirectoryReturns:
        return await self.methods.send(method="FileSystem.getDirectory", params=params,session_id=session_id)
