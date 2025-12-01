
"""CDP FileSystem Methods Types"""

from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from protocol.file_system.types import BucketFileSystemLocator
    from protocol.file_system.types import Directory


class getDirectoryParameters(TypedDict, total=True):
    bucketFileSystemLocator: BucketFileSystemLocator


class getDirectoryReturns(TypedDict):
    directory: Directory
    """Returns the directory object at the path."""

