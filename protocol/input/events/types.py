
"""CDP Input Events"""

from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from input.types import DragData


class dragInterceptedEvent(TypedDict, total=True):
    data: DragData

