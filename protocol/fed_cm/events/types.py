
"""CDP FedCm Events"""

from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fed_cm.types import Account
    from fed_cm.types import DialogType


class dialogShownEvent(TypedDict, total=True):
    dialogId: str
    dialogType: DialogType
    accounts: List[Account]
    title: str
    """These exist primarily so that the caller can verify the RP context was used appropriately."""
    subtitle: NotRequired[str]


class dialogClosedEvent(TypedDict, total=True):
    dialogId: str

