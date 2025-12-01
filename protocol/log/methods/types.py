
"""CDP Log Methods Types"""

from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from protocol.log.types import ViolationSetting





class startViolationsReportParameters(TypedDict, total=True):
    config: List[ViolationSetting]
    """Configuration for violations."""







