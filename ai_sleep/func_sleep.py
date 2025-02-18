from utils import obsidian as obs
# from decouple import config
# from setup import bot

'''
    Модуль, содержащий функции, которые может вызвать ИИ во сне 
'''

async def question(text: str) -> None:
    '''
    Задать уточняющий вопрос, если не достает информации для следующего шага. Использовать в крайнем случае

    Keys:
        step (int)
        text (str)
        dependencies (str, optional)

    ### Example
    {
        "function_name": "question",
        "args": [
            {
                "step": "1",
                "text": "На что должна опираться диета?",
                "dependencies": ""
            }
        ]
    }
    '''
    results = ''
    
    
    return results


async def search(text: str) -> None:
    '''
    Поиск информации по теме для определения дальнейших действий

    Parameters:
    tasks (list): A list of dictionaries, each containing the task details.
        Keys:
            step (int)
            text (str)
            dependencies (str, optional)

    ### Example
    {
        "function_name": "search",
        "args": [
            {
                "step": "2",
                "text": "Основа здоровой диеты",
                "dependencies": "1"
            }
        ]
    }
    '''
    results = ''
    
    
    return results



async def think(text: str) -> None:
    '''
    Определение дальнейших действий на основе полученной информации

    Keys:
        step (int)
        dependencies (str, optional)

    ### Example
    {
        "function_name": "think",
        "args": [
            {
                "step": "3",
                "dependencies": "1, 2"
            }
        ]
    }
    '''
    results = ''
    
    
    return results



async def model(text: str) -> None:
    '''
    Создание математисекой модели задачи

    Keys:
        step (int)
        program (str)
        text (str)
        dependencies (str, optional)

    ### Example
    {
        "function_name": "model",
        "args": [
            {
                "step": "4",
                "program": "Obsidian ",
                "text": "Модель диеты на 21 день",
                "dependencies": "3"
            }
        ]
    }
    '''
    results = ''
    
    
    return results


