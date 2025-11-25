
"""CDP Extensions Methods"""

from client.methods import CDPMethods
from typing import TypedDict,Optional
from protocol.extensions.methods.types import *

class ExtensionsMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def load_unpacked(self, params: Optional[loadUnpackedParameters]=None) -> loadUnpackedReturns:
        """Installs an unpacked extension from the filesystem similar to --load-extension CLI flags. Returns extension ID once the extension has been installed. Available if the client is connected using the --remote-debugging-pipe flag and the --enable-unsafe-extension-debugging flag is set."""
        return await self.methods.send(method="Extensions.loadUnpacked", params=params)

    async def uninstall(self, params: Optional[uninstallParameters]=None) -> Dict[str, Any]:
        """Uninstalls an unpacked extension (others not supported) from the profile. Available if the client is connected using the --remote-debugging-pipe flag and the --enable-unsafe-extension-debugging."""
        return await self.methods.send(method="Extensions.uninstall", params=params)

    async def get_storage_items(self, params: Optional[getStorageItemsParameters]=None) -> getStorageItemsReturns:
        """Gets data from extension storage in the given `storageArea`. If `keys` is specified, these are used to filter the result."""
        return await self.methods.send(method="Extensions.getStorageItems", params=params)

    async def remove_storage_items(self, params: Optional[removeStorageItemsParameters]=None) -> Dict[str, Any]:
        """Removes `keys` from extension storage in the given `storageArea`."""
        return await self.methods.send(method="Extensions.removeStorageItems", params=params)

    async def clear_storage_items(self, params: Optional[clearStorageItemsParameters]=None) -> Dict[str, Any]:
        """Clears extension storage in the given `storageArea`."""
        return await self.methods.send(method="Extensions.clearStorageItems", params=params)

    async def set_storage_items(self, params: Optional[setStorageItemsParameters]=None) -> Dict[str, Any]:
        """Sets `values` in extension storage in the given `storageArea`. The provided `values` will be merged with existing values in the storage area."""
        return await self.methods.send(method="Extensions.setStorageItems", params=params)
