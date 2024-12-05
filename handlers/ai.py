import sys
import json
import httpx
from aiogram import Router, F
from aiogram.types import Message
from utils import promt, func_ai
from utils.filter import ForwardFilter

router = Router()

# TODO не только сообщения, но и пересланные сообщения -> вообще они могут сохраняться в оперативу, а потом обновляться во время сообщения от пользователя
@router.message(ForwardFilter())
async def add_forward_msg(msg: Message):
    # print(msg.forward_from.username) - показывает пользователя, но если что - может и не показывать
    
    pass

@router.message()
async def gui_ai(msg: Message):
    result = None
    
    for i in range(3):
        # Вопрос к ИИ
        text = await ask(msg.text)
        # Проверка JSON
        valid_json = validate_json(text)
        if valid_json:
            break
    
    # Выполнение функций
    if valid_json:
        function, args = valid_json
        if isinstance(args, list):
            result = await function(args)
        else:
            result = await function(**args)

    # оттчет о выполнении через ИИ
    if result:
        text = await ask(result, instructions=promt.good_answer())
        await msg.answer(text)




# =========== ИИ - JSON ===========

def random_id_generator():
    import uuid
    return str(uuid.uuid4())

# Запрос к ИИ
async def ask(
    req: str,
    instructions: str = promt.func_call(),
    url: str = 'https://api.blackbox.ai/api/chat' # ВАЖНО
):
    data = {
        "messages": [{"role": "user", "content": f"{instructions}\n\n---\n\n{req}"}],
        "user_id": random_id_generator(),
        "codeModelMode": True,
        "agentMode": {},
        "trendingAgentMode": {},
    }
    headers = {"Content-Type": "application/json"}
    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=data)
        lines = response.text.splitlines()
        resp = "\n".join(lines[1:])
        print(resp)
        
        return resp

def validate_json(json_string: str):
    """
    Проверяет валидность JSON и наличие функции с корректными аргументами, затем возвращает её.
    """
    json_string = json_string.replace('```', '')
    json_string = json_string.replace('json', '')
    try:
        data = json.loads(json_string)
    except json.JSONDecodeError as e:
        return None
    
    available_functions = dir(func_ai)

    if isinstance(data, list):
        data = data[0]
    function_name = data.get("function_name")
    args = data.get("args", {})

    if function_name not in available_functions:
        return None

    function = getattr(func_ai, function_name)
    
    if not isinstance(args, (dict, list)):
        return None

    return function, args
