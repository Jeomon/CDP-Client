
"""CDP Audits Methods"""

from client.service import CDPClient
from typing import TypedDict,Optional
from protocol.audits.methods.types import *

class AuditsMethods:
    def __init__(self, client:CDPClient):
        self.client = client

    async def get_encoded_response(self, params: Optional[getEncodedResponseParameters]=None,session_id: Optional[str] = None) -> getEncodedResponseReturns:
        """Returns the response body and size if it were re-encoded with the specified settings. Only applies to images."""
        return await self.client.send(method="Audits.getEncodedResponse", params=params,session_id=session_id)

    async def disable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Disables issues domain, prevents further issues from being reported to the client."""
        return await self.client.send(method="Audits.disable", params=params,session_id=session_id)

    async def enable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Enables issues domain, sends the issues collected so far to the client by means of the `issueAdded` event."""
        return await self.client.send(method="Audits.enable", params=params,session_id=session_id)

    async def check_contrast(self, params: Optional[checkContrastParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Runs the contrast check for the target page. Found issues are reported using Audits.issueAdded event."""
        return await self.client.send(method="Audits.checkContrast", params=params,session_id=session_id)

    async def check_forms_issues(self, params: None=None,session_id: Optional[str] = None) -> checkFormsIssuesReturns:
        """Runs the form issues check for the target page. Found issues are reported using Audits.issueAdded event."""
        return await self.client.send(method="Audits.checkFormsIssues", params=params,session_id=session_id)
