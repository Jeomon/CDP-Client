
"""CDP DOMStorage Methods Types"""

from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from protocol.dom_storage.types import Item
    from protocol.dom_storage.types import StorageId


class clearParameters(TypedDict, total=True):
    storageId: 'StorageId'




class getDOMStorageItemsParameters(TypedDict, total=True):
    storageId: 'StorageId'


class removeDOMStorageItemParameters(TypedDict, total=True):
    storageId: 'StorageId'
    key: 'str'


class setDOMStorageItemParameters(TypedDict, total=True):
    storageId: 'StorageId'
    key: 'str'
    value: 'str'





class getDOMStorageItemsReturns(TypedDict):
    entries: 'List[Item]'



