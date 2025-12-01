
"""CDP Performance Methods Types"""

from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from protocol.performance.types import Metric



class enableParameters(TypedDict, total=False):
    timeDomain: NotRequired[Literal["timeTicks", "threadTicks"]]
    """Time domain to use for collecting and reporting duration metrics."""





class getMetricsReturns(TypedDict):
    metrics: List[Metric]
    """Current values for run-time metrics."""

