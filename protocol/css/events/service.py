
"""CDP CSS Events"""

from client.events import CDPEvents
from typing import TypedDict, Optional, Callable
from protocol.css.events.types import *

class CSSEvents:
    def __init__(self,events:CDPEvents):
        self.events=events
    
    def on_fonts_updated(self, callback: Callable[[fontsUpdatedEvent,Optional[str]], None]=None) -> None:
        """Fires whenever a web font is updated.  A non-empty font parameter indicates a successfully loaded web font."""
        self.events.on('fontsUpdated', callback)
    
    def on_media_query_result_changed(self, callback: Callable[[mediaQueryResultChangedEvent,Optional[str]], None]=None) -> None:
        """Fires whenever a MediaQuery result changes (for example, after a browser window has been resized.) The current implementation considers only viewport-dependent media features."""
        self.events.on('mediaQueryResultChanged', callback)
    
    def on_style_sheet_added(self, callback: Callable[[styleSheetAddedEvent,Optional[str]], None]=None) -> None:
        """Fired whenever an active document stylesheet is added."""
        self.events.on('styleSheetAdded', callback)
    
    def on_style_sheet_changed(self, callback: Callable[[styleSheetChangedEvent,Optional[str]], None]=None) -> None:
        """Fired whenever a stylesheet is changed as a result of the client operation."""
        self.events.on('styleSheetChanged', callback)
    
    def on_style_sheet_removed(self, callback: Callable[[styleSheetRemovedEvent,Optional[str]], None]=None) -> None:
        """Fired whenever an active document stylesheet is removed."""
        self.events.on('styleSheetRemoved', callback)
    
    def on_computed_style_updated(self, callback: Callable[[computedStyleUpdatedEvent,Optional[str]], None]=None) -> None:
        self.events.on('computedStyleUpdated', callback)
     