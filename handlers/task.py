from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from utils.change_room import CustomScene
from aiogram.fsm.scene import on
from aiogram.types.callback_query import CallbackQuery
from aiogram.dispatcher.middlewares.base import BaseMiddleware
from utils import keyboard as kb
from utils.globals import Globals
from utils.filter import RoomMiddleware

'''
    Тут все сообщения превращаются в заметку с датой, временем
    и добавляются в shreduler (напоминание от бота) 
'''

class TaskScene(CustomScene, state='task'):
    @on.message.enter()
    async def on_msg_enter(self, message: Message) -> None:
        await message.answer('Комната с заметками')
    
    @on.message()
    async def on_msg(self, message: Message) -> None:
        await message.answer('Да-да, это заметки черт возьми!')

router = Router()
router.message.register(TaskScene.as_handler(), Command('task'))






# router = Router()

# router.message.outer_middleware(RoomMiddleware('task'))

# @router.message()
# async def add_task(msg: Message):
#     try:
#         await msg.answer(f'Таски')
#     except SkipHandler:
#         print("Обработчик пропущен.")

# @router.message()
# async def another_handler(msg: Message):
#     await msg.answer('Это другой обработчик!')
















# Панель управления
# @router.callback_query(F.data == 'task_manager')
# async def task_manager(callback: CallbackQuery):
#     await kb.inline(
#         callback,
#         'Управление тасками',
#         kb.task_manager()
#     )

# Отображение всех заданий
# @router.callback_query(F.data == 'all_task')
# async def task_all(callback: CallbackQuery):
#     tasks = await db.get_tasks()
#     if not tasks:
#         await callback.answer("Нет доступных задач.")
#         return
    
#     tasks_message = "Список задач:\n"
#     for task in tasks:
#         tasks_message += f"- {task.title} (Приоритет: {task.priority.name}, Тип: {task.task_type.name})\n"
    
#     await callback.message.answer(tasks_message)

# Добавление
# @router.callback_query(F.data == 'add_task')
# async def task_all(callback: CallbackQuery):
    
#     await callback.message.answer("Задача успешно добавлена!")
