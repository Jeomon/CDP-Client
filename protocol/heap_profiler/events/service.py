
"""CDP HeapProfiler Events"""

from client.service import CDPClient
from typing import TypedDict, Optional, Callable
from protocol.heap_profiler.events.types import *

class HeapProfilerEvents:
    def __init__(self,client:CDPClient):
        self.client=client
    
    def on_add_heap_snapshot_chunk(self, callback: Callable[[addHeapSnapshotChunkEvent,Optional[str]], None]=None) -> None:
        self.client.on('HeapProfiler.addHeapSnapshotChunk', callback)
    
    def on_heap_stats_update(self, callback: Callable[[heapStatsUpdateEvent,Optional[str]], None]=None) -> None:
        """If heap objects tracking has been started then backend may send update for one or more fragments"""
        self.client.on('HeapProfiler.heapStatsUpdate', callback)
    
    def on_last_seen_object_id(self, callback: Callable[[lastSeenObjectIdEvent,Optional[str]], None]=None) -> None:
        """If heap objects tracking has been started then backend regularly sends a current value for last seen object id and corresponding timestamp. If the were changes in the heap since last event then one or more heapStatsUpdate events will be sent before a new lastSeenObjectId event."""
        self.client.on('HeapProfiler.lastSeenObjectId', callback)
    
    def on_report_heap_snapshot_progress(self, callback: Callable[[reportHeapSnapshotProgressEvent,Optional[str]], None]=None) -> None:
        self.client.on('HeapProfiler.reportHeapSnapshotProgress', callback)
    
    def on_reset_profiles(self, callback: Callable[[resetProfilesEvent,Optional[str]], None]=None) -> None:
        self.client.on('HeapProfiler.resetProfiles', callback)
     