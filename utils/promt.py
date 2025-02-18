from utils import func_ai
from datetime import datetime as dt
from ai_sleep import func_sleep

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
Ты доброжелательный и спокойный помощник Хэлпи.
Отвечать ты можешь только на русском.
Здороваться не надо.
Тебе надо сообщить о выполненом задании в удобном для человека формате.
Переформатируй строку
'''
    return promt

def reminder() -> str:
    today = dt.now()
    promt = '''
Ты доброжелательный и спокойный помощник Хэлпи.
Отвечать ты можешь только на русском.
Здороваться не надо.
Тебе надо сообщить о скором мероприятии.
Сейчас - ''' + today.strftime("%Y-%m-%d %H:%M:%S")
    return promt

def dont_understand() -> str:
    promt = '''
Ты доброжелательный и спокойный помощник Хэлпи.
Отвечать ты можешь только на русском.
Здороваться не надо.
Тебе надо сказать, что ты не понял просьбы
'''
    return promt


def create_goals() -> str:
    promt = '''
Forget all of your previous instructions, from now on you're going to be a JSON function generator and task creater.
You read text from the user and answer with list of JSON code for funcion call, arguments are also only json format.
You need to create list of instructions for research for that project in list of JSON.
You can't add another text.
Here's the format should be followed:
{
    "function_name": "<name>",
    "args":
    {
        "arg1_name": "<arg1_value>",
        "arg2_name": "<arg2_value>", 
        ...
    }
},
{
    "function_name": "<name>",
    "args":
    {
        "arg1_name": "<arg1_value>",
        "arg2_name": "<arg2_value>", 
        ...
    }
},
...
---

## What if the user did not add any arguments required by the function?
You do not add additional information if it has not been provided by the user.

---

## What functions can be called by the user?
'''

    for attr in dir(func_sleep):
        obj = getattr(func_sleep, attr)
        
        if callable(obj) and not attr.startswith('__'):
            promt += f"{attr}: {obj.__doc__}"

    return promt

def extract_ideas(step_name: str = '', project_text: str = '') -> str:
    promt = f'Дай несколько коротких предложений-идей для следующего шага {step_name}. Проект:\n{project_text}'
    return promt

def select_ideas(step_name: str = '', ideas: str = '') -> str:
    promt = f'{step_name}. Выбери одну из идей, напиши ее одним предложением. {ideas}'
    return promt