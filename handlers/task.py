from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.types.callback_query import CallbackQuery
from aiogram.dispatcher.middlewares.base import BaseMiddleware
from utils import keyboard as kb
from db import db_task as db

# class TaskMiddleware(BaseMiddleware):
#     async def __call__(
#         self,
#         handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
#         event: TelegramObject,
#         data: dict
#     ) -> Any:
#         # Состояние необходимо сохранять где-то на сервере
#         # Через callback нормально не выйдет
        
        
#         if isinstance(event, CallbackQuery):
#             callback_data = CallbackFactory.parse(event.data)
#             if callback_data['action'] == 'task':
#                 pass
#         return

router = Router()

# router.message.middleware(TaskMiddleware())
# router.callback_query.middleware(TaskMiddleware())

# Тут все сообщения превращаются в заметку с датой, временем
# и добавляются в shreduler (напоминание от бота) 

@router.message()
async def add_task(msg: Message):
    await msg.answer('Хехе')
    


















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
