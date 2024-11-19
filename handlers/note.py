from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.scene import on

from handlers.change_room import CustomScene


'''
    Комната с заметками - можно создать заметку, она сохранится в определенный файл
'''

class NoteScene(CustomScene, state='note'):
    @on.message.enter()
    @on.callback_query.enter()
    async def on_msg_enter(self, message: Message = None) -> None:
        await message.answer('Комната с заметками')
    
    @on.message()
    async def on_msg(self, message: Message) -> None:
        await message.answer('Да-да, это заметки черт возьми!')

router = Router()
router.message.register(NoteScene.as_handler(), Command('task'))