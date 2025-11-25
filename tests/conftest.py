import pytest
import subprocess
import asyncio
import httpx
import time
import os
from pathlib import Path
from client.service import CDPClient

# Use the path from main.py
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PORT = 9222
USER_DATA_DIR = Path.cwd() / 'tests_user_data'

@pytest.fixture(scope="session")
def chrome_process():
    """Launch Chrome process for the test session."""
    if not os.path.exists(CHROME_PATH):
        pytest.skip(f"Chrome executable not found at {CHROME_PATH}")

    # Ensure user data dir exists
    USER_DATA_DIR.mkdir(exist_ok=True)

    process = subprocess.Popen([
        CHROME_PATH,
        f"--remote-debugging-port={PORT}",
        f"--user-data-dir={USER_DATA_DIR.as_posix()}",
        '--no-first-run',
        '--no-default-browser-check',
        '--headless=new' # Run in headless mode for tests
    ])
    
    # Wait for Chrome to start
    time.sleep(2)
    
    yield process
    
    # Teardown
    process.terminate()
    process.wait()
    # Optional: Clean up user data dir if needed, but might be risky to delete files

@pytest.fixture
async def cdp_client(chrome_process):
    """Create a connected CDPClient."""
    async with httpx.AsyncClient() as http_client:
        try:
            response = await http_client.get(f"http://localhost:{PORT}/json")
            response.raise_for_status()
            tabs = response.json()
            # Find a page target
            ws_url = None
            for tab in tabs:
                if tab['type'] == 'page':
                    ws_url = tab['webSocketDebuggerUrl']
                    break
            
            if not ws_url and tabs:
                 # Fallback to the first available if no page type found (e.g. about:blank might be 'other' sometimes?)
                 ws_url = tabs[0]['webSocketDebuggerUrl']

            if not ws_url:
                pytest.fail("No WebSocket URL found in Chrome targets")

        except httpx.RequestError as e:
            pytest.fail(f"Failed to connect to Chrome DevTools: {e}")

    client = CDPClient(ws_url)
    async with client:
        yield client
