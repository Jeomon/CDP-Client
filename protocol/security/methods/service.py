
"""CDP Security Methods"""

from client.methods import CDPMethods
from typing import TypedDict,Optional
from protocol.security.methods.types import *

class SecurityMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def disable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Disables tracking security state changes."""
        return await self.methods.send(method="Security.disable", params=params,session_id=session_id)

    async def enable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Enables tracking security state changes."""
        return await self.methods.send(method="Security.enable", params=params,session_id=session_id)

    async def set_ignore_certificate_errors(self, params: Optional[setIgnoreCertificateErrorsParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Enable/disable whether all certificate errors should be ignored."""
        return await self.methods.send(method="Security.setIgnoreCertificateErrors", params=params,session_id=session_id)
