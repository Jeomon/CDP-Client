
"""CDP CSS Methods"""

from client.service import CDPClient
from typing import TypedDict,Optional
from protocol.css.methods.types import *

class CSSMethods:
    def __init__(self, client:CDPClient):
        self.client = client

    async def add_rule(self, params: Optional[addRuleParameters]=None,session_id: Optional[str] = None) -> addRuleReturns:
        """Inserts a new rule with the given `ruleText` in a stylesheet with given `styleSheetId`, at the position specified by `location`."""
        return await self.client.send(method="CSS.addRule", params=params,session_id=session_id)

    async def collect_class_names(self, params: Optional[collectClassNamesParameters]=None,session_id: Optional[str] = None) -> collectClassNamesReturns:
        """Returns all class names from specified stylesheet."""
        return await self.client.send(method="CSS.collectClassNames", params=params,session_id=session_id)

    async def create_style_sheet(self, params: Optional[createStyleSheetParameters]=None,session_id: Optional[str] = None) -> createStyleSheetReturns:
        """Creates a new special "via-inspector" stylesheet in the frame with given `frameId`."""
        return await self.client.send(method="CSS.createStyleSheet", params=params,session_id=session_id)

    async def disable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Disables the CSS agent for the given page."""
        return await self.client.send(method="CSS.disable", params=params,session_id=session_id)

    async def enable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Enables the CSS agent for the given page. Clients should not assume that the CSS agent has been enabled until the result of this command is received."""
        return await self.client.send(method="CSS.enable", params=params,session_id=session_id)

    async def force_pseudo_state(self, params: Optional[forcePseudoStateParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Ensures that the given node will have specified pseudo-classes whenever its style is computed by the browser."""
        return await self.client.send(method="CSS.forcePseudoState", params=params,session_id=session_id)

    async def force_starting_style(self, params: Optional[forceStartingStyleParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Ensures that the given node is in its starting-style state."""
        return await self.client.send(method="CSS.forceStartingStyle", params=params,session_id=session_id)

    async def get_background_colors(self, params: Optional[getBackgroundColorsParameters]=None,session_id: Optional[str] = None) -> getBackgroundColorsReturns:
        return await self.client.send(method="CSS.getBackgroundColors", params=params,session_id=session_id)

    async def get_computed_style_for_node(self, params: Optional[getComputedStyleForNodeParameters]=None,session_id: Optional[str] = None) -> getComputedStyleForNodeReturns:
        """Returns the computed style for a DOM node identified by `nodeId`."""
        return await self.client.send(method="CSS.getComputedStyleForNode", params=params,session_id=session_id)

    async def resolve_values(self, params: Optional[resolveValuesParameters]=None,session_id: Optional[str] = None) -> resolveValuesReturns:
        """Resolve the specified values in the context of the provided element. For example, a value of '1em' is evaluated according to the computed 'font-size' of the element and a value 'calc(1px + 2px)' will be resolved to '3px'. If the `propertyName` was specified the `values` are resolved as if they were property's declaration. If a value cannot be parsed according to the provided property syntax, the value is parsed using combined syntax as if null `propertyName` was provided. If the value cannot be resolved even then, return the provided value without any changes."""
        return await self.client.send(method="CSS.resolveValues", params=params,session_id=session_id)

    async def get_longhand_properties(self, params: Optional[getLonghandPropertiesParameters]=None,session_id: Optional[str] = None) -> getLonghandPropertiesReturns:
        return await self.client.send(method="CSS.getLonghandProperties", params=params,session_id=session_id)

    async def get_inline_styles_for_node(self, params: Optional[getInlineStylesForNodeParameters]=None,session_id: Optional[str] = None) -> getInlineStylesForNodeReturns:
        """Returns the styles defined inline (explicitly in the "style" attribute and implicitly, using DOM attributes) for a DOM node identified by `nodeId`."""
        return await self.client.send(method="CSS.getInlineStylesForNode", params=params,session_id=session_id)

    async def get_animated_styles_for_node(self, params: Optional[getAnimatedStylesForNodeParameters]=None,session_id: Optional[str] = None) -> getAnimatedStylesForNodeReturns:
        """Returns the styles coming from animations & transitions including the animation & transition styles coming from inheritance chain."""
        return await self.client.send(method="CSS.getAnimatedStylesForNode", params=params,session_id=session_id)

    async def get_matched_styles_for_node(self, params: Optional[getMatchedStylesForNodeParameters]=None,session_id: Optional[str] = None) -> getMatchedStylesForNodeReturns:
        """Returns requested styles for a DOM node identified by `nodeId`."""
        return await self.client.send(method="CSS.getMatchedStylesForNode", params=params,session_id=session_id)

    async def get_environment_variables(self, params: None=None,session_id: Optional[str] = None) -> getEnvironmentVariablesReturns:
        """Returns the values of the default UA-defined environment variables used in env()"""
        return await self.client.send(method="CSS.getEnvironmentVariables", params=params,session_id=session_id)

    async def get_media_queries(self, params: None=None,session_id: Optional[str] = None) -> getMediaQueriesReturns:
        """Returns all media queries parsed by the rendering engine."""
        return await self.client.send(method="CSS.getMediaQueries", params=params,session_id=session_id)

    async def get_platform_fonts_for_node(self, params: Optional[getPlatformFontsForNodeParameters]=None,session_id: Optional[str] = None) -> getPlatformFontsForNodeReturns:
        """Requests information about platform fonts which we used to render child TextNodes in the given node."""
        return await self.client.send(method="CSS.getPlatformFontsForNode", params=params,session_id=session_id)

    async def get_style_sheet_text(self, params: Optional[getStyleSheetTextParameters]=None,session_id: Optional[str] = None) -> getStyleSheetTextReturns:
        """Returns the current textual content for a stylesheet."""
        return await self.client.send(method="CSS.getStyleSheetText", params=params,session_id=session_id)

    async def get_layers_for_node(self, params: Optional[getLayersForNodeParameters]=None,session_id: Optional[str] = None) -> getLayersForNodeReturns:
        """Returns all layers parsed by the rendering engine for the tree scope of a node. Given a DOM element identified by nodeId, getLayersForNode returns the root layer for the nearest ancestor document or shadow root. The layer root contains the full layer tree for the tree scope and their ordering."""
        return await self.client.send(method="CSS.getLayersForNode", params=params,session_id=session_id)

    async def get_location_for_selector(self, params: Optional[getLocationForSelectorParameters]=None,session_id: Optional[str] = None) -> getLocationForSelectorReturns:
        """Given a CSS selector text and a style sheet ID, getLocationForSelector returns an array of locations of the CSS selector in the style sheet."""
        return await self.client.send(method="CSS.getLocationForSelector", params=params,session_id=session_id)

    async def track_computed_style_updates_for_node(self, params: Optional[trackComputedStyleUpdatesForNodeParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Starts tracking the given node for the computed style updates and whenever the computed style is updated for node, it queues a `computedStyleUpdated` event with throttling. There can only be 1 node tracked for computed style updates so passing a new node id removes tracking from the previous node. Pass `undefined` to disable tracking."""
        return await self.client.send(method="CSS.trackComputedStyleUpdatesForNode", params=params,session_id=session_id)

    async def track_computed_style_updates(self, params: Optional[trackComputedStyleUpdatesParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Starts tracking the given computed styles for updates. The specified array of properties replaces the one previously specified. Pass empty array to disable tracking. Use takeComputedStyleUpdates to retrieve the list of nodes that had properties modified. The changes to computed style properties are only tracked for nodes pushed to the front-end by the DOM agent. If no changes to the tracked properties occur after the node has been pushed to the front-end, no updates will be issued for the node."""
        return await self.client.send(method="CSS.trackComputedStyleUpdates", params=params,session_id=session_id)

    async def take_computed_style_updates(self, params: None=None,session_id: Optional[str] = None) -> takeComputedStyleUpdatesReturns:
        """Polls the next batch of computed style updates."""
        return await self.client.send(method="CSS.takeComputedStyleUpdates", params=params,session_id=session_id)

    async def set_effective_property_value_for_node(self, params: Optional[setEffectivePropertyValueForNodeParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Find a rule with the given active property for the given node and set the new value for this property"""
        return await self.client.send(method="CSS.setEffectivePropertyValueForNode", params=params,session_id=session_id)

    async def set_property_rule_property_name(self, params: Optional[setPropertyRulePropertyNameParameters]=None,session_id: Optional[str] = None) -> setPropertyRulePropertyNameReturns:
        """Modifies the property rule property name."""
        return await self.client.send(method="CSS.setPropertyRulePropertyName", params=params,session_id=session_id)

    async def set_keyframe_key(self, params: Optional[setKeyframeKeyParameters]=None,session_id: Optional[str] = None) -> setKeyframeKeyReturns:
        """Modifies the keyframe rule key text."""
        return await self.client.send(method="CSS.setKeyframeKey", params=params,session_id=session_id)

    async def set_media_text(self, params: Optional[setMediaTextParameters]=None,session_id: Optional[str] = None) -> setMediaTextReturns:
        """Modifies the rule selector."""
        return await self.client.send(method="CSS.setMediaText", params=params,session_id=session_id)

    async def set_container_query_text(self, params: Optional[setContainerQueryTextParameters]=None,session_id: Optional[str] = None) -> setContainerQueryTextReturns:
        """Modifies the expression of a container query."""
        return await self.client.send(method="CSS.setContainerQueryText", params=params,session_id=session_id)

    async def set_supports_text(self, params: Optional[setSupportsTextParameters]=None,session_id: Optional[str] = None) -> setSupportsTextReturns:
        """Modifies the expression of a supports at-rule."""
        return await self.client.send(method="CSS.setSupportsText", params=params,session_id=session_id)

    async def set_scope_text(self, params: Optional[setScopeTextParameters]=None,session_id: Optional[str] = None) -> setScopeTextReturns:
        """Modifies the expression of a scope at-rule."""
        return await self.client.send(method="CSS.setScopeText", params=params,session_id=session_id)

    async def set_rule_selector(self, params: Optional[setRuleSelectorParameters]=None,session_id: Optional[str] = None) -> setRuleSelectorReturns:
        """Modifies the rule selector."""
        return await self.client.send(method="CSS.setRuleSelector", params=params,session_id=session_id)

    async def set_style_sheet_text(self, params: Optional[setStyleSheetTextParameters]=None,session_id: Optional[str] = None) -> setStyleSheetTextReturns:
        """Sets the new stylesheet text."""
        return await self.client.send(method="CSS.setStyleSheetText", params=params,session_id=session_id)

    async def set_style_texts(self, params: Optional[setStyleTextsParameters]=None,session_id: Optional[str] = None) -> setStyleTextsReturns:
        """Applies specified style edits one after another in the given order."""
        return await self.client.send(method="CSS.setStyleTexts", params=params,session_id=session_id)

    async def start_rule_usage_tracking(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Enables the selector recording."""
        return await self.client.send(method="CSS.startRuleUsageTracking", params=params,session_id=session_id)

    async def stop_rule_usage_tracking(self, params: None=None,session_id: Optional[str] = None) -> stopRuleUsageTrackingReturns:
        """Stop tracking rule usage and return the list of rules that were used since last call to `takeCoverageDelta` (or since start of coverage instrumentation)."""
        return await self.client.send(method="CSS.stopRuleUsageTracking", params=params,session_id=session_id)

    async def take_coverage_delta(self, params: None=None,session_id: Optional[str] = None) -> takeCoverageDeltaReturns:
        """Obtain list of rules that became used since last call to this method (or since start of coverage instrumentation)."""
        return await self.client.send(method="CSS.takeCoverageDelta", params=params,session_id=session_id)

    async def set_local_fonts_enabled(self, params: Optional[setLocalFontsEnabledParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Enables/disables rendering of local CSS fonts (enabled by default)."""
        return await self.client.send(method="CSS.setLocalFontsEnabled", params=params,session_id=session_id)
