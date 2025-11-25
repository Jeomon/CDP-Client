
"""CDP Storage Methods"""

from client.methods import CDPMethods
from typing import TypedDict,Optional
from protocol.storage.methods.types import *

class StorageMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def get_storage_key(self, params: Optional[getStorageKeyParameters]=None) -> getStorageKeyReturns:
        """Returns storage key for the given frame. If no frame ID is provided, the storage key of the target executing this command is returned."""
        return await self.methods.send(method="Storage.getStorageKey", params=params)

    async def clear_data_for_origin(self, params: Optional[clearDataForOriginParameters]=None) -> Dict[str, Any]:
        """Clears storage for origin."""
        return await self.methods.send(method="Storage.clearDataForOrigin", params=params)

    async def clear_data_for_storage_key(self, params: Optional[clearDataForStorageKeyParameters]=None) -> Dict[str, Any]:
        """Clears storage for storage key."""
        return await self.methods.send(method="Storage.clearDataForStorageKey", params=params)

    async def get_cookies(self, params: Optional[getCookiesParameters]=None) -> getCookiesReturns:
        """Returns all browser cookies."""
        return await self.methods.send(method="Storage.getCookies", params=params)

    async def set_cookies(self, params: Optional[setCookiesParameters]=None) -> Dict[str, Any]:
        """Sets given cookies."""
        return await self.methods.send(method="Storage.setCookies", params=params)

    async def clear_cookies(self, params: Optional[clearCookiesParameters]=None) -> Dict[str, Any]:
        """Clears cookies."""
        return await self.methods.send(method="Storage.clearCookies", params=params)

    async def get_usage_and_quota(self, params: Optional[getUsageAndQuotaParameters]=None) -> getUsageAndQuotaReturns:
        """Returns usage and quota in bytes."""
        return await self.methods.send(method="Storage.getUsageAndQuota", params=params)

    async def override_quota_for_origin(self, params: Optional[overrideQuotaForOriginParameters]=None) -> Dict[str, Any]:
        """Override quota for the specified origin"""
        return await self.methods.send(method="Storage.overrideQuotaForOrigin", params=params)

    async def track_cache_storage_for_origin(self, params: Optional[trackCacheStorageForOriginParameters]=None) -> Dict[str, Any]:
        """Registers origin to be notified when an update occurs to its cache storage list."""
        return await self.methods.send(method="Storage.trackCacheStorageForOrigin", params=params)

    async def track_cache_storage_for_storage_key(self, params: Optional[trackCacheStorageForStorageKeyParameters]=None) -> Dict[str, Any]:
        """Registers storage key to be notified when an update occurs to its cache storage list."""
        return await self.methods.send(method="Storage.trackCacheStorageForStorageKey", params=params)

    async def track_indexed_db_for_origin(self, params: Optional[trackIndexedDBForOriginParameters]=None) -> Dict[str, Any]:
        """Registers origin to be notified when an update occurs to its IndexedDB."""
        return await self.methods.send(method="Storage.trackIndexedDBForOrigin", params=params)

    async def track_indexed_db_for_storage_key(self, params: Optional[trackIndexedDBForStorageKeyParameters]=None) -> Dict[str, Any]:
        """Registers storage key to be notified when an update occurs to its IndexedDB."""
        return await self.methods.send(method="Storage.trackIndexedDBForStorageKey", params=params)

    async def untrack_cache_storage_for_origin(self, params: Optional[untrackCacheStorageForOriginParameters]=None) -> Dict[str, Any]:
        """Unregisters origin from receiving notifications for cache storage."""
        return await self.methods.send(method="Storage.untrackCacheStorageForOrigin", params=params)

    async def untrack_cache_storage_for_storage_key(self, params: Optional[untrackCacheStorageForStorageKeyParameters]=None) -> Dict[str, Any]:
        """Unregisters storage key from receiving notifications for cache storage."""
        return await self.methods.send(method="Storage.untrackCacheStorageForStorageKey", params=params)

    async def untrack_indexed_db_for_origin(self, params: Optional[untrackIndexedDBForOriginParameters]=None) -> Dict[str, Any]:
        """Unregisters origin from receiving notifications for IndexedDB."""
        return await self.methods.send(method="Storage.untrackIndexedDBForOrigin", params=params)

    async def untrack_indexed_db_for_storage_key(self, params: Optional[untrackIndexedDBForStorageKeyParameters]=None) -> Dict[str, Any]:
        """Unregisters storage key from receiving notifications for IndexedDB."""
        return await self.methods.send(method="Storage.untrackIndexedDBForStorageKey", params=params)

    async def get_trust_tokens(self, params: None=None) -> getTrustTokensReturns:
        """Returns the number of stored Trust Tokens per issuer for the current browsing context."""
        return await self.methods.send(method="Storage.getTrustTokens", params=params)

    async def clear_trust_tokens(self, params: Optional[clearTrustTokensParameters]=None) -> clearTrustTokensReturns:
        """Removes all Trust Tokens issued by the provided issuerOrigin. Leaves other stored data, including the issuer's Redemption Records, intact."""
        return await self.methods.send(method="Storage.clearTrustTokens", params=params)

    async def get_interest_group_details(self, params: Optional[getInterestGroupDetailsParameters]=None) -> getInterestGroupDetailsReturns:
        """Gets details for a named interest group."""
        return await self.methods.send(method="Storage.getInterestGroupDetails", params=params)

    async def set_interest_group_tracking(self, params: Optional[setInterestGroupTrackingParameters]=None) -> Dict[str, Any]:
        """Enables/Disables issuing of interestGroupAccessed events."""
        return await self.methods.send(method="Storage.setInterestGroupTracking", params=params)

    async def set_interest_group_auction_tracking(self, params: Optional[setInterestGroupAuctionTrackingParameters]=None) -> Dict[str, Any]:
        """Enables/Disables issuing of interestGroupAuctionEventOccurred and interestGroupAuctionNetworkRequestCreated."""
        return await self.methods.send(method="Storage.setInterestGroupAuctionTracking", params=params)

    async def get_shared_storage_metadata(self, params: Optional[getSharedStorageMetadataParameters]=None) -> getSharedStorageMetadataReturns:
        """Gets metadata for an origin's shared storage."""
        return await self.methods.send(method="Storage.getSharedStorageMetadata", params=params)

    async def get_shared_storage_entries(self, params: Optional[getSharedStorageEntriesParameters]=None) -> getSharedStorageEntriesReturns:
        """Gets the entries in an given origin's shared storage."""
        return await self.methods.send(method="Storage.getSharedStorageEntries", params=params)

    async def set_shared_storage_entry(self, params: Optional[setSharedStorageEntryParameters]=None) -> Dict[str, Any]:
        """Sets entry with `key` and `value` for a given origin's shared storage."""
        return await self.methods.send(method="Storage.setSharedStorageEntry", params=params)

    async def delete_shared_storage_entry(self, params: Optional[deleteSharedStorageEntryParameters]=None) -> Dict[str, Any]:
        """Deletes entry for `key` (if it exists) for a given origin's shared storage."""
        return await self.methods.send(method="Storage.deleteSharedStorageEntry", params=params)

    async def clear_shared_storage_entries(self, params: Optional[clearSharedStorageEntriesParameters]=None) -> Dict[str, Any]:
        """Clears all entries for a given origin's shared storage."""
        return await self.methods.send(method="Storage.clearSharedStorageEntries", params=params)

    async def reset_shared_storage_budget(self, params: Optional[resetSharedStorageBudgetParameters]=None) -> Dict[str, Any]:
        """Resets the budget for `ownerOrigin` by clearing all budget withdrawals."""
        return await self.methods.send(method="Storage.resetSharedStorageBudget", params=params)

    async def set_shared_storage_tracking(self, params: Optional[setSharedStorageTrackingParameters]=None) -> Dict[str, Any]:
        """Enables/disables issuing of sharedStorageAccessed events."""
        return await self.methods.send(method="Storage.setSharedStorageTracking", params=params)

    async def set_storage_bucket_tracking(self, params: Optional[setStorageBucketTrackingParameters]=None) -> Dict[str, Any]:
        """Set tracking for a storage key's buckets."""
        return await self.methods.send(method="Storage.setStorageBucketTracking", params=params)

    async def delete_storage_bucket(self, params: Optional[deleteStorageBucketParameters]=None) -> Dict[str, Any]:
        """Deletes the Storage Bucket with the given storage key and bucket name."""
        return await self.methods.send(method="Storage.deleteStorageBucket", params=params)

    async def run_bounce_tracking_mitigations(self, params: None=None) -> runBounceTrackingMitigationsReturns:
        """Deletes state for sites identified as potential bounce trackers, immediately."""
        return await self.methods.send(method="Storage.runBounceTrackingMitigations", params=params)

    async def set_attribution_reporting_local_testing_mode(self, params: Optional[setAttributionReportingLocalTestingModeParameters]=None) -> Dict[str, Any]:
        """https://wicg.github.io/attribution-reporting-api/"""
        return await self.methods.send(method="Storage.setAttributionReportingLocalTestingMode", params=params)

    async def set_attribution_reporting_tracking(self, params: Optional[setAttributionReportingTrackingParameters]=None) -> Dict[str, Any]:
        """Enables/disables issuing of Attribution Reporting events."""
        return await self.methods.send(method="Storage.setAttributionReportingTracking", params=params)

    async def send_pending_attribution_reports(self, params: None=None) -> sendPendingAttributionReportsReturns:
        """Sends all pending Attribution Reports immediately, regardless of their scheduled report time."""
        return await self.methods.send(method="Storage.sendPendingAttributionReports", params=params)

    async def get_related_website_sets(self, params: None=None) -> getRelatedWebsiteSetsReturns:
        """Returns the effective Related Website Sets in use by this profile for the browser session. The effective Related Website Sets will not change during a browser session."""
        return await self.methods.send(method="Storage.getRelatedWebsiteSets", params=params)

    async def get_affected_urls_for_third_party_cookie_metadata(self, params: Optional[getAffectedUrlsForThirdPartyCookieMetadataParameters]=None) -> getAffectedUrlsForThirdPartyCookieMetadataReturns:
        """Returns the list of URLs from a page and its embedded resources that match existing grace period URL pattern rules. https://developers.google.com/privacy-sandbox/cookies/temporary-exceptions/grace-period"""
        return await self.methods.send(method="Storage.getAffectedUrlsForThirdPartyCookieMetadata", params=params)

    async def set_protected_audience_k_anonymity(self, params: Optional[setProtectedAudienceKAnonymityParameters]=None) -> Dict[str, Any]:
        return await self.methods.send(method="Storage.setProtectedAudienceKAnonymity", params=params)
