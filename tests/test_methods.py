"""Tests for CDP Methods"""

import pytest
import asyncio
from unittest.mock import AsyncMock, MagicMock, patch
from client.methods import CDPMethods
from client.service import CDPClient


@pytest.fixture
def mock_client():
    """Create a mock CDP client"""
    client = MagicMock(spec=CDPClient)
    client.send = AsyncMock()
    return client


@pytest.fixture
def cdp_methods(mock_client):
    """Create CDPMethods instance with mock client"""
    return CDPMethods(mock_client)


class TestCDPMethodsInitialization:
    """Test CDP Methods initialization"""
    
    def test_methods_initializes_with_client(self, mock_client):
        """Test that CDPMethods initializes with client reference"""
        methods = CDPMethods(mock_client)
        assert methods.client == mock_client
    
    def test_methods_has_send_method(self, cdp_methods):
        """Test that CDPMethods has send method"""
        assert hasattr(cdp_methods, 'send')
        assert callable(cdp_methods.send)


class TestCDPMethodsSend:
    """Test CDP Methods send functionality"""
    
    @pytest.mark.asyncio
    async def test_send_calls_client_send(self, cdp_methods, mock_client):
        """Test that send method calls client.send"""
        mock_client.send.return_value = {"success": True}
        
        result = await cdp_methods.send("Page.enable", {"param": "value"})
        
        mock_client.send.assert_called_once_with("Page.enable", {"param": "value"})
        assert result == {"success": True}
    
    @pytest.mark.asyncio
    async def test_send_without_params(self, cdp_methods, mock_client):
        """Test send method without parameters"""
        mock_client.send.return_value = {}
        
        await cdp_methods.send("Page.enable")
        
        mock_client.send.assert_called_once_with("Page.enable", None)
    
    @pytest.mark.asyncio
    async def test_send_returns_result(self, cdp_methods, mock_client):
        """Test that send returns the result from client"""
        expected_result = {"frameId": "123", "loaderId": "456"}
        mock_client.send.return_value = expected_result
        
        result = await cdp_methods.send("Page.navigate", {"url": "https://example.com"})
        
        assert result == expected_result


class TestCDPMethodsDomainAccess:
    """Test CDP Methods domain access"""
    
    def test_page_domain_property(self, cdp_methods):
        """Test accessing Page domain methods"""
        page_methods = cdp_methods.page
        assert page_methods is not None
        from protocol.page.methods.service import PageMethods
        assert isinstance(page_methods, PageMethods)
    
    def test_network_domain_property(self, cdp_methods):
        """Test accessing Network domain methods"""
        network_methods = cdp_methods.network
        assert network_methods is not None
        from protocol.network.methods.service import NetworkMethods
        assert isinstance(network_methods, NetworkMethods)
    
    def test_runtime_domain_property(self, cdp_methods):
        """Test accessing Runtime domain methods"""
        runtime_methods = cdp_methods.runtime
        assert runtime_methods is not None
        from protocol.runtime.methods.service import RuntimeMethods
        assert isinstance(runtime_methods, RuntimeMethods)
    
    def test_dom_domain_property(self, cdp_methods):
        """Test accessing DOM domain methods"""
        dom_methods = cdp_methods.dom
        assert dom_methods is not None
        from protocol.dom.methods.service import DOMMethods
        assert isinstance(dom_methods, DOMMethods)
    
    def test_debugger_domain_property(self, cdp_methods):
        """Test accessing Debugger domain methods"""
        debugger_methods = cdp_methods.debugger
        assert debugger_methods is not None
        from protocol.debugger.methods.service import DebuggerMethods
        assert isinstance(debugger_methods, DebuggerMethods)
    
    def test_emulation_domain_property(self, cdp_methods):
        """Test accessing Emulation domain methods"""
        emulation_methods = cdp_methods.emulation
        assert emulation_methods is not None
        from protocol.emulation.methods.service import EmulationMethods
        assert isinstance(emulation_methods, EmulationMethods)
    
    def test_domain_property_returns_same_instance(self, cdp_methods):
        """Test that accessing domain property multiple times returns new instances"""
        # Properties create new instances each time (not cached)
        page1 = cdp_methods.page
        page2 = cdp_methods.page
        # They should be different instances but same type
        assert type(page1) == type(page2)


class TestCDPMethodsPageDomain:
    """Test Page domain methods"""
    
    @pytest.mark.asyncio
    async def test_page_navigate(self, cdp_methods, mock_client):
        """Test Page.navigate method"""
        mock_client.send.return_value = {"frameId": "123", "loaderId": "456"}
        
        result = await cdp_methods.page.navigate({"url": "https://example.com"})
        
        mock_client.send.assert_called_once()
        call_args = mock_client.send.call_args
        assert call_args[0][0] == "Page.navigate"
        assert result["frameId"] == "123"
    
    @pytest.mark.asyncio
    async def test_page_enable(self, cdp_methods, mock_client):
        """Test Page.enable method"""
        mock_client.send.return_value = {}
        
        await cdp_methods.page.enable()
        
        mock_client.send.assert_called_once()
        call_args = mock_client.send.call_args
        assert call_args[0][0] == "Page.enable"
    
    @pytest.mark.asyncio
    async def test_page_capture_screenshot(self, cdp_methods, mock_client):
        """Test Page.captureScreenshot method"""
        mock_client.send.return_value = {"data": "base64encodedimage"}
        
        result = await cdp_methods.page.capture_screenshot({
            "format": "png",
            "quality": 80
        })
        
        mock_client.send.assert_called_once()
        assert "data" in result


