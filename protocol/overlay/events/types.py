
"""CDP Overlay Events"""

from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from protocol.dom.types import BackendNodeId
    from protocol.dom.types import NodeId
    from protocol.page.types import Viewport


class inspectNodeRequestedEvent(TypedDict, total=True):
    backendNodeId: 'BackendNodeId'
    """Id of the node to inspect."""


class nodeHighlightRequestedEvent(TypedDict, total=True):
    nodeId: 'NodeId'


class screenshotRequestedEvent(TypedDict, total=True):
    viewport: 'Viewport'
    """Viewport to capture, in device independent pixels (dip)."""


class inspectModeCanceledEvent(TypedDict, total=True):
    pass

