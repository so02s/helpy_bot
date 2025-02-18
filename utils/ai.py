import json, aiohttp
from decouple import config

async def ask_ai(
    req: str,
    instructions: str,
    url: str = config("API_URL"),
    tokens: int = 1024,
    model: str = "llama3.2"
) -> str:
    
    data = {
        "messages": [{"content": f"{req}\n\n{instructions}", "role": "user"}],
        "max_tokens": tokens,
        "model": model
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
    
    lines = response_text.splitlines()

    messages = []
    for line in lines:
        try:
            response_json = json.loads(line)
            if response_json.get("message"):
                messages.append(response_json["message"]["content"])
        except json.JSONDecodeError:
            pass
        
    response_text = "".join(messages)

    # print(response_text)
    return response_text