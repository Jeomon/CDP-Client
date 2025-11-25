
"""CDP Page Methods"""

from client.methods import CDPMethods
from typing import TypedDict,Optional
from protocol.page.methods.types import *

class PageMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def add_script_to_evaluate_on_new_document(self, params: Optional[addScriptToEvaluateOnNewDocumentParameters]=None) -> addScriptToEvaluateOnNewDocumentReturns:
        """Evaluates given script in every frame upon creation (before loading frame's scripts)."""
        return await self.methods.send(method="Page.addScriptToEvaluateOnNewDocument", params=params)

    async def bring_to_front(self, params: None=None) -> Dict[str, Any]:
        """Brings page to front (activates tab)."""
        return await self.methods.send(method="Page.bringToFront", params=params)

    async def capture_screenshot(self, params: Optional[captureScreenshotParameters]=None) -> captureScreenshotReturns:
        """Capture page screenshot."""
        return await self.methods.send(method="Page.captureScreenshot", params=params)

    async def capture_snapshot(self, params: Optional[captureSnapshotParameters]=None) -> captureSnapshotReturns:
        """Returns a snapshot of the page as a string. For MHTML format, the serialization includes iframes, shadow DOM, external resources, and element-inline styles."""
        return await self.methods.send(method="Page.captureSnapshot", params=params)

    async def create_isolated_world(self, params: Optional[createIsolatedWorldParameters]=None) -> createIsolatedWorldReturns:
        """Creates an isolated world for the given frame."""
        return await self.methods.send(method="Page.createIsolatedWorld", params=params)

    async def disable(self, params: None=None) -> Dict[str, Any]:
        """Disables page domain notifications."""
        return await self.methods.send(method="Page.disable", params=params)

    async def enable(self, params: Optional[enableParameters]=None) -> Dict[str, Any]:
        """Enables page domain notifications."""
        return await self.methods.send(method="Page.enable", params=params)

    async def get_app_manifest(self, params: Optional[getAppManifestParameters]=None) -> getAppManifestReturns:
        """Gets the processed manifest for this current document.   This API always waits for the manifest to be loaded.   If manifestId is provided, and it does not match the manifest of the     current document, this API errors out.   If there is not a loaded page, this API errors out immediately."""
        return await self.methods.send(method="Page.getAppManifest", params=params)

    async def get_installability_errors(self, params: None=None) -> getInstallabilityErrorsReturns:
        return await self.methods.send(method="Page.getInstallabilityErrors", params=params)

    async def get_app_id(self, params: None=None) -> getAppIdReturns:
        """Returns the unique (PWA) app id. Only returns values if the feature flag 'WebAppEnableManifestId' is enabled"""
        return await self.methods.send(method="Page.getAppId", params=params)

    async def get_ad_script_ancestry(self, params: Optional[getAdScriptAncestryParameters]=None) -> getAdScriptAncestryReturns:
        return await self.methods.send(method="Page.getAdScriptAncestry", params=params)

    async def get_frame_tree(self, params: None=None) -> getFrameTreeReturns:
        """Returns present frame tree structure."""
        return await self.methods.send(method="Page.getFrameTree", params=params)

    async def get_layout_metrics(self, params: None=None) -> getLayoutMetricsReturns:
        """Returns metrics relating to the layouting of the page, such as viewport bounds/scale."""
        return await self.methods.send(method="Page.getLayoutMetrics", params=params)

    async def get_navigation_history(self, params: None=None) -> getNavigationHistoryReturns:
        """Returns navigation history for the current page."""
        return await self.methods.send(method="Page.getNavigationHistory", params=params)

    async def reset_navigation_history(self, params: None=None) -> Dict[str, Any]:
        """Resets navigation history for the current page."""
        return await self.methods.send(method="Page.resetNavigationHistory", params=params)

    async def get_resource_content(self, params: Optional[getResourceContentParameters]=None) -> getResourceContentReturns:
        """Returns content of the given resource."""
        return await self.methods.send(method="Page.getResourceContent", params=params)

    async def get_resource_tree(self, params: None=None) -> getResourceTreeReturns:
        """Returns present frame / resource tree structure."""
        return await self.methods.send(method="Page.getResourceTree", params=params)

    async def handle_java_script_dialog(self, params: Optional[handleJavaScriptDialogParameters]=None) -> Dict[str, Any]:
        """Accepts or dismisses a JavaScript initiated dialog (alert, confirm, prompt, or onbeforeunload)."""
        return await self.methods.send(method="Page.handleJavaScriptDialog", params=params)

    async def navigate(self, params: Optional[navigateParameters]=None) -> navigateReturns:
        """Navigates current page to the given URL."""
        return await self.methods.send(method="Page.navigate", params=params)

    async def navigate_to_history_entry(self, params: Optional[navigateToHistoryEntryParameters]=None) -> Dict[str, Any]:
        """Navigates current page to the given history entry."""
        return await self.methods.send(method="Page.navigateToHistoryEntry", params=params)

    async def print_to_pdf(self, params: Optional[printToPDFParameters]=None) -> printToPDFReturns:
        """Print page as PDF."""
        return await self.methods.send(method="Page.printToPDF", params=params)

    async def reload(self, params: Optional[reloadParameters]=None) -> Dict[str, Any]:
        """Reloads given page optionally ignoring the cache."""
        return await self.methods.send(method="Page.reload", params=params)

    async def remove_script_to_evaluate_on_new_document(self, params: Optional[removeScriptToEvaluateOnNewDocumentParameters]=None) -> Dict[str, Any]:
        """Removes given script from the list."""
        return await self.methods.send(method="Page.removeScriptToEvaluateOnNewDocument", params=params)

    async def screencast_frame_ack(self, params: Optional[screencastFrameAckParameters]=None) -> Dict[str, Any]:
        """Acknowledges that a screencast frame has been received by the frontend."""
        return await self.methods.send(method="Page.screencastFrameAck", params=params)

    async def search_in_resource(self, params: Optional[searchInResourceParameters]=None) -> searchInResourceReturns:
        """Searches for given string in resource content."""
        return await self.methods.send(method="Page.searchInResource", params=params)

    async def set_ad_blocking_enabled(self, params: Optional[setAdBlockingEnabledParameters]=None) -> Dict[str, Any]:
        """Enable Chrome's experimental ad filter on all sites."""
        return await self.methods.send(method="Page.setAdBlockingEnabled", params=params)

    async def set_bypass_csp(self, params: Optional[setBypassCSPParameters]=None) -> Dict[str, Any]:
        """Enable page Content Security Policy by-passing."""
        return await self.methods.send(method="Page.setBypassCSP", params=params)

    async def get_permissions_policy_state(self, params: Optional[getPermissionsPolicyStateParameters]=None) -> getPermissionsPolicyStateReturns:
        """Get Permissions Policy state on given frame."""
        return await self.methods.send(method="Page.getPermissionsPolicyState", params=params)

    async def get_origin_trials(self, params: Optional[getOriginTrialsParameters]=None) -> getOriginTrialsReturns:
        """Get Origin Trials on given frame."""
        return await self.methods.send(method="Page.getOriginTrials", params=params)

    async def set_font_families(self, params: Optional[setFontFamiliesParameters]=None) -> Dict[str, Any]:
        """Set generic font families."""
        return await self.methods.send(method="Page.setFontFamilies", params=params)

    async def set_font_sizes(self, params: Optional[setFontSizesParameters]=None) -> Dict[str, Any]:
        """Set default font sizes."""
        return await self.methods.send(method="Page.setFontSizes", params=params)

    async def set_document_content(self, params: Optional[setDocumentContentParameters]=None) -> Dict[str, Any]:
        """Sets given markup as the document's HTML."""
        return await self.methods.send(method="Page.setDocumentContent", params=params)

    async def set_lifecycle_events_enabled(self, params: Optional[setLifecycleEventsEnabledParameters]=None) -> Dict[str, Any]:
        """Controls whether page will emit lifecycle events."""
        return await self.methods.send(method="Page.setLifecycleEventsEnabled", params=params)

    async def start_screencast(self, params: Optional[startScreencastParameters]=None) -> Dict[str, Any]:
        """Starts sending each frame using the `screencastFrame` event."""
        return await self.methods.send(method="Page.startScreencast", params=params)

    async def stop_loading(self, params: None=None) -> Dict[str, Any]:
        """Force the page stop all navigations and pending resource fetches."""
        return await self.methods.send(method="Page.stopLoading", params=params)

    async def crash(self, params: None=None) -> Dict[str, Any]:
        """Crashes renderer on the IO thread, generates minidumps."""
        return await self.methods.send(method="Page.crash", params=params)

    async def close(self, params: None=None) -> Dict[str, Any]:
        """Tries to close page, running its beforeunload hooks, if any."""
        return await self.methods.send(method="Page.close", params=params)

    async def set_web_lifecycle_state(self, params: Optional[setWebLifecycleStateParameters]=None) -> Dict[str, Any]:
        """Tries to update the web lifecycle state of the page. It will transition the page to the given state according to: https://github.com/WICG/web-lifecycle/"""
        return await self.methods.send(method="Page.setWebLifecycleState", params=params)

    async def stop_screencast(self, params: None=None) -> Dict[str, Any]:
        """Stops sending each frame in the `screencastFrame`."""
        return await self.methods.send(method="Page.stopScreencast", params=params)

    async def produce_compilation_cache(self, params: Optional[produceCompilationCacheParameters]=None) -> Dict[str, Any]:
        """Requests backend to produce compilation cache for the specified scripts. `scripts` are appended to the list of scripts for which the cache would be produced. The list may be reset during page navigation. When script with a matching URL is encountered, the cache is optionally produced upon backend discretion, based on internal heuristics. See also: `Page.compilationCacheProduced`."""
        return await self.methods.send(method="Page.produceCompilationCache", params=params)

    async def add_compilation_cache(self, params: Optional[addCompilationCacheParameters]=None) -> Dict[str, Any]:
        """Seeds compilation cache for given url. Compilation cache does not survive cross-process navigation."""
        return await self.methods.send(method="Page.addCompilationCache", params=params)

    async def clear_compilation_cache(self, params: None=None) -> Dict[str, Any]:
        """Clears seeded compilation cache."""
        return await self.methods.send(method="Page.clearCompilationCache", params=params)

    async def set_spc_transaction_mode(self, params: Optional[setSPCTransactionModeParameters]=None) -> Dict[str, Any]:
        """Sets the Secure Payment Confirmation transaction mode. https://w3c.github.io/secure-payment-confirmation/#sctn-automation-set-spc-transaction-mode"""
        return await self.methods.send(method="Page.setSPCTransactionMode", params=params)

    async def set_rph_registration_mode(self, params: Optional[setRPHRegistrationModeParameters]=None) -> Dict[str, Any]:
        """Extensions for Custom Handlers API: https://html.spec.whatwg.org/multipage/system-state.html#rph-automation"""
        return await self.methods.send(method="Page.setRPHRegistrationMode", params=params)

    async def generate_test_report(self, params: Optional[generateTestReportParameters]=None) -> Dict[str, Any]:
        """Generates a report for testing."""
        return await self.methods.send(method="Page.generateTestReport", params=params)

    async def wait_for_debugger(self, params: None=None) -> Dict[str, Any]:
        """Pauses page execution. Can be resumed using generic Runtime.runIfWaitingForDebugger."""
        return await self.methods.send(method="Page.waitForDebugger", params=params)

    async def set_intercept_file_chooser_dialog(self, params: Optional[setInterceptFileChooserDialogParameters]=None) -> Dict[str, Any]:
        """Intercept file chooser requests and transfer control to protocol clients. When file chooser interception is enabled, native file chooser dialog is not shown. Instead, a protocol event `Page.fileChooserOpened` is emitted."""
        return await self.methods.send(method="Page.setInterceptFileChooserDialog", params=params)

    async def set_prerendering_allowed(self, params: Optional[setPrerenderingAllowedParameters]=None) -> Dict[str, Any]:
        """Enable/disable prerendering manually.  This command is a short-term solution for https://crbug.com/1440085. See https://docs.google.com/document/d/12HVmFxYj5Jc-eJr5OmWsa2bqTJsbgGLKI6ZIyx0_wpA for more details.  TODO(https://crbug.com/1440085): Remove this once Puppeteer supports tab targets."""
        return await self.methods.send(method="Page.setPrerenderingAllowed", params=params)

    async def get_annotated_page_content(self, params: Optional[getAnnotatedPageContentParameters]=None) -> getAnnotatedPageContentReturns:
        """Get the annotated page content for the main frame. This is an experimental command that is subject to change."""
        return await self.methods.send(method="Page.getAnnotatedPageContent", params=params)
