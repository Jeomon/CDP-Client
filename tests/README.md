# CDP Client Test Suite

This directory contains comprehensive tests for the CDP Client project.

## Test Structure

- `test_client.py` - Tests for the CDP WebSocket client
- `test_generator.py` - Tests for the CDP code generator
- `test_methods.py` - Tests for CDP method invocations
- `test_events.py` - Tests for CDP event handling

## Running Tests

### Run all tests
```bash
pytest
```

### Run specific test file
```bash
pytest tests/test_client.py
```

### Run specific test class
```bash
pytest tests/test_client.py::TestCDPClientConnection
```

### Run specific test
```bash
pytest tests/test_client.py::TestCDPClientConnection::test_client_initialization
```

### Run with coverage
```bash
pytest --cov=client --cov=generator --cov-report=html
```

### Run with verbose output
```bash
pytest -v
```

### Run only async tests
```bash
pytest -m asyncio
```

## Test Coverage

The test suite covers:

### Client Tests (`test_client.py`)
- Connection management (context manager, cleanup)
- Method invocation (message formatting, ID incrementing, error handling)
- Event handling (registration, callbacks, async handlers)
- Message listening (response handling, multiple messages)
- Integration with CDPMethods and CDPEvents

### Generator Tests (`test_generator.py`)
- Initialization and configuration
- Domain loading from protocol URLs
- File writing and directory creation
- Type generation for domains
- Service generation (methods and events)
- Client generation (filtering deprecated domains)
- Full generation workflow

### Methods Tests (`test_methods.py`)
- Initialization with client
- Send method functionality
- Domain property access (Page, Network, Runtime, DOM, etc.)
- Domain-specific method calls
- Error propagation
- Integration across multiple domains

### Events Tests (`test_events.py`)
- Initialization with client
- Event registration via `on` method
- Domain property access
- Domain-specific event handlers
- Async callback support
- Multiple event handler registration
- Parameter passing to callbacks

## Mocking Strategy

Tests use mocking to avoid actual WebSocket connections and HTTP requests:
- `MockWebSocket` - Simulates WebSocket behavior
- `unittest.mock.AsyncMock` - For async method mocking
- `unittest.mock.patch` - For patching external dependencies

## Requirements

Install test dependencies:
```bash
pip install pytest pytest-asyncio pytest-cov
```

Or with uv:
```bash
uv pip install pytest pytest-asyncio pytest-cov
```
