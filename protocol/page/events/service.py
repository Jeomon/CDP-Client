
"""CDP Page Events"""

from client.service import CDPClient
from typing import TypedDict, Optional, Callable
from protocol.page.events.types import *

class PageEvents:
    def __init__(self,client:CDPClient):
        self.client=client
    
    def on_dom_content_event_fired(self, callback: Callable[[domContentEventFiredEvent,Optional[str]], None]=None) -> None:
        self.client.on('Page.domContentEventFired', callback)
    
    def on_file_chooser_opened(self, callback: Callable[[fileChooserOpenedEvent,Optional[str]], None]=None) -> None:
        """Emitted only when `page.interceptFileChooser` is enabled."""
        self.client.on('Page.fileChooserOpened', callback)
    
    def on_frame_attached(self, callback: Callable[[frameAttachedEvent,Optional[str]], None]=None) -> None:
        """Fired when frame has been attached to its parent."""
        self.client.on('Page.frameAttached', callback)
    
    def on_frame_cleared_scheduled_navigation(self, callback: Callable[[frameClearedScheduledNavigationEvent,Optional[str]], None]=None) -> None:
        """Fired when frame no longer has a scheduled navigation."""
        self.client.on('Page.frameClearedScheduledNavigation', callback)
    
    def on_frame_detached(self, callback: Callable[[frameDetachedEvent,Optional[str]], None]=None) -> None:
        """Fired when frame has been detached from its parent."""
        self.client.on('Page.frameDetached', callback)
    
    def on_frame_subtree_will_be_detached(self, callback: Callable[[frameSubtreeWillBeDetachedEvent,Optional[str]], None]=None) -> None:
        """Fired before frame subtree is detached. Emitted before any frame of the subtree is actually detached."""
        self.client.on('Page.frameSubtreeWillBeDetached', callback)
    
    def on_frame_navigated(self, callback: Callable[[frameNavigatedEvent,Optional[str]], None]=None) -> None:
        """Fired once navigation of the frame has completed. Frame is now associated with the new loader."""
        self.client.on('Page.frameNavigated', callback)
    
    def on_document_opened(self, callback: Callable[[documentOpenedEvent,Optional[str]], None]=None) -> None:
        """Fired when opening document to write to."""
        self.client.on('Page.documentOpened', callback)
    
    def on_frame_resized(self, callback: Callable[[frameResizedEvent,Optional[str]], None]=None) -> None:
        self.client.on('Page.frameResized', callback)
    
    def on_frame_started_navigating(self, callback: Callable[[frameStartedNavigatingEvent,Optional[str]], None]=None) -> None:
        """Fired when a navigation starts. This event is fired for both renderer-initiated and browser-initiated navigations. For renderer-initiated navigations, the event is fired after `frameRequestedNavigation`. Navigation may still be cancelled after the event is issued. Multiple events can be fired for a single navigation, for example, when a same-document navigation becomes a cross-document navigation (such as in the case of a frameset)."""
        self.client.on('Page.frameStartedNavigating', callback)
    
    def on_frame_requested_navigation(self, callback: Callable[[frameRequestedNavigationEvent,Optional[str]], None]=None) -> None:
        """Fired when a renderer-initiated navigation is requested. Navigation may still be cancelled after the event is issued."""
        self.client.on('Page.frameRequestedNavigation', callback)
    
    def on_frame_scheduled_navigation(self, callback: Callable[[frameScheduledNavigationEvent,Optional[str]], None]=None) -> None:
        """Fired when frame schedules a potential navigation."""
        self.client.on('Page.frameScheduledNavigation', callback)
    
    def on_frame_started_loading(self, callback: Callable[[frameStartedLoadingEvent,Optional[str]], None]=None) -> None:
        """Fired when frame has started loading."""
        self.client.on('Page.frameStartedLoading', callback)
    
    def on_frame_stopped_loading(self, callback: Callable[[frameStoppedLoadingEvent,Optional[str]], None]=None) -> None:
        """Fired when frame has stopped loading."""
        self.client.on('Page.frameStoppedLoading', callback)
    
    def on_download_will_begin(self, callback: Callable[[downloadWillBeginEvent,Optional[str]], None]=None) -> None:
        """Fired when page is about to start a download. Deprecated. Use Browser.downloadWillBegin instead."""
        self.client.on('Page.downloadWillBegin', callback)
    
    def on_download_progress(self, callback: Callable[[downloadProgressEvent,Optional[str]], None]=None) -> None:
        """Fired when download makes progress. Last call has |done| == true. Deprecated. Use Browser.downloadProgress instead."""
        self.client.on('Page.downloadProgress', callback)
    
    def on_interstitial_hidden(self, callback: Callable[[interstitialHiddenEvent,Optional[str]], None]=None) -> None:
        """Fired when interstitial page was hidden"""
        self.client.on('Page.interstitialHidden', callback)
    
    def on_interstitial_shown(self, callback: Callable[[interstitialShownEvent,Optional[str]], None]=None) -> None:
        """Fired when interstitial page was shown"""
        self.client.on('Page.interstitialShown', callback)
    
    def on_javascript_dialog_closed(self, callback: Callable[[javascriptDialogClosedEvent,Optional[str]], None]=None) -> None:
        """Fired when a JavaScript initiated dialog (alert, confirm, prompt, or onbeforeunload) has been closed."""
        self.client.on('Page.javascriptDialogClosed', callback)
    
    def on_javascript_dialog_opening(self, callback: Callable[[javascriptDialogOpeningEvent,Optional[str]], None]=None) -> None:
        """Fired when a JavaScript initiated dialog (alert, confirm, prompt, or onbeforeunload) is about to open."""
        self.client.on('Page.javascriptDialogOpening', callback)
    
    def on_lifecycle_event(self, callback: Callable[[lifecycleEventEvent,Optional[str]], None]=None) -> None:
        """Fired for lifecycle events (navigation, load, paint, etc) in the current target (including local frames)."""
        self.client.on('Page.lifecycleEvent', callback)
    
    def on_back_forward_cache_not_used(self, callback: Callable[[backForwardCacheNotUsedEvent,Optional[str]], None]=None) -> None:
        """Fired for failed bfcache history navigations if BackForwardCache feature is enabled. Do not assume any ordering with the Page.frameNavigated event. This event is fired only for main-frame history navigation where the document changes (non-same-document navigations), when bfcache navigation fails."""
        self.client.on('Page.backForwardCacheNotUsed', callback)
    
    def on_load_event_fired(self, callback: Callable[[loadEventFiredEvent,Optional[str]], None]=None) -> None:
        self.client.on('Page.loadEventFired', callback)
    
    def on_navigated_within_document(self, callback: Callable[[navigatedWithinDocumentEvent,Optional[str]], None]=None) -> None:
        """Fired when same-document navigation happens, e.g. due to history API usage or anchor navigation."""
        self.client.on('Page.navigatedWithinDocument', callback)
    
    def on_screencast_frame(self, callback: Callable[[screencastFrameEvent,Optional[str]], None]=None) -> None:
        """Compressed image data requested by the `startScreencast`."""
        self.client.on('Page.screencastFrame', callback)
    
    def on_screencast_visibility_changed(self, callback: Callable[[screencastVisibilityChangedEvent,Optional[str]], None]=None) -> None:
        """Fired when the page with currently enabled screencast was shown or hidden `."""
        self.client.on('Page.screencastVisibilityChanged', callback)
    
    def on_window_open(self, callback: Callable[[windowOpenEvent,Optional[str]], None]=None) -> None:
        """Fired when a new window is going to be opened, via window.open(), link click, form submission, etc."""
        self.client.on('Page.windowOpen', callback)
    
    def on_compilation_cache_produced(self, callback: Callable[[compilationCacheProducedEvent,Optional[str]], None]=None) -> None:
        """Issued for every compilation cache generated."""
        self.client.on('Page.compilationCacheProduced', callback)
     