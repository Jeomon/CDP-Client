
"""CDP Fetch Events"""

from cdp_client.events import CDPEvents
from typing import TypedDict, Optional, Callable
from fetch.events.types import *

class FetchEvents:
    def __init__(self,events:CDPEvents):
        self.events=events
    
    def on_request_paused(self, callback: Callable[requestPausedEvent, None]=None) -> None:
        """Issued when the domain is enabled and the request URL matches the specified filter. The request is paused until the client responds with one of continueRequest, failRequest or fulfillRequest. The stage of the request can be determined by presence of responseErrorReason and responseStatusCode -- the request is at the response stage if either of these fields is present and in the request stage otherwise. Redirect responses and subsequent requests are reported similarly to regular responses and requests. Redirect responses may be distinguished by the value of `responseStatusCode` (which is one of 301, 302, 303, 307, 308) along with presence of the `location` header. Requests resulting from a redirect will have `redirectedRequestId` field set."""
        self.events.on('requestPaused', callback)
    
    def on_auth_required(self, callback: Callable[authRequiredEvent, None]=None) -> None:
        """Issued when the domain is enabled with handleAuthRequests set to true. The request is paused until client responds with continueWithAuth."""
        self.events.on('authRequired', callback)
     