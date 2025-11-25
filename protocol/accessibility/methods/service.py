
"""CDP Accessibility Methods"""

from client.service import CDPClient
from typing import TypedDict,Optional
from protocol.accessibility.methods.types import *

class AccessibilityMethods:
    def __init__(self, client:CDPClient):
        self.client = client

    async def disable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Disables the accessibility domain."""
        return await self.client.send(method="Accessibility.disable", params=params,session_id=session_id)

    async def enable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Enables the accessibility domain which causes `AXNodeId`s to remain consistent between method calls. This turns on accessibility for the page, which can impact performance until accessibility is disabled."""
        return await self.client.send(method="Accessibility.enable", params=params,session_id=session_id)

    async def get_partial_ax_tree(self, params: Optional[getPartialAXTreeParameters]=None,session_id: Optional[str] = None) -> getPartialAXTreeReturns:
        """Fetches the accessibility node and partial accessibility tree for this DOM node, if it exists."""
        return await self.client.send(method="Accessibility.getPartialAXTree", params=params,session_id=session_id)

    async def get_full_ax_tree(self, params: Optional[getFullAXTreeParameters]=None,session_id: Optional[str] = None) -> getFullAXTreeReturns:
        """Fetches the entire accessibility tree for the root Document"""
        return await self.client.send(method="Accessibility.getFullAXTree", params=params,session_id=session_id)

    async def get_root_ax_node(self, params: Optional[getRootAXNodeParameters]=None,session_id: Optional[str] = None) -> getRootAXNodeReturns:
        """Fetches the root node. Requires `enable()` to have been called previously."""
        return await self.client.send(method="Accessibility.getRootAXNode", params=params,session_id=session_id)

    async def get_ax_node_and_ancestors(self, params: Optional[getAXNodeAndAncestorsParameters]=None,session_id: Optional[str] = None) -> getAXNodeAndAncestorsReturns:
        """Fetches a node and all ancestors up to and including the root. Requires `enable()` to have been called previously."""
        return await self.client.send(method="Accessibility.getAXNodeAndAncestors", params=params,session_id=session_id)

    async def get_child_ax_nodes(self, params: Optional[getChildAXNodesParameters]=None,session_id: Optional[str] = None) -> getChildAXNodesReturns:
        """Fetches a particular accessibility node by AXNodeId. Requires `enable()` to have been called previously."""
        return await self.client.send(method="Accessibility.getChildAXNodes", params=params,session_id=session_id)

    async def query_ax_tree(self, params: Optional[queryAXTreeParameters]=None,session_id: Optional[str] = None) -> queryAXTreeReturns:
        """Query a DOM node's accessibility subtree for accessible name and role. This command computes the name and role for all nodes in the subtree, including those that are ignored for accessibility, and returns those that match the specified name and role. If no DOM node is specified, or the DOM node does not exist, the command returns an error. If neither `accessibleName` or `role` is specified, it returns all the accessibility nodes in the subtree."""
        return await self.client.send(method="Accessibility.queryAXTree", params=params,session_id=session_id)
