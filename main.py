from client.service import CDPClient
from httpx import AsyncClient
from pathlib import Path
import subprocess
import time

async def main():
    executable_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    user_data_dir = Path.cwd()/'user_data'
    port = 9222
    process=subprocess.Popen([
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

    async with CDPClient(ws_url) as client:
        targets=await client.methods.target.get_targets()
        for target in targets['targetInfos']:
            if target['type']=='page':
                page=await client.methods.target.attach_to_target({'targetId':target['targetId']})
                response=await client.methods.page.navigate({'url':'https://www.google.com'})
                print(response)
    time.sleep(5)
    process.terminate()
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
