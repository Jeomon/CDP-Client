
"""CDP Cast Types"""

from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple


class Sink(TypedDict, total=True):
    """"""
    name: 'str'
    id: 'str'
    session: NotRequired['str']
    """Text describing the current session. Present only if there is an active session on the sink."""

