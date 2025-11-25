
"""CDP HeapProfiler Methods"""

from client.methods import CDPMethods
from typing import TypedDict,Optional
from protocol.heap_profiler.methods.types import *

class HeapProfilerMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def add_inspected_heap_object(self, params: Optional[addInspectedHeapObjectParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Enables console to refer to the node with given id via $x (see Command Line API for more details $x functions)."""
        return await self.methods.send(method="HeapProfiler.addInspectedHeapObject", params=params,session_id=session_id)

    async def collect_garbage(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        return await self.methods.send(method="HeapProfiler.collectGarbage", params=params,session_id=session_id)

    async def disable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        return await self.methods.send(method="HeapProfiler.disable", params=params,session_id=session_id)

    async def enable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        return await self.methods.send(method="HeapProfiler.enable", params=params,session_id=session_id)

    async def get_heap_object_id(self, params: Optional[getHeapObjectIdParameters]=None,session_id: Optional[str] = None) -> getHeapObjectIdReturns:
        return await self.methods.send(method="HeapProfiler.getHeapObjectId", params=params,session_id=session_id)

    async def get_object_by_heap_object_id(self, params: Optional[getObjectByHeapObjectIdParameters]=None,session_id: Optional[str] = None) -> getObjectByHeapObjectIdReturns:
        return await self.methods.send(method="HeapProfiler.getObjectByHeapObjectId", params=params,session_id=session_id)

    async def get_sampling_profile(self, params: None=None,session_id: Optional[str] = None) -> getSamplingProfileReturns:
        return await self.methods.send(method="HeapProfiler.getSamplingProfile", params=params,session_id=session_id)

    async def start_sampling(self, params: Optional[startSamplingParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        return await self.methods.send(method="HeapProfiler.startSampling", params=params,session_id=session_id)

    async def start_tracking_heap_objects(self, params: Optional[startTrackingHeapObjectsParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        return await self.methods.send(method="HeapProfiler.startTrackingHeapObjects", params=params,session_id=session_id)

    async def stop_sampling(self, params: None=None,session_id: Optional[str] = None) -> stopSamplingReturns:
        return await self.methods.send(method="HeapProfiler.stopSampling", params=params,session_id=session_id)

    async def stop_tracking_heap_objects(self, params: Optional[stopTrackingHeapObjectsParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        return await self.methods.send(method="HeapProfiler.stopTrackingHeapObjects", params=params,session_id=session_id)

    async def take_heap_snapshot(self, params: Optional[takeHeapSnapshotParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        return await self.methods.send(method="HeapProfiler.takeHeapSnapshot", params=params,session_id=session_id)
