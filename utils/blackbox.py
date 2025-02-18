import json
from utils import promt
import aiohttp

async def ask_ai(
    req: str,
    instructions: str = promt.func_call(),
    tokens: int = 1024,
    url: str = "https://api.blackbox.ai/api/chat"
) -> str:
    
    # Модель можно поменять
    data = {
        "messages": [{"id": "2wlAo5V", "content": f"{instructions}\n\n---\n\n{req}", "role": "user"}],
        "model": "mistralai/Mistral-Small-24B-Instruct-2501",
        "max_tokens": tokens
    }
    
    headers = {
    'Content-Type': 'application/json'
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(
            url, 
            data=json.dumps(data), 
            headers=headers
        ) as response:
            response_text = await response.text()
            print(response_text)
    
    return response_text