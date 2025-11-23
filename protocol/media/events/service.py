
"""CDP Media Events"""

from cdp_client.events import CDPEvents
from typing import TypedDict, Optional, Callable
from media.events.types import *

class MediaEvents:
    def __init__(self,events:CDPEvents):
        self.events=events
    
    def on_player_properties_changed(self, callback: Callable[playerPropertiesChangedEvent, None]=None) -> None:
        """This can be called multiple times, and can be used to set / override / remove player properties. A null propValue indicates removal."""
        self.events.on('playerPropertiesChanged', callback)
    
    def on_player_events_added(self, callback: Callable[playerEventsAddedEvent, None]=None) -> None:
        """Send events as a list, allowing them to be batched on the browser for less congestion. If batched, events must ALWAYS be in chronological order."""
        self.events.on('playerEventsAdded', callback)
    
    def on_player_messages_logged(self, callback: Callable[playerMessagesLoggedEvent, None]=None) -> None:
        """Send a list of any messages that need to be delivered."""
        self.events.on('playerMessagesLogged', callback)
    
    def on_player_errors_raised(self, callback: Callable[playerErrorsRaisedEvent, None]=None) -> None:
        """Send a list of any errors that need to be delivered."""
        self.events.on('playerErrorsRaised', callback)
    
    def on_player_created(self, callback: Callable[playerCreatedEvent, None]=None) -> None:
        """Called whenever a player is created, or when a new agent joins and receives a list of active players. If an agent is restored, it will receive one event for each active player."""
        self.events.on('playerCreated', callback)
     