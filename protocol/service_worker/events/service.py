
"""CDP ServiceWorker Events"""

from client.events import CDPEvents
from typing import TypedDict, Optional, Callable
from protocol.service_worker.events.types import *

class ServiceWorkerEvents:
    def __init__(self,events:CDPEvents):
        self.events=events
    
    def on_worker_error_reported(self, callback: Callable[[workerErrorReportedEvent,Optional[str]], None]=None) -> None:
        self.events.on('workerErrorReported', callback)
    
    def on_worker_registration_updated(self, callback: Callable[[workerRegistrationUpdatedEvent,Optional[str]], None]=None) -> None:
        self.events.on('workerRegistrationUpdated', callback)
    
    def on_worker_version_updated(self, callback: Callable[[workerVersionUpdatedEvent,Optional[str]], None]=None) -> None:
        self.events.on('workerVersionUpdated', callback)
     