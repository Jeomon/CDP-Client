"""Integration Tests for CDP Methods"""

import pytest
import asyncio
from client.service import CDPClient

# We don't need mocks anymore, we use the cdp_client fixture from conftest.py

class TestCDPMethodsIntegration:
    """Integration tests using real Chrome browser"""

    async def test_page_navigate(self, cdp_client: CDPClient):
        """Test Page.navigate method"""
        # Navigate to a blank page
        result = await cdp_client.methods.page.navigate({"url": "about:blank"})
        assert "frameId" in result
        
        # Verify we are on the correct page (using Runtime to check location)
        eval_result = await cdp_client.methods.runtime.evaluate({"expression": "window.location.href"})
        assert eval_result["result"]["value"] == "about:blank"

    async def test_runtime_evaluate(self, cdp_client: CDPClient):
        """Test Runtime.evaluate method"""
        result = await cdp_client.methods.runtime.evaluate({
            "expression": "1 + 1"
        })
        assert result["result"]["type"] == "number"
        assert result["result"]["value"] == 2

    async def test_network_enable(self, cdp_client: CDPClient):
        """Test Network.enable method"""
        # Just ensure it doesn't raise an error
        await cdp_client.methods.network.enable()

    async def test_dom_get_document(self, cdp_client: CDPClient):
        """Test DOM.getDocument method"""
        doc = await cdp_client.methods.dom.get_document()
        assert "root" in doc
        assert doc["root"]["nodeName"] == "#document"

    async def test_domain_access(self, cdp_client: CDPClient):
        """Test accessing various domains"""
        assert cdp_client.methods.page is not None
        assert cdp_client.methods.network is not None
        assert cdp_client.methods.runtime is not None
        assert cdp_client.methods.dom is not None
        # Check a few others
        assert cdp_client.methods.target is not None
        assert cdp_client.methods.browser is not None

    async def test_method_error_handling(self, cdp_client: CDPClient):
        """Test that method errors are propagated correctly"""
        # Try to navigate to an invalid URL or call a method with bad params
        # Page.navigate to a non-existent protocol usually just fails to load, 
        # let's try a Runtime evaluation that throws
        
        # Actually, let's try calling a method with invalid parameters if possible,
        # or a method that requires a specific state.
        
        # Using a made-up method should raise an error from the server (Method not found)
        # But our client wrapper methods are typed. 
        # Let's try Runtime.evaluate with a syntax error in JS. 
        # Note: Runtime.evaluate usually returns an exceptionDetails, it doesn't necessarily raise a protocol error unless the request itself is malformed.
        
        eval_result = await cdp_client.methods.runtime.evaluate({"expression": "throw new Error('oops')"})
        assert "exceptionDetails" in eval_result
        
        # Let's try to send a raw command that doesn't exist to test the client's error handling
        with pytest.raises(Exception):
             await cdp_client.send("Invalid.Method", {})

