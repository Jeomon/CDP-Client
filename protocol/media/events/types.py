
"""CDP Media Events"""

from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from media.types import Player
    from media.types import PlayerError
    from media.types import PlayerEvent
    from media.types import PlayerId
    from media.types import PlayerMessage
    from media.types import PlayerProperty


class playerPropertiesChangedEvent(TypedDict, total=True):
    playerId: PlayerId
    properties: List[PlayerProperty]


class playerEventsAddedEvent(TypedDict, total=True):
    playerId: PlayerId
    events: List[PlayerEvent]


class playerMessagesLoggedEvent(TypedDict, total=True):
    playerId: PlayerId
    messages: List[PlayerMessage]


class playerErrorsRaisedEvent(TypedDict, total=True):
    playerId: PlayerId
    errors: List[PlayerError]


class playerCreatedEvent(TypedDict, total=True):
    player: Player

