
"""CDP ServiceWorker Events"""

from cdp_client.events import CDPEvents
from typing import TypedDict, Optional, Callable
from service_worker.events.types import *

class ServiceWorkerEvents:
    def __init__(self,events:CDPEvents):
        self.events=events
    
    def on_worker_error_reported(self, callback: Callable[workerErrorReportedEvent, None]=None) -> None:
        self.events.on('workerErrorReported', callback)
    
    def on_worker_registration_updated(self, callback: Callable[workerRegistrationUpdatedEvent, None]=None) -> None:
        self.events.on('workerRegistrationUpdated', callback)
    
    def on_worker_version_updated(self, callback: Callable[workerVersionUpdatedEvent, None]=None) -> None:
        self.events.on('workerVersionUpdated', callback)
     