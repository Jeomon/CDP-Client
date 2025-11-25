
"""CDP DOM Methods"""

from client.methods import CDPMethods
from typing import TypedDict,Optional
from protocol.dom.methods.types import *

class DOMMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def collect_class_names_from_subtree(self, params: Optional[collectClassNamesFromSubtreeParameters]=None) -> collectClassNamesFromSubtreeReturns:
        """Collects class names for the node with given id and all of it's child nodes."""
        return await self.methods.send(method="DOM.collectClassNamesFromSubtree", params=params)

    async def copy_to(self, params: Optional[copyToParameters]=None) -> copyToReturns:
        """Creates a deep copy of the specified node and places it into the target container before the given anchor."""
        return await self.methods.send(method="DOM.copyTo", params=params)

    async def describe_node(self, params: Optional[describeNodeParameters]=None) -> describeNodeReturns:
        """Describes node given its id, does not require domain to be enabled. Does not start tracking any objects, can be used for automation."""
        return await self.methods.send(method="DOM.describeNode", params=params)

    async def scroll_into_view_if_needed(self, params: Optional[scrollIntoViewIfNeededParameters]=None) -> Dict[str, Any]:
        """Scrolls the specified rect of the given node into view if not already visible. Note: exactly one between nodeId, backendNodeId and objectId should be passed to identify the node."""
        return await self.methods.send(method="DOM.scrollIntoViewIfNeeded", params=params)

    async def disable(self, params: None=None) -> Dict[str, Any]:
        """Disables DOM agent for the given page."""
        return await self.methods.send(method="DOM.disable", params=params)

    async def discard_search_results(self, params: Optional[discardSearchResultsParameters]=None) -> Dict[str, Any]:
        """Discards search results from the session with the given id. `getSearchResults` should no longer be called for that search."""
        return await self.methods.send(method="DOM.discardSearchResults", params=params)

    async def enable(self, params: Optional[enableParameters]=None) -> Dict[str, Any]:
        """Enables DOM agent for the given page."""
        return await self.methods.send(method="DOM.enable", params=params)

    async def focus(self, params: Optional[focusParameters]=None) -> Dict[str, Any]:
        """Focuses the given element."""
        return await self.methods.send(method="DOM.focus", params=params)

    async def get_attributes(self, params: Optional[getAttributesParameters]=None) -> getAttributesReturns:
        """Returns attributes for the specified node."""
        return await self.methods.send(method="DOM.getAttributes", params=params)

    async def get_box_model(self, params: Optional[getBoxModelParameters]=None) -> getBoxModelReturns:
        """Returns boxes for the given node."""
        return await self.methods.send(method="DOM.getBoxModel", params=params)

    async def get_content_quads(self, params: Optional[getContentQuadsParameters]=None) -> getContentQuadsReturns:
        """Returns quads that describe node position on the page. This method might return multiple quads for inline nodes."""
        return await self.methods.send(method="DOM.getContentQuads", params=params)

    async def get_document(self, params: Optional[getDocumentParameters]=None) -> getDocumentReturns:
        """Returns the root DOM node (and optionally the subtree) to the caller. Implicitly enables the DOM domain events for the current target."""
        return await self.methods.send(method="DOM.getDocument", params=params)

    async def get_nodes_for_subtree_by_style(self, params: Optional[getNodesForSubtreeByStyleParameters]=None) -> getNodesForSubtreeByStyleReturns:
        """Finds nodes with a given computed style in a subtree."""
        return await self.methods.send(method="DOM.getNodesForSubtreeByStyle", params=params)

    async def get_node_for_location(self, params: Optional[getNodeForLocationParameters]=None) -> getNodeForLocationReturns:
        """Returns node id at given location. Depending on whether DOM domain is enabled, nodeId is either returned or not."""
        return await self.methods.send(method="DOM.getNodeForLocation", params=params)

    async def get_outer_html(self, params: Optional[getOuterHTMLParameters]=None) -> getOuterHTMLReturns:
        """Returns node's HTML markup."""
        return await self.methods.send(method="DOM.getOuterHTML", params=params)

    async def get_relayout_boundary(self, params: Optional[getRelayoutBoundaryParameters]=None) -> getRelayoutBoundaryReturns:
        """Returns the id of the nearest ancestor that is a relayout boundary."""
        return await self.methods.send(method="DOM.getRelayoutBoundary", params=params)

    async def get_search_results(self, params: Optional[getSearchResultsParameters]=None) -> getSearchResultsReturns:
        """Returns search results from given `fromIndex` to given `toIndex` from the search with the given identifier."""
        return await self.methods.send(method="DOM.getSearchResults", params=params)

    async def hide_highlight(self, params: None=None) -> Dict[str, Any]:
        """Hides any highlight."""
        return await self.methods.send(method="DOM.hideHighlight", params=params)

    async def highlight_node(self, params: None=None) -> Dict[str, Any]:
        """Highlights DOM node."""
        return await self.methods.send(method="DOM.highlightNode", params=params)

    async def highlight_rect(self, params: None=None) -> Dict[str, Any]:
        """Highlights given rectangle."""
        return await self.methods.send(method="DOM.highlightRect", params=params)

    async def mark_undoable_state(self, params: None=None) -> Dict[str, Any]:
        """Marks last undoable state."""
        return await self.methods.send(method="DOM.markUndoableState", params=params)

    async def move_to(self, params: Optional[moveToParameters]=None) -> moveToReturns:
        """Moves node into the new container, places it before the given anchor."""
        return await self.methods.send(method="DOM.moveTo", params=params)

    async def perform_search(self, params: Optional[performSearchParameters]=None) -> performSearchReturns:
        """Searches for a given string in the DOM tree. Use `getSearchResults` to access search results or `cancelSearch` to end this search session."""
        return await self.methods.send(method="DOM.performSearch", params=params)

    async def push_node_by_path_to_frontend(self, params: Optional[pushNodeByPathToFrontendParameters]=None) -> pushNodeByPathToFrontendReturns:
        """Requests that the node is sent to the caller given its path. // FIXME, use XPath"""
        return await self.methods.send(method="DOM.pushNodeByPathToFrontend", params=params)

    async def push_nodes_by_backend_ids_to_frontend(self, params: Optional[pushNodesByBackendIdsToFrontendParameters]=None) -> pushNodesByBackendIdsToFrontendReturns:
        """Requests that a batch of nodes is sent to the caller given their backend node ids."""
        return await self.methods.send(method="DOM.pushNodesByBackendIdsToFrontend", params=params)

    async def query_selector(self, params: Optional[querySelectorParameters]=None) -> querySelectorReturns:
        """Executes `querySelector` on a given node."""
        return await self.methods.send(method="DOM.querySelector", params=params)

    async def query_selector_all(self, params: Optional[querySelectorAllParameters]=None) -> querySelectorAllReturns:
        """Executes `querySelectorAll` on a given node."""
        return await self.methods.send(method="DOM.querySelectorAll", params=params)

    async def get_top_layer_elements(self, params: None=None) -> getTopLayerElementsReturns:
        """Returns NodeIds of current top layer elements. Top layer is rendered closest to the user within a viewport, therefore its elements always appear on top of all other content."""
        return await self.methods.send(method="DOM.getTopLayerElements", params=params)

    async def get_element_by_relation(self, params: Optional[getElementByRelationParameters]=None) -> getElementByRelationReturns:
        """Returns the NodeId of the matched element according to certain relations."""
        return await self.methods.send(method="DOM.getElementByRelation", params=params)

    async def redo(self, params: None=None) -> Dict[str, Any]:
        """Re-does the last undone action."""
        return await self.methods.send(method="DOM.redo", params=params)

    async def remove_attribute(self, params: Optional[removeAttributeParameters]=None) -> Dict[str, Any]:
        """Removes attribute with given name from an element with given id."""
        return await self.methods.send(method="DOM.removeAttribute", params=params)

    async def remove_node(self, params: Optional[removeNodeParameters]=None) -> Dict[str, Any]:
        """Removes node with given id."""
        return await self.methods.send(method="DOM.removeNode", params=params)

    async def request_child_nodes(self, params: Optional[requestChildNodesParameters]=None) -> Dict[str, Any]:
        """Requests that children of the node with given id are returned to the caller in form of `setChildNodes` events where not only immediate children are retrieved, but all children down to the specified depth."""
        return await self.methods.send(method="DOM.requestChildNodes", params=params)

    async def request_node(self, params: Optional[requestNodeParameters]=None) -> requestNodeReturns:
        """Requests that the node is sent to the caller given the JavaScript node object reference. All nodes that form the path from the node to the root are also sent to the client as a series of `setChildNodes` notifications."""
        return await self.methods.send(method="DOM.requestNode", params=params)

    async def resolve_node(self, params: Optional[resolveNodeParameters]=None) -> resolveNodeReturns:
        """Resolves the JavaScript node object for a given NodeId or BackendNodeId."""
        return await self.methods.send(method="DOM.resolveNode", params=params)

    async def set_attribute_value(self, params: Optional[setAttributeValueParameters]=None) -> Dict[str, Any]:
        """Sets attribute for an element with given id."""
        return await self.methods.send(method="DOM.setAttributeValue", params=params)

    async def set_attributes_as_text(self, params: Optional[setAttributesAsTextParameters]=None) -> Dict[str, Any]:
        """Sets attributes on element with given id. This method is useful when user edits some existing attribute value and types in several attribute name/value pairs."""
        return await self.methods.send(method="DOM.setAttributesAsText", params=params)

    async def set_file_input_files(self, params: Optional[setFileInputFilesParameters]=None) -> Dict[str, Any]:
        """Sets files for the given file input element."""
        return await self.methods.send(method="DOM.setFileInputFiles", params=params)

    async def set_node_stack_traces_enabled(self, params: Optional[setNodeStackTracesEnabledParameters]=None) -> Dict[str, Any]:
        """Sets if stack traces should be captured for Nodes. See `Node.getNodeStackTraces`. Default is disabled."""
        return await self.methods.send(method="DOM.setNodeStackTracesEnabled", params=params)

    async def get_node_stack_traces(self, params: Optional[getNodeStackTracesParameters]=None) -> getNodeStackTracesReturns:
        """Gets stack traces associated with a Node. As of now, only provides stack trace for Node creation."""
        return await self.methods.send(method="DOM.getNodeStackTraces", params=params)

    async def get_file_info(self, params: Optional[getFileInfoParameters]=None) -> getFileInfoReturns:
        """Returns file information for the given File wrapper."""
        return await self.methods.send(method="DOM.getFileInfo", params=params)

    async def get_detached_dom_nodes(self, params: None=None) -> getDetachedDomNodesReturns:
        """Returns list of detached nodes"""
        return await self.methods.send(method="DOM.getDetachedDomNodes", params=params)

    async def set_inspected_node(self, params: Optional[setInspectedNodeParameters]=None) -> Dict[str, Any]:
        """Enables console to refer to the node with given id via $x (see Command Line API for more details $x functions)."""
        return await self.methods.send(method="DOM.setInspectedNode", params=params)

    async def set_node_name(self, params: Optional[setNodeNameParameters]=None) -> setNodeNameReturns:
        """Sets node name for a node with given id."""
        return await self.methods.send(method="DOM.setNodeName", params=params)

    async def set_node_value(self, params: Optional[setNodeValueParameters]=None) -> Dict[str, Any]:
        """Sets node value for a node with given id."""
        return await self.methods.send(method="DOM.setNodeValue", params=params)

    async def set_outer_html(self, params: Optional[setOuterHTMLParameters]=None) -> Dict[str, Any]:
        """Sets node HTML markup, returns new node id."""
        return await self.methods.send(method="DOM.setOuterHTML", params=params)

    async def undo(self, params: None=None) -> Dict[str, Any]:
        """Undoes the last performed action."""
        return await self.methods.send(method="DOM.undo", params=params)

    async def get_frame_owner(self, params: Optional[getFrameOwnerParameters]=None) -> getFrameOwnerReturns:
        """Returns iframe node that owns iframe with the given domain."""
        return await self.methods.send(method="DOM.getFrameOwner", params=params)

    async def get_container_for_node(self, params: Optional[getContainerForNodeParameters]=None) -> getContainerForNodeReturns:
        """Returns the query container of the given node based on container query conditions: containerName, physical and logical axes, and whether it queries scroll-state or anchored elements. If no axes are provided and queriesScrollState is false, the style container is returned, which is the direct parent or the closest element with a matching container-name."""
        return await self.methods.send(method="DOM.getContainerForNode", params=params)

    async def get_querying_descendants_for_container(self, params: Optional[getQueryingDescendantsForContainerParameters]=None) -> getQueryingDescendantsForContainerReturns:
        """Returns the descendants of a container query container that have container queries against this container."""
        return await self.methods.send(method="DOM.getQueryingDescendantsForContainer", params=params)

    async def get_anchor_element(self, params: Optional[getAnchorElementParameters]=None) -> getAnchorElementReturns:
        """Returns the target anchor element of the given anchor query according to https://www.w3.org/TR/css-anchor-position-1/#target."""
        return await self.methods.send(method="DOM.getAnchorElement", params=params)

    async def force_show_popover(self, params: Optional[forceShowPopoverParameters]=None) -> forceShowPopoverReturns:
        """When enabling, this API force-opens the popover identified by nodeId and keeps it open until disabled."""
        return await self.methods.send(method="DOM.forceShowPopover", params=params)
