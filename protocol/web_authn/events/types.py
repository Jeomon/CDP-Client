
"""CDP WebAuthn Events"""

from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from protocol.web_authn.types import AuthenticatorId
    from protocol.web_authn.types import Credential


class credentialAddedEvent(TypedDict, total=True):
    authenticatorId: 'AuthenticatorId'
    credential: 'Credential'


class credentialDeletedEvent(TypedDict, total=True):
    authenticatorId: 'AuthenticatorId'
    credentialId: 'str'


class credentialUpdatedEvent(TypedDict, total=True):
    authenticatorId: 'AuthenticatorId'
    credential: 'Credential'


class credentialAssertedEvent(TypedDict, total=True):
    authenticatorId: 'AuthenticatorId'
    credential: 'Credential'

