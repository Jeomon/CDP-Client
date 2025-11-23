
"""CDP Accessibility Events"""

from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from accessibility.types import AXNode


class loadCompleteEvent(TypedDict, total=True):
    root: AXNode
    """New document root node."""


class nodesUpdatedEvent(TypedDict, total=True):
    nodes: List[AXNode]
    """Updated node data."""

