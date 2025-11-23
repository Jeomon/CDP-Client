
"""CDP Memory Methods"""

from cdp_client.methods import CDPMethods
from typing import TypedDict,Optional
from memory.methods.types import *

class MemoryMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def get_dom_counters(self, params: None=None) -> getDOMCountersReturns:
        """Retruns current DOM object counters."""
        return await self.methods.send(method="Memory.getDOMCounters", params=params)

    async def get_dom_counters_for_leak_detection(self, params: None=None) -> getDOMCountersForLeakDetectionReturns:
        """Retruns DOM object counters after preparing renderer for leak detection."""
        return await self.methods.send(method="Memory.getDOMCountersForLeakDetection", params=params)

    async def prepare_for_leak_detection(self, params: None=None) -> Dict[str, Any]:
        """Prepares for leak detection by terminating workers, stopping spellcheckers, dropping non-essential internal caches, running garbage collections, etc."""
        return await self.methods.send(method="Memory.prepareForLeakDetection", params=params)

    async def forcibly_purge_java_script_memory(self, params: None=None) -> Dict[str, Any]:
        """Simulate OomIntervention by purging V8 memory."""
        return await self.methods.send(method="Memory.forciblyPurgeJavaScriptMemory", params=params)

    async def set_pressure_notifications_suppressed(self, params: Optional[setPressureNotificationsSuppressedParameters]=None) -> Dict[str, Any]:
        """Enable/disable suppressing memory pressure notifications in all processes."""
        return await self.methods.send(method="Memory.setPressureNotificationsSuppressed", params=params)

    async def simulate_pressure_notification(self, params: Optional[simulatePressureNotificationParameters]=None) -> Dict[str, Any]:
        """Simulate a memory pressure notification in all processes."""
        return await self.methods.send(method="Memory.simulatePressureNotification", params=params)

    async def start_sampling(self, params: Optional[startSamplingParameters]=None) -> Dict[str, Any]:
        """Start collecting native memory profile."""
        return await self.methods.send(method="Memory.startSampling", params=params)

    async def stop_sampling(self, params: None=None) -> Dict[str, Any]:
        """Stop collecting native memory profile."""
        return await self.methods.send(method="Memory.stopSampling", params=params)

    async def get_all_time_sampling_profile(self, params: None=None) -> getAllTimeSamplingProfileReturns:
        """Retrieve native memory allocations profile collected since renderer process startup."""
        return await self.methods.send(method="Memory.getAllTimeSamplingProfile", params=params)

    async def get_browser_sampling_profile(self, params: None=None) -> getBrowserSamplingProfileReturns:
        """Retrieve native memory allocations profile collected since browser process startup."""
        return await self.methods.send(method="Memory.getBrowserSamplingProfile", params=params)

    async def get_sampling_profile(self, params: None=None) -> getSamplingProfileReturns:
        """Retrieve native memory allocations profile collected since last `startSampling` call."""
        return await self.methods.send(method="Memory.getSamplingProfile", params=params)
