
"""CDP Animation Methods"""

from client.methods import CDPMethods
from typing import TypedDict,Optional
from protocol.animation.methods.types import *

class AnimationMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def disable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Disables animation domain notifications."""
        return await self.methods.send(method="Animation.disable", params=params,session_id=session_id)

    async def enable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Enables animation domain notifications."""
        return await self.methods.send(method="Animation.enable", params=params,session_id=session_id)

    async def get_current_time(self, params: Optional[getCurrentTimeParameters]=None,session_id: Optional[str] = None) -> getCurrentTimeReturns:
        """Returns the current time of the an animation."""
        return await self.methods.send(method="Animation.getCurrentTime", params=params,session_id=session_id)

    async def get_playback_rate(self, params: None=None,session_id: Optional[str] = None) -> getPlaybackRateReturns:
        """Gets the playback rate of the document timeline."""
        return await self.methods.send(method="Animation.getPlaybackRate", params=params,session_id=session_id)

    async def release_animations(self, params: Optional[releaseAnimationsParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Releases a set of animations to no longer be manipulated."""
        return await self.methods.send(method="Animation.releaseAnimations", params=params,session_id=session_id)

    async def resolve_animation(self, params: Optional[resolveAnimationParameters]=None,session_id: Optional[str] = None) -> resolveAnimationReturns:
        """Gets the remote object of the Animation."""
        return await self.methods.send(method="Animation.resolveAnimation", params=params,session_id=session_id)

    async def seek_animations(self, params: Optional[seekAnimationsParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Seek a set of animations to a particular time within each animation."""
        return await self.methods.send(method="Animation.seekAnimations", params=params,session_id=session_id)

    async def set_paused(self, params: Optional[setPausedParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Sets the paused state of a set of animations."""
        return await self.methods.send(method="Animation.setPaused", params=params,session_id=session_id)

    async def set_playback_rate(self, params: Optional[setPlaybackRateParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Sets the playback rate of the document timeline."""
        return await self.methods.send(method="Animation.setPlaybackRate", params=params,session_id=session_id)

    async def set_timing(self, params: Optional[setTimingParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Sets the timing of an animation node."""
        return await self.methods.send(method="Animation.setTiming", params=params,session_id=session_id)
