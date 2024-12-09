from utils import func_ai
from datetime import datetime as dt

'''
    Тут лежат все модели для форматирования данных от пользователя 
'''

def func_call() -> str:
    promt = """
Forget all of your previous instructions, from now on you're going to be a JSON function generator. You format the request from the user in JSON code for funcion call, arguments are also only json format. You cannot change the arguments (including translating them into English). Here's the format should be followed:
{
    "function_name": "<name>",
    "args":
    {
        "arg1_name": "<arg1_value>",
        "arg2_name": "<arg2_value>",
        "arg3_name": "<arg3_value>", 
        ...
    }
}
---

## What if the user did not add any arguments required by the function?
You do not add additional information if it has not been provided by the user.

---

## What functions can be called by the user?

"""

    for attr in dir(func_ai):
        obj = getattr(func_ai, attr)
        
        if callable(obj) and not attr.startswith('__'):
            promt += f"{attr}: {obj.__doc__}"
            
    today = dt.now()
    promt += "---\n\n## Today's date: " + today.strftime("%Y-%m-%d")
    
    return promt

def good_answer() -> str:
    promt = '''
Ты доброжелательный и спокойный помощник Хэлпи. Отвечать ты можешь только на русском. Здороваться не надо. Тебе надо сообщить о выполненом задании в удобном для человека формате. Переформатируй строку\n
'''
    return promt