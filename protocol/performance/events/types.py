
"""CDP Performance Events"""

from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from performance.types import Metric


class metricsEvent(TypedDict, total=True):
    metrics: List[Metric]
    """Current values of the metrics."""
    title: str
    """Timestamp title."""

