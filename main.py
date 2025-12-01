from client.service import CDPClient
from protocol.accessibility.events.types import loadCompleteEvent
from httpx import AsyncClient
from pathlib import Path
import subprocess
import logging
import time
import json


logging.basicConfig(level=logging.INFO)

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
    async with AsyncClient() as client:
        response = await client.get(f"http://localhost:{port}/json/version")
    ws_url = response.json()['webSocketDebuggerUrl']

    async with CDPClient(ws_url) as client:
        targets=await client.methods.target.get_targets()
        page_targets=[target for target in targets['targetInfos'] if target['type']=='page']

        if not page_targets:
            raise Exception("No page targets found")

        target_id=page_targets[0]['targetId']
        response=await client.methods.target.attach_to_target(params={'targetId':target_id,"flatten":True})
        session_id=response['sessionId']
        await client.methods.dom_snapshot.enable(session_id=session_id)
        await client.methods.page.navigate(params={'url':'https://www.google.com/'},session_id=session_id)
        document=await client.methods.dom_snapshot.capture_snapshot(params={'depth':-1,'pierce':True},session_id=session_id)
        print(json.dumps(document,indent=4))
        await client.methods.dom_snapshot.disable(session_id=session_id)
    time.sleep(5)
    process.terminate()
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
