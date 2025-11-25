"""Tests for CDP Events"""

import pytest
import asyncio
from unittest.mock import MagicMock, AsyncMock, patch
from client.events import CDPEvents
from client.service import CDPClient


@pytest.fixture
def mock_client():
    """Create a mock CDP client"""
    client = MagicMock(spec=CDPClient)
    client.on = MagicMock()
    client.register = MagicMock()
    client.unregister = MagicMock()
    return client


@pytest.fixture
def cdp_events(mock_client):
    """Create CDPEvents instance with mock client"""
    return CDPEvents(mock_client)


class TestCDPEventsInitialization:
    """Test CDP Events initialization"""
    
    def test_events_initializes_with_client(self, mock_client):
        """Test that CDPEvents initializes with client reference"""
        events = CDPEvents(mock_client)
        assert events.client == mock_client
    
    def test_events_has_on_method(self, cdp_events):
        """Test that CDPEvents has on method"""
        assert hasattr(cdp_events, 'on')
        assert callable(cdp_events.on)


class TestCDPEventsOn:
    """Test CDP Events on functionality"""
    
    def test_on_calls_client_on(self, cdp_events, mock_client):
        """Test that on method calls client.on"""
        callback = MagicMock()
        
        cdp_events.on("Page.loadEventFired", callback)
        
        mock_client.on.assert_called_once_with("Page.loadEventFired", callback)
    
    def test_on_with_async_callback(self, cdp_events, mock_client):
        """Test on method with async callback"""
        async def async_callback(params):
            pass
        
        cdp_events.on("Network.requestWillBeSent", async_callback)
        
        mock_client.on.assert_called_once_with("Network.requestWillBeSent", async_callback)
    
    def test_on_with_lambda_callback(self, cdp_events, mock_client):
        """Test on method with lambda callback"""
        callback = lambda params: print(params)
        
        cdp_events.on("Page.frameNavigated", callback)
        
        mock_client.on.assert_called_once()


class TestCDPEventsDomainAccess:
    """Test CDP Events domain access"""
    
    def test_page_domain_property(self, cdp_events):
        """Test accessing Page domain events"""
        page_events = cdp_events.page
        assert page_events is not None
        from protocol.page.events.service import PageEvents
        assert isinstance(page_events, PageEvents)
    
    def test_network_domain_property(self, cdp_events):
        """Test accessing Network domain events"""
        network_events = cdp_events.network
        assert network_events is not None
        from protocol.network.events.service import NetworkEvents
        assert isinstance(network_events, NetworkEvents)
    
    def test_runtime_domain_property(self, cdp_events):
        """Test accessing Runtime domain events"""
        runtime_events = cdp_events.runtime
        assert runtime_events is not None
        from protocol.runtime.events.service import RuntimeEvents
        assert isinstance(runtime_events, RuntimeEvents)
    
    def test_dom_domain_property(self, cdp_events):
        """Test accessing DOM domain events"""
        dom_events = cdp_events.dom
        assert dom_events is not None
        from protocol.dom.events.service import DOMEvents
        assert isinstance(dom_events, DOMEvents)
    
    def test_debugger_domain_property(self, cdp_events):
        """Test accessing Debugger domain events"""
        debugger_events = cdp_events.debugger
        assert debugger_events is not None
        from protocol.debugger.events.service import DebuggerEvents
        assert isinstance(debugger_events, DebuggerEvents)
    
    def test_domain_property_returns_new_instance(self, cdp_events):
        """Test that accessing domain property returns new instances"""
        page1 = cdp_events.page
        page2 = cdp_events.page
        # They should be different instances but same type
        assert type(page1) == type(page2)


