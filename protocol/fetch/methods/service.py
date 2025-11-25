
"""CDP Fetch Methods"""

from client.methods import CDPMethods
from typing import TypedDict,Optional
from protocol.fetch.methods.types import *

class FetchMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def disable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Disables the fetch domain."""
        return await self.methods.send(method="Fetch.disable", params=params,session_id=session_id)

    async def enable(self, params: Optional[enableParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Enables issuing of requestPaused events. A request will be paused until client calls one of failRequest, fulfillRequest or continueRequest/continueWithAuth."""
        return await self.methods.send(method="Fetch.enable", params=params,session_id=session_id)

    async def fail_request(self, params: Optional[failRequestParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Causes the request to fail with specified reason."""
        return await self.methods.send(method="Fetch.failRequest", params=params,session_id=session_id)

    async def fulfill_request(self, params: Optional[fulfillRequestParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Provides response to the request."""
        return await self.methods.send(method="Fetch.fulfillRequest", params=params,session_id=session_id)

    async def continue_request(self, params: Optional[continueRequestParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Continues the request, optionally modifying some of its parameters."""
        return await self.methods.send(method="Fetch.continueRequest", params=params,session_id=session_id)

    async def continue_with_auth(self, params: Optional[continueWithAuthParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Continues a request supplying authChallengeResponse following authRequired event."""
        return await self.methods.send(method="Fetch.continueWithAuth", params=params,session_id=session_id)

    async def continue_response(self, params: Optional[continueResponseParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Continues loading of the paused response, optionally modifying the response headers. If either responseCode or headers are modified, all of them must be present."""
        return await self.methods.send(method="Fetch.continueResponse", params=params,session_id=session_id)

    async def get_response_body(self, params: Optional[getResponseBodyParameters]=None,session_id: Optional[str] = None) -> getResponseBodyReturns:
        """Causes the body of the response to be received from the server and returned as a single string. May only be issued for a request that is paused in the Response stage and is mutually exclusive with takeResponseBodyForInterceptionAsStream. Calling other methods that affect the request or disabling fetch domain before body is received results in an undefined behavior. Note that the response body is not available for redirects. Requests paused in the _redirect received_ state may be differentiated by `responseCode` and presence of `location` response header, see comments to `requestPaused` for details."""
        return await self.methods.send(method="Fetch.getResponseBody", params=params,session_id=session_id)

    async def take_response_body_as_stream(self, params: Optional[takeResponseBodyAsStreamParameters]=None,session_id: Optional[str] = None) -> takeResponseBodyAsStreamReturns:
        """Returns a handle to the stream representing the response body. The request must be paused in the HeadersReceived stage. Note that after this command the request can't be continued as is -- client either needs to cancel it or to provide the response body. The stream only supports sequential read, IO.read will fail if the position is specified. This method is mutually exclusive with getResponseBody. Calling other methods that affect the request or disabling fetch domain before body is received results in an undefined behavior."""
        return await self.methods.send(method="Fetch.takeResponseBodyAsStream", params=params,session_id=session_id)
