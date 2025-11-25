
"""CDP Storage Events"""

from client.service import CDPClient
from typing import TypedDict, Optional, Callable
from protocol.storage.events.types import *

class StorageEvents:
    def __init__(self,client:CDPClient):
        self.client=client
    
    def on_cache_storage_content_updated(self, callback: Callable[[cacheStorageContentUpdatedEvent,Optional[str]], None]=None) -> None:
        """A cache's contents have been modified."""
        self.client.on('Storage.cacheStorageContentUpdated', callback)
    
    def on_cache_storage_list_updated(self, callback: Callable[[cacheStorageListUpdatedEvent,Optional[str]], None]=None) -> None:
        """A cache has been added/deleted."""
        self.client.on('Storage.cacheStorageListUpdated', callback)
    
    def on_indexed_db_content_updated(self, callback: Callable[[indexedDBContentUpdatedEvent,Optional[str]], None]=None) -> None:
        """The origin's IndexedDB object store has been modified."""
        self.client.on('Storage.indexedDBContentUpdated', callback)
    
    def on_indexed_db_list_updated(self, callback: Callable[[indexedDBListUpdatedEvent,Optional[str]], None]=None) -> None:
        """The origin's IndexedDB database list has been modified."""
        self.client.on('Storage.indexedDBListUpdated', callback)
    
    def on_interest_group_accessed(self, callback: Callable[[interestGroupAccessedEvent,Optional[str]], None]=None) -> None:
        """One of the interest groups was accessed. Note that these events are global to all targets sharing an interest group store."""
        self.client.on('Storage.interestGroupAccessed', callback)
    
    def on_interest_group_auction_event_occurred(self, callback: Callable[[interestGroupAuctionEventOccurredEvent,Optional[str]], None]=None) -> None:
        """An auction involving interest groups is taking place. These events are target-specific."""
        self.client.on('Storage.interestGroupAuctionEventOccurred', callback)
    
    def on_interest_group_auction_network_request_created(self, callback: Callable[[interestGroupAuctionNetworkRequestCreatedEvent,Optional[str]], None]=None) -> None:
        """Specifies which auctions a particular network fetch may be related to, and in what role. Note that it is not ordered with respect to Network.requestWillBeSent (but will happen before loadingFinished loadingFailed)."""
        self.client.on('Storage.interestGroupAuctionNetworkRequestCreated', callback)
    
    def on_shared_storage_accessed(self, callback: Callable[[sharedStorageAccessedEvent,Optional[str]], None]=None) -> None:
        """Shared storage was accessed by the associated page. The following parameters are included in all events."""
        self.client.on('Storage.sharedStorageAccessed', callback)
    
    def on_shared_storage_worklet_operation_execution_finished(self, callback: Callable[[sharedStorageWorkletOperationExecutionFinishedEvent,Optional[str]], None]=None) -> None:
        """A shared storage run or selectURL operation finished its execution. The following parameters are included in all events."""
        self.client.on('Storage.sharedStorageWorkletOperationExecutionFinished', callback)
    
    def on_storage_bucket_created_or_updated(self, callback: Callable[[storageBucketCreatedOrUpdatedEvent,Optional[str]], None]=None) -> None:
        self.client.on('Storage.storageBucketCreatedOrUpdated', callback)
    
    def on_storage_bucket_deleted(self, callback: Callable[[storageBucketDeletedEvent,Optional[str]], None]=None) -> None:
        self.client.on('Storage.storageBucketDeleted', callback)
    
    def on_attribution_reporting_source_registered(self, callback: Callable[[attributionReportingSourceRegisteredEvent,Optional[str]], None]=None) -> None:
        self.client.on('Storage.attributionReportingSourceRegistered', callback)
    
    def on_attribution_reporting_trigger_registered(self, callback: Callable[[attributionReportingTriggerRegisteredEvent,Optional[str]], None]=None) -> None:
        self.client.on('Storage.attributionReportingTriggerRegistered', callback)
    
    def on_attribution_reporting_report_sent(self, callback: Callable[[attributionReportingReportSentEvent,Optional[str]], None]=None) -> None:
        self.client.on('Storage.attributionReportingReportSent', callback)
    
    def on_attribution_reporting_verbose_debug_report_sent(self, callback: Callable[[attributionReportingVerboseDebugReportSentEvent,Optional[str]], None]=None) -> None:
        self.client.on('Storage.attributionReportingVerboseDebugReportSent', callback)
     