
"""CDP Input Methods"""

from cdp_client.methods import CDPMethods
from typing import TypedDict,Optional
from input.methods.types import *

class InputMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def dispatch_drag_event(self, params: Optional[dispatchDragEventParameters]=None) -> Dict[str, Any]:
        """Dispatches a drag event into the page."""
        return await self.methods.send(method="Input.dispatchDragEvent", params=params)

    async def dispatch_key_event(self, params: Optional[dispatchKeyEventParameters]=None) -> Dict[str, Any]:
        """Dispatches a key event to the page."""
        return await self.methods.send(method="Input.dispatchKeyEvent", params=params)

    async def insert_text(self, params: Optional[insertTextParameters]=None) -> Dict[str, Any]:
        """This method emulates inserting text that doesn't come from a key press, for example an emoji keyboard or an IME."""
        return await self.methods.send(method="Input.insertText", params=params)

    async def ime_set_composition(self, params: Optional[imeSetCompositionParameters]=None) -> Dict[str, Any]:
        """This method sets the current candidate text for IME. Use imeCommitComposition to commit the final text. Use imeSetComposition with empty string as text to cancel composition."""
        return await self.methods.send(method="Input.imeSetComposition", params=params)

    async def dispatch_mouse_event(self, params: Optional[dispatchMouseEventParameters]=None) -> Dict[str, Any]:
        """Dispatches a mouse event to the page."""
        return await self.methods.send(method="Input.dispatchMouseEvent", params=params)

    async def dispatch_touch_event(self, params: Optional[dispatchTouchEventParameters]=None) -> Dict[str, Any]:
        """Dispatches a touch event to the page."""
        return await self.methods.send(method="Input.dispatchTouchEvent", params=params)

    async def cancel_dragging(self, params: None=None) -> Dict[str, Any]:
        """Cancels any active dragging in the page."""
        return await self.methods.send(method="Input.cancelDragging", params=params)

    async def emulate_touch_from_mouse_event(self, params: Optional[emulateTouchFromMouseEventParameters]=None) -> Dict[str, Any]:
        """Emulates touch event from the mouse event parameters."""
        return await self.methods.send(method="Input.emulateTouchFromMouseEvent", params=params)

    async def set_ignore_input_events(self, params: Optional[setIgnoreInputEventsParameters]=None) -> Dict[str, Any]:
        """Ignores input events (useful while auditing page)."""
        return await self.methods.send(method="Input.setIgnoreInputEvents", params=params)

    async def set_intercept_drags(self, params: Optional[setInterceptDragsParameters]=None) -> Dict[str, Any]:
        """Prevents default drag and drop behavior and instead emits `Input.dragIntercepted` events. Drag and drop behavior can be directly controlled via `Input.dispatchDragEvent`."""
        return await self.methods.send(method="Input.setInterceptDrags", params=params)

    async def synthesize_pinch_gesture(self, params: Optional[synthesizePinchGestureParameters]=None) -> Dict[str, Any]:
        """Synthesizes a pinch gesture over a time period by issuing appropriate touch events."""
        return await self.methods.send(method="Input.synthesizePinchGesture", params=params)

    async def synthesize_scroll_gesture(self, params: Optional[synthesizeScrollGestureParameters]=None) -> Dict[str, Any]:
        """Synthesizes a scroll gesture over a time period by issuing appropriate touch events."""
        return await self.methods.send(method="Input.synthesizeScrollGesture", params=params)

    async def synthesize_tap_gesture(self, params: Optional[synthesizeTapGestureParameters]=None) -> Dict[str, Any]:
        """Synthesizes a tap gesture over a time period by issuing appropriate touch events."""
        return await self.methods.send(method="Input.synthesizeTapGesture", params=params)
