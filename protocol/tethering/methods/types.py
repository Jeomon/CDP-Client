
"""CDP Tethering Methods Types"""

from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple


class bindParameters(TypedDict, total=True):
    port: 'int'
    """Port number to bind."""


class unbindParameters(TypedDict, total=True):
    port: 'int'
    """Port number to unbind."""



