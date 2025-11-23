
"""CDP FileSystem Methods"""

from cdp_client.methods import CDPMethods
from typing import TypedDict,Optional
from file_system.methods.types import *

class FileSystemMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def get_directory(self, params: Optional[getDirectoryParameters]=None) -> getDirectoryReturns:
        return await self.methods.send(method="FileSystem.getDirectory", params=params)
