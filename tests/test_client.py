import pytest
import asyncio
import json
from unittest.mock import AsyncMock, MagicMock, patch, call
from client.service import CDPClient


class MockWebSocket:
    """Mock WebSocket for testing"""

    def __init__(self):
        self.messages = []
        self.responses = []
        self.closed = False

    async def send(self, message):
        self.messages.append(message)

    async def recv(self):
        if self.responses:
            return self.responses.pop(0)
        await asyncio.sleep(0.05)
        raise Exception("No more responses")

    async def close(self):
        self.closed = True


@pytest.fixture
def mock_ws():
    return MockWebSocket()


@pytest.fixture
async def cdp_client(mock_ws):
    """Use correct patch for websockets.connect based on client.service import"""
    with patch("client.service.connect", new=AsyncMock(return_value=mock_ws)):
        client = CDPClient("ws://localhost:9222")
        async with client:
            yield client


class TestCDPClientConnection:

    @pytest.mark.asyncio
    async def test_client_initialization(self):
        client = CDPClient("ws://localhost:9222")
        assert client.url == "ws://localhost:9222"
        assert client.ws is None
        assert client.listen_task is None
        assert client.id_counter == 0
        assert len(client.pending_requests) == 0
        assert len(client.event_handlers) == 0

    @pytest.mark.asyncio
    async def test_client_context_manager(self, mock_ws):
        with patch("client.service.connect", new=AsyncMock(return_value=mock_ws)):
            async with CDPClient("ws://localhost:9222") as client:
                assert client.ws is not None
                assert client.listen_task is not None
                assert not mock_ws.closed

            assert mock_ws.closed

    @pytest.mark.asyncio
    async def test_client_cleanup_on_exit(self, mock_ws):
        with patch("client.service.connect", new=AsyncMock(return_value=mock_ws)):
            client = CDPClient("ws://localhost:9222")
            async with client:
                f1 = asyncio.Future()
                f2 = asyncio.Future()
                client.pending_requests[1] = f1
                client.pending_requests[2] = f2

            assert f1.done()
            assert f2.done()
            assert len(client.pending_requests) == 0


class TestCDPClientMethods:

    @pytest.mark.asyncio
    async def test_send_method_increments_id(self, cdp_client, mock_ws):
        initial_id = cdp_client.id_counter
        mock_ws.responses.append(json.dumps({"id": initial_id + 1, "result": {}}))

        await cdp_client.send("Page.navigate", {"url": "https://example.com"})

        assert cdp_client.id_counter == initial_id + 1

    @pytest.mark.asyncio
    async def test_send_method_formats_message_correctly(self, cdp_client, mock_ws):
        mock_ws.responses.append(json.dumps({"id": 1, "result": {"success": True}}))

        await cdp_client.send("Page.navigate", {"url": "https://example.com"})

        sent = json.loads(mock_ws.messages[0])
        assert sent["id"] == 1
        assert sent["method"] == "Page.navigate"
        assert sent["params"] == {"url": "https://example.com"}

    @pytest.mark.asyncio
    async def test_send_method_returns_result(self, cdp_client, mock_ws):
        expected = {"frameId": "123", "loaderId": "456"}
        mock_ws.responses.append(json.dumps({"id": 1, "result": expected}))

        result = await cdp_client.send("Page.navigate", {"url": "https://example.com"})

        assert result == expected

    @pytest.mark.asyncio
    async def test_send_method_handles_error(self, cdp_client, mock_ws):
        mock_ws.responses.append(json.dumps({
            "id": 1,
            "error": {"code": -32000, "message": "Invalid URL"}
        }))

        with pytest.raises(Exception):
            await cdp_client.send("Page.navigate", {"url": "bad"})

    @pytest.mark.asyncio
    async def test_send_method_with_no_params(self, cdp_client, mock_ws):
        mock_ws.responses.append(json.dumps({"id": 1, "result": {}}))

        await cdp_client.send("Page.enable")

        sent = json.loads(mock_ws.messages[0])
        assert sent["params"] == {}


