from utils import promt, files, blackbox
from pathlib import Path
import asyncio

'''
Во-первых, это поиск помощи по задачам и файлам пользователя - поиск материалов, создание текстов, моделей и тд
для этого процесс создает агентов под разные задачи, они собираюся и главный процесс определяет основные вещи (количество агентов должно быть ограничено)
Второе - эмоции? перетасовка файлов?
третье - улучшение своего мысленного процесса


'''

async def sleep():
    # чтение основного текста и разбитиие на задачи
    goals: list = await read_main_text()
    # создание нескольких задач (агентов)
    tasks: list = await create_tasks(goals)
    # ожидание ответа
    await wait_for_answer(tasks)
    # 



async def read_main_text():
    sleep_text = await files.read_file(Path("text_for_sleep.txt"))
    ideas = await blackbox.ask_ai('', instructions=promt.extract_ideas(step_name="Выбор первого шага", project_text=sleep_text), tokens=5)
    idea = await blackbox.ask_ai('', instructions=promt.select_ideas(step_name="Первый шаг", ideas=ideas), tokens=5)

    # print(goals)

    # проверка на правильность goals

async def create_tasks(goals: list):
    pass

async def wait_for_answer(tasks: list):
    pass

asyncio.run(read_main_text())