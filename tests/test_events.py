"""Integration Tests for CDP Events"""

import pytest
import asyncio
from client.service import CDPClient

class TestCDPEventsIntegration:
    """Integration tests using real Chrome browser"""

    async def test_page_load_event(self, cdp_client: CDPClient):
        """Test receiving Page.loadEventFired"""
        await cdp_client.methods.page.enable()
        
        event_future = asyncio.Future()
        
        def on_load(params):
            if not event_future.done():
                event_future.set_result(params)
        
        cdp_client.events.page.on_load_event_fired(on_load)
        
        # Trigger navigation
        await cdp_client.methods.page.navigate({"url": "about:blank"})
        
        # Wait for event
        params = await asyncio.wait_for(event_future, timeout=5.0)
        assert "timestamp" in params

    async def test_network_request_event(self, cdp_client: CDPClient):
        """Test receiving Network.requestWillBeSent"""
        await cdp_client.methods.network.enable()
        
        event_future = asyncio.Future()
        
        def on_request(params):
            if not event_future.done():
                event_future.set_result(params)
                
        cdp_client.events.network.on_request_will_be_sent(on_request)
        
        # Trigger a request via Runtime
        await cdp_client.methods.runtime.evaluate({
            "expression": "fetch('data:text/plain,hello')"
        })
        
        params = await asyncio.wait_for(event_future, timeout=5.0)
        assert "requestId" in params
        assert "request" in params

    async def test_multiple_event_handlers(self, cdp_client: CDPClient):
        """Test registering multiple handlers"""
        await cdp_client.methods.runtime.enable()
        
        count = 0
        done = asyncio.Future()
        
        def handler1(params):
            nonlocal count
            count += 1
            if count == 2 and not done.done():
                done.set_result(True)
                
        def handler2(params):
            nonlocal count
            count += 1
            if count == 2 and not done.done():
                done.set_result(True)
        
        # Register two handlers for the same event
        # Note: Runtime.executionContextCreated is fired when we enable Runtime or reload
        # Let's use consoleAPICalled and trigger it
        cdp_client.events.runtime.on_console_api_called(handler1)
        cdp_client.events.runtime.on_console_api_called(handler2)
        
        await cdp_client.methods.runtime.evaluate({
            "expression": "console.log('test')"
        })
        
        await asyncio.wait_for(done, timeout=5.0)
        assert count == 2

    async def test_async_event_handler(self, cdp_client: CDPClient):
        """Test async event handler"""
        await cdp_client.methods.runtime.enable()
        
        event_future = asyncio.Future()
        
        async def async_handler(params):
            # Simulate some async work
            await asyncio.sleep(0.01)
            if not event_future.done():
                event_future.set_result(params)
        
        cdp_client.events.runtime.on_console_api_called(async_handler)
        
        await cdp_client.methods.runtime.evaluate({
            "expression": "console.log('async test')"
        })
        
        params = await asyncio.wait_for(event_future, timeout=5.0)
        assert params["args"][0]["value"] == "async test"