class TestCDPClientEvents:

    @pytest.mark.asyncio
    async def test_register_event_handler(self, cdp_client):
        cb = MagicMock()
        cdp_client.register("Page.loadEventFired", cb)
        assert cdp_client.event_handlers["Page.loadEventFired"] == cb

    @pytest.mark.asyncio
    async def test_on_method_registers_handler(self, cdp_client):
        cb = MagicMock()
        cdp_client.on("Page.frameNavigated", cb)
        assert "Page.frameNavigated" in cdp_client.event_handlers

    @pytest.mark.asyncio
    async def test_unregister_event_handler(self, cdp_client):
        cb = MagicMock()
        cdp_client.register("Page.loadEventFired", cb)
        cdp_client.unregister("Page.loadEventFired")
        assert "Page.loadEventFired" not in cdp_client.event_handlers

    @pytest.mark.asyncio
    async def test_event_handler_called_on_event(self, mock_ws):
        event_received = asyncio.Event()
        received = {}

        def cb(params):
            received.update(params)
            event_received.set()

        event_msg = {
            "method": "Page.loadEventFired",
            "params": {"timestamp": 123}
        }
        mock_ws.responses.append(json.dumps(event_msg))

        with patch("client.service.connect", new=AsyncMock(return_value=mock_ws)):
            async with CDPClient("ws://localhost:9222") as client:
                client.register("Page.loadEventFired", cb)
                await asyncio.wait_for(event_received.wait(), timeout=1)

        assert received.get("timestamp") == 123

    @pytest.mark.asyncio
    async def test_async_event_handler(self, mock_ws):
        event_received = asyncio.Event()
        received = {}

        async def async_cb(params):
            received.update(params)
            event_received.set()

        mock_ws.responses.append(json.dumps({
            "method": "Network.requestWillBeSent",
            "params": {"requestId": "123"}
        }))

        with patch("client.service.connect", new=AsyncMock(return_value=mock_ws)):
            async with CDPClient("ws://localhost:9222") as client:
                client.register("Network.requestWillBeSent", async_cb)
                await asyncio.wait_for(event_received.wait(), timeout=1)

        assert received["requestId"] == "123"


class TestCDPClientListenLoop:

    @pytest.mark.asyncio
    async def test_listen_handles_method_response(self, mock_ws):
        mock_ws.responses.append(json.dumps({"id": 1, "result": {"frameId": "A"}}))

        with patch("client.service.connect", new=AsyncMock(return_value=mock_ws)):
            async with CDPClient("ws://localhost:9222") as client:
                fut = asyncio.Future()
                client.pending_requests[1] = fut
                result = await asyncio.wait_for(fut, timeout=1)
                assert result == {"frameId": "A"}

    @pytest.mark.asyncio
    async def test_listen_handles_multiple_messages(self, mock_ws):
        mock_ws.responses.extend([
            json.dumps({"id": 1, "result": {"success": True}}),
            json.dumps({"method": "Page.loadEventFired", "params": {}}),
            json.dumps({"id": 2, "result": {"data": "x"}}),
        ])

        with patch("client.service.connect", new=AsyncMock(return_value=mock_ws)):
            async with CDPClient("ws://localhost:9222") as client:
                f1 = asyncio.Future()
                f2 = asyncio.Future()
                client.pending_requests[1] = f1
                client.pending_requests[2] = f2

                r1, r2 = await asyncio.wait_for(asyncio.gather(f1, f2), timeout=1)
                assert r1 == {"success": True}
                assert r2 == {"data": "x"}


class TestCDPClientIntegration:

    async def test_methods_property_returns_cdp_methods(self):
        client = CDPClient("ws://localhost:9222")
        assert client.methods is not None

    async def test_events_property_returns_cdp_events(self):
        client = CDPClient("ws://localhost:9222")
        assert client.events is not None

    async def test_client_can_access_domain_methods(self):
        client = CDPClient("ws://localhost:9222")
        assert hasattr(client.methods, "page")
        assert hasattr(client.methods, "network")
        assert hasattr(client.methods, "runtime")
        assert hasattr(client.methods, "dom")

    async def test_client_can_access_domain_events(self):
        client = CDPClient("ws://localhost:9222")
        assert hasattr(client.events, "page")
        assert hasattr(client.events, "network")
        assert hasattr(client.events, "runtime")
        assert hasattr(client.events, "dom")
