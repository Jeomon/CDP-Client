
"""CDP BackgroundService Methods Types"""

from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from protocol.background_service.types import ServiceName


class startObservingParameters(TypedDict, total=True):
    service: ServiceName


class stopObservingParameters(TypedDict, total=True):
    service: ServiceName


class setRecordingParameters(TypedDict, total=True):
    shouldRecord: bool
    service: ServiceName


class clearEventsParameters(TypedDict, total=True):
    service: ServiceName





