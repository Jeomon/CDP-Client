
"""CDP Network Methods"""

from client.service import CDPClient
from typing import TypedDict,Optional
from protocol.network.methods.types import *

class NetworkMethods:
    def __init__(self, client:CDPClient):
        self.client = client

    async def set_accepted_encodings(self, params: Optional[setAcceptedEncodingsParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Sets a list of content encodings that will be accepted. Empty list means no encoding is accepted."""
        return await self.client.send(method="Network.setAcceptedEncodings", params=params,session_id=session_id)

    async def clear_accepted_encodings_override(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Clears accepted encodings set by setAcceptedEncodings"""
        return await self.client.send(method="Network.clearAcceptedEncodingsOverride", params=params,session_id=session_id)

    async def clear_browser_cache(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Clears browser cache."""
        return await self.client.send(method="Network.clearBrowserCache", params=params,session_id=session_id)

    async def clear_browser_cookies(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Clears browser cookies."""
        return await self.client.send(method="Network.clearBrowserCookies", params=params,session_id=session_id)

    async def delete_cookies(self, params: Optional[deleteCookiesParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Deletes browser cookies with matching name and url or domain/path/partitionKey pair."""
        return await self.client.send(method="Network.deleteCookies", params=params,session_id=session_id)

    async def disable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Disables network tracking, prevents network events from being sent to the client."""
        return await self.client.send(method="Network.disable", params=params,session_id=session_id)

    async def emulate_network_conditions_by_rule(self, params: Optional[emulateNetworkConditionsByRuleParameters]=None,session_id: Optional[str] = None) -> emulateNetworkConditionsByRuleReturns:
        """Activates emulation of network conditions for individual requests using URL match patterns. Unlike the deprecated Network.emulateNetworkConditions this method does not affect `navigator` state. Use Network.overrideNetworkState to explicitly modify `navigator` behavior."""
        return await self.client.send(method="Network.emulateNetworkConditionsByRule", params=params,session_id=session_id)

    async def override_network_state(self, params: Optional[overrideNetworkStateParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Override the state of navigator.onLine and navigator.connection."""
        return await self.client.send(method="Network.overrideNetworkState", params=params,session_id=session_id)

    async def enable(self, params: Optional[enableParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Enables network tracking, network events will now be delivered to the client."""
        return await self.client.send(method="Network.enable", params=params,session_id=session_id)

    async def get_certificate(self, params: Optional[getCertificateParameters]=None,session_id: Optional[str] = None) -> getCertificateReturns:
        """Returns the DER-encoded certificate."""
        return await self.client.send(method="Network.getCertificate", params=params,session_id=session_id)

    async def get_cookies(self, params: Optional[getCookiesParameters]=None,session_id: Optional[str] = None) -> getCookiesReturns:
        """Returns all browser cookies for the current URL. Depending on the backend support, will return detailed cookie information in the `cookies` field."""
        return await self.client.send(method="Network.getCookies", params=params,session_id=session_id)

    async def get_response_body(self, params: Optional[getResponseBodyParameters]=None,session_id: Optional[str] = None) -> getResponseBodyReturns:
        """Returns content served for the given request."""
        return await self.client.send(method="Network.getResponseBody", params=params,session_id=session_id)

    async def get_request_post_data(self, params: Optional[getRequestPostDataParameters]=None,session_id: Optional[str] = None) -> getRequestPostDataReturns:
        """Returns post data sent with the request. Returns an error when no data was sent with the request."""
        return await self.client.send(method="Network.getRequestPostData", params=params,session_id=session_id)

    async def get_response_body_for_interception(self, params: Optional[getResponseBodyForInterceptionParameters]=None,session_id: Optional[str] = None) -> getResponseBodyForInterceptionReturns:
        """Returns content served for the given currently intercepted request."""
        return await self.client.send(method="Network.getResponseBodyForInterception", params=params,session_id=session_id)

    async def take_response_body_for_interception_as_stream(self, params: Optional[takeResponseBodyForInterceptionAsStreamParameters]=None,session_id: Optional[str] = None) -> takeResponseBodyForInterceptionAsStreamReturns:
        """Returns a handle to the stream representing the response body. Note that after this command, the intercepted request can't be continued as is -- you either need to cancel it or to provide the response body. The stream only supports sequential read, IO.read will fail if the position is specified."""
        return await self.client.send(method="Network.takeResponseBodyForInterceptionAsStream", params=params,session_id=session_id)

    async def replay_xhr(self, params: Optional[replayXHRParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """This method sends a new XMLHttpRequest which is identical to the original one. The following parameters should be identical: method, url, async, request body, extra headers, withCredentials attribute, user, password."""
        return await self.client.send(method="Network.replayXHR", params=params,session_id=session_id)

    async def search_in_response_body(self, params: Optional[searchInResponseBodyParameters]=None,session_id: Optional[str] = None) -> searchInResponseBodyReturns:
        """Searches for given string in response content."""
        return await self.client.send(method="Network.searchInResponseBody", params=params,session_id=session_id)

    async def set_blocked_ur_ls(self, params: Optional[setBlockedURLsParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Blocks URLs from loading."""
        return await self.client.send(method="Network.setBlockedURLs", params=params,session_id=session_id)

    async def set_bypass_service_worker(self, params: Optional[setBypassServiceWorkerParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Toggles ignoring of service worker for each request."""
        return await self.client.send(method="Network.setBypassServiceWorker", params=params,session_id=session_id)

    async def set_cache_disabled(self, params: Optional[setCacheDisabledParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Toggles ignoring cache for each request. If `true`, cache will not be used."""
        return await self.client.send(method="Network.setCacheDisabled", params=params,session_id=session_id)

    async def set_cookie(self, params: Optional[setCookieParameters]=None,session_id: Optional[str] = None) -> setCookieReturns:
        """Sets a cookie with the given cookie data; may overwrite equivalent cookies if they exist."""
        return await self.client.send(method="Network.setCookie", params=params,session_id=session_id)

    async def set_cookies(self, params: Optional[setCookiesParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Sets given cookies."""
        return await self.client.send(method="Network.setCookies", params=params,session_id=session_id)

    async def set_extra_http_headers(self, params: Optional[setExtraHTTPHeadersParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Specifies whether to always send extra HTTP headers with the requests from this page."""
        return await self.client.send(method="Network.setExtraHTTPHeaders", params=params,session_id=session_id)

    async def set_attach_debug_stack(self, params: Optional[setAttachDebugStackParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Specifies whether to attach a page script stack id in requests"""
        return await self.client.send(method="Network.setAttachDebugStack", params=params,session_id=session_id)

    async def set_user_agent_override(self, params: Optional[setUserAgentOverrideParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Allows overriding user agent with the given string."""
        return await self.client.send(method="Network.setUserAgentOverride", params=params,session_id=session_id)

    async def stream_resource_content(self, params: Optional[streamResourceContentParameters]=None,session_id: Optional[str] = None) -> streamResourceContentReturns:
        """Enables streaming of the response for the given requestId. If enabled, the dataReceived event contains the data that was received during streaming."""
        return await self.client.send(method="Network.streamResourceContent", params=params,session_id=session_id)

    async def get_security_isolation_status(self, params: Optional[getSecurityIsolationStatusParameters]=None,session_id: Optional[str] = None) -> getSecurityIsolationStatusReturns:
        """Returns information about the COEP/COOP isolation status."""
        return await self.client.send(method="Network.getSecurityIsolationStatus", params=params,session_id=session_id)

    async def enable_reporting_api(self, params: Optional[enableReportingApiParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Enables tracking for the Reporting API, events generated by the Reporting API will now be delivered to the client. Enabling triggers 'reportingApiReportAdded' for all existing reports."""
        return await self.client.send(method="Network.enableReportingApi", params=params,session_id=session_id)

    async def load_network_resource(self, params: Optional[loadNetworkResourceParameters]=None,session_id: Optional[str] = None) -> loadNetworkResourceReturns:
        """Fetches the resource and returns the content."""
        return await self.client.send(method="Network.loadNetworkResource", params=params,session_id=session_id)

    async def set_cookie_controls(self, params: Optional[setCookieControlsParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Sets Controls for third-party cookie access Page reload is required before the new cookie behavior will be observed"""
        return await self.client.send(method="Network.setCookieControls", params=params,session_id=session_id)
