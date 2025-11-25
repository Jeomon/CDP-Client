
"""CDP IndexedDB Methods"""

from client.service import CDPClient
from typing import TypedDict,Optional
from protocol.indexed_db.methods.types import *

class IndexedDBMethods:
    def __init__(self, client:CDPClient):
        self.client = client

    async def clear_object_store(self, params: Optional[clearObjectStoreParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Clears all entries from an object store."""
        return await self.client.send(method="IndexedDB.clearObjectStore", params=params,session_id=session_id)

    async def delete_database(self, params: Optional[deleteDatabaseParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Deletes a database."""
        return await self.client.send(method="IndexedDB.deleteDatabase", params=params,session_id=session_id)

    async def delete_object_store_entries(self, params: Optional[deleteObjectStoreEntriesParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Delete a range of entries from an object store"""
        return await self.client.send(method="IndexedDB.deleteObjectStoreEntries", params=params,session_id=session_id)

    async def disable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Disables events from backend."""
        return await self.client.send(method="IndexedDB.disable", params=params,session_id=session_id)

    async def enable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Enables events from backend."""
        return await self.client.send(method="IndexedDB.enable", params=params,session_id=session_id)

    async def request_data(self, params: Optional[requestDataParameters]=None,session_id: Optional[str] = None) -> requestDataReturns:
        """Requests data from object store or index."""
        return await self.client.send(method="IndexedDB.requestData", params=params,session_id=session_id)

    async def get_metadata(self, params: Optional[getMetadataParameters]=None,session_id: Optional[str] = None) -> getMetadataReturns:
        """Gets metadata of an object store."""
        return await self.client.send(method="IndexedDB.getMetadata", params=params,session_id=session_id)

    async def request_database(self, params: Optional[requestDatabaseParameters]=None,session_id: Optional[str] = None) -> requestDatabaseReturns:
        """Requests database with given name in given frame."""
        return await self.client.send(method="IndexedDB.requestDatabase", params=params,session_id=session_id)

    async def request_database_names(self, params: Optional[requestDatabaseNamesParameters]=None,session_id: Optional[str] = None) -> requestDatabaseNamesReturns:
        """Requests database names for given security origin."""
        return await self.client.send(method="IndexedDB.requestDatabaseNames", params=params,session_id=session_id)
