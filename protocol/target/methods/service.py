
"""CDP Target Methods"""

from client.service import CDPClient
from typing import TypedDict,Optional
from protocol.target.methods.types import *

class TargetMethods:
    def __init__(self, client:CDPClient):
        self.client = client

    async def activate_target(self, params: Optional[activateTargetParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Activates (focuses) the target."""
        return await self.client.send(method="Target.activateTarget", params=params,session_id=session_id)

    async def attach_to_target(self, params: Optional[attachToTargetParameters]=None,session_id: Optional[str] = None) -> attachToTargetReturns:
        """Attaches to the target with given id."""
        return await self.client.send(method="Target.attachToTarget", params=params,session_id=session_id)

    async def attach_to_browser_target(self, params: None=None,session_id: Optional[str] = None) -> attachToBrowserTargetReturns:
        """Attaches to the browser target, only uses flat sessionId mode."""
        return await self.client.send(method="Target.attachToBrowserTarget", params=params,session_id=session_id)

    async def close_target(self, params: Optional[closeTargetParameters]=None,session_id: Optional[str] = None) -> closeTargetReturns:
        """Closes the target. If the target is a page that gets closed too."""
        return await self.client.send(method="Target.closeTarget", params=params,session_id=session_id)

    async def expose_dev_tools_protocol(self, params: Optional[exposeDevToolsProtocolParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Inject object to the target's main frame that provides a communication channel with browser target.  Injected object will be available as `window[bindingName]`.  The object has the following API: - `binding.send(json)` - a method to send messages over the remote debugging protocol - `binding.onmessage = json => handleMessage(json)` - a callback that will be called for the protocol notifications and command responses."""
        return await self.client.send(method="Target.exposeDevToolsProtocol", params=params,session_id=session_id)

    async def create_browser_context(self, params: Optional[createBrowserContextParameters]=None,session_id: Optional[str] = None) -> createBrowserContextReturns:
        """Creates a new empty BrowserContext. Similar to an incognito profile but you can have more than one."""
        return await self.client.send(method="Target.createBrowserContext", params=params,session_id=session_id)

    async def get_browser_contexts(self, params: None=None,session_id: Optional[str] = None) -> getBrowserContextsReturns:
        """Returns all browser contexts created with `Target.createBrowserContext` method."""
        return await self.client.send(method="Target.getBrowserContexts", params=params,session_id=session_id)

    async def create_target(self, params: Optional[createTargetParameters]=None,session_id: Optional[str] = None) -> createTargetReturns:
        """Creates a new page."""
        return await self.client.send(method="Target.createTarget", params=params,session_id=session_id)

    async def detach_from_target(self, params: Optional[detachFromTargetParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Detaches session with given id."""
        return await self.client.send(method="Target.detachFromTarget", params=params,session_id=session_id)

    async def dispose_browser_context(self, params: Optional[disposeBrowserContextParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Deletes a BrowserContext. All the belonging pages will be closed without calling their beforeunload hooks."""
        return await self.client.send(method="Target.disposeBrowserContext", params=params,session_id=session_id)

    async def get_target_info(self, params: Optional[getTargetInfoParameters]=None,session_id: Optional[str] = None) -> getTargetInfoReturns:
        """Returns information about a target."""
        return await self.client.send(method="Target.getTargetInfo", params=params,session_id=session_id)

    async def get_targets(self, params: Optional[getTargetsParameters]=None,session_id: Optional[str] = None) -> getTargetsReturns:
        """Retrieves a list of available targets."""
        return await self.client.send(method="Target.getTargets", params=params,session_id=session_id)

    async def set_auto_attach(self, params: Optional[setAutoAttachParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Controls whether to automatically attach to new targets which are considered to be directly related to this one (for example, iframes or workers). When turned on, attaches to all existing related targets as well. When turned off, automatically detaches from all currently attached targets. This also clears all targets added by `autoAttachRelated` from the list of targets to watch for creation of related targets. You might want to call this recursively for auto-attached targets to attach to all available targets."""
        return await self.client.send(method="Target.setAutoAttach", params=params,session_id=session_id)

    async def auto_attach_related(self, params: Optional[autoAttachRelatedParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Adds the specified target to the list of targets that will be monitored for any related target creation (such as child frames, child workers and new versions of service worker) and reported through `attachedToTarget`. The specified target is also auto-attached. This cancels the effect of any previous `setAutoAttach` and is also cancelled by subsequent `setAutoAttach`. Only available at the Browser target."""
        return await self.client.send(method="Target.autoAttachRelated", params=params,session_id=session_id)

    async def set_discover_targets(self, params: Optional[setDiscoverTargetsParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Controls whether to discover available targets and notify via `targetCreated/targetInfoChanged/targetDestroyed` events."""
        return await self.client.send(method="Target.setDiscoverTargets", params=params,session_id=session_id)

    async def set_remote_locations(self, params: Optional[setRemoteLocationsParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Enables target discovery for the specified locations, when `setDiscoverTargets` was set to `true`."""
        return await self.client.send(method="Target.setRemoteLocations", params=params,session_id=session_id)

    async def open_dev_tools(self, params: Optional[openDevToolsParameters]=None,session_id: Optional[str] = None) -> openDevToolsReturns:
        """Opens a DevTools window for the target."""
        return await self.client.send(method="Target.openDevTools", params=params,session_id=session_id)
