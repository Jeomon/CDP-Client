
"""CDP CacheStorage Methods"""

from client.methods import CDPMethods
from typing import TypedDict,Optional
from protocol.cache_storage.methods.types import *

class CacheStorageMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def delete_cache(self, params: Optional[deleteCacheParameters]=None) -> Dict[str, Any]:
        """Deletes a cache."""
        return await self.methods.send(method="CacheStorage.deleteCache", params=params)

    async def delete_entry(self, params: Optional[deleteEntryParameters]=None) -> Dict[str, Any]:
        """Deletes a cache entry."""
        return await self.methods.send(method="CacheStorage.deleteEntry", params=params)

    async def request_cache_names(self, params: Optional[requestCacheNamesParameters]=None) -> requestCacheNamesReturns:
        """Requests cache names."""
        return await self.methods.send(method="CacheStorage.requestCacheNames", params=params)

    async def request_cached_response(self, params: Optional[requestCachedResponseParameters]=None) -> requestCachedResponseReturns:
        """Fetches cache entry."""
        return await self.methods.send(method="CacheStorage.requestCachedResponse", params=params)

    async def request_entries(self, params: Optional[requestEntriesParameters]=None) -> requestEntriesReturns:
        """Requests data from cache."""
        return await self.methods.send(method="CacheStorage.requestEntries", params=params)
