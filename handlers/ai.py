from aiogram import Router
from aiogram.types import Message
from utils import blackbox, func_ai, globals
import json
from utils.promt import good_answer

router = Router()

@router.message()
async def gui_ai(msg: Message):
    result = None
    print(msg.text)
    for i in range(3):
        # Вопрос к ИИ
        text = await blackbox.ask_ai(
            req=msg.text,
            forward_msg=globals.ForwardMessage.get_text()
        )
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

    # отчет о выполнении через ИИ
    if result:
        text = await blackbox.ask_ai(result, instructions=good_answer())
        await msg.answer(text)


def validate_json(json_string: str):
    """
    Проверяет валидность JSON и наличие функции с корректными аргументами, затем возвращает её.
    """
    json_string = json_string.replace('```', '').replace('json', '').replace('\\', '')
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