
"""CDP LayerTree Methods"""

from client.methods import CDPMethods
from typing import TypedDict,Optional
from protocol.layer_tree.methods.types import *

class LayerTreeMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def compositing_reasons(self, params: Optional[compositingReasonsParameters]=None,session_id: Optional[str] = None) -> compositingReasonsReturns:
        """Provides the reasons why the given layer was composited."""
        return await self.methods.send(method="LayerTree.compositingReasons", params=params,session_id=session_id)

    async def disable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Disables compositing tree inspection."""
        return await self.methods.send(method="LayerTree.disable", params=params,session_id=session_id)

    async def enable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Enables compositing tree inspection."""
        return await self.methods.send(method="LayerTree.enable", params=params,session_id=session_id)

    async def load_snapshot(self, params: Optional[loadSnapshotParameters]=None,session_id: Optional[str] = None) -> loadSnapshotReturns:
        """Returns the snapshot identifier."""
        return await self.methods.send(method="LayerTree.loadSnapshot", params=params,session_id=session_id)

    async def make_snapshot(self, params: Optional[makeSnapshotParameters]=None,session_id: Optional[str] = None) -> makeSnapshotReturns:
        """Returns the layer snapshot identifier."""
        return await self.methods.send(method="LayerTree.makeSnapshot", params=params,session_id=session_id)

    async def profile_snapshot(self, params: Optional[profileSnapshotParameters]=None,session_id: Optional[str] = None) -> profileSnapshotReturns:
        return await self.methods.send(method="LayerTree.profileSnapshot", params=params,session_id=session_id)

    async def release_snapshot(self, params: Optional[releaseSnapshotParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Releases layer snapshot captured by the back-end."""
        return await self.methods.send(method="LayerTree.releaseSnapshot", params=params,session_id=session_id)

    async def replay_snapshot(self, params: Optional[replaySnapshotParameters]=None,session_id: Optional[str] = None) -> replaySnapshotReturns:
        """Replays the layer snapshot and returns the resulting bitmap."""
        return await self.methods.send(method="LayerTree.replaySnapshot", params=params,session_id=session_id)

    async def snapshot_command_log(self, params: Optional[snapshotCommandLogParameters]=None,session_id: Optional[str] = None) -> snapshotCommandLogReturns:
        """Replays the layer snapshot and returns canvas log."""
        return await self.methods.send(method="LayerTree.snapshotCommandLog", params=params,session_id=session_id)
