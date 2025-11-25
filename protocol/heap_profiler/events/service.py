
"""CDP HeapProfiler Events"""

from client.events import CDPEvents
from typing import TypedDict, Optional, Callable
from protocol.heap_profiler.events.types import *

class HeapProfilerEvents:
    def __init__(self,events:CDPEvents):
        self.events=events
    
    def on_add_heap_snapshot_chunk(self, callback: Callable[addHeapSnapshotChunkEvent, None]=None) -> None:
        self.events.on('addHeapSnapshotChunk', callback)
    
    def on_heap_stats_update(self, callback: Callable[heapStatsUpdateEvent, None]=None) -> None:
        """If heap objects tracking has been started then backend may send update for one or more fragments"""
        self.events.on('heapStatsUpdate', callback)
    
    def on_last_seen_object_id(self, callback: Callable[lastSeenObjectIdEvent, None]=None) -> None:
        """If heap objects tracking has been started then backend regularly sends a current value for last seen object id and corresponding timestamp. If the were changes in the heap since last event then one or more heapStatsUpdate events will be sent before a new lastSeenObjectId event."""
        self.events.on('lastSeenObjectId', callback)
    
    def on_report_heap_snapshot_progress(self, callback: Callable[reportHeapSnapshotProgressEvent, None]=None) -> None:
        self.events.on('reportHeapSnapshotProgress', callback)
    
    def on_reset_profiles(self, callback: Callable[resetProfilesEvent, None]=None) -> None:
        self.events.on('resetProfiles', callback)
     