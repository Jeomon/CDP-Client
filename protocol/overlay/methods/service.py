
"""CDP Overlay Methods"""

from cdp_client.methods import CDPMethods
from typing import TypedDict,Optional
from overlay.methods.types import *

class OverlayMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def disable(self, params: None=None) -> Dict[str, Any]:
        """Disables domain notifications."""
        return await self.methods.send(method="Overlay.disable", params=params)

    async def enable(self, params: None=None) -> Dict[str, Any]:
        """Enables domain notifications."""
        return await self.methods.send(method="Overlay.enable", params=params)

    async def get_highlight_object_for_test(self, params: Optional[getHighlightObjectForTestParameters]=None) -> getHighlightObjectForTestReturns:
        """For testing."""
        return await self.methods.send(method="Overlay.getHighlightObjectForTest", params=params)

    async def get_grid_highlight_objects_for_test(self, params: Optional[getGridHighlightObjectsForTestParameters]=None) -> getGridHighlightObjectsForTestReturns:
        """For Persistent Grid testing."""
        return await self.methods.send(method="Overlay.getGridHighlightObjectsForTest", params=params)

    async def get_source_order_highlight_object_for_test(self, params: Optional[getSourceOrderHighlightObjectForTestParameters]=None) -> getSourceOrderHighlightObjectForTestReturns:
        """For Source Order Viewer testing."""
        return await self.methods.send(method="Overlay.getSourceOrderHighlightObjectForTest", params=params)

    async def hide_highlight(self, params: None=None) -> Dict[str, Any]:
        """Hides any highlight."""
        return await self.methods.send(method="Overlay.hideHighlight", params=params)

    async def highlight_node(self, params: Optional[highlightNodeParameters]=None) -> Dict[str, Any]:
        """Highlights DOM node with given id or with the given JavaScript object wrapper. Either nodeId or objectId must be specified."""
        return await self.methods.send(method="Overlay.highlightNode", params=params)

    async def highlight_quad(self, params: Optional[highlightQuadParameters]=None) -> Dict[str, Any]:
        """Highlights given quad. Coordinates are absolute with respect to the main frame viewport."""
        return await self.methods.send(method="Overlay.highlightQuad", params=params)

    async def highlight_rect(self, params: Optional[highlightRectParameters]=None) -> Dict[str, Any]:
        """Highlights given rectangle. Coordinates are absolute with respect to the main frame viewport. Issue: the method does not handle device pixel ratio (DPR) correctly. The coordinates currently have to be adjusted by the client if DPR is not 1 (see crbug.com/437807128)."""
        return await self.methods.send(method="Overlay.highlightRect", params=params)

    async def highlight_source_order(self, params: Optional[highlightSourceOrderParameters]=None) -> Dict[str, Any]:
        """Highlights the source order of the children of the DOM node with given id or with the given JavaScript object wrapper. Either nodeId or objectId must be specified."""
        return await self.methods.send(method="Overlay.highlightSourceOrder", params=params)

    async def set_inspect_mode(self, params: Optional[setInspectModeParameters]=None) -> Dict[str, Any]:
        """Enters the 'inspect' mode. In this mode, elements that user is hovering over are highlighted. Backend then generates 'inspectNodeRequested' event upon element selection."""
        return await self.methods.send(method="Overlay.setInspectMode", params=params)

    async def set_show_ad_highlights(self, params: Optional[setShowAdHighlightsParameters]=None) -> Dict[str, Any]:
        """Highlights owner element of all frames detected to be ads."""
        return await self.methods.send(method="Overlay.setShowAdHighlights", params=params)

    async def set_paused_in_debugger_message(self, params: Optional[setPausedInDebuggerMessageParameters]=None) -> Dict[str, Any]:
        return await self.methods.send(method="Overlay.setPausedInDebuggerMessage", params=params)

    async def set_show_debug_borders(self, params: Optional[setShowDebugBordersParameters]=None) -> Dict[str, Any]:
        """Requests that backend shows debug borders on layers"""
        return await self.methods.send(method="Overlay.setShowDebugBorders", params=params)

    async def set_show_fps_counter(self, params: Optional[setShowFPSCounterParameters]=None) -> Dict[str, Any]:
        """Requests that backend shows the FPS counter"""
        return await self.methods.send(method="Overlay.setShowFPSCounter", params=params)

    async def set_show_grid_overlays(self, params: Optional[setShowGridOverlaysParameters]=None) -> Dict[str, Any]:
        """Highlight multiple elements with the CSS Grid overlay."""
        return await self.methods.send(method="Overlay.setShowGridOverlays", params=params)

    async def set_show_flex_overlays(self, params: Optional[setShowFlexOverlaysParameters]=None) -> Dict[str, Any]:
        return await self.methods.send(method="Overlay.setShowFlexOverlays", params=params)

    async def set_show_scroll_snap_overlays(self, params: Optional[setShowScrollSnapOverlaysParameters]=None) -> Dict[str, Any]:
        return await self.methods.send(method="Overlay.setShowScrollSnapOverlays", params=params)

    async def set_show_container_query_overlays(self, params: Optional[setShowContainerQueryOverlaysParameters]=None) -> Dict[str, Any]:
        return await self.methods.send(method="Overlay.setShowContainerQueryOverlays", params=params)

    async def set_show_paint_rects(self, params: Optional[setShowPaintRectsParameters]=None) -> Dict[str, Any]:
        """Requests that backend shows paint rectangles"""
        return await self.methods.send(method="Overlay.setShowPaintRects", params=params)

    async def set_show_layout_shift_regions(self, params: Optional[setShowLayoutShiftRegionsParameters]=None) -> Dict[str, Any]:
        """Requests that backend shows layout shift regions"""
        return await self.methods.send(method="Overlay.setShowLayoutShiftRegions", params=params)

    async def set_show_scroll_bottleneck_rects(self, params: Optional[setShowScrollBottleneckRectsParameters]=None) -> Dict[str, Any]:
        """Requests that backend shows scroll bottleneck rects"""
        return await self.methods.send(method="Overlay.setShowScrollBottleneckRects", params=params)

    async def set_show_viewport_size_on_resize(self, params: Optional[setShowViewportSizeOnResizeParameters]=None) -> Dict[str, Any]:
        """Paints viewport size upon main frame resize."""
        return await self.methods.send(method="Overlay.setShowViewportSizeOnResize", params=params)

    async def set_show_hinge(self, params: Optional[setShowHingeParameters]=None) -> Dict[str, Any]:
        """Add a dual screen device hinge"""
        return await self.methods.send(method="Overlay.setShowHinge", params=params)

    async def set_show_isolated_elements(self, params: Optional[setShowIsolatedElementsParameters]=None) -> Dict[str, Any]:
        """Show elements in isolation mode with overlays."""
        return await self.methods.send(method="Overlay.setShowIsolatedElements", params=params)

    async def set_show_window_controls_overlay(self, params: Optional[setShowWindowControlsOverlayParameters]=None) -> Dict[str, Any]:
        """Show Window Controls Overlay for PWA"""
        return await self.methods.send(method="Overlay.setShowWindowControlsOverlay", params=params)
