
"""CDP Profiler Events"""

from client.events import CDPEvents
from typing import TypedDict, Optional, Callable
from protocol.profiler.events.types import *

class ProfilerEvents:
    def __init__(self,events:CDPEvents):
        self.events=events
    
    def on_console_profile_finished(self, callback: Callable[consoleProfileFinishedEvent, None]=None) -> None:
        self.events.on('consoleProfileFinished', callback)
    
    def on_console_profile_started(self, callback: Callable[consoleProfileStartedEvent, None]=None) -> None:
        """Sent when new profile recording is started using console.profile() call."""
        self.events.on('consoleProfileStarted', callback)
    
    def on_precise_coverage_delta_update(self, callback: Callable[preciseCoverageDeltaUpdateEvent, None]=None) -> None:
        """Reports coverage delta since the last poll (either from an event like this, or from `takePreciseCoverage` for the current isolate. May only be sent if precise code coverage has been started. This event can be trigged by the embedder to, for example, trigger collection of coverage data immediately at a certain point in time."""
        self.events.on('preciseCoverageDeltaUpdate', callback)
     