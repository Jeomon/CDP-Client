
"""CDP BackgroundService Events"""

from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from background_service.types import BackgroundServiceEvent
    from background_service.types import ServiceName


class recordingStateChangedEvent(TypedDict, total=True):
    isRecording: bool
    service: ServiceName


class backgroundServiceEventReceivedEvent(TypedDict, total=True):
    backgroundServiceEvent: BackgroundServiceEvent

