
"""CDP Accessibility Methods"""

from client.methods import CDPMethods
from typing import TypedDict,Optional
from protocol.accessibility.methods.types import *

class AccessibilityMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def disable(self, params: None=None) -> Dict[str, Any]:
        """Disables the accessibility domain."""
        return await self.methods.send(method="Accessibility.disable", params=params)

    async def enable(self, params: None=None) -> Dict[str, Any]:
        """Enables the accessibility domain which causes `AXNodeId`s to remain consistent between method calls. This turns on accessibility for the page, which can impact performance until accessibility is disabled."""
        return await self.methods.send(method="Accessibility.enable", params=params)

    async def get_partial_ax_tree(self, params: Optional[getPartialAXTreeParameters]=None) -> getPartialAXTreeReturns:
        """Fetches the accessibility node and partial accessibility tree for this DOM node, if it exists."""
        return await self.methods.send(method="Accessibility.getPartialAXTree", params=params)

    async def get_full_ax_tree(self, params: Optional[getFullAXTreeParameters]=None) -> getFullAXTreeReturns:
        """Fetches the entire accessibility tree for the root Document"""
        return await self.methods.send(method="Accessibility.getFullAXTree", params=params)

    async def get_root_ax_node(self, params: Optional[getRootAXNodeParameters]=None) -> getRootAXNodeReturns:
        """Fetches the root node. Requires `enable()` to have been called previously."""
        return await self.methods.send(method="Accessibility.getRootAXNode", params=params)

    async def get_ax_node_and_ancestors(self, params: Optional[getAXNodeAndAncestorsParameters]=None) -> getAXNodeAndAncestorsReturns:
        """Fetches a node and all ancestors up to and including the root. Requires `enable()` to have been called previously."""
        return await self.methods.send(method="Accessibility.getAXNodeAndAncestors", params=params)

    async def get_child_ax_nodes(self, params: Optional[getChildAXNodesParameters]=None) -> getChildAXNodesReturns:
        """Fetches a particular accessibility node by AXNodeId. Requires `enable()` to have been called previously."""
        return await self.methods.send(method="Accessibility.getChildAXNodes", params=params)

    async def query_ax_tree(self, params: Optional[queryAXTreeParameters]=None) -> queryAXTreeReturns:
        """Query a DOM node's accessibility subtree for accessible name and role. This command computes the name and role for all nodes in the subtree, including those that are ignored for accessibility, and returns those that match the specified name and role. If no DOM node is specified, or the DOM node does not exist, the command returns an error. If neither `accessibleName` or `role` is specified, it returns all the accessibility nodes in the subtree."""
        return await self.methods.send(method="Accessibility.queryAXTree", params=params)
