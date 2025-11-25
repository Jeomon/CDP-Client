
"""CDP Audits Events"""

from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from protocol.audits.types import InspectorIssue


class issueAddedEvent(TypedDict, total=True):
    issue: 'InspectorIssue'

