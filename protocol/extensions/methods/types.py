
"""CDP Extensions Methods Types"""

from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from protocol.extensions.types import StorageArea


class loadUnpackedParameters(TypedDict, total=True):
    path: str
    """Absolute file path."""


class uninstallParameters(TypedDict, total=True):
    id: str
    """Extension id."""


class getStorageItemsParameters(TypedDict, total=True):
    id: str
    """ID of extension."""
    storageArea: StorageArea
    """StorageArea to retrieve data from."""
    keys: NotRequired[List[str]]
    """Keys to retrieve."""


class removeStorageItemsParameters(TypedDict, total=True):
    id: str
    """ID of extension."""
    storageArea: StorageArea
    """StorageArea to remove data from."""
    keys: List[str]
    """Keys to remove."""


class clearStorageItemsParameters(TypedDict, total=True):
    id: str
    """ID of extension."""
    storageArea: StorageArea
    """StorageArea to remove data from."""


class setStorageItemsParameters(TypedDict, total=True):
    id: str
    """ID of extension."""
    storageArea: StorageArea
    """StorageArea to set data in."""
    values: Dict[str, Any]
    """Values to set."""


class loadUnpackedReturns(TypedDict):
    id: str
    """Extension id."""



class getStorageItemsReturns(TypedDict):
    data: Dict[str, Any]




