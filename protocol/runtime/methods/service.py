
"""CDP Runtime Methods"""

from client.service import CDPClient
from typing import TypedDict,Optional
from protocol.runtime.methods.types import *

class RuntimeMethods:
    def __init__(self, client:CDPClient):
        self.client = client

    async def await_promise(self, params: Optional[awaitPromiseParameters]=None,session_id: Optional[str] = None) -> awaitPromiseReturns:
        """Add handler to promise with given promise object id."""
        return await self.client.send(method="Runtime.awaitPromise", params=params,session_id=session_id)

    async def call_function_on(self, params: Optional[callFunctionOnParameters]=None,session_id: Optional[str] = None) -> callFunctionOnReturns:
        """Calls function with given declaration on the given object. Object group of the result is inherited from the target object."""
        return await self.client.send(method="Runtime.callFunctionOn", params=params,session_id=session_id)

    async def compile_script(self, params: Optional[compileScriptParameters]=None,session_id: Optional[str] = None) -> compileScriptReturns:
        """Compiles expression."""
        return await self.client.send(method="Runtime.compileScript", params=params,session_id=session_id)

    async def disable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Disables reporting of execution contexts creation."""
        return await self.client.send(method="Runtime.disable", params=params,session_id=session_id)

    async def discard_console_entries(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Discards collected exceptions and console API calls."""
        return await self.client.send(method="Runtime.discardConsoleEntries", params=params,session_id=session_id)

    async def enable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Enables reporting of execution contexts creation by means of `executionContextCreated` event. When the reporting gets enabled the event will be sent immediately for each existing execution context."""
        return await self.client.send(method="Runtime.enable", params=params,session_id=session_id)

    async def evaluate(self, params: Optional[evaluateParameters]=None,session_id: Optional[str] = None) -> evaluateReturns:
        """Evaluates expression on global object."""
        return await self.client.send(method="Runtime.evaluate", params=params,session_id=session_id)

    async def get_isolate_id(self, params: None=None,session_id: Optional[str] = None) -> getIsolateIdReturns:
        """Returns the isolate id."""
        return await self.client.send(method="Runtime.getIsolateId", params=params,session_id=session_id)

    async def get_heap_usage(self, params: None=None,session_id: Optional[str] = None) -> getHeapUsageReturns:
        """Returns the JavaScript heap usage. It is the total usage of the corresponding isolate not scoped to a particular Runtime."""
        return await self.client.send(method="Runtime.getHeapUsage", params=params,session_id=session_id)

    async def get_properties(self, params: Optional[getPropertiesParameters]=None,session_id: Optional[str] = None) -> getPropertiesReturns:
        """Returns properties of a given object. Object group of the result is inherited from the target object."""
        return await self.client.send(method="Runtime.getProperties", params=params,session_id=session_id)

    async def global_lexical_scope_names(self, params: Optional[globalLexicalScopeNamesParameters]=None,session_id: Optional[str] = None) -> globalLexicalScopeNamesReturns:
        """Returns all let, const and class variables from global scope."""
        return await self.client.send(method="Runtime.globalLexicalScopeNames", params=params,session_id=session_id)

    async def query_objects(self, params: Optional[queryObjectsParameters]=None,session_id: Optional[str] = None) -> queryObjectsReturns:
        return await self.client.send(method="Runtime.queryObjects", params=params,session_id=session_id)

    async def release_object(self, params: Optional[releaseObjectParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Releases remote object with given id."""
        return await self.client.send(method="Runtime.releaseObject", params=params,session_id=session_id)

    async def release_object_group(self, params: Optional[releaseObjectGroupParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Releases all remote objects that belong to a given group."""
        return await self.client.send(method="Runtime.releaseObjectGroup", params=params,session_id=session_id)

    async def run_if_waiting_for_debugger(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Tells inspected instance to run if it was waiting for debugger to attach."""
        return await self.client.send(method="Runtime.runIfWaitingForDebugger", params=params,session_id=session_id)

    async def run_script(self, params: Optional[runScriptParameters]=None,session_id: Optional[str] = None) -> runScriptReturns:
        """Runs script with given id in a given context."""
        return await self.client.send(method="Runtime.runScript", params=params,session_id=session_id)

    async def set_async_call_stack_depth(self, params: Optional[setAsyncCallStackDepthParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Enables or disables async call stacks tracking."""
        return await self.client.send(method="Runtime.setAsyncCallStackDepth", params=params,session_id=session_id)

    async def set_custom_object_formatter_enabled(self, params: Optional[setCustomObjectFormatterEnabledParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        return await self.client.send(method="Runtime.setCustomObjectFormatterEnabled", params=params,session_id=session_id)

    async def set_max_call_stack_size_to_capture(self, params: Optional[setMaxCallStackSizeToCaptureParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        return await self.client.send(method="Runtime.setMaxCallStackSizeToCapture", params=params,session_id=session_id)

    async def terminate_execution(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Terminate current or next JavaScript execution. Will cancel the termination when the outer-most script execution ends."""
        return await self.client.send(method="Runtime.terminateExecution", params=params,session_id=session_id)

    async def add_binding(self, params: Optional[addBindingParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """If executionContextId is empty, adds binding with the given name on the global objects of all inspected contexts, including those created later, bindings survive reloads. Binding function takes exactly one argument, this argument should be string, in case of any other input, function throws an exception. Each binding function call produces Runtime.bindingCalled notification."""
        return await self.client.send(method="Runtime.addBinding", params=params,session_id=session_id)

    async def remove_binding(self, params: Optional[removeBindingParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """This method does not remove binding function from global object but unsubscribes current runtime agent from Runtime.bindingCalled notifications."""
        return await self.client.send(method="Runtime.removeBinding", params=params,session_id=session_id)

    async def get_exception_details(self, params: Optional[getExceptionDetailsParameters]=None,session_id: Optional[str] = None) -> getExceptionDetailsReturns:
        """This method tries to lookup and populate exception details for a JavaScript Error object. Note that the stackTrace portion of the resulting exceptionDetails will only be populated if the Runtime domain was enabled at the time when the Error was thrown."""
        return await self.client.send(method="Runtime.getExceptionDetails", params=params,session_id=session_id)
