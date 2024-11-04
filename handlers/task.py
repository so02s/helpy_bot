from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types.callback_query import CallbackQuery
from utils import keyboard as kb
from db import db_task as db

router = Router()

# Панель управления
@router.callback_query(F.data == 'task_manager')
async def task_manager(callback: CallbackQuery):
    await kb.inline(
        callback,
        'Управление тасками',
        kb.task_manager()
    )

# Отображение всех заданий
@router.callback_query(F.data == 'task_all')
async def task_all(callback: CallbackQuery):
    tasks = await db.get_tasks()
    if not tasks:
        await callback.answer("Нет доступных задач.")
        return
    
    tasks_message = "Список задач:\n"
    for task in tasks:
        tasks_message += f"- {task.title} (Приоритет: {task.priority.name}, Тип: {task.task_type.name})\n"
    
    await callback.message.answer(tasks_message)

