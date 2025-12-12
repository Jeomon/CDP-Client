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
    try:
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
            response=await client.methods.target.attach_to_target(params={'targetId':target_id,'flatten':True})
            session_id=response['sessionId']
            await client.methods.dom.enable(session_id=session_id)
            await client.methods.page.navigate(params={'url':'https://www.google.com/'},session_id=session_id)
            await client.methods.runtime.enable(session_id=session_id)
            while True:
                ready_state=await client.methods.runtime.evaluate(params={'expression':'document.readyState'},session_id=session_id)
                if ready_state['result']['value']=='interactive':
                    break
            await client.methods.runtime.disable(session_id=session_id)
            # await client.methods.accessibility.enable(session_id=session_id)
            # response=await client.methods.accessibility.get_full_ax_tree(session_id=session_id)
            # await client.methods.accessibility.disable(session_id=session_id)
            await client.methods.dom.enable(session_id=session_id)
            response=await client.methods.dom.get_document(params={'depth':-1,'pierce':True},session_id=session_id)
            await client.methods.dom.disable(session_id=session_id)
            with open('document.json','w') as f:
                f.write(json.dumps(response,indent=4))
    finally:
        if process:
            process.terminate()
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
