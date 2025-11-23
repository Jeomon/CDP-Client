
"""CDP WebAudio Events"""

from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from web_audio.types import AudioListener
    from web_audio.types import AudioNode
    from web_audio.types import AudioParam
    from web_audio.types import BaseAudioContext
    from web_audio.types import GraphObjectId


class contextCreatedEvent(TypedDict, total=True):
    context: BaseAudioContext


class contextWillBeDestroyedEvent(TypedDict, total=True):
    contextId: GraphObjectId


class contextChangedEvent(TypedDict, total=True):
    context: BaseAudioContext


class audioListenerCreatedEvent(TypedDict, total=True):
    listener: AudioListener


class audioListenerWillBeDestroyedEvent(TypedDict, total=True):
    contextId: GraphObjectId
    listenerId: GraphObjectId


class audioNodeCreatedEvent(TypedDict, total=True):
    node: AudioNode


class audioNodeWillBeDestroyedEvent(TypedDict, total=True):
    contextId: GraphObjectId
    nodeId: GraphObjectId


class audioParamCreatedEvent(TypedDict, total=True):
    param: AudioParam


class audioParamWillBeDestroyedEvent(TypedDict, total=True):
    contextId: GraphObjectId
    nodeId: GraphObjectId
    paramId: GraphObjectId


class nodesConnectedEvent(TypedDict, total=True):
    contextId: GraphObjectId
    sourceId: GraphObjectId
    destinationId: GraphObjectId
    sourceOutputIndex: NotRequired[float]
    destinationInputIndex: NotRequired[float]


class nodesDisconnectedEvent(TypedDict, total=True):
    contextId: GraphObjectId
    sourceId: GraphObjectId
    destinationId: GraphObjectId
    sourceOutputIndex: NotRequired[float]
    destinationInputIndex: NotRequired[float]


class nodeParamConnectedEvent(TypedDict, total=True):
    contextId: GraphObjectId
    sourceId: GraphObjectId
    destinationId: GraphObjectId
    sourceOutputIndex: NotRequired[float]


class nodeParamDisconnectedEvent(TypedDict, total=True):
    contextId: GraphObjectId
    sourceId: GraphObjectId
    destinationId: GraphObjectId
    sourceOutputIndex: NotRequired[float]

