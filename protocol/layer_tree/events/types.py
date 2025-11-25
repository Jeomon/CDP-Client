
"""CDP LayerTree Events"""

from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from protocol.dom.types import Rect
    from protocol.layer_tree.types import Layer
    from protocol.layer_tree.types import LayerId


class layerPaintedEvent(TypedDict, total=True):
    layerId: 'LayerId'
    """The id of the painted layer."""
    clip: 'Rect'
    """Clip rectangle."""


class layerTreeDidChangeEvent(TypedDict, total=False):
    layers: NotRequired['List[Layer]']
    """Layer tree, absent if not in the compositing mode."""

