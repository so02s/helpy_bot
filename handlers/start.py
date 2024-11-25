from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from create_bot import bot
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

# @router.message(CommandStart())
# async def start_console(msg: Message, state: FSMContext = None):
#     if state:
#         await state.clear()
#     msg_bot = await msg.answer(
#         'Приветик!\nТы молодец, продолжай в том же духе!',
#         reply_markup=kb.testing()
#     )
#     await bot.delete_messages(
#         msg.from_user.id,
#         [msg_bot.message_id - i for i in range(1, 40)]
#     )

# @router.callback_query(F.data == "start_model")
# async def start_cmd(callback: CallbackQuery, state: FSMContext):
#     await state.clear()
#     await kb.inline(
#         callback,
#         'Все получится, ты умничка',
#         reply_markup=kb.start_menu()
#     )