
"""CDP Audits Methods"""

from cdp_client.methods import CDPMethods
from typing import TypedDict,Optional
from audits.methods.types import *

class AuditsMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def get_encoded_response(self, params: Optional[getEncodedResponseParameters]=None) -> getEncodedResponseReturns:
        """Returns the response body and size if it were re-encoded with the specified settings. Only applies to images."""
        return await self.methods.send(method="Audits.getEncodedResponse", params=params)

    async def disable(self, params: None=None) -> Dict[str, Any]:
        """Disables issues domain, prevents further issues from being reported to the client."""
        return await self.methods.send(method="Audits.disable", params=params)

    async def enable(self, params: None=None) -> Dict[str, Any]:
        """Enables issues domain, sends the issues collected so far to the client by means of the `issueAdded` event."""
        return await self.methods.send(method="Audits.enable", params=params)

    async def check_contrast(self, params: Optional[checkContrastParameters]=None) -> Dict[str, Any]:
        """Runs the contrast check for the target page. Found issues are reported using Audits.issueAdded event."""
        return await self.methods.send(method="Audits.checkContrast", params=params)

    async def check_forms_issues(self, params: None=None) -> checkFormsIssuesReturns:
        """Runs the form issues check for the target page. Found issues are reported using Audits.issueAdded event."""
        return await self.methods.send(method="Audits.checkFormsIssues", params=params)
