
"""CDP Tethering Events"""

from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple


class acceptedEvent(TypedDict, total=True):
    port: int
    """Port number that was successfully bound."""
    connectionId: str
    """Connection id to be used."""

