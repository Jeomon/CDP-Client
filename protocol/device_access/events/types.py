
"""CDP DeviceAccess Events"""

from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from protocol.device_access.types import PromptDevice
    from protocol.device_access.types import RequestId


class deviceRequestPromptedEvent(TypedDict, total=True):
    id: 'RequestId'
    devices: 'List[PromptDevice]'

