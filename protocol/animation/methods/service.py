
"""CDP Animation Methods"""

from client.methods import CDPMethods
from typing import TypedDict,Optional
from protocol.animation.methods.types import *

class AnimationMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def disable(self, params: None=None) -> Dict[str, Any]:
        """Disables animation domain notifications."""
        return await self.methods.send(method="Animation.disable", params=params)

    async def enable(self, params: None=None) -> Dict[str, Any]:
        """Enables animation domain notifications."""
        return await self.methods.send(method="Animation.enable", params=params)

    async def get_current_time(self, params: Optional[getCurrentTimeParameters]=None) -> getCurrentTimeReturns:
        """Returns the current time of the an animation."""
        return await self.methods.send(method="Animation.getCurrentTime", params=params)

    async def get_playback_rate(self, params: None=None) -> getPlaybackRateReturns:
        """Gets the playback rate of the document timeline."""
        return await self.methods.send(method="Animation.getPlaybackRate", params=params)

    async def release_animations(self, params: Optional[releaseAnimationsParameters]=None) -> Dict[str, Any]:
        """Releases a set of animations to no longer be manipulated."""
        return await self.methods.send(method="Animation.releaseAnimations", params=params)

    async def resolve_animation(self, params: Optional[resolveAnimationParameters]=None) -> resolveAnimationReturns:
        """Gets the remote object of the Animation."""
        return await self.methods.send(method="Animation.resolveAnimation", params=params)

    async def seek_animations(self, params: Optional[seekAnimationsParameters]=None) -> Dict[str, Any]:
        """Seek a set of animations to a particular time within each animation."""
        return await self.methods.send(method="Animation.seekAnimations", params=params)

    async def set_paused(self, params: Optional[setPausedParameters]=None) -> Dict[str, Any]:
        """Sets the paused state of a set of animations."""
        return await self.methods.send(method="Animation.setPaused", params=params)

    async def set_playback_rate(self, params: Optional[setPlaybackRateParameters]=None) -> Dict[str, Any]:
        """Sets the playback rate of the document timeline."""
        return await self.methods.send(method="Animation.setPlaybackRate", params=params)

    async def set_timing(self, params: Optional[setTimingParameters]=None) -> Dict[str, Any]:
        """Sets the timing of an animation node."""
        return await self.methods.send(method="Animation.setTiming", params=params)
