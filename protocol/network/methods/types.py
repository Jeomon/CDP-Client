
"""CDP Network Methods Types"""

from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from debugger.types import SearchMatch
    from emulation.types import UserAgentMetadata
    from io.types import StreamHandle
    from network.types import BlockPattern
    from network.types import ConnectionType
    from network.types import ContentEncoding
    from network.types import Cookie
    from network.types import CookieParam
    from network.types import CookiePartitionKey
    from network.types import CookiePriority
    from network.types import CookieSameSite
    from network.types import CookieSourceScheme
    from network.types import Headers
    from network.types import InterceptionId
    from network.types import LoadNetworkResourceOptions
    from network.types import LoadNetworkResourcePageResult
    from network.types import NetworkConditions
    from network.types import RequestId
    from network.types import SecurityIsolationStatus
    from network.types import TimeSinceEpoch
    from page.types import FrameId


class setAcceptedEncodingsParameters(TypedDict, total=True):
    encodings: List[ContentEncoding]
    """List of accepted content encodings."""





class deleteCookiesParameters(TypedDict, total=True):
    name: str
    """Name of the cookies to remove."""
    url: NotRequired[str]
    """If specified, deletes all the cookies with the given name where domain and path match provided URL."""
    domain: NotRequired[str]
    """If specified, deletes only cookies with the exact domain."""
    path: NotRequired[str]
    """If specified, deletes only cookies with the exact path."""
    partitionKey: NotRequired[CookiePartitionKey]
    """If specified, deletes only cookies with the the given name and partitionKey where all partition key attributes match the cookie partition key attribute."""



class emulateNetworkConditionsByRuleParameters(TypedDict, total=True):
    offline: bool
    """True to emulate internet disconnection."""
    matchedNetworkConditions: List[NetworkConditions]
    """Configure conditions for matching requests. If multiple entries match a request, the first entry wins.  Global conditions can be configured by leaving the urlPattern for the conditions empty. These global conditions are also applied for throttling of p2p connections."""


class overrideNetworkStateParameters(TypedDict, total=True):
    offline: bool
    """True to emulate internet disconnection."""
    latency: float
    """Minimum latency from request sent to response headers received (ms)."""
    downloadThroughput: float
    """Maximal aggregated download throughput (bytes/sec). -1 disables download throttling."""
    uploadThroughput: float
    """Maximal aggregated upload throughput (bytes/sec).  -1 disables upload throttling."""
    connectionType: NotRequired[ConnectionType]
    """Connection type if known."""


class enableParameters(TypedDict, total=False):
    maxTotalBufferSize: NotRequired[int]
    """Buffer size in bytes to use when preserving network payloads (XHRs, etc)."""
    maxResourceBufferSize: NotRequired[int]
    """Per-resource buffer size in bytes to use when preserving network payloads (XHRs, etc)."""
    maxPostDataSize: NotRequired[int]
    """Longest post body size (in bytes) that would be included in requestWillBeSent notification"""
    reportDirectSocketTraffic: NotRequired[bool]
    """Whether DirectSocket chunk send/receive events should be reported."""
    enableDurableMessages: NotRequired[bool]
    """Enable storing response bodies outside of renderer, so that these survive a cross-process navigation. Requires maxTotalBufferSize to be set. Currently defaults to false."""


class getCertificateParameters(TypedDict, total=True):
    origin: str
    """Origin to get certificate for."""


class getCookiesParameters(TypedDict, total=False):
    urls: NotRequired[List[str]]
    """The list of URLs for which applicable cookies will be fetched. If not specified, it's assumed to be set to the list containing the URLs of the page and all of its subframes."""


class getResponseBodyParameters(TypedDict, total=True):
    requestId: RequestId
    """Identifier of the network request to get content for."""


class getRequestPostDataParameters(TypedDict, total=True):
    requestId: RequestId
    """Identifier of the network request to get content for."""


class getResponseBodyForInterceptionParameters(TypedDict, total=True):
    interceptionId: InterceptionId
    """Identifier for the intercepted request to get body for."""


class takeResponseBodyForInterceptionAsStreamParameters(TypedDict, total=True):
    interceptionId: InterceptionId


class replayXHRParameters(TypedDict, total=True):
    requestId: RequestId
    """Identifier of XHR to replay."""


class searchInResponseBodyParameters(TypedDict, total=True):
    requestId: RequestId
    """Identifier of the network response to search."""
    query: str
    """String to search for."""
    caseSensitive: NotRequired[bool]
    """If true, search is case sensitive."""
    isRegex: NotRequired[bool]
    """If true, treats string parameter as regex."""


class setBlockedURLsParameters(TypedDict, total=False):
    urlPatterns: NotRequired[List[BlockPattern]]
    """Patterns to match in the order in which they are given. These patterns also take precedence over any wildcard patterns defined in urls."""
    urls: NotRequired[List[str]]
    """URL patterns to block. Wildcards ('*') are allowed."""


class setBypassServiceWorkerParameters(TypedDict, total=True):
    bypass: bool
    """Bypass service worker and load from network."""


