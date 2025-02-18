from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from ai_sleep.setup import bot
from utils import keyboard as kb

'''
    Это стартовая "пустая" комната. Отсюда открываются все остальные комнаты.
'''

router = Router()

@router.message(CommandStart())
async def what_can_i_do(msg: Message, state: FSMContext = None):
    await msg.answer(
'''Привет! Меня зовут Хэлпи и я готов помочь тебе со всеми проблемами

Что я могу?
- Добавлять таски (мероприятия и задания) и напоминать про них
- Добавлять заметки, организовывать их и помогать тебе с редакцией
- Показать все твои заметки и таски в web
- Помогаю с распорядком дня

И просто могу поддержать :3
''')