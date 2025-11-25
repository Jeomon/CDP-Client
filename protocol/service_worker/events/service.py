
"""CDP ServiceWorker Events"""

from client.service import CDPClient
from typing import TypedDict, Optional, Callable
from protocol.service_worker.events.types import *

class ServiceWorkerEvents:
    def __init__(self,client:CDPClient):
        self.client=client
    
    def on_worker_error_reported(self, callback: Callable[[workerErrorReportedEvent,Optional[str]], None]=None) -> None:
        self.client.on('workerErrorReported', callback)
    
    def on_worker_registration_updated(self, callback: Callable[[workerRegistrationUpdatedEvent,Optional[str]], None]=None) -> None:
        self.client.on('workerRegistrationUpdated', callback)
    
    def on_worker_version_updated(self, callback: Callable[[workerVersionUpdatedEvent,Optional[str]], None]=None) -> None:
        self.client.on('workerVersionUpdated', callback)
     