
"""CDP Memory Methods"""

from client.methods import CDPMethods
from typing import TypedDict,Optional
from protocol.memory.methods.types import *

class MemoryMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def get_dom_counters(self, params: None=None,session_id: Optional[str] = None) -> getDOMCountersReturns:
        """Retruns current DOM object counters."""
        return await self.methods.send(method="Memory.getDOMCounters", params=params,session_id=session_id)

    async def get_dom_counters_for_leak_detection(self, params: None=None,session_id: Optional[str] = None) -> getDOMCountersForLeakDetectionReturns:
        """Retruns DOM object counters after preparing renderer for leak detection."""
        return await self.methods.send(method="Memory.getDOMCountersForLeakDetection", params=params,session_id=session_id)

    async def prepare_for_leak_detection(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Prepares for leak detection by terminating workers, stopping spellcheckers, dropping non-essential internal caches, running garbage collections, etc."""
        return await self.methods.send(method="Memory.prepareForLeakDetection", params=params,session_id=session_id)

    async def forcibly_purge_java_script_memory(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Simulate OomIntervention by purging V8 memory."""
        return await self.methods.send(method="Memory.forciblyPurgeJavaScriptMemory", params=params,session_id=session_id)

    async def set_pressure_notifications_suppressed(self, params: Optional[setPressureNotificationsSuppressedParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Enable/disable suppressing memory pressure notifications in all processes."""
        return await self.methods.send(method="Memory.setPressureNotificationsSuppressed", params=params,session_id=session_id)

    async def simulate_pressure_notification(self, params: Optional[simulatePressureNotificationParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Simulate a memory pressure notification in all processes."""
        return await self.methods.send(method="Memory.simulatePressureNotification", params=params,session_id=session_id)

    async def start_sampling(self, params: Optional[startSamplingParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Start collecting native memory profile."""
        return await self.methods.send(method="Memory.startSampling", params=params,session_id=session_id)

    async def stop_sampling(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Stop collecting native memory profile."""
        return await self.methods.send(method="Memory.stopSampling", params=params,session_id=session_id)

    async def get_all_time_sampling_profile(self, params: None=None,session_id: Optional[str] = None) -> getAllTimeSamplingProfileReturns:
        """Retrieve native memory allocations profile collected since renderer process startup."""
        return await self.methods.send(method="Memory.getAllTimeSamplingProfile", params=params,session_id=session_id)

    async def get_browser_sampling_profile(self, params: None=None,session_id: Optional[str] = None) -> getBrowserSamplingProfileReturns:
        """Retrieve native memory allocations profile collected since browser process startup."""
        return await self.methods.send(method="Memory.getBrowserSamplingProfile", params=params,session_id=session_id)

    async def get_sampling_profile(self, params: None=None,session_id: Optional[str] = None) -> getSamplingProfileReturns:
        """Retrieve native memory allocations profile collected since last `startSampling` call."""
        return await self.methods.send(method="Memory.getSamplingProfile", params=params,session_id=session_id)
