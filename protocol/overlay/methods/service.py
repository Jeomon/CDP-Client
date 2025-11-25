
"""CDP Overlay Methods"""

from client.methods import CDPMethods
from typing import TypedDict,Optional
from protocol.overlay.methods.types import *

class OverlayMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def disable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Disables domain notifications."""
        return await self.methods.send(method="Overlay.disable", params=params,session_id=session_id)

    async def enable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Enables domain notifications."""
        return await self.methods.send(method="Overlay.enable", params=params,session_id=session_id)

    async def get_highlight_object_for_test(self, params: Optional[getHighlightObjectForTestParameters]=None,session_id: Optional[str] = None) -> getHighlightObjectForTestReturns:
        """For testing."""
        return await self.methods.send(method="Overlay.getHighlightObjectForTest", params=params,session_id=session_id)

    async def get_grid_highlight_objects_for_test(self, params: Optional[getGridHighlightObjectsForTestParameters]=None,session_id: Optional[str] = None) -> getGridHighlightObjectsForTestReturns:
        """For Persistent Grid testing."""
        return await self.methods.send(method="Overlay.getGridHighlightObjectsForTest", params=params,session_id=session_id)

    async def get_source_order_highlight_object_for_test(self, params: Optional[getSourceOrderHighlightObjectForTestParameters]=None,session_id: Optional[str] = None) -> getSourceOrderHighlightObjectForTestReturns:
        """For Source Order Viewer testing."""
        return await self.methods.send(method="Overlay.getSourceOrderHighlightObjectForTest", params=params,session_id=session_id)

    async def hide_highlight(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Hides any highlight."""
        return await self.methods.send(method="Overlay.hideHighlight", params=params,session_id=session_id)

    async def highlight_node(self, params: Optional[highlightNodeParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Highlights DOM node with given id or with the given JavaScript object wrapper. Either nodeId or objectId must be specified."""
        return await self.methods.send(method="Overlay.highlightNode", params=params,session_id=session_id)

    async def highlight_quad(self, params: Optional[highlightQuadParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Highlights given quad. Coordinates are absolute with respect to the main frame viewport."""
        return await self.methods.send(method="Overlay.highlightQuad", params=params,session_id=session_id)

    async def highlight_rect(self, params: Optional[highlightRectParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Highlights given rectangle. Coordinates are absolute with respect to the main frame viewport. Issue: the method does not handle device pixel ratio (DPR) correctly. The coordinates currently have to be adjusted by the client if DPR is not 1 (see crbug.com/437807128)."""
        return await self.methods.send(method="Overlay.highlightRect", params=params,session_id=session_id)

    async def highlight_source_order(self, params: Optional[highlightSourceOrderParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Highlights the source order of the children of the DOM node with given id or with the given JavaScript object wrapper. Either nodeId or objectId must be specified."""
        return await self.methods.send(method="Overlay.highlightSourceOrder", params=params,session_id=session_id)

    async def set_inspect_mode(self, params: Optional[setInspectModeParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Enters the 'inspect' mode. In this mode, elements that user is hovering over are highlighted. Backend then generates 'inspectNodeRequested' event upon element selection."""
        return await self.methods.send(method="Overlay.setInspectMode", params=params,session_id=session_id)

    async def set_show_ad_highlights(self, params: Optional[setShowAdHighlightsParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Highlights owner element of all frames detected to be ads."""
        return await self.methods.send(method="Overlay.setShowAdHighlights", params=params,session_id=session_id)

    async def set_paused_in_debugger_message(self, params: Optional[setPausedInDebuggerMessageParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        return await self.methods.send(method="Overlay.setPausedInDebuggerMessage", params=params,session_id=session_id)

    async def set_show_debug_borders(self, params: Optional[setShowDebugBordersParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Requests that backend shows debug borders on layers"""
        return await self.methods.send(method="Overlay.setShowDebugBorders", params=params,session_id=session_id)

    async def set_show_fps_counter(self, params: Optional[setShowFPSCounterParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Requests that backend shows the FPS counter"""
        return await self.methods.send(method="Overlay.setShowFPSCounter", params=params,session_id=session_id)

    async def set_show_grid_overlays(self, params: Optional[setShowGridOverlaysParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Highlight multiple elements with the CSS Grid overlay."""
        return await self.methods.send(method="Overlay.setShowGridOverlays", params=params,session_id=session_id)

    async def set_show_flex_overlays(self, params: Optional[setShowFlexOverlaysParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        return await self.methods.send(method="Overlay.setShowFlexOverlays", params=params,session_id=session_id)

    async def set_show_scroll_snap_overlays(self, params: Optional[setShowScrollSnapOverlaysParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        return await self.methods.send(method="Overlay.setShowScrollSnapOverlays", params=params,session_id=session_id)

    async def set_show_container_query_overlays(self, params: Optional[setShowContainerQueryOverlaysParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        return await self.methods.send(method="Overlay.setShowContainerQueryOverlays", params=params,session_id=session_id)

    async def set_show_paint_rects(self, params: Optional[setShowPaintRectsParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Requests that backend shows paint rectangles"""
        return await self.methods.send(method="Overlay.setShowPaintRects", params=params,session_id=session_id)

    async def set_show_layout_shift_regions(self, params: Optional[setShowLayoutShiftRegionsParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Requests that backend shows layout shift regions"""
        return await self.methods.send(method="Overlay.setShowLayoutShiftRegions", params=params,session_id=session_id)

    async def set_show_scroll_bottleneck_rects(self, params: Optional[setShowScrollBottleneckRectsParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Requests that backend shows scroll bottleneck rects"""
        return await self.methods.send(method="Overlay.setShowScrollBottleneckRects", params=params,session_id=session_id)

    async def set_show_viewport_size_on_resize(self, params: Optional[setShowViewportSizeOnResizeParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Paints viewport size upon main frame resize."""
        return await self.methods.send(method="Overlay.setShowViewportSizeOnResize", params=params,session_id=session_id)

    async def set_show_hinge(self, params: Optional[setShowHingeParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Add a dual screen device hinge"""
        return await self.methods.send(method="Overlay.setShowHinge", params=params,session_id=session_id)

    async def set_show_isolated_elements(self, params: Optional[setShowIsolatedElementsParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Show elements in isolation mode with overlays."""
        return await self.methods.send(method="Overlay.setShowIsolatedElements", params=params,session_id=session_id)

    async def set_show_window_controls_overlay(self, params: Optional[setShowWindowControlsOverlayParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Show Window Controls Overlay for PWA"""
        return await self.methods.send(method="Overlay.setShowWindowControlsOverlay", params=params,session_id=session_id)
