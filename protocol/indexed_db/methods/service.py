
"""CDP IndexedDB Methods"""

from cdp_client.methods import CDPMethods
from typing import TypedDict,Optional
from indexed_db.methods.types import *

class IndexedDBMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def clear_object_store(self, params: Optional[clearObjectStoreParameters]=None) -> Dict[str, Any]:
        """Clears all entries from an object store."""
        return await self.methods.send(method="IndexedDB.clearObjectStore", params=params)

    async def delete_database(self, params: Optional[deleteDatabaseParameters]=None) -> Dict[str, Any]:
        """Deletes a database."""
        return await self.methods.send(method="IndexedDB.deleteDatabase", params=params)

    async def delete_object_store_entries(self, params: Optional[deleteObjectStoreEntriesParameters]=None) -> Dict[str, Any]:
        """Delete a range of entries from an object store"""
        return await self.methods.send(method="IndexedDB.deleteObjectStoreEntries", params=params)

    async def disable(self, params: None=None) -> Dict[str, Any]:
        """Disables events from backend."""
        return await self.methods.send(method="IndexedDB.disable", params=params)

    async def enable(self, params: None=None) -> Dict[str, Any]:
        """Enables events from backend."""
        return await self.methods.send(method="IndexedDB.enable", params=params)

    async def request_data(self, params: Optional[requestDataParameters]=None) -> requestDataReturns:
        """Requests data from object store or index."""
        return await self.methods.send(method="IndexedDB.requestData", params=params)

    async def get_metadata(self, params: Optional[getMetadataParameters]=None) -> getMetadataReturns:
        """Gets metadata of an object store."""
        return await self.methods.send(method="IndexedDB.getMetadata", params=params)

    async def request_database(self, params: Optional[requestDatabaseParameters]=None) -> requestDatabaseReturns:
        """Requests database with given name in given frame."""
        return await self.methods.send(method="IndexedDB.requestDatabase", params=params)

    async def request_database_names(self, params: Optional[requestDatabaseNamesParameters]=None) -> requestDatabaseNamesReturns:
        """Requests database names for given security origin."""
        return await self.methods.send(method="IndexedDB.requestDatabaseNames", params=params)
