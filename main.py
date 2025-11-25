from client.service import CDPClient
import subprocess
from httpx import AsyncClient
from pathlib import Path
import time

async def main():
    executable_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    user_data_dir = Path.cwd()/'user_data'
    port = 9222
    subprocess.Popen([
        executable_path, 
        f"--remote-debugging-port={port}",
        f"--user-data-dir={user_data_dir.as_posix()}",
        '--no-first-run',
        '--no-default-browser-check',
    ])
    time.sleep(2)  # Wait for Chrome to start
    async with AsyncClient() as client:
        response = await client.get(f"http://localhost:{port}/json")
    ws_url = response.json()[0]['webSocketDebuggerUrl']
    client = CDPClient(ws_url)
    await client.start()
    response=await client.methods.target.get_targets()
    print(response)
    await client.stop()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
