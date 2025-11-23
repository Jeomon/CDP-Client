
"""CDP ServiceWorker Methods"""

from cdp_client.methods import CDPMethods
from typing import TypedDict,Optional
from service_worker.methods.types import *

class ServiceWorkerMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def deliver_push_message(self, params: Optional[deliverPushMessageParameters]=None) -> Dict[str, Any]:
        return await self.methods.send(method="ServiceWorker.deliverPushMessage", params=params)

    async def disable(self, params: None=None) -> Dict[str, Any]:
        return await self.methods.send(method="ServiceWorker.disable", params=params)

    async def dispatch_sync_event(self, params: Optional[dispatchSyncEventParameters]=None) -> Dict[str, Any]:
        return await self.methods.send(method="ServiceWorker.dispatchSyncEvent", params=params)

    async def dispatch_periodic_sync_event(self, params: Optional[dispatchPeriodicSyncEventParameters]=None) -> Dict[str, Any]:
        return await self.methods.send(method="ServiceWorker.dispatchPeriodicSyncEvent", params=params)

    async def enable(self, params: None=None) -> Dict[str, Any]:
        return await self.methods.send(method="ServiceWorker.enable", params=params)

    async def set_force_update_on_page_load(self, params: Optional[setForceUpdateOnPageLoadParameters]=None) -> Dict[str, Any]:
        return await self.methods.send(method="ServiceWorker.setForceUpdateOnPageLoad", params=params)

    async def skip_waiting(self, params: Optional[skipWaitingParameters]=None) -> Dict[str, Any]:
        return await self.methods.send(method="ServiceWorker.skipWaiting", params=params)

    async def start_worker(self, params: Optional[startWorkerParameters]=None) -> Dict[str, Any]:
        return await self.methods.send(method="ServiceWorker.startWorker", params=params)

    async def stop_all_workers(self, params: None=None) -> Dict[str, Any]:
        return await self.methods.send(method="ServiceWorker.stopAllWorkers", params=params)

    async def stop_worker(self, params: Optional[stopWorkerParameters]=None) -> Dict[str, Any]:
        return await self.methods.send(method="ServiceWorker.stopWorker", params=params)

    async def unregister(self, params: Optional[unregisterParameters]=None) -> Dict[str, Any]:
        return await self.methods.send(method="ServiceWorker.unregister", params=params)

    async def update_registration(self, params: Optional[updateRegistrationParameters]=None) -> Dict[str, Any]:
        return await self.methods.send(method="ServiceWorker.updateRegistration", params=params)
