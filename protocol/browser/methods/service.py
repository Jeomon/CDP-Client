
"""CDP Browser Methods"""

from cdp_client.methods import CDPMethods
from typing import TypedDict,Optional
from browser.methods.types import *

class BrowserMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def set_permission(self, params: Optional[setPermissionParameters]=None) -> Dict[str, Any]:
        """Set permission settings for given embedding and embedded origins."""
        return await self.methods.send(method="Browser.setPermission", params=params)

    async def reset_permissions(self, params: Optional[resetPermissionsParameters]=None) -> Dict[str, Any]:
        """Reset all permission management for all origins."""
        return await self.methods.send(method="Browser.resetPermissions", params=params)

    async def set_download_behavior(self, params: Optional[setDownloadBehaviorParameters]=None) -> Dict[str, Any]:
        """Set the behavior when downloading a file."""
        return await self.methods.send(method="Browser.setDownloadBehavior", params=params)

    async def cancel_download(self, params: Optional[cancelDownloadParameters]=None) -> Dict[str, Any]:
        """Cancel a download if in progress"""
        return await self.methods.send(method="Browser.cancelDownload", params=params)

    async def close(self, params: None=None) -> Dict[str, Any]:
        """Close browser gracefully."""
        return await self.methods.send(method="Browser.close", params=params)

    async def crash(self, params: None=None) -> Dict[str, Any]:
        """Crashes browser on the main thread."""
        return await self.methods.send(method="Browser.crash", params=params)

    async def crash_gpu_process(self, params: None=None) -> Dict[str, Any]:
        """Crashes GPU process."""
        return await self.methods.send(method="Browser.crashGpuProcess", params=params)

    async def get_version(self, params: None=None) -> getVersionReturns:
        """Returns version information."""
        return await self.methods.send(method="Browser.getVersion", params=params)

    async def get_browser_command_line(self, params: None=None) -> getBrowserCommandLineReturns:
        """Returns the command line switches for the browser process if, and only if --enable-automation is on the commandline."""
        return await self.methods.send(method="Browser.getBrowserCommandLine", params=params)

    async def get_histograms(self, params: Optional[getHistogramsParameters]=None) -> getHistogramsReturns:
        """Get Chrome histograms."""
        return await self.methods.send(method="Browser.getHistograms", params=params)

    async def get_histogram(self, params: Optional[getHistogramParameters]=None) -> getHistogramReturns:
        """Get a Chrome histogram by name."""
        return await self.methods.send(method="Browser.getHistogram", params=params)

    async def get_window_bounds(self, params: Optional[getWindowBoundsParameters]=None) -> getWindowBoundsReturns:
        """Get position and size of the browser window."""
        return await self.methods.send(method="Browser.getWindowBounds", params=params)

    async def get_window_for_target(self, params: Optional[getWindowForTargetParameters]=None) -> getWindowForTargetReturns:
        """Get the browser window that contains the devtools target."""
        return await self.methods.send(method="Browser.getWindowForTarget", params=params)

    async def set_window_bounds(self, params: Optional[setWindowBoundsParameters]=None) -> Dict[str, Any]:
        """Set position and/or size of the browser window."""
        return await self.methods.send(method="Browser.setWindowBounds", params=params)

    async def set_contents_size(self, params: Optional[setContentsSizeParameters]=None) -> Dict[str, Any]:
        """Set size of the browser contents resizing browser window as necessary."""
        return await self.methods.send(method="Browser.setContentsSize", params=params)

    async def set_dock_tile(self, params: Optional[setDockTileParameters]=None) -> Dict[str, Any]:
        """Set dock tile details, platform-specific."""
        return await self.methods.send(method="Browser.setDockTile", params=params)

    async def execute_browser_command(self, params: Optional[executeBrowserCommandParameters]=None) -> Dict[str, Any]:
        """Invoke custom browser commands used by telemetry."""
        return await self.methods.send(method="Browser.executeBrowserCommand", params=params)

    async def add_privacy_sandbox_enrollment_override(self, params: Optional[addPrivacySandboxEnrollmentOverrideParameters]=None) -> Dict[str, Any]:
        """Allows a site to use privacy sandbox features that require enrollment without the site actually being enrolled. Only supported on page targets."""
        return await self.methods.send(method="Browser.addPrivacySandboxEnrollmentOverride", params=params)

    async def add_privacy_sandbox_coordinator_key_config(self, params: Optional[addPrivacySandboxCoordinatorKeyConfigParameters]=None) -> Dict[str, Any]:
        """Configures encryption keys used with a given privacy sandbox API to talk to a trusted coordinator.  Since this is intended for test automation only, coordinatorOrigin must be a .test domain. No existing coordinator configuration for the origin may exist."""
        return await self.methods.send(method="Browser.addPrivacySandboxCoordinatorKeyConfig", params=params)
