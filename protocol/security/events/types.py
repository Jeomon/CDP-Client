
"""CDP Security Events"""

from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from protocol.security.types import VisibleSecurityState


class visibleSecurityStateChangedEvent(TypedDict, total=True):
    visibleSecurityState: 'VisibleSecurityState'
    """Security state information about the page."""

