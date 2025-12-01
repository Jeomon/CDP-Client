
"""CDP Performance Types"""

from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple


class Metric(TypedDict, total=True):
    """Run-time execution metric."""
    name: str
    """Metric name."""
    value: float
    """Metric value."""

