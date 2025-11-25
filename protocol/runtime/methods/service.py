
"""CDP Runtime Methods"""

from client.methods import CDPMethods
from typing import TypedDict,Optional
from protocol.runtime.methods.types import *

class RuntimeMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def await_promise(self, params: Optional[awaitPromiseParameters]=None) -> awaitPromiseReturns:
        """Add handler to promise with given promise object id."""
        return await self.methods.send(method="Runtime.awaitPromise", params=params)

    async def call_function_on(self, params: Optional[callFunctionOnParameters]=None) -> callFunctionOnReturns:
        """Calls function with given declaration on the given object. Object group of the result is inherited from the target object."""
        return await self.methods.send(method="Runtime.callFunctionOn", params=params)

    async def compile_script(self, params: Optional[compileScriptParameters]=None) -> compileScriptReturns:
        """Compiles expression."""
        return await self.methods.send(method="Runtime.compileScript", params=params)

    async def disable(self, params: None=None) -> Dict[str, Any]:
        """Disables reporting of execution contexts creation."""
        return await self.methods.send(method="Runtime.disable", params=params)

    async def discard_console_entries(self, params: None=None) -> Dict[str, Any]:
        """Discards collected exceptions and console API calls."""
        return await self.methods.send(method="Runtime.discardConsoleEntries", params=params)

    async def enable(self, params: None=None) -> Dict[str, Any]:
        """Enables reporting of execution contexts creation by means of `executionContextCreated` event. When the reporting gets enabled the event will be sent immediately for each existing execution context."""
        return await self.methods.send(method="Runtime.enable", params=params)

    async def evaluate(self, params: Optional[evaluateParameters]=None) -> evaluateReturns:
        """Evaluates expression on global object."""
        return await self.methods.send(method="Runtime.evaluate", params=params)

    async def get_isolate_id(self, params: None=None) -> getIsolateIdReturns:
        """Returns the isolate id."""
        return await self.methods.send(method="Runtime.getIsolateId", params=params)

    async def get_heap_usage(self, params: None=None) -> getHeapUsageReturns:
        """Returns the JavaScript heap usage. It is the total usage of the corresponding isolate not scoped to a particular Runtime."""
        return await self.methods.send(method="Runtime.getHeapUsage", params=params)

    async def get_properties(self, params: Optional[getPropertiesParameters]=None) -> getPropertiesReturns:
        """Returns properties of a given object. Object group of the result is inherited from the target object."""
        return await self.methods.send(method="Runtime.getProperties", params=params)

    async def global_lexical_scope_names(self, params: Optional[globalLexicalScopeNamesParameters]=None) -> globalLexicalScopeNamesReturns:
        """Returns all let, const and class variables from global scope."""
        return await self.methods.send(method="Runtime.globalLexicalScopeNames", params=params)

    async def query_objects(self, params: Optional[queryObjectsParameters]=None) -> queryObjectsReturns:
        return await self.methods.send(method="Runtime.queryObjects", params=params)

    async def release_object(self, params: Optional[releaseObjectParameters]=None) -> Dict[str, Any]:
        """Releases remote object with given id."""
        return await self.methods.send(method="Runtime.releaseObject", params=params)

    async def release_object_group(self, params: Optional[releaseObjectGroupParameters]=None) -> Dict[str, Any]:
        """Releases all remote objects that belong to a given group."""
        return await self.methods.send(method="Runtime.releaseObjectGroup", params=params)

    async def run_if_waiting_for_debugger(self, params: None=None) -> Dict[str, Any]:
        """Tells inspected instance to run if it was waiting for debugger to attach."""
        return await self.methods.send(method="Runtime.runIfWaitingForDebugger", params=params)

    async def run_script(self, params: Optional[runScriptParameters]=None) -> runScriptReturns:
        """Runs script with given id in a given context."""
        return await self.methods.send(method="Runtime.runScript", params=params)

    async def set_async_call_stack_depth(self, params: Optional[setAsyncCallStackDepthParameters]=None) -> Dict[str, Any]:
        """Enables or disables async call stacks tracking."""
        return await self.methods.send(method="Runtime.setAsyncCallStackDepth", params=params)

    async def set_custom_object_formatter_enabled(self, params: Optional[setCustomObjectFormatterEnabledParameters]=None) -> Dict[str, Any]:
        return await self.methods.send(method="Runtime.setCustomObjectFormatterEnabled", params=params)

    async def set_max_call_stack_size_to_capture(self, params: Optional[setMaxCallStackSizeToCaptureParameters]=None) -> Dict[str, Any]:
        return await self.methods.send(method="Runtime.setMaxCallStackSizeToCapture", params=params)

    async def terminate_execution(self, params: None=None) -> Dict[str, Any]:
        """Terminate current or next JavaScript execution. Will cancel the termination when the outer-most script execution ends."""
        return await self.methods.send(method="Runtime.terminateExecution", params=params)

    async def add_binding(self, params: Optional[addBindingParameters]=None) -> Dict[str, Any]:
        """If executionContextId is empty, adds binding with the given name on the global objects of all inspected contexts, including those created later, bindings survive reloads. Binding function takes exactly one argument, this argument should be string, in case of any other input, function throws an exception. Each binding function call produces Runtime.bindingCalled notification."""
        return await self.methods.send(method="Runtime.addBinding", params=params)

    async def remove_binding(self, params: Optional[removeBindingParameters]=None) -> Dict[str, Any]:
        """This method does not remove binding function from global object but unsubscribes current runtime agent from Runtime.bindingCalled notifications."""
        return await self.methods.send(method="Runtime.removeBinding", params=params)

    async def get_exception_details(self, params: Optional[getExceptionDetailsParameters]=None) -> getExceptionDetailsReturns:
        """This method tries to lookup and populate exception details for a JavaScript Error object. Note that the stackTrace portion of the resulting exceptionDetails will only be populated if the Runtime domain was enabled at the time when the Error was thrown."""
        return await self.methods.send(method="Runtime.getExceptionDetails", params=params)