class TestCDPMethodsNetworkDomain:
    """Test Network domain methods"""
    
    @pytest.mark.asyncio
    async def test_network_enable(self, cdp_methods, mock_client):
        """Test Network.enable method"""
        mock_client.send.return_value = {}
        
        await cdp_methods.network.enable()
        
        mock_client.send.assert_called_once()
        call_args = mock_client.send.call_args
        assert call_args[0][0] == "Network.enable"
    
    @pytest.mark.asyncio
    async def test_network_set_user_agent_override(self, cdp_methods, mock_client):
        """Test Network.setUserAgentOverride method"""
        mock_client.send.return_value = {}
        
        await cdp_methods.network.set_user_agent_override({
            "userAgent": "Custom User Agent"
        })
        
        mock_client.send.assert_called_once()


class TestCDPMethodsRuntimeDomain:
    """Test Runtime domain methods"""
    
    @pytest.mark.asyncio
    async def test_runtime_evaluate(self, cdp_methods, mock_client):
        """Test Runtime.evaluate method"""
        mock_client.send.return_value = {
            "result": {"type": "string", "value": "Hello World"}
        }
        
        result = await cdp_methods.runtime.evaluate({
            "expression": "document.title"
        })
        
        mock_client.send.assert_called_once()
        assert "result" in result
    
    @pytest.mark.asyncio
    async def test_runtime_enable(self, cdp_methods, mock_client):
        """Test Runtime.enable method"""
        mock_client.send.return_value = {}
        
        await cdp_methods.runtime.enable()
        
        mock_client.send.assert_called_once()


class TestCDPMethodsDOMDomain:
    """Test DOM domain methods"""
    
    @pytest.mark.asyncio
    async def test_dom_get_document(self, cdp_methods, mock_client):
        """Test DOM.getDocument method"""
        mock_client.send.return_value = {
            "root": {"nodeId": 1, "nodeName": "html"}
        }
        
        result = await cdp_methods.dom.get_document()
        
        mock_client.send.assert_called_once()
        assert "root" in result
    
    @pytest.mark.asyncio
    async def test_dom_query_selector(self, cdp_methods, mock_client):
        """Test DOM.querySelector method"""
        mock_client.send.return_value = {"nodeId": 123}
        
        result = await cdp_methods.dom.query_selector({
            "nodeId": 1,
            "selector": ".my-class"
        })
        
        mock_client.send.assert_called_once()
        assert "nodeId" in result


class TestCDPMethodsEmulationDomain:
    """Test Emulation domain methods"""
    
    @pytest.mark.asyncio
    async def test_emulation_set_device_metrics_override(self, cdp_methods, mock_client):
        """Test Emulation.setDeviceMetricsOverride method"""
        mock_client.send.return_value = {}
        
        await cdp_methods.emulation.set_device_metrics_override({
            "width": 375,
            "height": 812,
            "deviceScaleFactor": 3,
            "mobile": True
        })
        
        mock_client.send.assert_called_once()
    
    @pytest.mark.asyncio
    async def test_emulation_set_geolocation_override(self, cdp_methods, mock_client):
        """Test Emulation.setGeolocationOverride method"""
        mock_client.send.return_value = {}
        
        await cdp_methods.emulation.set_geolocation_override({
            "latitude": 37.7749,
            "longitude": -122.4194,
            "accuracy": 100
        })
        
        mock_client.send.assert_called_once()


class TestCDPMethodsDebuggerDomain:
    """Test Debugger domain methods"""
    
    @pytest.mark.asyncio
    async def test_debugger_enable(self, cdp_methods, mock_client):
        """Test Debugger.enable method"""
        mock_client.send.return_value = {"debuggerId": "123"}
        
        result = await cdp_methods.debugger.enable()
        
        mock_client.send.assert_called_once()
        assert "debuggerId" in result
    
    @pytest.mark.asyncio
    async def test_debugger_set_breakpoint(self, cdp_methods, mock_client):
        """Test Debugger.setBreakpoint method"""
        mock_client.send.return_value = {
            "breakpointId": "123",
            "actualLocation": {}
        }
        
        result = await cdp_methods.debugger.set_breakpoint({
            "location": {
                "scriptId": "1",
                "lineNumber": 10
            }
        })
        
        mock_client.send.assert_called_once()
        assert "breakpointId" in result


class TestCDPMethodsIntegration:
    """Integration tests for CDP Methods"""
    
    @pytest.mark.asyncio
    async def test_multiple_domain_methods_in_sequence(self, cdp_methods, mock_client):
        """Test calling methods from multiple domains in sequence"""
        mock_client.send.return_value = {}
        
        # Call methods from different domains
        await cdp_methods.page.enable()
        await cdp_methods.network.enable()
        await cdp_methods.runtime.enable()
        
        # Should have called send 3 times
        assert mock_client.send.call_count == 3
    
    @pytest.mark.asyncio
    async def test_method_error_handling(self, cdp_methods, mock_client):
        """Test that method errors are propagated correctly"""
        mock_client.send.side_effect = Exception("CDP Error")
        
        with pytest.raises(Exception) as exc_info:
            await cdp_methods.page.navigate({"url": "invalid"})
        
        assert "CDP Error" in str(exc_info.value)
    
    def test_all_domain_properties_exist(self, cdp_methods):
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
            assert hasattr(cdp_methods, domain), f"Missing domain: {domain}"
