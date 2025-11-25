
"""CDP Storage Events"""

from client.events import CDPEvents
from typing import TypedDict, Optional, Callable
from protocol.storage.events.types import *

class StorageEvents:
    def __init__(self,events:CDPEvents):
        self.events=events
    
    def on_cache_storage_content_updated(self, callback: Callable[cacheStorageContentUpdatedEvent, None]=None) -> None:
        """A cache's contents have been modified."""
        self.events.on('cacheStorageContentUpdated', callback)
    
    def on_cache_storage_list_updated(self, callback: Callable[cacheStorageListUpdatedEvent, None]=None) -> None:
        """A cache has been added/deleted."""
        self.events.on('cacheStorageListUpdated', callback)
    
    def on_indexed_db_content_updated(self, callback: Callable[indexedDBContentUpdatedEvent, None]=None) -> None:
        """The origin's IndexedDB object store has been modified."""
        self.events.on('indexedDBContentUpdated', callback)
    
    def on_indexed_db_list_updated(self, callback: Callable[indexedDBListUpdatedEvent, None]=None) -> None:
        """The origin's IndexedDB database list has been modified."""
        self.events.on('indexedDBListUpdated', callback)
    
    def on_interest_group_accessed(self, callback: Callable[interestGroupAccessedEvent, None]=None) -> None:
        """One of the interest groups was accessed. Note that these events are global to all targets sharing an interest group store."""
        self.events.on('interestGroupAccessed', callback)
    
    def on_interest_group_auction_event_occurred(self, callback: Callable[interestGroupAuctionEventOccurredEvent, None]=None) -> None:
        """An auction involving interest groups is taking place. These events are target-specific."""
        self.events.on('interestGroupAuctionEventOccurred', callback)
    
    def on_interest_group_auction_network_request_created(self, callback: Callable[interestGroupAuctionNetworkRequestCreatedEvent, None]=None) -> None:
        """Specifies which auctions a particular network fetch may be related to, and in what role. Note that it is not ordered with respect to Network.requestWillBeSent (but will happen before loadingFinished loadingFailed)."""
        self.events.on('interestGroupAuctionNetworkRequestCreated', callback)
    
    def on_shared_storage_accessed(self, callback: Callable[sharedStorageAccessedEvent, None]=None) -> None:
        """Shared storage was accessed by the associated page. The following parameters are included in all events."""
        self.events.on('sharedStorageAccessed', callback)
    
    def on_shared_storage_worklet_operation_execution_finished(self, callback: Callable[sharedStorageWorkletOperationExecutionFinishedEvent, None]=None) -> None:
        """A shared storage run or selectURL operation finished its execution. The following parameters are included in all events."""
        self.events.on('sharedStorageWorkletOperationExecutionFinished', callback)
    
    def on_storage_bucket_created_or_updated(self, callback: Callable[storageBucketCreatedOrUpdatedEvent, None]=None) -> None:
        self.events.on('storageBucketCreatedOrUpdated', callback)
    
    def on_storage_bucket_deleted(self, callback: Callable[storageBucketDeletedEvent, None]=None) -> None:
        self.events.on('storageBucketDeleted', callback)
    
    def on_attribution_reporting_source_registered(self, callback: Callable[attributionReportingSourceRegisteredEvent, None]=None) -> None:
        self.events.on('attributionReportingSourceRegistered', callback)
    
    def on_attribution_reporting_trigger_registered(self, callback: Callable[attributionReportingTriggerRegisteredEvent, None]=None) -> None:
        self.events.on('attributionReportingTriggerRegistered', callback)
    
    def on_attribution_reporting_report_sent(self, callback: Callable[attributionReportingReportSentEvent, None]=None) -> None:
        self.events.on('attributionReportingReportSent', callback)
    
    def on_attribution_reporting_verbose_debug_report_sent(self, callback: Callable[attributionReportingVerboseDebugReportSentEvent, None]=None) -> None:
        self.events.on('attributionReportingVerboseDebugReportSent', callback)
     