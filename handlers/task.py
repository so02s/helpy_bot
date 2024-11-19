from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.scene import on

from handlers.change_room import CustomScene


'''
    Тут все сообщения превращаются в заметку с датой, временем
    и добавляются в shreduler (напоминание от бота)
    
    TODO не забыть про приоритет
'''

class TaskScene(CustomScene, state='task'):
    @on.message.enter()
    @on.callback_query.enter()
    async def on_msg_enter(self, message: Message = None) -> None:
        await message.answer('Комната с задачами')
    
    @on.message()
    async def on_msg(self, message: Message) -> None:
        await message.answer('Да-да, это задачи черт возьми!')

router = Router()
router.message.register(TaskScene.as_handler(), Command('task'))





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
