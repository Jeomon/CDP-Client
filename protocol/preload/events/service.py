
"""CDP Preload Events"""

from client.events import CDPEvents
from typing import TypedDict, Optional, Callable
from protocol.preload.events.types import *

class PreloadEvents:
    def __init__(self,events:CDPEvents):
        self.events=events
    
    def on_rule_set_updated(self, callback: Callable[[ruleSetUpdatedEvent,Optional[str]], None]=None) -> None:
        """Upsert. Currently, it is only emitted when a rule set added."""
        self.events.on('ruleSetUpdated', callback)
    
    def on_rule_set_removed(self, callback: Callable[[ruleSetRemovedEvent,Optional[str]], None]=None) -> None:
        self.events.on('ruleSetRemoved', callback)
    
    def on_preload_enabled_state_updated(self, callback: Callable[[preloadEnabledStateUpdatedEvent,Optional[str]], None]=None) -> None:
        """Fired when a preload enabled state is updated."""
        self.events.on('preloadEnabledStateUpdated', callback)
    
    def on_prefetch_status_updated(self, callback: Callable[[prefetchStatusUpdatedEvent,Optional[str]], None]=None) -> None:
        """Fired when a prefetch attempt is updated."""
        self.events.on('prefetchStatusUpdated', callback)
    
    def on_prerender_status_updated(self, callback: Callable[[prerenderStatusUpdatedEvent,Optional[str]], None]=None) -> None:
        """Fired when a prerender attempt is updated."""
        self.events.on('prerenderStatusUpdated', callback)
    
    def on_preloading_attempt_sources_updated(self, callback: Callable[[preloadingAttemptSourcesUpdatedEvent,Optional[str]], None]=None) -> None:
        """Send a list of sources for all preloading attempts in a document."""
        self.events.on('preloadingAttemptSourcesUpdated', callback)
     