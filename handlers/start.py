from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.types.callback_query import CallbackQuery

from create_bot import bot
from utils.filter import IsAdmin
from utils import keyboard as kb

router = Router()

@router.message(IsAdmin(), CommandStart())
async def start_cmd(msg: Message, state: FSMContext):
    await state.clear()
    msg_bot = await msg.answer(
        'Приветик!\nТы молодец, продолжай в том же духе!',
        reply_markup=kb.start_menu()
    )
    await bot.delete_messages(
        msg.from_user.id,
        [msg_bot.message_id - i for i in range(1, 10)]
    )
    
@router.callback_query(F.data == "start_model")
async def start_cmd(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await kb.inline(
        callback,
        'Все получится',
        reply_markup=kb.start_menu()
    )