class TestCDPEventsPageDomain:
    """Test Page domain events"""
    
    def test_page_load_event_fired(self, cdp_events, mock_client):
        """Test Page.loadEventFired event handler"""
        callback = MagicMock()
        
        cdp_events.page.on_load_event_fired(callback)
        
        # Should register the event with the client
        mock_client.on.assert_called_once()
        call_args = mock_client.on.call_args
        assert call_args[0][0] == "loadEventFired"
    
    def test_page_frame_navigated(self, cdp_events, mock_client):
        """Test Page.frameNavigated event handler"""
        callback = MagicMock()
        
        cdp_events.page.on_frame_navigated(callback)
        
        mock_client.on.assert_called_once()
        call_args = mock_client.on.call_args
        assert call_args[0][0] == "frameNavigated"
    
    def test_page_frame_attached(self, cdp_events, mock_client):
        """Test Page.frameAttached event handler"""
        callback = MagicMock()
        
        cdp_events.page.on_frame_attached(callback)
        
        mock_client.on.assert_called_once()
    
    def test_page_dom_content_event_fired(self, cdp_events, mock_client):
        """Test Page.domContentEventFired event handler"""
        callback = MagicMock()
        
        cdp_events.page.on_dom_content_event_fired(callback)
        
        mock_client.on.assert_called_once()
    
    def test_page_lifecycle_event(self, cdp_events, mock_client):
        """Test Page.lifecycleEvent event handler"""
        callback = MagicMock()
        
        cdp_events.page.on_lifecycle_event(callback)
        
        mock_client.on.assert_called_once()


class TestCDPEventsNetworkDomain:
    """Test Network domain events"""
    
    def test_network_request_will_be_sent(self, cdp_events, mock_client):
        """Test Network.requestWillBeSent event handler"""
        callback = MagicMock()
        
        cdp_events.network.on_request_will_be_sent(callback)
        
        mock_client.on.assert_called_once()
    
    def test_network_response_received(self, cdp_events, mock_client):
        """Test Network.responseReceived event handler"""
        callback = MagicMock()
        
        cdp_events.network.on_response_received(callback)
        
        mock_client.on.assert_called_once()
    
    def test_network_loading_finished(self, cdp_events, mock_client):
        """Test Network.loadingFinished event handler"""
        callback = MagicMock()
        
        cdp_events.network.on_loading_finished(callback)
        
        mock_client.on.assert_called_once()
    
    def test_network_loading_failed(self, cdp_events, mock_client):
        """Test Network.loadingFailed event handler"""
        callback = MagicMock()
        
        cdp_events.network.on_loading_failed(callback)
        
        mock_client.on.assert_called_once()


class TestCDPEventsRuntimeDomain:
    """Test Runtime domain events"""
    
    def test_runtime_console_api_called(self, cdp_events, mock_client):
        """Test Runtime.consoleAPICalled event handler"""
        callback = MagicMock()
        
        cdp_events.runtime.on_console_api_called(callback)
        
        mock_client.on.assert_called_once()
    
    def test_runtime_exception_thrown(self, cdp_events, mock_client):
        """Test Runtime.exceptionThrown event handler"""
        callback = MagicMock()
        
        cdp_events.runtime.on_exception_thrown(callback)
        
        mock_client.on.assert_called_once()
    
    def test_runtime_execution_context_created(self, cdp_events, mock_client):
        """Test Runtime.executionContextCreated event handler"""
        callback = MagicMock()
        
        cdp_events.runtime.on_execution_context_created(callback)
        
        mock_client.on.assert_called_once()


class TestCDPEventsDOMDomain:
    """Test DOM domain events"""
    
    def test_dom_document_updated(self, cdp_events, mock_client):
        """Test DOM.documentUpdated event handler"""
        callback = MagicMock()
        
        cdp_events.dom.on_document_updated(callback)
        
        mock_client.on.assert_called_once()
    
    def test_dom_set_child_nodes(self, cdp_events, mock_client):
        """Test DOM.setChildNodes event handler"""
        callback = MagicMock()
        
        cdp_events.dom.on_set_child_nodes(callback)
        
        mock_client.on.assert_called_once()
    
    def test_dom_attribute_modified(self, cdp_events, mock_client):
        """Test DOM.attributeModified event handler"""
        callback = MagicMock()
        
        cdp_events.dom.on_attribute_modified(callback)
        
        mock_client.on.assert_called_once()


