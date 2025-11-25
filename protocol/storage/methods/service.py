
"""CDP Storage Methods"""

from client.service import CDPClient
from typing import TypedDict,Optional
from protocol.storage.methods.types import *

class StorageMethods:
    def __init__(self, client:CDPClient):
        self.client = client

    async def get_storage_key(self, params: Optional[getStorageKeyParameters]=None,session_id: Optional[str] = None) -> getStorageKeyReturns:
        """Returns storage key for the given frame. If no frame ID is provided, the storage key of the target executing this command is returned."""
        return await self.client.send(method="Storage.getStorageKey", params=params,session_id=session_id)

    async def clear_data_for_origin(self, params: Optional[clearDataForOriginParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Clears storage for origin."""
        return await self.client.send(method="Storage.clearDataForOrigin", params=params,session_id=session_id)

    async def clear_data_for_storage_key(self, params: Optional[clearDataForStorageKeyParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Clears storage for storage key."""
        return await self.client.send(method="Storage.clearDataForStorageKey", params=params,session_id=session_id)

    async def get_cookies(self, params: Optional[getCookiesParameters]=None,session_id: Optional[str] = None) -> getCookiesReturns:
        """Returns all browser cookies."""
        return await self.client.send(method="Storage.getCookies", params=params,session_id=session_id)

    async def set_cookies(self, params: Optional[setCookiesParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Sets given cookies."""
        return await self.client.send(method="Storage.setCookies", params=params,session_id=session_id)

    async def clear_cookies(self, params: Optional[clearCookiesParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Clears cookies."""
        return await self.client.send(method="Storage.clearCookies", params=params,session_id=session_id)

    async def get_usage_and_quota(self, params: Optional[getUsageAndQuotaParameters]=None,session_id: Optional[str] = None) -> getUsageAndQuotaReturns:
        """Returns usage and quota in bytes."""
        return await self.client.send(method="Storage.getUsageAndQuota", params=params,session_id=session_id)

    async def override_quota_for_origin(self, params: Optional[overrideQuotaForOriginParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Override quota for the specified origin"""
        return await self.client.send(method="Storage.overrideQuotaForOrigin", params=params,session_id=session_id)

    async def track_cache_storage_for_origin(self, params: Optional[trackCacheStorageForOriginParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Registers origin to be notified when an update occurs to its cache storage list."""
        return await self.client.send(method="Storage.trackCacheStorageForOrigin", params=params,session_id=session_id)

    async def track_cache_storage_for_storage_key(self, params: Optional[trackCacheStorageForStorageKeyParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Registers storage key to be notified when an update occurs to its cache storage list."""
        return await self.client.send(method="Storage.trackCacheStorageForStorageKey", params=params,session_id=session_id)

    async def track_indexed_db_for_origin(self, params: Optional[trackIndexedDBForOriginParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Registers origin to be notified when an update occurs to its IndexedDB."""
        return await self.client.send(method="Storage.trackIndexedDBForOrigin", params=params,session_id=session_id)

    async def track_indexed_db_for_storage_key(self, params: Optional[trackIndexedDBForStorageKeyParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Registers storage key to be notified when an update occurs to its IndexedDB."""
        return await self.client.send(method="Storage.trackIndexedDBForStorageKey", params=params,session_id=session_id)

    async def untrack_cache_storage_for_origin(self, params: Optional[untrackCacheStorageForOriginParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Unregisters origin from receiving notifications for cache storage."""
        return await self.client.send(method="Storage.untrackCacheStorageForOrigin", params=params,session_id=session_id)

    async def untrack_cache_storage_for_storage_key(self, params: Optional[untrackCacheStorageForStorageKeyParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Unregisters storage key from receiving notifications for cache storage."""
        return await self.client.send(method="Storage.untrackCacheStorageForStorageKey", params=params,session_id=session_id)

    async def untrack_indexed_db_for_origin(self, params: Optional[untrackIndexedDBForOriginParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Unregisters origin from receiving notifications for IndexedDB."""
        return await self.client.send(method="Storage.untrackIndexedDBForOrigin", params=params,session_id=session_id)

    async def untrack_indexed_db_for_storage_key(self, params: Optional[untrackIndexedDBForStorageKeyParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Unregisters storage key from receiving notifications for IndexedDB."""
        return await self.client.send(method="Storage.untrackIndexedDBForStorageKey", params=params,session_id=session_id)

    async def get_trust_tokens(self, params: None=None,session_id: Optional[str] = None) -> getTrustTokensReturns:
        """Returns the number of stored Trust Tokens per issuer for the current browsing context."""
        return await self.client.send(method="Storage.getTrustTokens", params=params,session_id=session_id)

    async def clear_trust_tokens(self, params: Optional[clearTrustTokensParameters]=None,session_id: Optional[str] = None) -> clearTrustTokensReturns:
        """Removes all Trust Tokens issued by the provided issuerOrigin. Leaves other stored data, including the issuer's Redemption Records, intact."""
        return await self.client.send(method="Storage.clearTrustTokens", params=params,session_id=session_id)

    async def get_interest_group_details(self, params: Optional[getInterestGroupDetailsParameters]=None,session_id: Optional[str] = None) -> getInterestGroupDetailsReturns:
        """Gets details for a named interest group."""
        return await self.client.send(method="Storage.getInterestGroupDetails", params=params,session_id=session_id)

    async def set_interest_group_tracking(self, params: Optional[setInterestGroupTrackingParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Enables/Disables issuing of interestGroupAccessed events."""
        return await self.client.send(method="Storage.setInterestGroupTracking", params=params,session_id=session_id)

    async def set_interest_group_auction_tracking(self, params: Optional[setInterestGroupAuctionTrackingParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Enables/Disables issuing of interestGroupAuctionEventOccurred and interestGroupAuctionNetworkRequestCreated."""
        return await self.client.send(method="Storage.setInterestGroupAuctionTracking", params=params,session_id=session_id)

    async def get_shared_storage_metadata(self, params: Optional[getSharedStorageMetadataParameters]=None,session_id: Optional[str] = None) -> getSharedStorageMetadataReturns:
        """Gets metadata for an origin's shared storage."""
        return await self.client.send(method="Storage.getSharedStorageMetadata", params=params,session_id=session_id)

    async def get_shared_storage_entries(self, params: Optional[getSharedStorageEntriesParameters]=None,session_id: Optional[str] = None) -> getSharedStorageEntriesReturns:
        """Gets the entries in an given origin's shared storage."""
        return await self.client.send(method="Storage.getSharedStorageEntries", params=params,session_id=session_id)

    async def set_shared_storage_entry(self, params: Optional[setSharedStorageEntryParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Sets entry with `key` and `value` for a given origin's shared storage."""
        return await self.client.send(method="Storage.setSharedStorageEntry", params=params,session_id=session_id)

    async def delete_shared_storage_entry(self, params: Optional[deleteSharedStorageEntryParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Deletes entry for `key` (if it exists) for a given origin's shared storage."""
        return await self.client.send(method="Storage.deleteSharedStorageEntry", params=params,session_id=session_id)

    async def clear_shared_storage_entries(self, params: Optional[clearSharedStorageEntriesParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Clears all entries for a given origin's shared storage."""
        return await self.client.send(method="Storage.clearSharedStorageEntries", params=params,session_id=session_id)

    async def reset_shared_storage_budget(self, params: Optional[resetSharedStorageBudgetParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Resets the budget for `ownerOrigin` by clearing all budget withdrawals."""
        return await self.client.send(method="Storage.resetSharedStorageBudget", params=params,session_id=session_id)

    async def set_shared_storage_tracking(self, params: Optional[setSharedStorageTrackingParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Enables/disables issuing of sharedStorageAccessed events."""
        return await self.client.send(method="Storage.setSharedStorageTracking", params=params,session_id=session_id)

    async def set_storage_bucket_tracking(self, params: Optional[setStorageBucketTrackingParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Set tracking for a storage key's buckets."""
        return await self.client.send(method="Storage.setStorageBucketTracking", params=params,session_id=session_id)

    async def delete_storage_bucket(self, params: Optional[deleteStorageBucketParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Deletes the Storage Bucket with the given storage key and bucket name."""
        return await self.client.send(method="Storage.deleteStorageBucket", params=params,session_id=session_id)

    async def run_bounce_tracking_mitigations(self, params: None=None,session_id: Optional[str] = None) -> runBounceTrackingMitigationsReturns:
        """Deletes state for sites identified as potential bounce trackers, immediately."""
        return await self.client.send(method="Storage.runBounceTrackingMitigations", params=params,session_id=session_id)

    async def set_attribution_reporting_local_testing_mode(self, params: Optional[setAttributionReportingLocalTestingModeParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """https://wicg.github.io/attribution-reporting-api/"""
        return await self.client.send(method="Storage.setAttributionReportingLocalTestingMode", params=params,session_id=session_id)

    async def set_attribution_reporting_tracking(self, params: Optional[setAttributionReportingTrackingParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Enables/disables issuing of Attribution Reporting events."""
        return await self.client.send(method="Storage.setAttributionReportingTracking", params=params,session_id=session_id)

    async def send_pending_attribution_reports(self, params: None=None,session_id: Optional[str] = None) -> sendPendingAttributionReportsReturns:
        """Sends all pending Attribution Reports immediately, regardless of their scheduled report time."""
        return await self.client.send(method="Storage.sendPendingAttributionReports", params=params,session_id=session_id)

    async def get_related_website_sets(self, params: None=None,session_id: Optional[str] = None) -> getRelatedWebsiteSetsReturns:
        """Returns the effective Related Website Sets in use by this profile for the browser session. The effective Related Website Sets will not change during a browser session."""
        return await self.client.send(method="Storage.getRelatedWebsiteSets", params=params,session_id=session_id)

    async def get_affected_urls_for_third_party_cookie_metadata(self, params: Optional[getAffectedUrlsForThirdPartyCookieMetadataParameters]=None,session_id: Optional[str] = None) -> getAffectedUrlsForThirdPartyCookieMetadataReturns:
        """Returns the list of URLs from a page and its embedded resources that match existing grace period URL pattern rules. https://developers.google.com/privacy-sandbox/cookies/temporary-exceptions/grace-period"""
        return await self.client.send(method="Storage.getAffectedUrlsForThirdPartyCookieMetadata", params=params,session_id=session_id)

    async def set_protected_audience_k_anonymity(self, params: Optional[setProtectedAudienceKAnonymityParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        return await self.client.send(method="Storage.setProtectedAudienceKAnonymity", params=params,session_id=session_id)
