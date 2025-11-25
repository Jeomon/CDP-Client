
"""CDP Debugger Methods"""

from client.service import CDPClient
from typing import TypedDict,Optional
from protocol.debugger.methods.types import *

class DebuggerMethods:
    def __init__(self, client:CDPClient):
        self.client = client

    async def continue_to_location(self, params: Optional[continueToLocationParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Continues execution until specific location is reached."""
        return await self.client.send(method="Debugger.continueToLocation", params=params,session_id=session_id)

    async def disable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Disables debugger for given page."""
        return await self.client.send(method="Debugger.disable", params=params,session_id=session_id)

    async def enable(self, params: Optional[enableParameters]=None,session_id: Optional[str] = None) -> enableReturns:
        """Enables debugger for the given page. Clients should not assume that the debugging has been enabled until the result for this command is received."""
        return await self.client.send(method="Debugger.enable", params=params,session_id=session_id)

    async def evaluate_on_call_frame(self, params: Optional[evaluateOnCallFrameParameters]=None,session_id: Optional[str] = None) -> evaluateOnCallFrameReturns:
        """Evaluates expression on a given call frame."""
        return await self.client.send(method="Debugger.evaluateOnCallFrame", params=params,session_id=session_id)

    async def get_possible_breakpoints(self, params: Optional[getPossibleBreakpointsParameters]=None,session_id: Optional[str] = None) -> getPossibleBreakpointsReturns:
        """Returns possible locations for breakpoint. scriptId in start and end range locations should be the same."""
        return await self.client.send(method="Debugger.getPossibleBreakpoints", params=params,session_id=session_id)

    async def get_script_source(self, params: Optional[getScriptSourceParameters]=None,session_id: Optional[str] = None) -> getScriptSourceReturns:
        """Returns source for the script with given id."""
        return await self.client.send(method="Debugger.getScriptSource", params=params,session_id=session_id)

    async def disassemble_wasm_module(self, params: Optional[disassembleWasmModuleParameters]=None,session_id: Optional[str] = None) -> disassembleWasmModuleReturns:
        return await self.client.send(method="Debugger.disassembleWasmModule", params=params,session_id=session_id)

    async def next_wasm_disassembly_chunk(self, params: Optional[nextWasmDisassemblyChunkParameters]=None,session_id: Optional[str] = None) -> nextWasmDisassemblyChunkReturns:
        """Disassemble the next chunk of lines for the module corresponding to the stream. If disassembly is complete, this API will invalidate the streamId and return an empty chunk. Any subsequent calls for the now invalid stream will return errors."""
        return await self.client.send(method="Debugger.nextWasmDisassemblyChunk", params=params,session_id=session_id)

    async def get_stack_trace(self, params: Optional[getStackTraceParameters]=None,session_id: Optional[str] = None) -> getStackTraceReturns:
        """Returns stack trace with given `stackTraceId`."""
        return await self.client.send(method="Debugger.getStackTrace", params=params,session_id=session_id)

    async def pause(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Stops on the next JavaScript statement."""
        return await self.client.send(method="Debugger.pause", params=params,session_id=session_id)

    async def remove_breakpoint(self, params: Optional[removeBreakpointParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Removes JavaScript breakpoint."""
        return await self.client.send(method="Debugger.removeBreakpoint", params=params,session_id=session_id)

    async def restart_frame(self, params: Optional[restartFrameParameters]=None,session_id: Optional[str] = None) -> restartFrameReturns:
        """Restarts particular call frame from the beginning. The old, deprecated behavior of `restartFrame` is to stay paused and allow further CDP commands after a restart was scheduled. This can cause problems with restarting, so we now continue execution immediatly after it has been scheduled until we reach the beginning of the restarted frame.  To stay back-wards compatible, `restartFrame` now expects a `mode` parameter to be present. If the `mode` parameter is missing, `restartFrame` errors out.  The various return values are deprecated and `callFrames` is always empty. Use the call frames from the `Debugger#paused` events instead, that fires once V8 pauses at the beginning of the restarted function."""
        return await self.client.send(method="Debugger.restartFrame", params=params,session_id=session_id)

    async def resume(self, params: Optional[resumeParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Resumes JavaScript execution."""
        return await self.client.send(method="Debugger.resume", params=params,session_id=session_id)

    async def search_in_content(self, params: Optional[searchInContentParameters]=None,session_id: Optional[str] = None) -> searchInContentReturns:
        """Searches for given string in script content."""
        return await self.client.send(method="Debugger.searchInContent", params=params,session_id=session_id)

    async def set_async_call_stack_depth(self, params: Optional[setAsyncCallStackDepthParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Enables or disables async call stacks tracking."""
        return await self.client.send(method="Debugger.setAsyncCallStackDepth", params=params,session_id=session_id)

    async def set_blackbox_execution_contexts(self, params: Optional[setBlackboxExecutionContextsParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Replace previous blackbox execution contexts with passed ones. Forces backend to skip stepping/pausing in scripts in these execution contexts. VM will try to leave blackboxed script by performing 'step in' several times, finally resorting to 'step out' if unsuccessful."""
        return await self.client.send(method="Debugger.setBlackboxExecutionContexts", params=params,session_id=session_id)

    async def set_blackbox_patterns(self, params: Optional[setBlackboxPatternsParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Replace previous blackbox patterns with passed ones. Forces backend to skip stepping/pausing in scripts with url matching one of the patterns. VM will try to leave blackboxed script by performing 'step in' several times, finally resorting to 'step out' if unsuccessful."""
        return await self.client.send(method="Debugger.setBlackboxPatterns", params=params,session_id=session_id)

    async def set_blackboxed_ranges(self, params: Optional[setBlackboxedRangesParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Makes backend skip steps in the script in blackboxed ranges. VM will try leave blacklisted scripts by performing 'step in' several times, finally resorting to 'step out' if unsuccessful. Positions array contains positions where blackbox state is changed. First interval isn't blackboxed. Array should be sorted."""
        return await self.client.send(method="Debugger.setBlackboxedRanges", params=params,session_id=session_id)

    async def set_breakpoint(self, params: Optional[setBreakpointParameters]=None,session_id: Optional[str] = None) -> setBreakpointReturns:
        """Sets JavaScript breakpoint at a given location."""
        return await self.client.send(method="Debugger.setBreakpoint", params=params,session_id=session_id)

    async def set_instrumentation_breakpoint(self, params: Optional[setInstrumentationBreakpointParameters]=None,session_id: Optional[str] = None) -> setInstrumentationBreakpointReturns:
        """Sets instrumentation breakpoint."""
        return await self.client.send(method="Debugger.setInstrumentationBreakpoint", params=params,session_id=session_id)

    async def set_breakpoint_by_url(self, params: Optional[setBreakpointByUrlParameters]=None,session_id: Optional[str] = None) -> setBreakpointByUrlReturns:
        """Sets JavaScript breakpoint at given location specified either by URL or URL regex. Once this command is issued, all existing parsed scripts will have breakpoints resolved and returned in `locations` property. Further matching script parsing will result in subsequent `breakpointResolved` events issued. This logical breakpoint will survive page reloads."""
        return await self.client.send(method="Debugger.setBreakpointByUrl", params=params,session_id=session_id)

    async def set_breakpoint_on_function_call(self, params: Optional[setBreakpointOnFunctionCallParameters]=None,session_id: Optional[str] = None) -> setBreakpointOnFunctionCallReturns:
        """Sets JavaScript breakpoint before each call to the given function. If another function was created from the same source as a given one, calling it will also trigger the breakpoint."""
        return await self.client.send(method="Debugger.setBreakpointOnFunctionCall", params=params,session_id=session_id)

    async def set_breakpoints_active(self, params: Optional[setBreakpointsActiveParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Activates / deactivates all breakpoints on the page."""
        return await self.client.send(method="Debugger.setBreakpointsActive", params=params,session_id=session_id)

    async def set_pause_on_exceptions(self, params: Optional[setPauseOnExceptionsParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Defines pause on exceptions state. Can be set to stop on all exceptions, uncaught exceptions, or caught exceptions, no exceptions. Initial pause on exceptions state is `none`."""
        return await self.client.send(method="Debugger.setPauseOnExceptions", params=params,session_id=session_id)

    async def set_return_value(self, params: Optional[setReturnValueParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Changes return value in top frame. Available only at return break position."""
        return await self.client.send(method="Debugger.setReturnValue", params=params,session_id=session_id)

    async def set_script_source(self, params: Optional[setScriptSourceParameters]=None,session_id: Optional[str] = None) -> setScriptSourceReturns:
        """Edits JavaScript source live.  In general, functions that are currently on the stack can not be edited with a single exception: If the edited function is the top-most stack frame and that is the only activation of that function on the stack. In this case the live edit will be successful and a `Debugger.restartFrame` for the top-most function is automatically triggered."""
        return await self.client.send(method="Debugger.setScriptSource", params=params,session_id=session_id)

    async def set_skip_all_pauses(self, params: Optional[setSkipAllPausesParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Makes page not interrupt on any pauses (breakpoint, exception, dom exception etc)."""
        return await self.client.send(method="Debugger.setSkipAllPauses", params=params,session_id=session_id)

    async def set_variable_value(self, params: Optional[setVariableValueParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Changes value of variable in a callframe. Object-based scopes are not supported and must be mutated manually."""
        return await self.client.send(method="Debugger.setVariableValue", params=params,session_id=session_id)

    async def step_into(self, params: Optional[stepIntoParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Steps into the function call."""
        return await self.client.send(method="Debugger.stepInto", params=params,session_id=session_id)

    async def step_out(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Steps out of the function call."""
        return await self.client.send(method="Debugger.stepOut", params=params,session_id=session_id)

    async def step_over(self, params: Optional[stepOverParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Steps over the statement."""
        return await self.client.send(method="Debugger.stepOver", params=params,session_id=session_id)