class setCacheDisabledParameters(TypedDict, total=True):
    cacheDisabled: bool
    """Cache disabled state."""


class setCookieParameters(TypedDict, total=True):
    name: str
    """Cookie name."""
    value: str
    """Cookie value."""
    url: NotRequired[str]
    """The request-URI to associate with the setting of the cookie. This value can affect the default domain, path, source port, and source scheme values of the created cookie."""
    domain: NotRequired[str]
    """Cookie domain."""
    path: NotRequired[str]
    """Cookie path."""
    secure: NotRequired[bool]
    """True if cookie is secure."""
    httpOnly: NotRequired[bool]
    """True if cookie is http-only."""
    sameSite: NotRequired[CookieSameSite]
    """Cookie SameSite type."""
    expires: NotRequired[TimeSinceEpoch]
    """Cookie expiration date, session cookie if not set"""
    priority: NotRequired[CookiePriority]
    """Cookie Priority type."""
    sameParty: NotRequired[bool]
    """True if cookie is SameParty."""
    sourceScheme: NotRequired[CookieSourceScheme]
    """Cookie source scheme type."""
    sourcePort: NotRequired[int]
    """Cookie source port. Valid values are {-1, [1, 65535]}, -1 indicates an unspecified port. An unspecified port value allows protocol clients to emulate legacy cookie scope for the port. This is a temporary ability and it will be removed in the future."""
    partitionKey: NotRequired[CookiePartitionKey]
    """Cookie partition key. If not set, the cookie will be set as not partitioned."""


class setCookiesParameters(TypedDict, total=True):
    cookies: List[CookieParam]
    """Cookies to be set."""


class setExtraHTTPHeadersParameters(TypedDict, total=True):
    headers: Headers
    """Map with extra HTTP headers."""


class setAttachDebugStackParameters(TypedDict, total=True):
    enabled: bool
    """Whether to attach a page script stack for debugging purpose."""


class setUserAgentOverrideParameters(TypedDict, total=True):
    userAgent: str
    """User agent to use."""
    acceptLanguage: NotRequired[str]
    """Browser language to emulate."""
    platform: NotRequired[str]
    """The platform navigator.platform should return."""
    userAgentMetadata: NotRequired[UserAgentMetadata]
    """To be sent in Sec-CH-UA-* headers and returned in navigator.userAgentData"""


class streamResourceContentParameters(TypedDict, total=True):
    requestId: RequestId
    """Identifier of the request to stream."""


class getSecurityIsolationStatusParameters(TypedDict, total=False):
    frameId: NotRequired[FrameId]
    """If no frameId is provided, the status of the target is provided."""


class enableReportingApiParameters(TypedDict, total=True):
    enable: bool
    """Whether to enable or disable events for the Reporting API"""


class loadNetworkResourceParameters(TypedDict, total=True):
    url: str
    """URL of the resource to get content for."""
    options: LoadNetworkResourceOptions
    """Options for the request."""
    frameId: NotRequired[FrameId]
    """Frame id to get the resource for. Mandatory for frame targets, and should be omitted for worker targets."""


class setCookieControlsParameters(TypedDict, total=True):
    enableThirdPartyCookieRestriction: bool
    """Whether 3pc restriction is enabled."""
    disableThirdPartyCookieMetadata: bool
    """Whether 3pc grace period exception should be enabled; false by default."""
    disableThirdPartyCookieHeuristics: bool
    """Whether 3pc heuristics exceptions should be enabled; false by default."""








class emulateNetworkConditionsByRuleReturns(TypedDict):
    ruleIds: List[str]
    """An id for each entry in matchedNetworkConditions. The id will be included in the requestWillBeSentExtraInfo for requests affected by a rule."""




class getCertificateReturns(TypedDict):
    tableNames: List[str]


class getCookiesReturns(TypedDict):
    cookies: List[Cookie]
    """Array of cookie objects."""


class getResponseBodyReturns(TypedDict):
    body: str
    """Response body."""
    base64Encoded: bool
    """True, if content was sent as base64."""


class getRequestPostDataReturns(TypedDict):
    postData: str
    """Request body string, omitting files from multipart requests"""


class getResponseBodyForInterceptionReturns(TypedDict):
    body: str
    """Response body."""
    base64Encoded: bool
    """True, if content was sent as base64."""


class takeResponseBodyForInterceptionAsStreamReturns(TypedDict):
    stream: StreamHandle



class searchInResponseBodyReturns(TypedDict):
    result: List[SearchMatch]
    """List of search matches."""





class setCookieReturns(TypedDict):
    success: bool
    """Always set to true. If an error occurs, the response indicates protocol error."""






class streamResourceContentReturns(TypedDict):
    bufferedData: str
    """Data that has been buffered until streaming is enabled. (Encoded as a base64 string when passed over JSON)"""


class getSecurityIsolationStatusReturns(TypedDict):
    status: SecurityIsolationStatus



class loadNetworkResourceReturns(TypedDict):
    resource: LoadNetworkResourcePageResult


