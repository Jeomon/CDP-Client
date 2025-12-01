
"""CDP EventBreakpoints Methods Types"""

from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple


class setInstrumentationBreakpointParameters(TypedDict, total=True):
    eventName: str
    """Instrumentation name to stop on."""


class removeInstrumentationBreakpointParameters(TypedDict, total=True):
    eventName: str
    """Instrumentation name to stop on."""





