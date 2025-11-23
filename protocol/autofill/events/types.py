
"""CDP Autofill Events"""

from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from autofill.types import AddressUI
    from autofill.types import FilledField


class addressFormFilledEvent(TypedDict, total=True):
    filledFields: List[FilledField]
    """Information about the fields that were filled"""
    addressUi: AddressUI
    """An UI representation of the address used to fill the form. Consists of a 2D array where each child represents an address/profile line."""

