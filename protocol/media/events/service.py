
"""CDP Media Events"""

from client.service import CDPClient
from typing import TypedDict, Optional, Callable
from protocol.media.events.types import *

class MediaEvents:
    def __init__(self,client:CDPClient):
        self.client=client
    
    def on_player_properties_changed(self, callback: Callable[[playerPropertiesChangedEvent,Optional[str]], None]=None) -> None:
        """This can be called multiple times, and can be used to set / override / remove player properties. A null propValue indicates removal."""
        self.client.on('playerPropertiesChanged', callback)
    
    def on_player_events_added(self, callback: Callable[[playerEventsAddedEvent,Optional[str]], None]=None) -> None:
        """Send events as a list, allowing them to be batched on the browser for less congestion. If batched, events must ALWAYS be in chronological order."""
        self.client.on('playerEventsAdded', callback)
    
    def on_player_messages_logged(self, callback: Callable[[playerMessagesLoggedEvent,Optional[str]], None]=None) -> None:
        """Send a list of any messages that need to be delivered."""
        self.client.on('playerMessagesLogged', callback)
    
    def on_player_errors_raised(self, callback: Callable[[playerErrorsRaisedEvent,Optional[str]], None]=None) -> None:
        """Send a list of any errors that need to be delivered."""
        self.client.on('playerErrorsRaised', callback)
    
    def on_player_created(self, callback: Callable[[playerCreatedEvent,Optional[str]], None]=None) -> None:
        """Called whenever a player is created, or when a new agent joins and receives a list of active players. If an agent is restored, it will receive one event for each active player."""
        self.client.on('playerCreated', callback)
     