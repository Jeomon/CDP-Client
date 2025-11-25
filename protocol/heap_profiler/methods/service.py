
"""CDP HeapProfiler Methods"""

from client.methods import CDPMethods
from typing import TypedDict,Optional
from protocol.heap_profiler.methods.types import *

class HeapProfilerMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def add_inspected_heap_object(self, params: Optional[addInspectedHeapObjectParameters]=None) -> Dict[str, Any]:
        """Enables console to refer to the node with given id via $x (see Command Line API for more details $x functions)."""
        return await self.methods.send(method="HeapProfiler.addInspectedHeapObject", params=params)

    async def collect_garbage(self, params: None=None) -> Dict[str, Any]:
        return await self.methods.send(method="HeapProfiler.collectGarbage", params=params)

    async def disable(self, params: None=None) -> Dict[str, Any]:
        return await self.methods.send(method="HeapProfiler.disable", params=params)

    async def enable(self, params: None=None) -> Dict[str, Any]:
        return await self.methods.send(method="HeapProfiler.enable", params=params)

    async def get_heap_object_id(self, params: Optional[getHeapObjectIdParameters]=None) -> getHeapObjectIdReturns:
        return await self.methods.send(method="HeapProfiler.getHeapObjectId", params=params)

    async def get_object_by_heap_object_id(self, params: Optional[getObjectByHeapObjectIdParameters]=None) -> getObjectByHeapObjectIdReturns:
        return await self.methods.send(method="HeapProfiler.getObjectByHeapObjectId", params=params)

    async def get_sampling_profile(self, params: None=None) -> getSamplingProfileReturns:
        return await self.methods.send(method="HeapProfiler.getSamplingProfile", params=params)

    async def start_sampling(self, params: Optional[startSamplingParameters]=None) -> Dict[str, Any]:
        return await self.methods.send(method="HeapProfiler.startSampling", params=params)

    async def start_tracking_heap_objects(self, params: Optional[startTrackingHeapObjectsParameters]=None) -> Dict[str, Any]:
        return await self.methods.send(method="HeapProfiler.startTrackingHeapObjects", params=params)

    async def stop_sampling(self, params: None=None) -> stopSamplingReturns:
        return await self.methods.send(method="HeapProfiler.stopSampling", params=params)

    async def stop_tracking_heap_objects(self, params: Optional[stopTrackingHeapObjectsParameters]=None) -> Dict[str, Any]:
        return await self.methods.send(method="HeapProfiler.stopTrackingHeapObjects", params=params)

    async def take_heap_snapshot(self, params: Optional[takeHeapSnapshotParameters]=None) -> Dict[str, Any]:
        return await self.methods.send(method="HeapProfiler.takeHeapSnapshot", params=params)
