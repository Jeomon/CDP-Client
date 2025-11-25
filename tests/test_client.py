"""Integration Tests for CDP Client"""

import pytest
import asyncio
from client.service import CDPClient

class TestCDPClientIntegration:
    """Integration tests using real Chrome browser"""

    async def test_client_connection(self, cdp_client: CDPClient):
        """Test that client is connected"""
        assert cdp_client.ws is not None
        assert not cdp_client.ws.closed
        assert cdp_client.listen_task is not None
        assert not cdp_client.listen_task.done()

    async def test_send_method(self, cdp_client: CDPClient):
        """Test sending a method"""
        # Get initial ID
        initial_id = cdp_client.id_counter
        
        # Send a command
        await cdp_client.send("Page.enable")
        
        # Verify ID incremented
        assert cdp_client.id_counter > initial_id

    async def test_send_method_returns_result(self, cdp_client: CDPClient):
        """Test that send returns the result"""
        result = await cdp_client.send("Runtime.evaluate", {"expression": "1+1"})
        assert result["result"]["value"] == 2

    async def test_concurrent_commands(self, cdp_client: CDPClient):
        """Test sending multiple commands concurrently"""
        # Send multiple evaluations
        futures = [
            cdp_client.send("Runtime.evaluate", {"expression": f"{i}+{i}"})
            for i in range(5)
        ]
        
        results = await asyncio.gather(*futures)
        
        for i, result in enumerate(results):
            assert result["result"]["value"] == i + i

    async def test_event_registration(self, cdp_client: CDPClient):
        """Test manual event registration"""
        await cdp_client.send("Page.enable")
        
        event_future = asyncio.Future()
        
        def handler(params):
            if not event_future.done():
                event_future.set_result(params)
        
        cdp_client.register("Page.loadEventFired", handler)
        
        # Trigger
        await cdp_client.send("Page.navigate", {"url": "about:blank"})
        
        await asyncio.wait_for(event_future, timeout=5.0)
        
        # Unregister
        cdp_client.unregister("Page.loadEventFired")
        assert "Page.loadEventFired" not in cdp_client.event_handlers

    async def test_context_manager_cleanup(self, chrome_process):
        """Test that context manager closes connection"""
        # We need to create a new client here to test its cleanup
        # We can reuse the chrome_process fixture to get the port
        import httpx
        async with httpx.AsyncClient() as http_client:
            response = await http_client.get("http://localhost:9222/json")
            ws_url = response.json()[0]['webSocketDebuggerUrl']
            
        client = CDPClient(ws_url)
        async with client:
            assert client.ws is not None
            assert not client.ws.closed
            
        # After exit
        assert client.ws is None # The client sets self.ws = None after close
        # We can't easily check if the websocket is closed since the object is gone, 
        # but we can check if listen task is cancelled
        assert client.listen_task is None

