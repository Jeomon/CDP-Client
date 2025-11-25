
"""CDP WebAuthn Methods"""

from client.service import CDPClient
from typing import TypedDict,Optional
from protocol.web_authn.methods.types import *

class WebAuthnMethods:
    def __init__(self, client:CDPClient):
        self.client = client

    async def enable(self, params: Optional[enableParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Enable the WebAuthn domain and start intercepting credential storage and retrieval with a virtual authenticator."""
        return await self.client.send(method="WebAuthn.enable", params=params,session_id=session_id)

    async def disable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Disable the WebAuthn domain."""
        return await self.client.send(method="WebAuthn.disable", params=params,session_id=session_id)

    async def add_virtual_authenticator(self, params: Optional[addVirtualAuthenticatorParameters]=None,session_id: Optional[str] = None) -> addVirtualAuthenticatorReturns:
        """Creates and adds a virtual authenticator."""
        return await self.client.send(method="WebAuthn.addVirtualAuthenticator", params=params,session_id=session_id)

    async def set_response_override_bits(self, params: Optional[setResponseOverrideBitsParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Resets parameters isBogusSignature, isBadUV, isBadUP to false if they are not present."""
        return await self.client.send(method="WebAuthn.setResponseOverrideBits", params=params,session_id=session_id)

    async def remove_virtual_authenticator(self, params: Optional[removeVirtualAuthenticatorParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Removes the given authenticator."""
        return await self.client.send(method="WebAuthn.removeVirtualAuthenticator", params=params,session_id=session_id)

    async def add_credential(self, params: Optional[addCredentialParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Adds the credential to the specified authenticator."""
        return await self.client.send(method="WebAuthn.addCredential", params=params,session_id=session_id)

    async def get_credential(self, params: Optional[getCredentialParameters]=None,session_id: Optional[str] = None) -> getCredentialReturns:
        """Returns a single credential stored in the given virtual authenticator that matches the credential ID."""
        return await self.client.send(method="WebAuthn.getCredential", params=params,session_id=session_id)

    async def get_credentials(self, params: Optional[getCredentialsParameters]=None,session_id: Optional[str] = None) -> getCredentialsReturns:
        """Returns all the credentials stored in the given virtual authenticator."""
        return await self.client.send(method="WebAuthn.getCredentials", params=params,session_id=session_id)

    async def remove_credential(self, params: Optional[removeCredentialParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Removes a credential from the authenticator."""
        return await self.client.send(method="WebAuthn.removeCredential", params=params,session_id=session_id)

    async def clear_credentials(self, params: Optional[clearCredentialsParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Clears all the credentials from the specified device."""
        return await self.client.send(method="WebAuthn.clearCredentials", params=params,session_id=session_id)

    async def set_user_verified(self, params: Optional[setUserVerifiedParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Sets whether User Verification succeeds or fails for an authenticator. The default is true."""
        return await self.client.send(method="WebAuthn.setUserVerified", params=params,session_id=session_id)

    async def set_automatic_presence_simulation(self, params: Optional[setAutomaticPresenceSimulationParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Sets whether tests of user presence will succeed immediately (if true) or fail to resolve (if false) for an authenticator. The default is true."""
        return await self.client.send(method="WebAuthn.setAutomaticPresenceSimulation", params=params,session_id=session_id)

    async def set_credential_properties(self, params: Optional[setCredentialPropertiesParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Allows setting credential properties. https://w3c.github.io/webauthn/#sctn-automation-set-credential-properties"""
        return await self.client.send(method="WebAuthn.setCredentialProperties", params=params,session_id=session_id)
