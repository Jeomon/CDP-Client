
"""CDP ServiceWorker Methods"""

from client.methods import CDPMethods
from typing import TypedDict,Optional
from protocol.service_worker.methods.types import *

class ServiceWorkerMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def deliver_push_message(self, params: Optional[deliverPushMessageParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        return await self.methods.send(method="ServiceWorker.deliverPushMessage", params=params,session_id=session_id)

    async def disable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        return await self.methods.send(method="ServiceWorker.disable", params=params,session_id=session_id)

    async def dispatch_sync_event(self, params: Optional[dispatchSyncEventParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        return await self.methods.send(method="ServiceWorker.dispatchSyncEvent", params=params,session_id=session_id)

    async def dispatch_periodic_sync_event(self, params: Optional[dispatchPeriodicSyncEventParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        return await self.methods.send(method="ServiceWorker.dispatchPeriodicSyncEvent", params=params,session_id=session_id)

    async def enable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        return await self.methods.send(method="ServiceWorker.enable", params=params,session_id=session_id)

    async def set_force_update_on_page_load(self, params: Optional[setForceUpdateOnPageLoadParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        return await self.methods.send(method="ServiceWorker.setForceUpdateOnPageLoad", params=params,session_id=session_id)

    async def skip_waiting(self, params: Optional[skipWaitingParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        return await self.methods.send(method="ServiceWorker.skipWaiting", params=params,session_id=session_id)

    async def start_worker(self, params: Optional[startWorkerParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        return await self.methods.send(method="ServiceWorker.startWorker", params=params,session_id=session_id)

    async def stop_all_workers(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        return await self.methods.send(method="ServiceWorker.stopAllWorkers", params=params,session_id=session_id)

    async def stop_worker(self, params: Optional[stopWorkerParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        return await self.methods.send(method="ServiceWorker.stopWorker", params=params,session_id=session_id)

    async def unregister(self, params: Optional[unregisterParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        return await self.methods.send(method="ServiceWorker.unregister", params=params,session_id=session_id)

    async def update_registration(self, params: Optional[updateRegistrationParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        return await self.methods.send(method="ServiceWorker.updateRegistration", params=params,session_id=session_id)
