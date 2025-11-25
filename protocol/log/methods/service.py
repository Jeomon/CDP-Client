
"""CDP Log Methods"""

from client.methods import CDPMethods
from typing import TypedDict,Optional
from protocol.log.methods.types import *

class LogMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def clear(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Clears the log."""
        return await self.methods.send(method="Log.clear", params=params,session_id=session_id)

    async def disable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Disables log domain, prevents further log entries from being reported to the client."""
        return await self.methods.send(method="Log.disable", params=params,session_id=session_id)

    async def enable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Enables log domain, sends the entries collected so far to the client by means of the `entryAdded` notification."""
        return await self.methods.send(method="Log.enable", params=params,session_id=session_id)

    async def start_violations_report(self, params: Optional[startViolationsReportParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """start violation reporting."""
        return await self.methods.send(method="Log.startViolationsReport", params=params,session_id=session_id)

    async def stop_violations_report(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Stop violation reporting."""
        return await self.methods.send(method="Log.stopViolationsReport", params=params,session_id=session_id)
