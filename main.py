from client.service import CDPClient
from tempfile import TemporaryDirectory
import subprocess
import httpx
import time

async def main():
    executable_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    user_data_dir = TemporaryDirectory().name
    port = 9222
    print(user_data_dir)
    subprocess.Popen([
        executable_path, 
        f"--remote-debugging-port={port}",
        '--no-first-run',
        '--no-default-browser-check',
        f'--user-data-dir={user_data_dir}'
    ])
    time.sleep(2)  # Wait for Chrome to start
    response = httpx.get(f"http://localhost:{port}/json")
    ws_url = response.json()[0]['webSocketDebuggerUrl']
    print(ws_url)
    time.sleep(1)  # Ensure the WebSocket URL is ready
    client = CDPClient(ws_url)
    await client.start()
    response=await client.methods.page.navigate(params={"url": "https://www.google.com"})
    print(response)
    await client.stop()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
