
"""CDP PWA Methods"""

from client.service import CDPClient
from typing import TypedDict,Optional
from protocol.pwa.methods.types import *

class PWAMethods:
    def __init__(self, client:CDPClient):
        self.client = client

    async def get_os_app_state(self, params: Optional[getOsAppStateParameters]=None,session_id: Optional[str] = None) -> getOsAppStateReturns:
        """Returns the following OS state for the given manifest id."""
        return await self.client.send(method="PWA.getOsAppState", params=params,session_id=session_id)

    async def install(self, params: Optional[installParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Installs the given manifest identity, optionally using the given installUrlOrBundleUrl  IWA-specific install description: manifestId corresponds to isolated-app:// + web_package::SignedWebBundleId  File installation mode: The installUrlOrBundleUrl can be either file:// or http(s):// pointing to a signed web bundle (.swbn). In this case SignedWebBundleId must correspond to The .swbn file's signing key.  Dev proxy installation mode: installUrlOrBundleUrl must be http(s):// that serves dev mode IWA. web_package::SignedWebBundleId must be of type dev proxy.  The advantage of dev proxy mode is that all changes to IWA automatically will be reflected in the running app without reinstallation.  To generate bundle id for proxy mode: 1. Generate 32 random bytes. 2. Add a specific suffix at the end following the documentation    https://github.com/WICG/isolated-web-apps/blob/main/Scheme.md#suffix 3. Encode the entire sequence using Base32 without padding.  If Chrome is not in IWA dev mode, the installation will fail, regardless of the state of the allowlist."""
        return await self.client.send(method="PWA.install", params=params,session_id=session_id)

    async def uninstall(self, params: Optional[uninstallParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Uninstalls the given manifest_id and closes any opened app windows."""
        return await self.client.send(method="PWA.uninstall", params=params,session_id=session_id)

    async def launch(self, params: Optional[launchParameters]=None,session_id: Optional[str] = None) -> launchReturns:
        """Launches the installed web app, or an url in the same web app instead of the default start url if it is provided. Returns a page Target.TargetID which can be used to attach to via Target.attachToTarget or similar APIs."""
        return await self.client.send(method="PWA.launch", params=params,session_id=session_id)

    async def launch_files_in_app(self, params: Optional[launchFilesInAppParameters]=None,session_id: Optional[str] = None) -> launchFilesInAppReturns:
        """Opens one or more local files from an installed web app identified by its manifestId. The web app needs to have file handlers registered to process the files. The API returns one or more page Target.TargetIDs which can be used to attach to via Target.attachToTarget or similar APIs. If some files in the parameters cannot be handled by the web app, they will be ignored. If none of the files can be handled, this API returns an error. If no files are provided as the parameter, this API also returns an error.  According to the definition of the file handlers in the manifest file, one Target.TargetID may represent a page handling one or more files. The order of the returned Target.TargetIDs is not guaranteed.  TODO(crbug.com/339454034): Check the existences of the input files."""
        return await self.client.send(method="PWA.launchFilesInApp", params=params,session_id=session_id)

    async def open_current_page_in_app(self, params: Optional[openCurrentPageInAppParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Opens the current page in its web app identified by the manifest id, needs to be called on a page target. This function returns immediately without waiting for the app to finish loading."""
        return await self.client.send(method="PWA.openCurrentPageInApp", params=params,session_id=session_id)

    async def change_app_user_settings(self, params: Optional[changeAppUserSettingsParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Changes user settings of the web app identified by its manifestId. If the app was not installed, this command returns an error. Unset parameters will be ignored; unrecognized values will cause an error.  Unlike the ones defined in the manifest files of the web apps, these settings are provided by the browser and controlled by the users, they impact the way the browser handling the web apps.  See the comment of each parameter."""
        return await self.client.send(method="PWA.changeAppUserSettings", params=params,session_id=session_id)