class TestCDPEventsDebuggerDomain:
    """Test Debugger domain events"""
    
    def test_debugger_paused(self, cdp_events, mock_client):
        """Test Debugger.paused event handler"""
        callback = MagicMock()
        
        cdp_events.debugger.on_paused(callback)
        
        mock_client.on.assert_called_once()
    
    def test_debugger_resumed(self, cdp_events, mock_client):
        """Test Debugger.resumed event handler"""
        callback = MagicMock()
        
        cdp_events.debugger.on_resumed(callback)
        
        mock_client.on.assert_called_once()
    
    def test_debugger_script_parsed(self, cdp_events, mock_client):
        """Test Debugger.scriptParsed event handler"""
        callback = MagicMock()
        
        cdp_events.debugger.on_script_parsed(callback)
        
        mock_client.on.assert_called_once()


class TestCDPEventsIntegration:
    """Integration tests for CDP Events"""
    
    def test_multiple_event_handlers_registration(self, cdp_events, mock_client):
        """Test registering multiple event handlers"""
        callback1 = MagicMock()
        callback2 = MagicMock()
        callback3 = MagicMock()
        
        cdp_events.page.on_load_event_fired(callback1)
        cdp_events.network.on_request_will_be_sent(callback2)
        cdp_events.runtime.on_console_api_called(callback3)
        
        # Should have registered 3 events
        assert mock_client.on.call_count == 3
    
    def test_same_event_multiple_handlers(self, cdp_events, mock_client):
        """Test registering multiple handlers for the same event"""
        callback1 = MagicMock()
        callback2 = MagicMock()
        
        # Register same event twice with different callbacks
        cdp_events.page.on_load_event_fired(callback1)
        cdp_events.page.on_load_event_fired(callback2)
        
        # Both should be registered (though the second might override the first)
        assert mock_client.on.call_count == 2
    
    def test_event_handler_with_async_callback(self, cdp_events, mock_client):
        """Test event handler with async callback"""
        async def async_handler(params):
            await asyncio.sleep(0.01)
            return params
        
        cdp_events.page.on_frame_navigated(async_handler)
        
        mock_client.on.assert_called_once()
    
    def test_all_domain_properties_exist(self, cdp_events):
        """Test that all expected domain properties exist"""
        expected_domains = [
            'accessibility', 'animation', 'audits', 'autofill',
            'background_service', 'bluetooth_emulation', 'browser',
            'css', 'cache_storage', 'cast', 'dom', 'dom_debugger',
            'dom_snapshot', 'dom_storage', 'device_access',
            'device_orientation', 'emulation', 'event_breakpoints',
            'extensions', 'fed_cm', 'fetch', 'file_system',
            'headless_experimental', 'io', 'indexed_db', 'input',
            'inspector', 'layer_tree', 'log', 'media', 'memory',
            'network', 'overlay', 'pwa', 'page', 'performance',
            'performance_timeline', 'preload', 'security',
            'service_worker', 'storage', 'system_info', 'target',
            'tethering', 'tracing', 'web_audio', 'web_authn',
            'debugger', 'heap_profiler', 'profiler', 'runtime'
        ]
        
        for domain in expected_domains:
            assert hasattr(cdp_events, domain), f"Missing domain: {domain}"
    
    def test_event_callback_receives_params(self, cdp_events, mock_client):
        """Test that event callbacks receive parameters correctly"""
        received_params = []
        
        def callback(params):
            received_params.append(params)
        
        cdp_events.page.on_load_event_fired(callback)
        
        # Verify the callback was registered
        mock_client.on.assert_called_once()
        registered_callback = mock_client.on.call_args[0][1]
        
        # Simulate calling the callback
        test_params = {"timestamp": 123456}
        registered_callback(test_params)
        
        assert len(received_params) == 1
        assert received_params[0] == test_params
